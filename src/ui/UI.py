# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import src.ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(383, 716)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(u"applications-science"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* \u57fa\u672c\u6837\u5f0f */\n"
"QMainWindow, QWidget {\n"
"    background-color: #f5f5f7;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"background-color: #f8f8f8;\n"
"border-radius: 10px;\n"
"border: 1px solid #d0d0d0;\n"
"padding: 6px, 8px;\n"
"}\n"
"\n"
"QScrollArea > QWidget {\n"
"    background-color: #f8f8f8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget {\n"
"    background-color: #f8f8f8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QScrollArea > .QWidget > * {\n"
"    background-color: #f8f8f8;\n"
"}\n"
"\n"
"\n"
"/* \u6309\u94ae\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 12px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f9f9f9;\n"
"    border-color: #d5d5d5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"/* \u5220\u9664"
                        "\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton#deleteButton, QPushButton[objectName*=\"delete\"], QPushButton[objectName*=\"remove\"] {\n"
"    color: #e95c63;\n"
"}\n"
"\n"
"QPushButton#deleteButton:hover, QPushButton[objectName*=\"delete\"]:hover, QPushButton[objectName*=\"remove\"]:hover {\n"
"    background-color: #fff8f8;\n"
"    color: #d64550;\n"
"}\n"
"\n"
"/* \u6587\u672c\u6846\u6837\u5f0f */\n"
"QTextEdit, QLineEdit {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px;\n"
"    border-left: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
""
                        "    width: 8px;\n"
"    height: 8px;\n"
"    border-top: 5px solid #a0a0a0;\n"
"    border-right: 4px solid transparent;\n"
"    border-left: 4px solid transparent;\n"
"}\n"
"\n"
"/* \u83dc\u5355\u6837\u5f0f */\n"
"QMenuBar {\n"
"    background-color: #f5f5f7;\n"
"    border-bottom: 1px solid #e8e8e8;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e8e8e8;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: #f5f5f7;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #d0d0d0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u9875\u6837\u5f0f */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #e2e2e2;\n"
"    background-color: #ffffff;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar:"
                        ":tab {\n"
"    background-color: #f0f0f2;\n"
"    color: #707070;\n"
"    padding: 6px 12px;\n"
"    border: 1px solid #e8e8e8;\n"
"    border-bottom: none;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"}\n"
"\n"
"/* \u590d\u9009\u6846\u548c\u5355\u9009\u6309\u94ae */\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border-radius: 3px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 8px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6495ed;\n"
"    border-color: #6495ed;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 4px solid #6495ed;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"QLabel {\n"
"           /* color: white;*/\n"
"        }")
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_3.addWidget(self.label)

        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy2)
        self.pushButton_close.setMinimumSize(QSize(34, 32))
        self.pushButton_close.setMaximumSize(QSize(34, 16777215))
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #808080;  /* \u4e2d\u7070\u8272\u6587\u5b57\uff0c\u7b80\u7ea6\u98ce\u683c */\n"
"    border: none;\n"
"    text-align: center;    \n"
"    width: 10px;\n"
"    min-width: 10px;\n"
"    max-width: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 0.1);  /* \u9f20\u6807\u60ac\u505c\u65f6\u663e\u793a\u6de1\u7070\u8272\u80cc\u666f */\n"
"    color: #4d4d4d;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6587\u5b57\u53d8\u4e3a\u6df1\u7070\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 0.2);  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u66f4\u6df1\u7684\u7070\u8272 */\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.pushButton_close.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_close)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"        border: 0px;\n"
"        margin: 0px;\n"
"        padding: 0px;\n"
"border-radius: 5px;\n"
"    }")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_current_conversation = QWidget()
        self.tab_current_conversation.setObjectName(u"tab_current_conversation")
        self.verticalLayout_2 = QVBoxLayout(self.tab_current_conversation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab_current_conversation)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border-radius: 5px;\n"
