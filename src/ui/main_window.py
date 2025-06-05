import os
import re
from PySide6.QtGui import (
    QDragEnterEvent,
    QDropEvent,
    Qt,
    QKeyEvent,
    QMouseEvent,
    QIcon,
    QStandardItemModel,
    QStandardItem,
    QFocusEvent,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPlainTextEdit,
    QMessageBox,
)
from PySide6.QtCore import QPropertyAnimation, QTimer, QByteArray

from src.ui.custom_widgets import *
from src.ui.UI import Ui_MainWindow
from src.ui.styles import *
from src.controllers.chat_controller import ChatController


class MainWindow(QMainWindow):
    """
    Main window class that handles the UI (View) part of the application.
    Communicates with the Controller to handle business logic.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize controller with model manager
        self.controller = ChatController()

        # Connect controller signals to UI update methods
        self.controller.message_received.connect(self.display_message)
        self.controller.generation_started.connect(self.on_generation_started)
        self.controller.generation_finished.connect(self.on_generation_finished)
        self.controller.conversation_loaded.connect(self.display_conversation)
        self.controller.conversation_history_updated.connect(
            self.update_conversation_list
        )

        # 预制一个 LLM，方便测试
        self.controller.set_api_key(self.ui.lineEdit_api_key.text())
        self.controller.register_model("QWen")
        self.controller.set_current_model("qwen-vl-plus")
        # Connect API key input
        self.ui.lineEdit_api_key.textChanged.connect(
            lambda: self.controller.set_api_key(self.ui.lineEdit_api_key.text())
        )

        # Hide title bar and keep window on top
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        self.statusBar().hide()

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Position window on the right side of the screen
        self._position_window()

        # Create main layout container
        self._setup_chat_container()

        # Connect UI events
        self._connect_events()

        # Initialize settings panel state
        self.settings_visible = False
        self.ui.stackedWidget_setting.setVisible(False)

        # Initialize file storage
        self.files = []
        self.upload_label = ""

        # Set up drag and drop for file upload
        self._setup_drag_drop()

        # Load conversation history
        self.controller.load_conversation_history()

    def _position_window(self):
        """Position the window on the right side of the screen"""
        screen = self.screen()
        screen_geometry = screen.geometry()
        window_size = self.geometry()
        new_height = int(screen_geometry.height() * 4 / 5)
        y = (screen_geometry.height() - new_height) // 2
        right_margin = 23
        x = screen_geometry.width() - window_size.width() - right_margin
        self.setGeometry(x, y, window_size.width(), new_height)

    def _setup_chat_container(self):
        """Set up the chat container and layout"""
        self.container = QWidget()
        self.main_layout = QVBoxLayout(self.container)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_boxes = []
        self.ui.scrollArea.setWidget(self.container)

    def _connect_events(self):
        """Connect UI events to handlers"""
        # 主界面按钮
        self.ui.pushButton_close.clicked.connect(self.close_window)
        self.ui.pushButton_send_question.clicked.connect(self.handle_chatting)
        self.ui.pushButton_new_conversation.clicked.connect(
            self.create_new_conversation
        )
        self.original_focusInEvent = self.ui.plainTextEdit_ask.focusInEvent
        self.ui.plainTextEdit_ask.focusInEvent = self._plainTextEdit_ask_focusInEvent
        self.ui.plainTextEdit_ask.focusOutEvent = self._plainTextEdit_ask_focusOutEvent

        # Tab 控件中的按钮
        self.ui.pushButton_clear_history.clicked.connect(self.clear_history)
        self.ui.comboBox_model_provider.currentTextChanged.connect(
            self.on_model_provider_changed
        )
        self.ui.comboBox_model_list.currentTextChanged.connect(self.on_model_changed)
        self.ui.pushButton_select_all_historical_conversation.clicked.connect(self.select_and_cancel_all)

        # 面板 1: 账户设置
        self.ui.pushButton_settings.clicked.connect(self.open_panel)
        self.ui.pushButton_hide_panel_0.clicked.connect(self.close_panel)

        # 面板 2: 模型设置
        self.ui.pushButton_model.clicked.connect(self.open_panel)
        self.ui.pushButton_hide_panel_1.clicked.connect(self.close_panel)

        # 面板 3: 文件上传
        self.ui.pushButton_upload_file.clicked.connect(self.open_panel)
        self.ui.pushButton_hide_panel_2.clicked.connect(self.close_panel)
        self.ui.pushButton_remove_attachment.clicked.connect(self.remove_attachment)

        # 鼠标与键盘
        self.ui.plainTextEdit_ask.keyPressEvent = self.plainTextEdit_ask_keyPressEvent
        self.ui.label.mousePressEvent = self.move_window
        self.ui.label.mouseMoveEvent = self.on_mouse_move

    def on_model_provider_changed(self, provider):
        """Handle model provider selection change"""
        # Clear existing models and combobox
        self.controller.model_manager.clear_models()
        self.ui.comboBox_model_list.clear()

        llm_list = self.controller.register_model(provider)
        self.ui.comboBox_model_list.addItems(llm_list)
        self.on_model_changed()

        
    def on_model_changed(self):
        # Connect model selection if we have models
        llm_name = self.ui.comboBox_model_list.currentText()
        self.controller.set_current_model(llm_name)
        
    def _plainTextEdit_ask_focusInEvent(self, e: QFocusEvent):
        """Handle focus in event for the ask text edit"""
        self.ui.plainTextEdit_ask.setPlaceholderText("")
        self.original_focusInEvent(e)

    def _plainTextEdit_ask_focusOutEvent(self, e: QFocusEvent):
        """Handle focus out event for the ask text edit"""
        self.ui.plainTextEdit_ask.setPlaceholderText("Please input your question ...")

    def _setup_drag_drop(self):
        """Set up drag and drop for file upload"""
        self.ui.widget_upload_file.dragEnterEvent = self.dragEnterEvent
        self.ui.widget_upload_file.dragLeaveEvent = self.dragLeaveEvent
        self.ui.widget_upload_file.dropEvent = self.dropEvent

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter events for file upload"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.ui.label_upload_file.setStyleSheet(label_drag_enter)

    def dragLeaveEvent(self, event):
        """Handle drag leave events for file upload"""
        self.ui.label_upload_file.setStyleSheet(label_drag_leave)

    def dropEvent(self, event: QDropEvent):
        """Handle drop events for file upload"""
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()

            # Get all file URLs
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path:
                    self.files.append(file_path)

            # Update display
            self.ui.label_upload_file.setText(
                f"已加载 {len(self.files)} 个文件\n{', '.join(self.files[-3:])}"
            )

            # Update style
            self.ui.label_upload_file.setStyleSheet(label_drop)

    def remove_attachment(self):
        # 删除dropEvent后上传的附件
        self.files = []  # Clear stored files
        self.ui.label_upload_file.setText("拖拽文件到此处上传")
        self.ui.label_upload_file.setStyleSheet(label_drag_leave)

    def confirm_upload_attachment(self, question):
        """
        对于dropEvent成功上传的文件（目前主要是image）将其上传到数据库中，并关联上当前的对话
        """
        # Process each uploaded file
        for file_path in self.files:
            # Determine file type based on extension
            file_extension = os.path.splitext(file_path)[1].lower()

            # Currently only supporting images
            if file_extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                file_type = "image"
            else:
                file_type = "file"

                # Save attachment to database
            attachment_id = self.controller.save_attachment(file_path, file_type)

            if attachment_id:
                # Create a message to indicate file upload
                file_name = os.path.basename(file_path)
                self.controller.send_message(
                    f"[Uploaded file: {file_name}] \n\n {question}"
                )

        # Clear the files list after processing
        self.files = []
        self.ui.label_upload_file.setText("拖拽文件到此处上传")
        self.ui.label_upload_file.setStyleSheet(label_drag_leave)

        # Close the panel
        self.close_panel()

    def open_panel(self):
        """Open settings panel"""
        # Get the sender button
        sender = self.sender()

        # Create height animation
        self.settings_animation = QPropertyAnimation(
            self.ui.stackedWidget_setting, QByteArray(b"maximumHeight")
        )
        self.settings_animation.setDuration(100)  # Animation duration in ms

        # Show settings panel
        self.ui.stackedWidget_setting.setVisible(True)

        # Set the appropriate page index based on the button
        if sender == self.ui.pushButton_model:
            self.ui.stackedWidget_setting.setCurrentIndex(2)
        elif sender == self.ui.pushButton_upload_file:
            self.ui.stackedWidget_setting.setCurrentIndex(1)
        else:  # Default to settings button
            self.ui.stackedWidget_setting.setCurrentIndex(0)

        if self.settings_visible:
            return

        # Get actual content height
        content_height = 200
        # Set animation from 0 to actual height
        self.settings_animation.setStartValue(0)
        self.settings_animation.setEndValue(content_height)

        # Start animation
        self.settings_animation.start()
        self.settings_visible = True

    def close_panel(self):
        """Close settings panel"""
        self.settings_visible = False

        # Create height animation
        self.settings_animation = QPropertyAnimation(
            self.ui.stackedWidget_setting, QByteArray(b"maximumHeight")
        )
        self.settings_animation.setDuration(100)  # Animation duration in ms

        # Set animation from current height to 0
        self.settings_animation.setStartValue(200)
        self.settings_animation.setEndValue(0)

        # Define what happens when animation finishes
        def on_animation_finished():
            # Hide the panel
            self.ui.stackedWidget_setting.setVisible(False)
            # Readjust chat display to ensure proper layout after panel closes
            QTimer.singleShot(50, self.adjust_chat_display)

        # Connect finished signal to our handler
        self.settings_animation.finished.connect(on_animation_finished)
        self.settings_animation.start()

    def plainTextEdit_ask_keyPressEvent(self, e: QKeyEvent):
        """Handle key press events in the question text edit"""
        # Check if Enter key was pressed without modifiers
        if e.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter) and not e.modifiers():
            # Trigger send message method
            self.send_message()
        else:
            # Handle other key events normally
            QPlainTextEdit.keyPressEvent(self.ui.plainTextEdit_ask, e)

    def handle_chatting(self):
        """Handle chat button click"""
        if self.controller.is_generating:
            self.controller.stop_generation()
        else:
            self.send_message()

    def send_message(self):
        """Get user input and send to controller"""
        question = self.ui.plainTextEdit_ask.toPlainText()

        if not self.files:
            if not question.strip():
                return
            self.ui.plainTextEdit_ask.clear()
            self.controller.send_message(question)
        else:
            self.confirm_upload_attachment(question)
            self.ui.plainTextEdit_ask.clear()

    def display_message(self, role, content):
        """在聊天区域添加一个消息框"""
        # For user messages, create a new chat box
        if role == "user":
            chat_box = AutoResizingTextEdit()
            chat_box.setReadOnly(True)
            chat_box.setMarkdown(f"### {self.ui.lineEdit_username.text()}:  \n{content}")
            # Delay calling adjust_height method
            QTimer.singleShot(10, lambda: chat_box.adjust_height())
            self.chat_boxes.append(chat_box)
            self.main_layout.addWidget(chat_box)

            # Create a new chat box for the assistant's response
            assistant_box = AutoResizingTextEdit()
            assistant_box.setReadOnly(True)
            assistant_box.setMarkdown(f"### {self.ui.lineEdit_AI_name.text()}:  \n")
            self.chat_boxes.append(assistant_box)
            self.main_layout.addWidget(assistant_box)
            self.adjust_chat_display()

        # For assistant messages, update the last chat box
        elif role == "assistant" and self.chat_boxes:
            chat_box = self.chat_boxes[-1]
            chat_box.setMarkdown(f"### {self.ui.lineEdit_AI_name.text()}:  \n{content}")
            self.adjust_chat_display()

    def adjust_chat_display(self):
        """Adjust the chat display container and scroll position"""
        # Adjust height of all chat boxes
        for chat_box in self.chat_boxes:
            chat_box.adjust_height()

        scroll_bar = self.ui.scrollArea.verticalScrollBar()

        # Calculate total height of all chat boxes
        total_chat_box_height = sum([box.height() for box in self.chat_boxes])

        # Add some padding to ensure there's space between messages
        total_chat_box_height += len(self.chat_boxes) * 10

        # Get the current container height
        container_height = self.container.height()

        # If total height of chat boxes exceeds container height, expand container
        # Use a more dynamic approach to determine new height
        if total_chat_box_height > container_height - 150:
            # Set container height to be slightly larger than total chat box height
            new_height = total_chat_box_height + 200  # Add extra space for new messages
            self.container.setFixedHeight(new_height)

        # Smooth scrolling
        target_value = scroll_bar.maximum()
        current_value = scroll_bar.value()
        if (target_value - current_value) > 800:
            scroll_bar.setValue(target_value)
        else:
            self.scroll_anim = QPropertyAnimation(scroll_bar, QByteArray(b"value"))
            self.scroll_anim.setDuration(150)
            self.scroll_anim.setStartValue(current_value)
            self.scroll_anim.setEndValue(target_value)
            self.scroll_anim.start()

    def on_generation_started(self):
        """Handle LLM generation start"""
        # Change button text to Stop when generation starts
        icon5 = QIcon(QIcon.fromTheme("process-stop"))
        self.ui.pushButton_send_question.setIcon(icon5)
        self.ui.pushButton_send_question.setStyleSheet("border: 2px solid #F87171;")

    def on_generation_finished(self):
        """Handle LLM generation finish"""
        # Change button text back to Send when generation completes
        icon5 = QIcon(QIcon.fromTheme("document-send"))
        self.ui.pushButton_send_question.setIcon(icon5)
        self.ui.pushButton_send_question.setStyleSheet("border: 1px solid #ffffff;")

    def close_window(self):
        """Close the application"""
        self.close()

    def closeEvent(self, event):
        """Handle window close event"""
        # Perform cleanup operations here
        event.accept()

    def on_mouse_move(self, ev: QMouseEvent):
        """Handle mouse move events for window dragging"""
        if ev.buttons() & Qt.MouseButton.LeftButton:
            self.move(ev.globalPosition().toPoint() - self.drag_position)

    def move_window(self, ev: QMouseEvent):
        """Handle mouse press events for window dragging"""
        if ev.button() == Qt.MouseButton.LeftButton:
            self.drag_position = (
                ev.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )
            ev.accept()

    def update_conversation_list(self, conversations):
        """Update the conversation history list view with checkable items

        Args:
            conversations: List of tuples (conversation_id, display_text)
        """
        # Store conversation IDs for later use
        self.conversation_ids, display_texts = (
            zip(*conversations) if conversations else ([], [])
        )

        # Create a standard item model for the listView with checkable items
        model = QStandardItemModel()

        # Add items to the model with checkboxes
        for text in display_texts:
            item = QStandardItem(text)
            item.setCheckable(True)
            model.appendRow(item)

        # Set the model to the listView
        self.ui.listView_history.setModel(model)

        # Connect the selection signal after setting the model
        if self.ui.listView_history.selectionModel():
            # 历史对话双击事件。注意：Blocksignal 避免在连接事件处理器的过程中，意外触发其他信号处理器
            self.ui.listView_history.selectionModel().blockSignals(True)
            self.ui.listView_history.doubleClicked.connect(
                self.on_conversation_double_clicked
            )
            self.ui.listView_history.selectionModel().blockSignals(False)

    def on_conversation_double_clicked(self, index):
        """Handle selection of a conversation from the history list"""

        self.ui.tabWidget.setCurrentIndex(0)

        if index:
            selected_index = index.row()
            self.controller.select_conversation(selected_index)

    def clear_chat_display(self):
        """Clear the chat display area"""
        # Remove all chat boxes from the layout
        for chat_box in self.chat_boxes:
            self.main_layout.removeWidget(chat_box)
            chat_box.deleteLater()

        self.chat_boxes = []

    def create_new_conversation(self):
        """Create a new conversation and switch to it"""
        # Tell controller to create a new conversation
        self.controller.create_new_conversation()
        self.clear_chat_display()
        self.container.setFixedHeight(0)

    def display_conversation(self, messages):
        """显示历史对话

        Args:
            messages: List of (role, content, timestamp) tuples
        """
        # Clear the current chat display
        self.clear_chat_display()

        if not messages:
            return

        # Reset container height to ensure proper layout
        self.container.setFixedHeight(self.ui.scrollArea.height())

        # Display each message in the chat area
        for role, content, timestamp in messages:
            # Create a chat box for the message
            chat_box = AutoResizingTextEdit()
            chat_box.setReadOnly(True)

            if role == "user":
                chat_box.setMarkdown(f"### {self.ui.lineEdit_username.text()}:  \n{content}")
            elif role == "assistant":
                chat_box.setMarkdown(f"### {self.ui.lineEdit_AI_name.text()}:  \n{content}")
            self.chat_boxes.append(chat_box)
            self.main_layout.addWidget(chat_box)

            # Adjust height for this specific chat box
            chat_box.adjust_height()

        # After all messages are added, do a final adjustment
        QTimer.singleShot(100, self.adjust_chat_display)
    def select_and_cancel_all(self):
        """全选或取消全选历史对话"""
        # Get the model from the list view
        model = self.ui.listView_history.model()

        if not model or model.rowCount() == 0:
            return

        # Check if all items are checked
        all_checked = all(
            model.item(row).checkState() == Qt.CheckState.Checked # type:ignore
            for row in range(model.rowCount())
        )

        # Set check state for all items based on current state
        new_check_state = (
            Qt.CheckState.Unchecked
            if all_checked
            else Qt.CheckState.Checked
        )
        for row in range(model.rowCount()):
            item = model.item(row) #type:ignore
            item.setCheckState(new_check_state)
    def clear_history(self):
        """清理选中的历史对话记录"""
        # Get the model from the list view
        model = self.ui.listView_history.model()

        if not model or model.rowCount() == 0:
            return

        # Check if any items are checked
        selected_conversation_ids = []
        for row in range(model.rowCount()):
            item = model.item(row)  # type:ignore
            if item and item.checkState() == Qt.CheckState.Checked:
                # Get the corresponding conversation ID
                if row < len(self.conversation_ids):
                    selected_conversation_ids.append(self.conversation_ids[row])

        # If no items are checked, show a message and return
        if not selected_conversation_ids:
            QMessageBox.warning(
                self, "No Conversations Selected", "Please select at least one conversation to delete."
            )
            return

        # Show confirmation dialog
        dialog = DialogClearHistoryConversation(self)
        if dialog.exec() == QMessageBox.StandardButton.Yes:
            # Tell controller to clear selected conversations
            self.controller.clear_selected_conversations(selected_conversation_ids)
            if self.controller.current_conversation_id is None:
                self.clear_chat_display()
