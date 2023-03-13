# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_action.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_GroupAction(object):
    def setupUi(self, GroupAction):
        if not GroupAction.objectName():
            GroupAction.setObjectName(u"GroupAction")
        GroupAction.resize(753, 520)
        GroupAction.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.stackedWidget = QStackedWidget(GroupAction)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 761, 521))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 130, 250, 230))
        self.widget.setStyleSheet(u"background-color: rgb(42, 48, 52);")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 150, 141, 40))
        self.pushButton_3.setStyleSheet(u"background-color: blue;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 110, 141, 25))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 20, 70, 70))
        icon = QIcon()
        icon.addFile(u"images/images/create.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(80, 70))
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(440, 130, 250, 230))
        self.widget_2.setStyleSheet(u"background-color: rgb(42, 48, 52);")
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 150, 141, 40))
        self.pushButton_4.setStyleSheet(u"background-color: blue;")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 110, 141, 25))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 20, 70, 70))
        icon1 = QIcon()
        icon1.addFile(u"images/images/join.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(70, 70))
        self.error_label = QLabel(self.page)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(90, 70, 591, 17))
        self.error_label.setStyleSheet(u"color: red;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(GroupAction)

        QMetaObject.connectSlotsByName(GroupAction)
    # setupUi

    def retranslateUi(self, GroupAction):
        GroupAction.setWindowTitle(QCoreApplication.translate("GroupAction", u"Frame", None))
        self.pushButton_3.setText(QCoreApplication.translate("GroupAction", u"T\u1ea1o nh\u00f3m", None))
        self.lineEdit_2.setText(QCoreApplication.translate("GroupAction", u"T\u00ean nh\u00f3m", None))
        self.pushButton.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("GroupAction", u"Tham gia b\u1eb1ng m\u00e3", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("GroupAction", u"Nh\u1eadp m\u00e3", None))
        self.pushButton_2.setText("")
        self.error_label.setText("")
    # retranslateUi

