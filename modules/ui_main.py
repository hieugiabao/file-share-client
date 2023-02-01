# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import modules.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1299, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setAcceptDrops(False)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          SET APP STYLESHEET - FULL STYLES HERE\n"
"          DARK THEME - DRACULA COLOR BASED\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          */\n"
"\n"
"          QWidget{\n"
"          color: rgb(221, 221, 221);\n"
"          font: 10pt \"Segoe UI\";\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Tooltip */\n"
"          QToolTip {\n"
"          color: #ffffff;\n"
"          background-color: rgba(33, 37, 43, 180);\n"
"          border: 1px solid rgb(44, 49, 58);\n"
"          background-image: none;\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 2px solid rgb(255, 121, 198);\n"
"          text-align:"
                        " left;\n"
"          padding-left: 8px;\n"
"          margin: 0px;\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Bg App */\n"
"          #bgApp {\n"
"          background-color: rgb(40, 44, 52);\n"
"          border: 1px solid rgb(44, 49, 58);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Left Menu */\n"
"          #leftMenuBg {\n"
"          background-color: rgb(33, 37, 43);\n"
"          }\n"
"          #topLogo {\n"
"          background-color: rgb(33, 37, 43);\n"
"          background-image: url(:/images/images/images/PyDracula.png);\n"
"          background-position: centered;\n"
"          background-repeat: no-repeat;\n"
"          }\n"
"          #titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"          #titleLeftDescription { font: 8pt \"Segoe UI\"; color: r"
                        "gb(189, 147, 249); }\n"
"\n"
"          /* MENUS */\n"
"          #topMenu .QPushButton {\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 22px solid transparent;\n"
"          background-color: transparent;\n"
"          text-align: left;\n"
"          padding-left: 44px;\n"
"          }\n"
"          #topMenu .QPushButton:hover {\n"
"          background-color: rgb(40, 44, 52);\n"
"          }\n"
"          #topMenu .QPushButton:pressed {\n"
"          background-color: rgb(189, 147, 249);\n"
"          color: rgb(255, 255, 255);\n"
"          }\n"
"          #bottomMenu .QPushButton {\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 20px solid transparent;\n"
"          background-color:transparent;\n"
"          text-align: left;\n"
"          padding-left: 44px;\n"
"          }\n"
"          #bottomMenu .QPushBut"
                        "ton:hover {\n"
"          background-color: rgb(40, 44, 52);\n"
"          }\n"
"          #bottomMenu .QPushButton:pressed {\n"
"          background-color: rgb(189, 147, 249);\n"
"          color: rgb(255, 255, 255);\n"
"          }\n"
"          #leftMenuFrame{\n"
"          border-top: 3px solid rgb(44, 49, 58);\n"
"          }\n"
"\n"
"          /* Toggle Button */\n"
"          #toggleButton {\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 20px solid transparent;\n"
"          background-color: rgb(37, 41, 48);\n"
"          text-align: left;\n"
"          padding-left: 44px;\n"
"          color: rgb(113, 126, 149);\n"
"          }\n"
"          #toggleButton:hover {\n"
"          background-color: rgb(40, 44, 52);\n"
"          }\n"
"          #toggleButton:pressed {\n"
"          background-color: rgb(189, 147, 249);\n"
"          }\n"
"\n"
"          /* Title Menu */\n"
"          #titleRightInfo { padd"
                        "ing-left: 10px; }\n"
"\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Extra Tab */\n"
"          #extraLeftBox {\n"
"          background-color: rgb(44, 49, 58);\n"
"          }\n"
"          #extraTopBg{\n"
"          background-color: rgb(189, 147, 249)\n"
"          }\n"
"\n"
"          /* Icon */\n"
"          #extraIcon {\n"
"          background-position: center;\n"
"          background-repeat: no-repeat;\n"
"          background-image: url(:/icons/images/icons/icon_settings.png);\n"
"          }\n"
"\n"
"          /* Label */\n"
"          #extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"          /* Btn Close */\n"
"          #extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;\n"
"          border-radius: 5px; }\n"
"          #extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid;\n"
"          border-radius: 4px; }\n"
"          #extraClose"
                        "ColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid;\n"
"          border-radius: 4px; }\n"
"\n"
"          /* Extra Content */\n"
"          #extraContent{\n"
"          border-top: 3px solid rgb(40, 44, 52);\n"
"          }\n"
"\n"
"          /* Extra Top Menus */\n"
"          #extraTopMenu .QPushButton {\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 22px solid transparent;\n"
"          background-color:transparent;\n"
"          text-align: left;\n"
"          padding-left: 44px;\n"
"          }\n"
"          #extraTopMenu .QPushButton:hover {\n"
"          background-color: rgb(40, 44, 52);\n"
"          }\n"
"          #extraTopMenu .QPushButton:pressed {\n"
"          background-color: rgb(189, 147, 249);\n"
"          color: rgb(255, 255, 255);\n"
"          }\n"
"\n"
"          /*\n"
"          //////////////////////////////////////////////////////////////////////////////////"
                        "///////////////\n"
