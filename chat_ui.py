from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 563)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.page2_widget = QWidget(self.centralwidget)
        self.page2_widget.setObjectName(u"page2_widget")
        self.page2_widget.setGeometry(QRect(10, 10, 829, 556))
        self.frame_chat = QFrame(self.page2_widget)
        self.frame_chat.setObjectName(u"frame_chat")
        self.frame_chat.setGeometry(QRect(0, 0, 821, 481))
        self.frame_chat.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(132, 220, 183);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame {border: 2px solid;} \n"
"QFrame > * {border: 0px;}")
        self.frame_chat.setFrameShape(QFrame.StyledPanel)
        self.frame_chat.setFrameShadow(QFrame.Raised)
        self.chat_frame = QFrame(self.frame_chat)
        self.chat_frame.setObjectName(u"chat_frame")
        self.chat_frame.setGeometry(QRect(20, 20, 781, 51))
        self.chat_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(198, 198, 198);\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame {border: 2px solid;} \n"
"QFrame > * {border: 0px;}\n"
"")
        self.chat_frame.setFrameShape(QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(QFrame.Raised)
        self.text_user = QLabel(self.chat_frame)
        self.text_user.setObjectName(u"text_user")
        self.text_user.setGeometry(QRect(660, 10, 49, 31))
        self.text_bot = QLabel(self.chat_frame)
        self.text_bot.setObjectName(u"text_bot")
        self.text_bot.setGeometry(QRect(70, 10, 49, 31))
        self.bot_image = QFrame(self.chat_frame)
        self.bot_image.setObjectName(u"bot_image")
        self.bot_image.setGeometry(QRect(20, 10, 31, 31))
        self.bot_image.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 248, 41);\n"
"}")
        self.bot_image.setFrameShape(QFrame.StyledPanel)
        self.bot_image.setFrameShadow(QFrame.Raised)
        self.user_image = QFrame(self.chat_frame)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setGeometry(QRect(730, 10, 31, 31))
        self.user_image.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 248, 41);\n"
"}")
        self.user_image.setFrameShape(QFrame.StyledPanel)
        self.user_image.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.page2_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 499, 821, 51))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(198, 198, 198);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame {border: 2px solid;} \n"
"QFrame > * {border: 0px;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.text_input = QLineEdit(self.frame_2)
        self.text_input.setObjectName(u"text_input")
        self.text_input.setGeometry(QRect(10, 10, 641, 31))
        self.text_input.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.send_button = QPushButton(self.frame_2)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(660, 10, 75, 31))
        self.mic_button = QPushButton(self.frame_2)
        self.mic_button.setObjectName(u"mic_button")
        self.mic_button.setGeometry(QRect(740, 10, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_user.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.text_bot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.mic_button.setText(QCoreApplication.translate("MainWindow", u"MIC", None))
