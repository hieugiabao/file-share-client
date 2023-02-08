# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QWidget)
import modules.resources_rc


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(481, 256)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, -10, 471, 281))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 20, 141, 71))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 71, 16))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 170, 71, 16))
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 120, 261, 22))
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 170, 261, 22))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 210, 75, 24))
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 210, 91, 24))
        self.error_label = QLabel(self.widget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(90, 90, 261, 21))
        self.error_label.setStyleSheet(u"color: red;")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(
            QCoreApplication.translate("Login", u"Form", None))
        self.label_3.setText(
            QCoreApplication.translate("Login", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate(
            "Login", u"Username: ", None))
        self.label_2.setText(QCoreApplication.translate(
            "Login", u"Password: ", None))
        self.lineEdit.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("Login", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "Login", u"Go to Register", None))
        self.error_label.setText("")
    # retranslateUi