"          Content App */\n"
"          #contentTopBg{\n"
"          background-color: rgb(33, 37, 43);\n"
"          }\n"
"          #contentBottom{\n"
"          border-top: 3px solid rgb(44, 49, 58);\n"
"          }\n"
"\n"
"          /* Top Buttons */\n"
"          #rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;\n"
"          border-radius: 5px; }\n"
"          #rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid;\n"
"          border-radius: 4px; }\n"
"          #rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style:\n"
"          solid; border-radius: 4px; }\n"
"\n"
"          /* Theme Settings */\n"
"          #extraRightBox { background-color: rgb(44, 49, 58); }\n"
"          #themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"          /* Bottom Bar */\n"
"          #bottomBar { background-color: rgb(44, 49, 58); }\n"
"          #bottomBar QLabel { font-size"
                        ": 11px; color: rgb(113, 126, 149); padding-left: 10px;\n"
"          padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"          /* CONTENT SETTINGS */\n"
"          /* MENUS */\n"
"          #contentSettings .QPushButton {\n"
"          background-position: left center;\n"
"          background-repeat: no-repeat;\n"
"          border: none;\n"
"          border-left: 22px solid transparent;\n"
"          background-color:transparent;\n"
"          text-align: left;\n"
"          padding-left: 44px;\n"
"          }\n"
"          #contentSettings .QPushButton:hover {\n"
"          background-color: rgb(40, 44, 52);\n"
"          }\n"
"          #contentSettings .QPushButton:pressed {\n"
"          background-color: rgb(189, 147, 249);\n"
"          color: rgb(255, 255, 255);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          QTableWidget */\n"
"          QTableWidget {\n"
"          background-col"
                        "or: transparent;\n"
"          padding: 10px;\n"
"          border-radius: 5px;\n"
"          gridline-color: rgb(44, 49, 58);\n"
"          border-bottom: 1px solid rgb(44, 49, 60);\n"
"          }\n"
"          QTableWidget::item{\n"
"          border-color: rgb(44, 49, 60);\n"
"          padding-left: 5px;\n"
"          padding-right: 5px;\n"
"          gridline-color: rgb(44, 49, 60);\n"
"          }\n"
"          QTableWidget::item:selected{\n"
"          background-color: rgb(189, 147, 249);\n"
"          }\n"
"          QHeaderView::section{\n"
"          background-color: rgb(33, 37, 43);\n"
"          max-width: 30px;\n"
"          border: 1px solid rgb(44, 49, 58);\n"
"          border-style: none;\n"
"          border-bottom: 1px solid rgb(44, 49, 60);\n"
"          border-right: 1px solid rgb(44, 49, 60);\n"
"          }\n"
"          QTableWidget::horizontalHeader {\n"
"          background-color: rgb(33, 37, 43);\n"
"          }\n"
"          QHeaderView::section:horizontal\n"
"          {\n"
"  "
                        "        border: 1px solid rgb(33, 37, 43);\n"
"          background-color: rgb(33, 37, 43);\n"
"          padding: 3px;\n"
"          border-top-left-radius: 7px;\n"
"          border-top-right-radius: 7px;\n"
"          }\n"
"          QHeaderView::section:vertical\n"
"          {\n"
"          border: 1px solid rgb(44, 49, 60);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          LineEdit */\n"
"          QLineEdit {\n"
"          background-color: rgb(33, 37, 43);\n"
"          border-radius: 5px;\n"
"          border: 2px solid rgb(33, 37, 43);\n"
"          padding-left: 10px;\n"
"          selection-color: rgb(255, 255, 255);\n"
"          selection-background-color: rgb(255, 121, 198);\n"
"          }\n"
"          QLineEdit:hover {\n"
"          border: 2px solid rgb(64, 71, 88);\n"
"          }\n"
"          QLineEdit:focus {\n"
"          border: 2px solid rgb(91, 101, 124);\n"
"          }\n"
""
                        "\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          PlainTextEdit */\n"
"          QPlainTextEdit {\n"
"          background-color: rgb(27, 29, 35);\n"
"          border-radius: 5px;\n"
"          padding: 10px;\n"
"          selection-color: rgb(255, 255, 255);\n"
"          selection-background-color: rgb(255, 121, 198);\n"
"          }\n"
"          QPlainTextEdit QScrollBar:vertical {\n"
"          width: 8px;\n"
"          }\n"
"          QPlainTextEdit QScrollBar:horizontal {\n"
"          height: 8px;\n"
"          }\n"
"          QPlainTextEdit:hover {\n"
"          border: 2px solid rgb(64, 71, 88);\n"
"          }\n"
"          QPlainTextEdit:focus {\n"
"          border: 2px solid rgb(91, 101, 124);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          ScrollBars */\n"
"          QScrollBar:horizontal"
                        " {\n"
