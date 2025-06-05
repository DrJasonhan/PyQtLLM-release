import sqlite3
import datetime
import os
import base64
from typing import List, Optional, Tuple

# SQLite Database Manager
class DatabaseManager:
    def __init__(self, db_path="data/conversations.db"):
        self.db_path = db_path
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.initialize_db()
        
    def initialize_db(self):
        """Initialize the database and create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create conversations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            session_id TEXT
        )
        ''')
        
        # Create messages table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER,
            role TEXT,
            content TEXT,
            timestamp TEXT,
            FOREIGN KEY (conversation_id) REFERENCES conversations (id)
        )
        ''')
        
        # Create attachments table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS attachments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER,
            message_id INTEGER,
            file_path TEXT,
            file_type TEXT,
            file_data BLOB,
            timestamp TEXT,
            FOREIGN KEY (conversation_id) REFERENCES conversations (id),
            FOREIGN KEY (message_id) REFERENCES messages (id)
        )
        ''')
        
        conn.commit()
        conn.close()
        
    def create_conversation(self):
        """Create a new conversation and return its ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        session_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        timestamp = datetime.datetime.now().isoformat()
        
        cursor.execute(
            "INSERT INTO conversations (timestamp, session_id) VALUES (?, ?)",
            (timestamp, session_id)
        )
        
        conversation_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return conversation_id
        
    def save_message(self, conversation_id, role, content):
        """Save a message to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        timestamp = datetime.datetime.now().isoformat()
        
        cursor.execute(
            "INSERT INTO messages (conversation_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
            (conversation_id, role, content, timestamp)
        )
        
        conn.commit()
        conn.close()
        
    def get_conversations(self):
        """Get all conversations"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, timestamp, session_id FROM conversations ORDER BY timestamp DESC")
        conversations = cursor.fetchall()
        
        conn.close()
        return conversations
        
    def get_messages(self, conversation_id):
        """Get all messages for a conversation"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT role, content, timestamp FROM messages WHERE conversation_id = ? ORDER BY timestamp",
            (conversation_id,)
        )
        messages = cursor.fetchall()
        
        conn.close()
        return messages
        
    def get_conversation_history(self, conversation_id, max_rounds=5):
        """
        Retrieve conversation history from the database limited to a specific number of rounds
        
        Args:
            conversation_id (int): The ID of the conversation
            max_rounds (int): Maximum number of conversation rounds to retrieve
            
        Returns:
            list: List of message dictionaries formatted for LLM API
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get all messages for the conversation
        cursor.execute(
            "SELECT role, content FROM messages WHERE conversation_id = ? ORDER BY timestamp",
            (conversation_id,)
        )
        all_messages = cursor.fetchall()
        conn.close()
        
        # Skip the most recent user message (as it will be included separately in the app)
        if all_messages and len(all_messages) > 0 and all_messages[-1][0] == "user":
            all_messages = all_messages[:-1]
        
        # Calculate how many messages to include (max_rounds * 2 for user+assistant pairs)
        # But limit to available messages
        message_limit = min(max_rounds * 2, len(all_messages))
        
        # Get the most recent messages up to the limit
        recent_messages = all_messages[-message_limit:] if message_limit > 0 else []
        
        # Format messages for the LLM API
        formatted_messages = []
        for role, content in recent_messages:
            formatted_messages.append({"role": role, "content": content})
            
        return formatted_messages
        
    def clear_all_history(self):
        """Clear all conversations and messages from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Delete all attachments
        cursor.execute("DELETE FROM attachments")
        
        # Delete all messages
        cursor.execute("DELETE FROM messages")
        
        # Delete all conversations
        cursor.execute("DELETE FROM conversations")
        
        conn.commit()
        conn.close()
        
    def clear_selected_conversations(self, conversation_ids):
        """Clear selected conversations and their messages from the database
        
        Args:
            conversation_ids: List of conversation IDs to clear
        """
        if not conversation_ids:
            return
            
        # Convert list to tuple for SQL IN clause
        if len(conversation_ids) == 1:
            # Special case for a single ID
            id_str = f"({conversation_ids[0]})"
        else:
            id_str = str(tuple(conversation_ids))
            
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Delete attachments for selected conversations
        cursor.execute(f"DELETE FROM attachments WHERE conversation_id IN {id_str}")
        
        # Delete messages for selected conversations
        cursor.execute(f"DELETE FROM messages WHERE conversation_id IN {id_str}")
        
        # Delete selected conversations
        cursor.execute(f"DELETE FROM conversations WHERE id IN {id_str}")
        
        conn.commit()
        conn.close()
        
    def save_attachment(self, conversation_id: int, file_path: str, file_type: str = "image") -> Optional[int]:
        """
        Save an attachment to the database
        
        Args:
            conversation_id: The ID of the conversation
            file_path: Path to the file
            file_type: Type of the file (default: "image")
            
        Returns:
            int: The ID of the saved attachment
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        timestamp = datetime.datetime.now().isoformat()
        
        # Read file data as binary
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        cursor.execute(
            "INSERT INTO attachments (conversation_id, message_id, file_path, file_type, file_data, timestamp) VALUES (?, NULL, ?, ?, ?, ?)",
            (conversation_id, file_path, file_type, file_data, timestamp)
        )
        
        attachment_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return attachment_id
        
    def get_attachments(self, conversation_id: int) -> List[Tuple[int, str, str]]:
        """
        Get all attachments for a conversation
        
        Args:
            conversation_id: The ID of the conversation
            
        Returns:
            List of tuples (attachment_id, file_path, file_type)
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id, file_path, file_type FROM attachments WHERE conversation_id = ? ORDER BY timestamp",
            (conversation_id,)
        )
        attachments = cursor.fetchall()
        
        conn.close()
        return attachments
        
    def get_attachment_data(self, attachment_id: int) -> Optional[Tuple[bytes, str]]:
        """
        Get attachment data by ID
        
        Args:
            attachment_id: The ID of the attachment
            
        Returns:
            Tuple of (file_data, file_type) or None if not found
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT file_data, file_type FROM attachments WHERE id = ?",
            (attachment_id,)
        )
        result = cursor.fetchone()
        
        conn.close()
        return result if result else None
        
    def get_latest_attachment(self, conversation_id: int) -> Optional[Tuple[int, str, str, bytes]]:
        """
        Get the most recent attachment for a conversation
        
        Args:
            conversation_id: The ID of the conversation
            
        Returns:
            Tuple of (attachment_id, file_path, file_type, file_data) or None if not found
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id, file_path, file_type, file_data FROM attachments WHERE conversation_id = ? ORDER BY timestamp DESC LIMIT 1",
            (conversation_id,)
        )
        result = cursor.fetchone()
        
        conn.close()
        return result if result else None
    # 添加到 DatabaseManager 类中
    def get_all_attachments(self, conversation_id):
        """
        Get all attachments for a conversation
        
        Args:
            conversation_id: The ID of the conversation
            
        Returns:
            List of tuples (attachment_id, file_path, file_type, file_data)
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT id, file_path, file_type, file_data FROM attachments WHERE conversation_id = ?",
                (conversation_id,)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error getting attachments: {e}")
            return []
