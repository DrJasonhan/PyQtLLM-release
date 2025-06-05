import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from src.ui.main_window import MainWindow


def main():
    """Main application entry point"""
    
    # Create application
    app = QApplication(sys.argv)
    
    # Set application icon
    app.setWindowIcon(QIcon("resources/icons/yinhexi.png"))
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