"          border: none;\n"
"          background: rgb(52, 59, 72);\n"
"          height: 8px;\n"
"          margin: 0px 21px 0 21px;\n"
"          border-radius: 0px;\n"
"          }\n"
"          QScrollBar::handle:horizontal {\n"
"          background: rgb(189, 147, 249);\n"
"          min-width: 25px;\n"
"          border-radius: 4px\n"
"          }\n"
"          QScrollBar::add-line:horizontal {\n"
"          border: none;\n"
"          background: rgb(55, 63, 77);\n"
"          width: 20px;\n"
"          border-top-right-radius: 4px;\n"
"          border-bottom-right-radius: 4px;\n"
"          subcontrol-position: right;\n"
"          subcontrol-origin: margin;\n"
"          }\n"
"          QScrollBar::sub-line:horizontal {\n"
"          border: none;\n"
"          background: rgb(55, 63, 77);\n"
"          width: 20px;\n"
"          border-top-left-radius: 4px;\n"
"          border-bottom-left-radius: 4px;\n"
"          subcontrol-position: left;\n"
"          subcontrol-origin: margin;\n"
"      "
                        "    }\n"
"          QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"          {\n"
"          background: none;\n"
"          }\n"
"          QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"          {\n"
"          background: none;\n"
"          }\n"
"          QScrollBar:vertical {\n"
"          border: none;\n"
"          background: rgb(52, 59, 72);\n"
"          width: 8px;\n"
"          margin: 21px 0 21px 0;\n"
"          border-radius: 0px;\n"
"          }\n"
"          QScrollBar::handle:vertical {\n"
"          background: rgb(189, 147, 249);\n"
"          min-height: 25px;\n"
"          border-radius: 4px\n"
"          }\n"
"          QScrollBar::add-line:vertical {\n"
"          border: none;\n"
"          background: rgb(55, 63, 77);\n"
"          height: 20px;\n"
"          border-bottom-left-radius: 4px;\n"
"          border-bottom-right-radius: 4px;\n"
"          subcontrol-position: bottom;\n"
"          subcontrol-origin: margin;\n"
"          }\n"
""
                        "          QScrollBar::sub-line:vertical {\n"
"          border: none;\n"
"          background: rgb(55, 63, 77);\n"
"          height: 20px;\n"
"          border-top-left-radius: 4px;\n"
"          border-top-right-radius: 4px;\n"
"          subcontrol-position: top;\n"
"          subcontrol-origin: margin;\n"
"          }\n"
"          QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"          background: none;\n"
"          }\n"
"\n"
"          QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"          background: none;\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          CheckBox */\n"
"          QCheckBox::indicator {\n"
"          border: 3px solid rgb(52, 59, 72);\n"
"          width: 15px;\n"
"          height: 15px;\n"
"          border-radius: 10px;\n"
"          background: rgb(44, 49, 60);\n"
"          }\n"
"          QCheckBox::indicator:hover {\n"
" "
                        "         border: 3px solid rgb(58, 66, 81);\n"
"          }\n"
"          QCheckBox::indicator:checked {\n"
"          background: 3px solid rgb(52, 59, 72);\n"
"          border: 3px solid rgb(52, 59, 72);\n"
"          background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          RadioButton */\n"
"          QRadioButton::indicator {\n"
"          border: 3px solid rgb(52, 59, 72);\n"
"          width: 15px;\n"
"          height: 15px;\n"
"          border-radius: 10px;\n"
"          background: rgb(44, 49, 60);\n"
"          }\n"
"          QRadioButton::indicator:hover {\n"
"          border: 3px solid rgb(58, 66, 81);\n"
"          }\n"
"          QRadioButton::indicator:checked {\n"
"          background: 3px solid rgb(94, 106, 130);\n"
"          border: 3px solid rgb(52, 59, 72);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////"
                        "////////////////////////////////////////////////////////////////////////////////////////\n"
"          ComboBox */\n"
"          QComboBox{\n"
"          background-color: rgb(27, 29, 35);\n"
"          border-radius: 5px;\n"
"          border: 2px solid rgb(33, 37, 43);\n"
"          padding: 5px;\n"
"          padding-left: 10px;\n"
"          }\n"
"          QComboBox:hover{\n"
"          border: 2px solid rgb(64, 71, 88);\n"
"          }\n"
"          QComboBox::drop-down {\n"
"          subcontrol-origin: padding;\n"
"          subcontrol-position: top right;\n"
"          width: 25px;\n"
"          border-left-width: 3px;\n"
"          border-left-color: rgba(39, 44, 54, 150);\n"
"          border-left-style: solid;\n"
"          border-top-right-radius: 3px;\n"
"          border-bottom-right-radius: 3px;\n"
"          background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"          background-position: center;\n"
"          background-repeat: no-reperat;\n"
"          }\n"
"          QCom"
                        "boBox QAbstractItemView {\n"
"          color: rgb(255, 121, 198);\n"
"          background-color: rgb(33, 37, 43);\n"
"          padding: 10px;\n"
"          selection-background-color: rgb(39, 44, 54);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Sliders */\n"
"          QSlider::groove:horizontal {\n"
"          border-radius: 5px;\n"
"          height: 10px;\n"
"          margin: 0px;\n"
"          background-color: rgb(52, 59, 72);\n"
"          }\n"
"          QSlider::groove:horizontal:hover {\n"
"          background-color: rgb(55, 62, 76);\n"
"          }\n"
"          QSlider::handle:horizontal {\n"
"          background-color: rgb(189, 147, 249);\n"
"          border: none;\n"
"          height: 10px;\n"
"          width: 10px;\n"
"          margin: 0px;\n"
"          border-radius: 5px;\n"
"          }\n"
"          QSlider::handle:horizontal:hover {\n"
"          background-color:"
                        " rgb(195, 155, 255);\n"
"          }\n"
"          QSlider::handle:horizontal:pressed {\n"
"          background-color: rgb(255, 121, 198);\n"
"          }\n"
"\n"
"          QSlider::groove:vertical {\n"
"          border-radius: 5px;\n"
"          width: 10px;\n"
"          margin: 0px;\n"
"          background-color: rgb(52, 59, 72);\n"
"          }\n"
"          QSlider::groove:vertical:hover {\n"
"          background-color: rgb(55, 62, 76);\n"
"          }\n"
"          QSlider::handle:vertical {\n"
"          background-color: rgb(189, 147, 249);\n"
"          border: none;\n"
"          height: 10px;\n"
"          width: 10px;\n"
"          margin: 0px;\n"
"          border-radius: 5px;\n"
"          }\n"
"          QSlider::handle:vertical:hover {\n"
"          background-color: rgb(195, 155, 255);\n"
"          }\n"
"          QSlider::handle:vertical:pressed {\n"
"          background-color: rgb(255, 121, 198);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////"
                        "////////////////////////////////////////////////////////////\n"
"          CommandLinkButton */\n"
"          QCommandLinkButton {\n"
"          color: rgb(255, 121, 198);\n"
"          border-radius: 5px;\n"
"          padding: 5px;\n"
"          color: rgb(255, 170, 255);\n"
"          }\n"
"          QCommandLinkButton:hover {\n"
"          color: rgb(255, 170, 255);\n"
"          background-color: rgb(44, 49, 60);\n"
"          }\n"
"          QCommandLinkButton:pressed {\n"
"          color: rgb(189, 147, 249);\n"
"          background-color: rgb(52, 58, 71);\n"
"          }\n"
"\n"
"          /*\n"
"          /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"          Button */\n"
"          #pagesContainer QPushButton {\n"
"          border: 2px solid rgb(52, 59, 72);\n"
"          border-radius: 5px;\n"
"          background-color: rgb(52, 59, 72);\n"
"          }\n"
"          #pagesContainer QPushButton:hover {\n"
"          background-color: rgb(57"
                        ", 65, 80);\n"
"          border: 2px solid rgb(61, 70, 86);\n"
"          }\n"
"          #pagesContainer QPushButton:pressed {\n"
"          background-color: rgb(35, 40, 49);\n"
"          border: 2px solid rgb(43, 50, 61);\n"
"          }\n"
"          #pushButton_2 QPushButton:hover {\n"
"          background-color: rgb(57, 65, 80);\n"
"          border: 2px solid #fff;\n"
"          }\n"
"        ")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image:\n"
"                                        url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"background-color: #cecece;\n"
"                                        border-radius: 14px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.pagesContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 1178, 814))
        self.stackedWidget.setMaximumSize(QSize(1178, 16777215))
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.scrollArea_2 = QScrollArea(self.home)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, -1, 1171, 591))
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1169, 1500))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"height: auto;")
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1171, 1141))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setVerticalSpacing(15)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.group_23 = QFrame(self.gridLayoutWidget)
        self.group_23.setObjectName(u"group_23")
        self.group_23.setEnabled(True)
        self.group_23.setMaximumSize(QSize(250, 250))
        self.group_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_23.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_23.setFrameShape(QFrame.StyledPanel)
        self.group_23.setFrameShadow(QFrame.Raised)
        self.pushButton_26 = QPushButton(self.group_23)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_26.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_46 = QLabel(self.group_23)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 180, 231, 51))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.label_46.setFont(font4)
        self.label_46.setMouseTracking(True)
        self.label_46.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_46.setTextFormat(Qt.AutoText)
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.group_23)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(60, 60, 120, 120))
        self.label_47.setStyleSheet(u"border: none")
        self.label_47.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_47.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_23, 2, 2, 1, 1)

        self.group_7 = QFrame(self.gridLayoutWidget)
        self.group_7.setObjectName(u"group_7")
        self.group_7.setEnabled(True)
        self.group_7.setMaximumSize(QSize(250, 250))
        self.group_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_7.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_7.setFrameShape(QFrame.StyledPanel)
        self.group_7.setFrameShadow(QFrame.Raised)
        self.pushButton_10 = QPushButton(self.group_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_10.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_14 = QLabel(self.group_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 180, 231, 51))
        self.label_14.setFont(font4)
        self.label_14.setMouseTracking(True)
        self.label_14.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.group_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 60, 120, 120))
        self.label_15.setStyleSheet(u"border: none")
        self.label_15.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_7, 1, 0, 1, 1)

        self.group_24 = QFrame(self.gridLayoutWidget)
        self.group_24.setObjectName(u"group_24")
        self.group_24.setEnabled(True)
        self.group_24.setMaximumSize(QSize(250, 250))
        self.group_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_24.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_24.setFrameShape(QFrame.StyledPanel)
        self.group_24.setFrameShadow(QFrame.Raised)
        self.pushButton_27 = QPushButton(self.group_24)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_27.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_48 = QLabel(self.group_24)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 180, 231, 51))
        self.label_48.setFont(font4)
        self.label_48.setMouseTracking(True)
        self.label_48.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_48.setTextFormat(Qt.AutoText)
        self.label_48.setScaledContents(True)
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_49 = QLabel(self.group_24)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(60, 60, 120, 120))
        self.label_49.setStyleSheet(u"border: none")
        self.label_49.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_49.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_24, 2, 3, 1, 1)

        self.group_11 = QFrame(self.gridLayoutWidget)
        self.group_11.setObjectName(u"group_11")
        self.group_11.setEnabled(True)
        self.group_11.setMaximumSize(QSize(250, 250))
        self.group_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_11.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_11.setFrameShape(QFrame.StyledPanel)
        self.group_11.setFrameShadow(QFrame.Raised)
        self.pushButton_14 = QPushButton(self.group_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_14.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_22 = QLabel(self.group_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 180, 231, 51))
        self.label_22.setFont(font4)
        self.label_22.setMouseTracking(True)
        self.label_22.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_22.setTextFormat(Qt.AutoText)
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.group_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(60, 60, 120, 120))
        self.label_23.setStyleSheet(u"border: none")
        self.label_23.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_23.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_11, 2, 0, 1, 1)

        self.group_3 = QFrame(self.gridLayoutWidget)
        self.group_3.setObjectName(u"group_3")
        self.group_3.setEnabled(True)
        self.group_3.setMaximumSize(QSize(250, 250))
        self.group_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_3.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_3.setFrameShape(QFrame.StyledPanel)
        self.group_3.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.group_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_6.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_6 = QLabel(self.group_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 180, 231, 51))
        self.label_6.setFont(font4)
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.group_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 60, 120, 120))
        self.label_7.setStyleSheet(u"border: none")
        self.label_7.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_3, 0, 0, 1, 1)

        self.group_9 = QFrame(self.gridLayoutWidget)
        self.group_9.setObjectName(u"group_9")
        self.group_9.setEnabled(True)
        self.group_9.setMaximumSize(QSize(250, 250))
        self.group_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_9.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_9.setFrameShape(QFrame.StyledPanel)
        self.group_9.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.group_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_12.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_18 = QLabel(self.group_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 180, 231, 51))
        self.label_18.setFont(font4)
        self.label_18.setMouseTracking(True)
        self.label_18.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_18.setTextFormat(Qt.AutoText)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.group_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 60, 120, 120))
        self.label_19.setStyleSheet(u"border: none")
        self.label_19.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_19.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_9, 1, 2, 1, 1)

        self.group_5 = QFrame(self.gridLayoutWidget)
        self.group_5.setObjectName(u"group_5")
        self.group_5.setEnabled(True)
        self.group_5.setMaximumSize(QSize(250, 250))
        self.group_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_5.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_5.setFrameShape(QFrame.StyledPanel)
        self.group_5.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.group_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_8.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_10 = QLabel(self.group_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 180, 231, 51))
        self.label_10.setFont(font4)
        self.label_10.setMouseTracking(True)
        self.label_10.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.group_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 60, 120, 120))
        self.label_11.setStyleSheet(u"border: none")
        self.label_11.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_5, 0, 2, 1, 1)

        self.group_10 = QFrame(self.gridLayoutWidget)
        self.group_10.setObjectName(u"group_10")
        self.group_10.setEnabled(True)
        self.group_10.setMaximumSize(QSize(250, 250))
        self.group_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_10.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_10.setFrameShape(QFrame.VLine)
        self.group_10.setFrameShadow(QFrame.Plain)
        self.pushButton_13 = QPushButton(self.group_10)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_13.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_20 = QLabel(self.group_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 180, 231, 51))
        self.label_20.setFont(font4)
        self.label_20.setMouseTracking(True)
        self.label_20.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_20.setTextFormat(Qt.AutoText)
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.group_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(60, 60, 120, 120))
        self.label_21.setStyleSheet(u"border: none")
        self.label_21.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_21.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_10, 1, 3, 1, 1)

        self.group_6 = QFrame(self.gridLayoutWidget)
        self.group_6.setObjectName(u"group_6")
        self.group_6.setEnabled(True)
        self.group_6.setMaximumSize(QSize(250, 250))
        self.group_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_6.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_6.setFrameShape(QFrame.StyledPanel)
        self.group_6.setFrameShadow(QFrame.Raised)
        self.pushButton_9 = QPushButton(self.group_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_9.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_12 = QLabel(self.group_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 180, 231, 51))
        self.label_12.setFont(font4)
        self.label_12.setMouseTracking(True)
        self.label_12.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.group_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 60, 120, 120))
        self.label_13.setStyleSheet(u"border: none")
        self.label_13.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_6, 0, 3, 1, 1)

        self.group_8 = QFrame(self.gridLayoutWidget)
        self.group_8.setObjectName(u"group_8")
        self.group_8.setEnabled(True)
        self.group_8.setMaximumSize(QSize(250, 250))
        self.group_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_8.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_8.setFrameShape(QFrame.StyledPanel)
        self.group_8.setFrameShadow(QFrame.Raised)
        self.pushButton_11 = QPushButton(self.group_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_11.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_16 = QLabel(self.group_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 180, 231, 51))
        self.label_16.setFont(font4)
        self.label_16.setMouseTracking(True)
        self.label_16.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.group_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 60, 120, 120))
        self.label_17.setStyleSheet(u"border: none")
        self.label_17.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_17.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_8, 1, 1, 1, 1)

        self.group_4 = QFrame(self.gridLayoutWidget)
        self.group_4.setObjectName(u"group_4")
        self.group_4.setEnabled(True)
        self.group_4.setMaximumSize(QSize(250, 250))
        self.group_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_4.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_4.setFrameShape(QFrame.StyledPanel)
        self.group_4.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.group_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_7.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_8 = QLabel(self.group_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 180, 231, 51))
        self.label_8.setFont(font4)
        self.label_8.setMouseTracking(True)
        self.label_8.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.group_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 60, 120, 120))
        self.label_9.setStyleSheet(u"border: none")
        self.label_9.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_4, 0, 1, 1, 1)

        self.group_12 = QFrame(self.gridLayoutWidget)
        self.group_12.setObjectName(u"group_12")
        self.group_12.setEnabled(True)
        self.group_12.setMaximumSize(QSize(250, 250))
        self.group_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_12.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_12.setFrameShape(QFrame.StyledPanel)
        self.group_12.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.group_12)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_15.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_24 = QLabel(self.group_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 180, 231, 51))
        self.label_24.setFont(font4)
        self.label_24.setMouseTracking(True)
        self.label_24.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(self.group_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(60, 60, 120, 120))
        self.label_25.setStyleSheet(u"border: none")
        self.label_25.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_25.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_12, 2, 1, 1, 1)

        self.group_25 = QFrame(self.gridLayoutWidget)
        self.group_25.setObjectName(u"group_25")
        self.group_25.setEnabled(True)
        self.group_25.setMaximumSize(QSize(250, 250))
        self.group_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_25.setStyleSheet(u"border: 1px solid\n"
"                                                              #999;\n"
"                                                              border-radius: 3px;\n"
"                                                              background-color: rgb(38, 42, 50);")
        self.group_25.setFrameShape(QFrame.StyledPanel)
        self.group_25.setFrameShadow(QFrame.Raised)
        self.pushButton_28 = QPushButton(self.group_25)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(210, 10, 31, 24))
        self.pushButton_28.setStyleSheet(u"border: none;\n"
"                                                                background-image:\n"
"                                                                url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                background-repeat: none;\n"
"                                                                background-position: center;")
        self.label_50 = QLabel(self.group_25)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 180, 231, 51))
        self.label_50.setFont(font4)
        self.label_50.setMouseTracking(True)
        self.label_50.setStyleSheet(u"border: none;\n"
"                                                                text-align: center;\n"
"                                                                font-size: 16px;")
        self.label_50.setTextFormat(Qt.AutoText)
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_51 = QLabel(self.group_25)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(60, 60, 120, 120))
        self.label_51.setStyleSheet(u"border: none")
        self.label_51.setPixmap(QPixmap(u"\n"
"                                                                :/images/images/images/PyDracula.png"))
        self.label_51.setScaledContents(True)

        self.gridLayout_5.addWidget(self.group_25, 3, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"background-color:\n"
"                                                                              rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u"\n"
"                                                                              :/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color:\n"
"                                                                              rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)

        self.gridLayout.addWidget(self.labelVersion_3, 2, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color:\n"
"                                                                              rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)

        self.tableWidget = QTableWidget(self.row_1)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_1)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.new_page.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.new_page.setLayoutDirection(Qt.LeftToRight)
        self.new_page.setAutoFillBackground(False)
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget_2 = QWidget(self.new_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setMaximumSize(QSize(1178, 50))
        self.widget_2.setLayoutDirection(Qt.RightToLeft)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 31))
        self.label.setStyleSheet(u"font-weight: 700;\n"
"                                                          font-size: 24px;")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(940, 10, 211, 31))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"padding-left: 20px;\n"
"                                                          background-image:\n"
"                                                          url(:/icons/images/icons/cil-user-follow.png);\n"
"                                                          background-origin: content;\n"
"                                                          background-repeat: no-repeat;\n"
"                                                          background-position: left center;")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(900, 10, 31, 31))
        self.pushButton_4.setStyleSheet(u"border: none;\n"
"                                                          background-image:\n"
"                                                          url(:/icons/images/icons/cil-settings.png);\n"
"                                                          background-repeat: none;\n"
"                                                          background-position: center;")

        self.verticalLayout_20.addWidget(self.widget_2)

        self.frame_2 = QFrame(self.new_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.scrollArea_3 = QScrollArea(self.frame_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 1160, 520))
        self.scrollArea_3.setMouseTracking(False)
        self.scrollArea_3.setTabletTracking(False)
        self.scrollArea_3.setAcceptDrops(False)
        self.scrollArea_3.setStyleSheet(u"border: none;")
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -180, 1152, 700))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 700))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.gridLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1161, 671))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.group_26 = QFrame(self.gridLayoutWidget_2)
        self.group_26.setObjectName(u"group_26")
        self.group_26.setEnabled(True)
        self.group_26.setMaximumSize(QSize(250, 250))
        self.group_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_26.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_26.setFrameShape(QFrame.StyledPanel)
        self.group_26.setFrameShadow(QFrame.Raised)
        self.pushButton_29 = QPushButton(self.group_26)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_29.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_52 = QLabel(self.group_26)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 180, 231, 51))
        self.label_52.setFont(font4)
        self.label_52.setMouseTracking(True)
        self.label_52.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_52.setTextFormat(Qt.AutoText)
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_53 = QLabel(self.group_26)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(60, 60, 120, 120))
        self.label_53.setStyleSheet(u"border: none")
        self.label_53.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_53.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_26, 0, 2, 1, 1)

        self.group_27 = QFrame(self.gridLayoutWidget_2)
        self.group_27.setObjectName(u"group_27")
        self.group_27.setEnabled(True)
        self.group_27.setMaximumSize(QSize(250, 250))
        self.group_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_27.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_27.setFrameShape(QFrame.StyledPanel)
        self.group_27.setFrameShadow(QFrame.Raised)
        self.pushButton_30 = QPushButton(self.group_27)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_30.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_54 = QLabel(self.group_27)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 180, 231, 51))
        self.label_54.setFont(font4)
        self.label_54.setMouseTracking(True)
        self.label_54.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_54.setTextFormat(Qt.AutoText)
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_55 = QLabel(self.group_27)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(60, 60, 120, 120))
        self.label_55.setStyleSheet(u"border: none")
        self.label_55.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_55.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_27, 0, 3, 1, 1)

        self.group_28 = QFrame(self.gridLayoutWidget_2)
        self.group_28.setObjectName(u"group_28")
        self.group_28.setEnabled(True)
        self.group_28.setMaximumSize(QSize(250, 250))
        self.group_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_28.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_28.setFrameShape(QFrame.StyledPanel)
        self.group_28.setFrameShadow(QFrame.Raised)
        self.pushButton_31 = QPushButton(self.group_28)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_31.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_56 = QLabel(self.group_28)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 180, 231, 51))
        self.label_56.setFont(font4)
        self.label_56.setMouseTracking(True)
        self.label_56.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_56.setTextFormat(Qt.AutoText)
        self.label_56.setScaledContents(True)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_57 = QLabel(self.group_28)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(60, 60, 120, 120))
        self.label_57.setStyleSheet(u"border: none")
        self.label_57.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_57.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_28, 1, 0, 1, 1)

        self.group_29 = QFrame(self.gridLayoutWidget_2)
        self.group_29.setObjectName(u"group_29")
        self.group_29.setEnabled(True)
        self.group_29.setMaximumSize(QSize(250, 250))
        self.group_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_29.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_29.setFrameShape(QFrame.StyledPanel)
        self.group_29.setFrameShadow(QFrame.Raised)
        self.pushButton_32 = QPushButton(self.group_29)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_32.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_58 = QLabel(self.group_29)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 180, 231, 51))
        self.label_58.setFont(font4)
        self.label_58.setMouseTracking(True)
        self.label_58.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_58.setTextFormat(Qt.AutoText)
        self.label_58.setScaledContents(True)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_59 = QLabel(self.group_29)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(60, 60, 120, 120))
        self.label_59.setStyleSheet(u"border: none")
        self.label_59.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_59.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_29, 1, 1, 1, 1)

        self.group_1 = QFrame(self.gridLayoutWidget_2)
        self.group_1.setObjectName(u"group_1")
        self.group_1.setEnabled(True)
        self.group_1.setMaximumSize(QSize(250, 250))
        self.group_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_1.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_1.setFrameShape(QFrame.StyledPanel)
        self.group_1.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.group_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"                                                                      {\n"
