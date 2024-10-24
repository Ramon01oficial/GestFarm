# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_login_ui(object):
    def setupUi(self, login_ui):
        if not login_ui.objectName():
            login_ui.setObjectName(u"login_ui")
        login_ui.resize(750, 608)
        login_ui.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.frame = QFrame(login_ui)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 160, 561, 361))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 1,0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(140, 60, 251, 31))
        font = QFont()
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(180, 240, 171, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.txtpassword = QLineEdit(self.frame)
        self.txtpassword.setObjectName(u"txtpassword")
        self.txtpassword.setGeometry(QRect(140, 150, 251, 31))
        self.txtpassword.setFont(font)
        self.txtpassword.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtpassword.setEchoMode(QLineEdit.Password)
        self.txtpassword.setAlignment(Qt.AlignCenter)
        self.label = QLabel(login_ui)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 30, 191, 141))
        self.label.setPixmap(QPixmap(u"../../../Downloads/icon_login.png"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.frame.raise_()
        QWidget.setTabOrder(self.txt_user, self.txtpassword)
        QWidget.setTabOrder(self.txtpassword, self.btn_login)

        self.retranslateUi(login_ui)

        QMetaObject.connectSlotsByName(login_ui)
    # setupUi

    def retranslateUi(self, login_ui):
        login_ui.setWindowTitle(QCoreApplication.translate("login_ui", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("login_ui", u"User", None))
        self.btn_login.setText(QCoreApplication.translate("login_ui", u"Login", None))
        self.txtpassword.setPlaceholderText(QCoreApplication.translate("login_ui", u"Password", None))
        self.label.setText("")
    # retranslateUi

