# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(455, 302)
        self.widget = QWidget(Register)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 451, 311))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 191, 51))
        font = QFont()
        font.setPointSize(29)
        font.setBold(True)
        self.label.setFont(font)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 71, 16))
        self.full_name_text = QLineEdit(self.widget)
        self.full_name_text.setObjectName(u"full_name_text")
        self.full_name_text.setGeometry(QRect(90, 100, 261, 22))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 71, 16))
        self.username_text = QLineEdit(self.widget)
        self.username_text.setObjectName(u"username_text")
        self.username_text.setGeometry(QRect(90, 140, 261, 22))
        self.password_text = QLineEdit(self.widget)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setGeometry(QRect(90, 180, 261, 22))
        self.password_text.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_text.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 71, 16))
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 220, 75, 24))
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 220, 75, 24))
        self.error_label = QLabel(self.widget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(90, 70, 261, 16))
        self.error_label.setStyleSheet(u"color: red;")

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Form", None))
        self.label.setText(QCoreApplication.translate("Register", u"REGISTER", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"Full Name: ", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"Username: ", None))
        self.password_text.setText("")
        self.label_3.setText(QCoreApplication.translate("Register", u"Password: ", None))
        self.pushButton.setText(QCoreApplication.translate("Register", u"Register", None))
        self.pushButton_2.setText(QCoreApplication.translate("Register", u"Go to Login", None))
        self.error_label.setText("")
    # retranslateUi