"                                                                      border: none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;\n"
"                                                                      border-radius: 14px;\n"
"                                                                      }\n"
"\n"
"                                                                      QPushButton:hover {\n"
"                                                                      background-color: #fff;\n"
"                                                       "
                        "               border: 2px solid rgb(61, 70,\n"
"                                                                      86);\n"
"                                                                      }")
        self.label_2 = QLabel(self.group_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 231, 51))
        self.label_2.setFont(font4)
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.group_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 60, 120, 120))
        self.label_3.setStyleSheet(u"border: none")
        self.label_3.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_1, 0, 0, 1, 1)

        self.group_31 = QFrame(self.gridLayoutWidget_2)
        self.group_31.setObjectName(u"group_31")
        self.group_31.setEnabled(True)
        self.group_31.setMaximumSize(QSize(250, 250))
        self.group_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_31.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_31.setFrameShape(QFrame.StyledPanel)
        self.group_31.setFrameShadow(QFrame.Raised)
        self.pushButton_34 = QPushButton(self.group_31)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_34.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_62 = QLabel(self.group_31)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 180, 231, 51))
        self.label_62.setFont(font4)
        self.label_62.setMouseTracking(True)
        self.label_62.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_62.setTextFormat(Qt.AutoText)
        self.label_62.setScaledContents(True)
        self.label_62.setAlignment(Qt.AlignCenter)
        self.label_63 = QLabel(self.group_31)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(60, 60, 120, 120))
        self.label_63.setStyleSheet(u"border: none")
        self.label_63.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_63.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_31, 1, 3, 1, 1)

        self.group_2 = QFrame(self.gridLayoutWidget_2)
        self.group_2.setObjectName(u"group_2")
        self.group_2.setEnabled(True)
        self.group_2.setMaximumSize(QSize(250, 250))
        self.group_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_2.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_2.setFrameShape(QFrame.StyledPanel)
        self.group_2.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.group_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_5.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_4 = QLabel(self.group_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 231, 51))
        self.label_4.setFont(font4)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.group_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 60, 120, 120))
        self.label_5.setStyleSheet(u"border: none")
        self.label_5.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_2, 0, 1, 1, 1)

        self.group_30 = QFrame(self.gridLayoutWidget_2)
        self.group_30.setObjectName(u"group_30")
        self.group_30.setEnabled(True)
        self.group_30.setMaximumSize(QSize(250, 250))
        self.group_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.group_30.setStyleSheet(u"border: 1px\n"
"                                                                    solid #999;\n"
"                                                                    border-radius: 3px;\n"
"                                                                    background-color: rgb(38, 42,\n"
"                                                                    50);")
        self.group_30.setFrameShape(QFrame.StyledPanel)
        self.group_30.setFrameShadow(QFrame.Raised)
        self.pushButton_33 = QPushButton(self.group_30)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(210, 10, 30, 30))
        self.pushButton_33.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      background-image:\n"
