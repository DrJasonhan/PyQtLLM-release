"""
Chat Controller - Handles the business logic for chat functionality
"""

from PySide6.QtCore import QObject, Signal, QTimer
from src.models.db_manager import DatabaseManager
from src.services.llm_service import LLMWorker, ModelManager
from typing import List, Dict, Any, Union
from markitdown import MarkItDown
import tempfile
import os


class ChatController(QObject):
    """
    Controller class that handles the business logic for chat functionality.
    Acts as an intermediary between the UI (View) and the data (Model).
    """

    # Signals to communicate with the View
    message_received = Signal(str, str)  # role, content
    generation_started = Signal()
    generation_finished = Signal()
    conversation_loaded = Signal(list)  # list of messages
    conversation_history_updated = Signal(list)  # list of conversations

    def __init__(self):
        super().__init__()
        # Initialize database manager (Model)
        self.db_manager = DatabaseManager()
        # Store model manager
        self.model_manager = ModelManager()
        # Create a new conversation
        self.current_conversation_id = self.db_manager.create_conversation()
        # Initialize state
        self.is_generating = False
        self.is_first_chunk = True
        self.markdown_buffers = {}
        self.worker = None
        self.conversation_ids = []

        # Load conversation history
        self.load_conversation_history()

    def register_model(self, provider: str):
        llm_list = []
        if provider == "QWen":
            base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
            llm_list = ["qwen-plus", "qwen-max", "qwen-turbo", "qwen-vl-plus"]
        elif provider == "Deepseek":
            base_url = "https://api.deepseek.com"
            llm_list = ["deepseek-chat", "deepseek-reasoner"]

        for model in llm_list:
            self.model_manager.register_model(model, provider, base_url)

        return llm_list

    def set_current_model(self, name: str):
        self.model_manager.set_current_model(name)

    def set_api_key(self, key: str):
        self.model_manager.set_api_key(key)

    def send_message(self, question):
        """
        Process user message and send to LLM
        """

        # Save user message to database
        self.db_manager.save_message(self.current_conversation_id, "user", question)

        # Emit signal for user message
        self.message_received.emit("user", question)

        # Prepare system message with base instructions and any attachments
        system_content = "You are a helpful assistant."

        # 获取附件中的内容，添加到系统消息中
        attachments_content = self.get_attachment_content(self.current_conversation_id)
        system_content += attachments_content if attachments_content else ""

        # Prepare messages with history and system content
        messages = [{"role": "system", "content": system_content}]

        # 获取历史对话，并添加到消息列表中
        conversation_history = self.db_manager.get_conversation_history(
            self.current_conversation_id, 5
        )
        messages.extend(conversation_history)

        # 如果有图片，就使用视觉模型进行解读
        if self.current_conversation_id is not None:
            # Check for image attachments that need special handling
            latest_attachment = self.db_manager.get_latest_attachment(
                self.current_conversation_id
            )

            if (
                latest_attachment
                and latest_attachment[2] == "image"
            ):
                if self.model_manager.current_model != "qwen-vl-plus":
                    # 警告用户，图片上传功能目前只支持 QWen-VL-Plus
                    self.message_received.emit(
                        "assistant",
                        "Warning: Image upload is currently only supported for QWen-VL-Plus.",
                    )
                    return

                attachment_id, file_path, file_type, file_data = latest_attachment
                # For vision models, we need to format the message with image content
                content_list = [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{file_type};base64,{self._encode_image_to_base64(file_data)}"
                        },
                    },
                ]
                # Add the message with the special content format for vision models
                vision_message: Dict[str, Any] = {
                    "role": "user",
                    "content": content_list,
                }
                messages.append(vision_message)
            else:
                # Regular text message
                messages.append({"role": "user", "content": question})
        else:
            # Regular text message
            messages.append({"role": "user", "content": question})

        # Create and start worker thread
        self.is_generating = True
        self.is_first_chunk = True
        self.worker = LLMWorker(self.model_manager, messages)
        self.worker.new_content.connect(self.handle_llm_response)
        # Connect start and finish signals
        self.worker.started_signal.connect(self.on_llm_start)
        self.worker.finished_signal.connect(self.on_llm_finish)
        self.worker.start()

    def get_attachment_content(self, conversation_id):
        attachments_content = ""

        # Get all attachments for this conversation (not just the latest)
        attachments = self.db_manager.get_all_attachments(conversation_id)

        if attachments:
            attachments_content = (
                "\n\nReference the following files when answering:\n\n"
            )
            for attachment_id, file_path, file_type, file_data in attachments:
                if file_type != "image":
                    if file_path and not file_data:
                        # If we have a file path (local file) but no binary data
                        file_content = MarkItDown().convert(file_path)
                    elif file_data:
                        # Create a temporary file with appropriate extension
                        file_ext = (
                            os.path.splitext(file_path)[1] if file_path else ".txt"
                        )
                        with tempfile.NamedTemporaryFile(
                            suffix=file_ext, delete=False
                        ) as temp_file:
                            temp_file.write(file_data)
                            temp_path = temp_file.name

                        # Use the temporary file path for conversion
                        try:
                            file_content = MarkItDown().convert(temp_path)
                        finally:
                            # Clean up temporary file
                            if os.path.exists(temp_path):
                                os.unlink(temp_path)
                    else:
                        # Fallback if neither is available
                        file_content = "Content unavailable"
                    # Add file information to system context
                    attachments_content += f"--- File: {file_path} (Type: {file_type}) ---\n{file_content}\n\n"
        return attachments_content

    def _encode_image_to_base64(self, image_data):
        """
        Encode image data to base64 string

        Args:
            image_data: Binary image data

        Returns:
            Base64 encoded string
        """
        import base64

        return base64.b64encode(image_data).decode("utf-8")

    def handle_llm_response(self, text):
        """
        Handle streaming response from LLM
        """
        chat_id = self.current_conversation_id

        # Initialize buffer for this response if it's the first chunk
        if self.is_first_chunk:
            self.markdown_buffers[chat_id] = text
            self.is_first_chunk = False
        else:
            self.markdown_buffers[chat_id] += text

        # Emit signal with current accumulated text
        self.message_received.emit("assistant", self.markdown_buffers[chat_id])

    def on_llm_start(self):
        """
        Handle LLM generation start
        """
        self.is_generating = True
        self.generation_started.emit()

    def on_llm_finish(self):
        self.is_generating = False

        # Save the complete assistant response to the database
        if self.current_conversation_id in self.markdown_buffers:
            assistant_response = self.markdown_buffers[self.current_conversation_id]
            # Save to database
            self.db_manager.save_message(
                self.current_conversation_id, "assistant", assistant_response
            )

            # Refresh the conversation history list
            self.load_conversation_history()

        self.generation_finished.emit()

    def stop_generation(self):
        if self.worker and self.is_generating:
            self.worker.stop()
            self.is_generating = False
            self.generation_finished.emit()

    def load_conversation_history(self):
        """
        Load all conversations
        """
        # Get all conversations from the database
        conversations = self.db_manager.get_conversations()

        # Create a list to store the first question of each conversation
        first_questions = []
        conversation_ids = []

        # For each conversation, get the first user message
        for conv_id, timestamp, session_id in conversations:
            messages = self.db_manager.get_messages(conv_id)

            # Find the first user message
            for role, content, msg_timestamp in messages:
                if role == "user":
                    # Truncate long messages for display
                    display_content = (
                        content[:50] + "..." if len(content) > 50 else content
                    )
                    display_content = display_content.replace("\n", "").replace(" ", "")
                    first_questions.append(display_content)
                    conversation_ids.append(conv_id)
                    break

        # Store conversation IDs for later use
        self.conversation_ids = conversation_ids

        # Emit signal with conversation history
        self.conversation_history_updated.emit(
            list(zip(conversation_ids, first_questions))
        )

    def select_conversation(self, index):
        """
        Select a conversation from history
        """
        if 0 <= index < len(self.conversation_ids):
            # Get the corresponding conversation ID
            selected_conversation_id = self.conversation_ids[index]

            # Update the current conversation ID
            self.current_conversation_id = selected_conversation_id

            # Load the selected conversation messages
            self.load_conversation_messages(selected_conversation_id)

    def load_conversation_messages(self, conversation_id):
        """
        Load and emit messages for a selected conversation
        """
        # Get all messages for the conversation
        messages = self.db_manager.get_messages(conversation_id)

        # Emit signal with messages
        self.conversation_loaded.emit(messages)

    def create_new_conversation(self):
        """
        Create a new conversation and switch to it
        """
        self.current_conversation_id = self.db_manager.create_conversation()

        # Emit signal to clear the chat display
        self.conversation_loaded.emit([])

        # Refresh the conversation history list
        self.load_conversation_history()

    def clear_all_history(self):
        """
        Clear all conversations and messages from the database
        """
        self.db_manager.clear_all_history()

        # Create a new conversation
        self.current_conversation_id = self.db_manager.create_conversation()

        # Emit signal to clear the chat display
        self.conversation_loaded.emit([])

        # Refresh the conversation history list
        self.load_conversation_history()

    def clear_selected_conversations(self, conversation_ids):
        """
        Clear selected conversations and their messages from the database

        Args:
            conversation_ids: List of conversation IDs to clear
        """
        # Check if current conversation is in the list to be deleted
        current_conversation_deleted = self.current_conversation_id in conversation_ids

        # Clear the selected conversations
        self.db_manager.clear_selected_conversations(conversation_ids)

        # If current conversation was deleted, create a new one
        if current_conversation_deleted:
            self.current_conversation_id = self.db_manager.create_conversation()
            # Emit signal to clear the chat display
            self.conversation_loaded.emit([])

        # Refresh the conversation history list
        self.load_conversation_history()

    def save_attachment(self, file_path, file_type):
        """
        Save an attachment to the database
        """
        if self.current_conversation_id:

            return self.db_manager.save_attachment(
                self.current_conversation_id, file_path, file_type
            )
        else:
            return None
