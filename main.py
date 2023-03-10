import sys

from modules import *
from widgets import *
from typing import List

from core.model import *
from core.http import login as login_fn, register as register_fn, logout as logout_fn, init_data

widgets = None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        title = "FileShare"
        description = "Share files with your friends"

        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True)
        )

        UIFunctions.uiDefinitions(self)

        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        
        widgets.btn_logout.clicked.connect(self.logout)

        # self.show()

        useCustomTheme = False
        themeFile = "themes\dark_theme.css"

        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.new_page)
        widgets.btn_new.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_new.styleSheet()))

        # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            UIFunctions.resetStyle(self, btnName)

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(
                widgets.new_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_exit":
            self.close()
            app.quit()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////

    def resizeEvent(self, event):
        # Update Size Grips
        # UIFunctions.resize_grips(self)
        pass

    # MOUSE CLICK EVENTS
        # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
            
    def render_group(self, groups: List[Group]):
        if groups is None:
            return
        
        rows = len(groups) // 4 + 1
        cols = 4 if len(groups) >= 4 else len(groups)
        self.ui.scrollAreaWidgetContents_3.setFixedSize(
            QSize(1280, rows * 315))
        self.ui.gridLayoutWidget_2.setGeometry(
            QRect(0, 0, cols * 320, rows * 315))

        for idx, group in enumerate(groups):
            group_frame = QFrame(self.ui.gridLayoutWidget_2)
            group_frame.setObjectName(f"group_{group.id}")
            group_frame.setEnabled(True)
            group_frame.setMaximumSize(QSize(265, 265))
            group_frame.setCursor(QCursor(Qt.PointingHandCursor))
            group_frame.setStyleSheet(u"border: 1px\n"
                                        "solid #999;\n"
                                        "border-radius: 3px;\n"
                                        "background-color: rgb(38, 42, 50);")
                                        # "background-color: red;")
                                        
            group_frame.setFrameShape(QFrame.StyledPanel)
            group_frame.setFrameShadow(QFrame.Raised)
            push_btn = QPushButton(group_frame)
            push_btn.setObjectName(f"pushButton_{group.id}")
            push_btn.setGeometry(QRect(225, 10, 30, 30))
            push_btn.setStyleSheet(u"border: none;\n"
                                            "background-image:\n"
                                            "url(:/icons/images/icons/cil-options-horizontal.png);\n"
                                            "background-repeat: none;\n"
                                            "background-position: center;")
            group_name_label = QLabel(group_frame)
            group_name_label.setObjectName(f"name_label_{group.id}")
            group_name_label.setGeometry(QRect(17, 190, 230, 56))
            font4 = QFont()
            font4.setFamilies([u"Segoe UI"])
            group_name_label.setFont(font4)
            group_name_label.setMouseTracking(True)
            group_name_label.setStyleSheet(u"border:\n"
                                        "none;\n"
                                        "text-align: center;\n"
                                        "font-size: 16px;")
            group_name_label.setTextFormat(Qt.AutoText)
            group_name_label.setScaledContents(True)
            group_name_label.setAlignment(Qt.AlignCenter)
            group_name_label.setToolTip(group.name)
            group_name_label.setText(QCoreApplication.translate("MainWindow", f"{group.name}"))
            
            label_avatar = QLabel(group_frame)
            label_avatar.setObjectName(f"avatar_{group.id}")
            label_avatar.setGeometry(QRect(70, 70, 125, 125))
            label_avatar.setStyleSheet(u"border: none")
            label_avatar.setPixmap(
                QPixmap(u":/images/images/images/PyDracula.png"))
            label_avatar.setScaledContents(True)
            
            row = idx // 4
            col = idx % 4
            
            self.ui.gridLayout_3.addWidget(group_frame, row, col, 1, 1)
        
    def remove_group_render(self):
        for i in reversed(range(self.ui.gridLayout_3.count())):
            self.ui.gridLayout_3.itemAt(i).widget().setParent(None)
        
    def logout(self):
        status, error = logout_fn()
        if status:
            self.remove_group_render()
            self.hide()
            self.setParent(None)
            widget.hide()
            setupUiLogin()
        else:
            print(error)
            


class LoginWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # set window non resizable
        self.setFixedSize(478, 256)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")

        self.ui.pushButton_2.clicked.connect(self.go_to_register)
        self.ui.pushButton.clicked.connect(self.login)

    def go_to_register(self):
        widget.setCurrentWidget(register)

    def login(self):
        global user
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if username and password:
            token, error = login_fn(username, password)
            if token is None:
                self.ui.error_label.setText(error)
            else:
                status, data = get_me_info()
                user = User.from_dict(data) if status else None
                print(user)
                setupUiMain()
                self.ui.error_label.setText("")
        else:
            self.ui.error_label.setText("Please fill all fields!")
        self.ui.lineEdit_2.setText("")


class RegisterWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_Register()
        self.ui.setupUi(self)

        self.setWindowTitle("Register")

        self.ui.pushButton_2.clicked.connect(self.go_to_login)
        self.ui.pushButton.clicked.connect(self.register)

    def go_to_login(self):
        widget.setCurrentWidget(login)

    def register(self):
        username = self.ui.username_text.text()
        display_name = self.ui.full_name_text.text()
        password = self.ui.password_text.text()
        if username and password and display_name:
            is_success, error = register_fn(username, password, display_name)
            if is_success == False and error:
                self.ui.error_label.setText(error)
            else:
                widget.setCurrentWidget(login)
        else:
            self.ui.error_label.setText("Please fill all fields!")


def setupUiMain():
    widget.addWidget(main)
    # fetch group
    groups = Group.fetch_my_group()
    main.render_group(groups)
    main.ui.btn_user.setText(user.display_name)
    widget.setCurrentWidget(main)
    widget.showMaximized()


def setupUiLogin():
    widget.setCurrentWidget(login)
    widget.showNormal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    app.setWindowIcon(QIcon("icon.ico"))

    main = MainWindow()
    login = LoginWindow()
    register = RegisterWindow()
    widget.addWidget(login)
    widget.addWidget(register)
    
    user = None
    status, data = init_data()
    if status == True: # if user is logged in
        user = User.from_dict(data)
        setupUiMain()
    else:
        setupUiLogin()

    # widget.show()
    sys.exit(app.exec())