"                                                                      url(:/icons/images/icons/cil-options-horizontal.png);\n"
"                                                                      background-repeat: none;\n"
"                                                                      background-position: center;")
        self.label_60 = QLabel(self.group_30)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(10, 180, 231, 51))
        self.label_60.setFont(font4)
        self.label_60.setMouseTracking(True)
        self.label_60.setStyleSheet(u"border:\n"
"                                                                      none;\n"
"                                                                      text-align: center;\n"
"                                                                      font-size: 16px;")
        self.label_60.setTextFormat(Qt.AutoText)
        self.label_60.setScaledContents(True)
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_61 = QLabel(self.group_30)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(60, 60, 120, 120))
        self.label_61.setStyleSheet(u"border: none")
        self.label_61.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_61.setScaledContents(True)

        self.gridLayout_3.addWidget(self.group_30, 1, 2, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_20.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.frame)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"\n"
"                                                          background-image:\n"
"                                                          url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"border: none;\n"
"                                                          background-image:\n"
"                                                          url(:/icons/images/icons/options-white.png);\n"
"                                                          backgrounf-color: #fff;")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"\n"
"                                                          background-image:\n"
"                                                          url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:6"
                        "00; color:#ff79c6;\">PyDracula</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created                                        using Python and PySide (support for PyQt), and with colors                                        based on the Dracula theme created by Zeno                                        Rocha.</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT                                        License</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wa"
                        "nderson                                        M. Pimenta</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt;                                        ui_main.py</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span>                                        </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin"
                        "-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o                                        resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"File share app", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.pushButton_26.setText("")
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_47.setText("")
        self.pushButton_10.setText("")
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_15.setText("")
        self.pushButton_27.setText("")