"    padding: 2px 6px;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 339, 228))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        icon2 = QIcon(QIcon.fromTheme(u"user-available"))
        self.tabWidget.addTab(self.tab_current_conversation, icon2, "")
        self.tab_history_conversation = QWidget()
        self.tab_history_conversation.setObjectName(u"tab_history_conversation")
        self.verticalLayout_4 = QVBoxLayout(self.tab_history_conversation)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView_history = QListView(self.tab_history_conversation)
        self.listView_history.setObjectName(u"listView_history")
        self.listView_history.setStyleSheet(u"QListView {\n"
"    background-color: #f8f9fa;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-family: 'Microsoft YaHei', 'Segoe UI', Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QListView::item {\n"
"    border-bottom: 1px solid #eeeeee;\n"
"    padding: 8px;\n"
"    margin: 2px 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #e7f3ff;\n"
"    color: #0078d7;\n"
"    border-bottom: 2px solid #0078d7;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c0c0c0;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a0a0a0;\n"
"}\n"
"\n"
""
                        "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.listView_history.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_history.setViewMode(QListView.ViewMode.ListMode)

        self.verticalLayout_3.addWidget(self.listView_history)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_select_all_historical_conversation = QPushButton(self.tab_history_conversation)
        self.pushButton_select_all_historical_conversation.setObjectName(u"pushButton_select_all_historical_conversation")
        icon3 = QIcon(QIcon.fromTheme(u"format-justify-fill"))
        self.pushButton_select_all_historical_conversation.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.pushButton_select_all_historical_conversation)

        self.pushButton_clear_history = QPushButton(self.tab_history_conversation)
        self.pushButton_clear_history.setObjectName(u"pushButton_clear_history")
        self.pushButton_clear_history.setStyleSheet(u"QPushButton#deleteButton, QPushButton[objectName*=\"delete\"], QPushButton[objectName*=\"remove\"] {\n"
"    background-color: #ffffff;\n"
"    color: #e95c63;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: 500;\n"
"    font-family: \"SF Pro Display\", -apple-system, BlinkMacSystemFont, sans-serif;\n"
"    font-size: 13px;\n"
"    min-height: 34px;\n"
"    min-width: 90px;\n"
"    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);\n"
"}\n"
"\n"
"QPushButton#deleteButton:hover, QPushButton[objectName*=\"delete\"]:hover, QPushButton[objectName*=\"remove\"]:hover {\n"
"    background-color: #fff8f8;\n"
"    border-color: #f0d0d0;\n"
"    color: #d64550;\n"
"}\n"
"\n"
"QPushButton#deleteButton:pressed, QPushButton[objectName*=\"delete\"]:pressed, QPushButton[objectName*=\"remove\"]:pressed {\n"
"    background-color: #fff0f0;\n"
"    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);\n"
"}")
        icon4 = QIcon(QIcon.fromTheme(u"user-trash"))
        self.pushButton_clear_history.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.pushButton_clear_history)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.frame = QFrame(self.tab_history_conversation)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        icon5 = QIcon(QIcon.fromTheme(u"user-away"))
        self.tabWidget.addTab(self.tab_history_conversation, icon5, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"/* \u6781\u7b80\u7248\u672c - \u53ea\u8bbe\u7f6e\u6309\u94ae\u548c\u8f93\u5165\u6846\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 0px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"/* \u5220\u9664\u6309\u94ae */\n"
"QPushButton#sendButton, QPushButton[objectName*=\"pushButton_send_question\"] {\n"
"    color: #e95c63;\n"
"}\n"
"\n"
"/* \u5149\u6807\u60ac\u505c\u6548\u679c */\n"
"QPushButton:hover, QComboBox:hover {\n"
"    border-color: #e2e2e2;\n"
"	background-color: #f5f5f5;  /* \u6dfb\u52a0\u80cc\u666f\u8272\u53d8\u5316 */\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.plainTextEdit_ask = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_ask.setObjectName(u"plainTextEdit_ask")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plainTextEdit_ask.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_ask.setSizePolicy(sizePolicy3)
        self.plainTextEdit_ask.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.plainTextEdit_ask.setFont(font1)
        self.plainTextEdit_ask.setStyleSheet(u"\n"
"QPlainTextEdit {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 0px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"padding: 4px 8px;\n"
"}")
        self.plainTextEdit_ask.setFrameShape(QFrame.Shape.Panel)
        self.plainTextEdit_ask.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.plainTextEdit_ask)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_new_conversation = QPushButton(self.frame_2)
        self.pushButton_new_conversation.setObjectName(u"pushButton_new_conversation")
        self.pushButton_new_conversation.setMaximumSize(QSize(16777215, 43))
        icon6 = QIcon(QIcon.fromTheme(u"list-add"))
        self.pushButton_new_conversation.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_new_conversation)

        self.pushButton_upload_file = QPushButton(self.frame_2)
        self.pushButton_upload_file.setObjectName(u"pushButton_upload_file")
        self.pushButton_upload_file.setMaximumSize(QSize(16777215, 43))
        icon7 = QIcon(QIcon.fromTheme(u"mail-attachment"))
        self.pushButton_upload_file.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_upload_file)

        self.pushButton_model = QPushButton(self.frame_2)
        self.pushButton_model.setObjectName(u"pushButton_model")
        self.pushButton_model.setMaximumSize(QSize(16777215, 43))
        icon8 = QIcon(QIcon.fromTheme(u"emblem-system"))
        self.pushButton_model.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_model)

        self.pushButton_settings = QPushButton(self.frame_2)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setMaximumSize(QSize(16777215, 43))
        icon9 = QIcon(QIcon.fromTheme(u"go-home"))
        self.pushButton_settings.setIcon(icon9)

        self.horizontalLayout.addWidget(self.pushButton_settings)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        icon10 = QIcon(QIcon.fromTheme(u"audio-input-microphone"))
        self.pushButton.setIcon(icon10)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_send_question = QPushButton(self.frame_2)
        self.pushButton_send_question.setObjectName(u"pushButton_send_question")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_send_question.sizePolicy().hasHeightForWidth())
        self.pushButton_send_question.setSizePolicy(sizePolicy4)
        self.pushButton_send_question.setMinimumSize(QSize(0, 30))
        self.pushButton_send_question.setMaximumSize(QSize(67, 50))
        self.pushButton_send_question.setStyleSheet(u"")
        self.pushButton_send_question.setText(u"")
        icon11 = QIcon(QIcon.fromTheme(u"document-send"))
        self.pushButton_send_question.setIcon(icon11)

        self.horizontalLayout.addWidget(self.pushButton_send_question)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.stackedWidget_setting = QStackedWidget(self.centralwidget)
        self.stackedWidget_setting.setObjectName(u"stackedWidget_setting")
        self.stackedWidget_setting.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #f8f8f8;\n"
