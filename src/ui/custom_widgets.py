from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QTimer


class AutoResizingTextEdit(QTextEdit):
    """
    A custom QTextEdit that automatically adjusts its height based on content.
    Supports Markdown rendering.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document().contentsChanged.connect(self.adjust_height)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setMinimumHeight(0)
        self.setMaximumHeight(0)
        # Enable rich text to support Markdown rendering
        self.setAcceptRichText(True)

    def setMarkdown(self, text):
        # Call parent's setMarkdown method to parse and display Markdown text
        super().setMarkdown(text)
        # Use a timer to ensure the document has been properly rendered
        QTimer.singleShot(100, self.adjust_height)

    def adjust_height(self):
        # Get document height and set text box height
        doc_height = self.document().size().toSize().height()
        margins = self.contentsMargins()
        height = doc_height + margins.top() + margins.bottom() + 10

        self.setMinimumHeight(int(height))
        self.setMaximumHeight(int(height))


class DialogClearHistoryConversation(QMessageBox):
    """A reusable confirmation dialog that inherits from QMessageBox."""

    def __init__(
        self,
        parent=None,
        title="Confirm",
        message="Are you sure to clear the historical records?",
        default_button=QMessageBox.StandardButton.No,
    ):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setText(message)
        self.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        self.setDefaultButton(default_button)
        self.setIcon(QMessageBox.Icon.Question)

    def exec(self):
        """Execute the dialog and return the result."""
        return super().exec()