#if QT_CONFIG(tooltip)
        self.label_48.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_49.setText("")
        self.pushButton_14.setText("")
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_23.setText("")
        self.pushButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_7.setText("")
        self.pushButton_12.setText("")
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_19.setText("")
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_11.setText("")
        self.pushButton_13.setText("")
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_21.setText("")
        self.pushButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_13.setText("")
        self.pushButton_11.setText("")
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_17.setText("")
        self.pushButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_9.setText("")
        self.pushButton_15.setText("")
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_25.setText("")
        self.pushButton_28.setText("")
#if QT_CONFIG(tooltip)
        self.label_50.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_51.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Choose file here", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Tham gia ho\u1eb7c t\u1ea1o nh\u00f3m", None))
        self.pushButton_4.setText("")
        self.pushButton_29.setText("")
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 3", None))
        self.label_53.setText("")
        self.pushButton_30.setText("")
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 4", None))
        self.label_55.setText("")
        self.pushButton_31.setText("")
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 5", None))
        self.label_57.setText("")
        self.pushButton_32.setText("")
#if QT_CONFIG(tooltip)
        self.label_58.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 6", None))
        self.label_59.setText("")
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 1", None))
        self.label_3.setText("")
        self.pushButton_34.setText("")
#if QT_CONFIG(tooltip)
        self.label_62.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 8", None))
        self.label_63.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 2", None))
        self.label_5.setText("")
        self.pushButton_33.setText("")
#if QT_CONFIG(tooltip)
        self.label_60.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 7", None))
        self.label_61.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