"    border: 5px solid #e2e2e2;\n"
"    border-radius: 10px;\n"
"    padding: 1px;\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"/* QStackedWidget\u4e2d\u5305\u542b\u7684\u63a7\u4ef6\u6837\u5f0f */\n"
"QStackedWidget QLabel {\n"
"    color: #404040;\n"
"    font-size: 12px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QStackedWidget QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 12px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"QStackedWidget QPushButton:hover {\n"
"    background-color: #f9f9f9;\n"
"    border-color: #d5d5d5;\n"
"}\n"
"\n"
"QStackedWidget QPushButton:pressed {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QStackedWidget QPushButton[objectName*=\"delete\"], QStackedWidget QPushButton[objectName*=\"remove\"] {\n"
"    color: #e95c63;\n"
"}\n"
"\n"
"QStackedWidget QPushButton[objectName*=\"delete\"]:hove"
                        "r, QStackedWidget QPushButton[objectName*=\"remove\"]:hover {\n"
"    background-color: #fff8f8;\n"
"    color: #d64550;\n"
"}\n"
"\n"
"QStackedWidget QSlider::handle {\n"
"    background-color: #6495ed;\n"
"    border-radius: 7px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"}\n"
"\n"
"QStackedWidget QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"    background-color: #e2e2e2;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QStackedWidget QLineEdit {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"QStackedWidget QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QStackedWidget QCheckBox::indicator {\n"
"    border: 1px solid #d0d0d0;\n"
"    background-color: #ffffff;\n"
"    border-radius: 3px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QStackedWidget QCheckBox::indicator:checked {\n"
"    background-color: #6495ed;\n"
"    border-color: #6495ed;\n"
"}\n"
""
                        "\n"
"QStackedWidget QComboBox {\n"
"    background-color: #ffffff;\n"
"    color: #404040;\n"
"    border: 1px solid #e2e2e2;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"QStackedWidget QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px;\n"
"    border-left: none;\n"
"}\n"
"\n"
"QStackedWidget QComboBox::down-arrow {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top: 5px solid #a0a0a0;\n"
"    border-right: 4px solid transparent;\n"
"    border-left: 4px solid transparent;\n"
"}\n"
"\n"
"QStackedWidget QScrollBar:vertical, QStackedWidget QScrollBar:horizontal {\n"
"    background: #f5f5f7;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QStackedWidget QScrollBar::handle:vertical, QStackedWidget QScrollBar::handle:horizontal {\n"
"    background: #d0d0d0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QStackedWidget QScrollBar::add-line, QStackedWidget QScrollBar::sub-line {\n"
""
                        "    height: 0px;\n"
"    width: 0px;\n"
"}")
        self.stackedWidget_setting.setFrameShape(QFrame.Shape.HLine)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_username = QLineEdit(self.page)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setFont(font1)
        self.lineEdit_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_username, 0, 2, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_AI_name = QLineEdit(self.page)
        self.lineEdit_AI_name.setObjectName(u"lineEdit_AI_name")
        self.lineEdit_AI_name.setFont(font1)
        self.lineEdit_AI_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_AI_name, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pushButton_hide_panel_2 = QPushButton(self.page)
        self.pushButton_hide_panel_2.setObjectName(u"pushButton_hide_panel_2")
        self.pushButton_hide_panel_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}")
        icon12 = QIcon(QIcon.fromTheme(u"go-down"))
        self.pushButton_hide_panel_2.setIcon(icon12)

        self.verticalLayout_5.addWidget(self.pushButton_hide_panel_2)

        self.stackedWidget_setting.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_upload_file = QWidget(self.page_3)
        self.widget_upload_file.setObjectName(u"widget_upload_file")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.widget_upload_file.sizePolicy().hasHeightForWidth())
        self.widget_upload_file.setSizePolicy(sizePolicy5)
        self.widget_upload_file.setAcceptDrops(True)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_upload_file)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_upload_file = QLabel(self.widget_upload_file)
        self.label_upload_file.setObjectName(u"label_upload_file")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.label_upload_file.setFont(font2)
        self.label_upload_file.setStyleSheet(u"QLabel {\n"
"                border: 2px dashed #aaa;\n"
"                border-radius: 5px;\n"
"                padding: 20px;\n"
"                background-color: #f8f8f8;\n"
"                font-size: 14px;\n"
"                color: #555;\n"
"            }")
        self.label_upload_file.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_upload_file.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_upload_file)

        self.pushButton_remove_attachment = QPushButton(self.widget_upload_file)
        self.pushButton_remove_attachment.setObjectName(u"pushButton_remove_attachment")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_remove_attachment.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_attachment.setSizePolicy(sizePolicy6)
        self.pushButton_remove_attachment.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.pushButton_remove_attachment)


        self.verticalLayout_9.addWidget(self.widget_upload_file)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_hide_panel_0 = QPushButton(self.page_3)
        self.pushButton_hide_panel_0.setObjectName(u"pushButton_hide_panel_0")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_hide_panel_0.sizePolicy().hasHeightForWidth())
        self.pushButton_hide_panel_0.setSizePolicy(sizePolicy7)
        self.pushButton_hide_panel_0.setMinimumSize(QSize(0, 32))
        self.pushButton_hide_panel_0.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_hide_panel_0.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}")
        self.pushButton_hide_panel_0.setIcon(icon12)

        self.horizontalLayout_2.addWidget(self.pushButton_hide_panel_0)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.stackedWidget_setting.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_3)

        self.comboBox_model_provider = QComboBox(self.page_2)
        self.comboBox_model_provider.addItem("")
        self.comboBox_model_provider.addItem("")
        self.comboBox_model_provider.addItem("")
        self.comboBox_model_provider.setObjectName(u"comboBox_model_provider")
        self.comboBox_model_provider.setFont(font1)
        self.comboBox_model_provider.setEditable(False)
        self.comboBox_model_provider.setFrame(True)

        self.horizontalLayout_7.addWidget(self.comboBox_model_provider)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.comboBox_model_list = QComboBox(self.page_2)
        self.comboBox_model_list.setObjectName(u"comboBox_model_list")
        self.comboBox_model_list.setEditable(False)

        self.horizontalLayout_7.addWidget(self.comboBox_model_list)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_api_key = QLineEdit(self.page_2)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        self.lineEdit_api_key.setStyleSheet(u"QLineEdit {\n"
"                color: #333333;\n"
"                font-size: 12px;\n"
"            }")
        self.lineEdit_api_key.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout_2.addWidget(self.lineEdit_api_key, 2, 3, 1, 1)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSlider_temperature = QSlider(self.page_2)
        self.horizontalSlider_temperature.setObjectName(u"horizontalSlider_temperature")
        self.horizontalSlider_temperature.setValue(25)
        self.horizontalSlider_temperature.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_8.addWidget(self.horizontalSlider_temperature)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.checkBox_function = QCheckBox(self.page_2)
        self.checkBox_function.setObjectName(u"checkBox_function")
        self.checkBox_function.setEnabled(True)
        self.checkBox_function.setChecked(True)

        self.horizontalLayout_8.addWidget(self.checkBox_function)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.pushButton_hide_panel_1 = QPushButton(self.page_2)
        self.pushButton_hide_panel_1.setObjectName(u"pushButton_hide_panel_1")
        self.pushButton_hide_panel_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}")
        self.pushButton_hide_panel_1.setIcon(icon12)

        self.verticalLayout_8.addWidget(self.pushButton_hide_panel_1)

        self.stackedWidget_setting.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget_setting)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 383, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_setting.setCurrentIndex(0)
        self.comboBox_model_provider.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JARVIS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/yinhexi.ico\" width=\"24\" height=\"24\" style=\"vertical-align: top;\"/><span style=\" font-size:14pt; font-weight:700;\">JARVIS </span><span style=\" font-size:12pt; vertical-align:super;\">(Copyrights@</span><a href=\"https://www.polyu.edu.hk/bre/people/academic-staff/dr-shuai-han/\"><span style=\" text-decoration: underline; color:#094fd1; vertical-align:super;\">Shuai</span></a><a href=\"https://www.polyu.edu.hk/bre/people/academic-staff/dr-shuai-han/\"><span style=\" text-decoration: underline; color:#094fd1;\"/></a><span style=\" font-size:12pt; vertical-align:super;\">) </span></p></body></html>", None))
        self.pushButton_close.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_current_conversation), QCoreApplication.translate("MainWindow", u"Current Chat", None))
        self.pushButton_select_all_historical_conversation.setText("")
        self.pushButton_clear_history.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history_conversation), QCoreApplication.translate("MainWindow", u"History Chats", None))
        self.plainTextEdit_ask.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input your question ...", None))
        self.pushButton_new_conversation.setText("")
        self.pushButton_upload_file.setText("")
        self.pushButton_model.setText("")
        self.pushButton_settings.setText("")
        self.pushButton.setText("")
        self.lineEdit_username.setText(QCoreApplication.translate("MainWindow", u"ME", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"AI:", None))
        self.lineEdit_AI_name.setText(QCoreApplication.translate("MainWindow", u"JARVIS", None))
        self.pushButton_hide_panel_2.setText("")
        self.label_upload_file.setText(QCoreApplication.translate("MainWindow", u"Drag and drop files here", None))
        self.pushButton_remove_attachment.setText("")
        self.pushButton_hide_panel_0.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Provider:", None))
        self.comboBox_model_provider.setItemText(0, QCoreApplication.translate("MainWindow", u"Please select", None))
        self.comboBox_model_provider.setItemText(1, QCoreApplication.translate("MainWindow", u"Deepseek", None))
        self.comboBox_model_provider.setItemText(2, QCoreApplication.translate("MainWindow", u"QWen", None))

        self.comboBox_model_provider.setCurrentText(QCoreApplication.translate("MainWindow", u"Please select", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.comboBox_model_list.setCurrentText("")
        self.lineEdit_api_key.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"API-Key:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Function:", None))
        self.checkBox_function.setText("")
        self.pushButton_hide_panel_1.setText("")
    # retranslateUi

