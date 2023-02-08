import sys

from modules import *
from widgets import *


from core.http.http import HttpHandle

widgets = None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "FileShare"
        description = "Share files with your friends"

        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True)
        )

        UIFunctions.uiDefinitions(self)

        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        useCustomTheme = False
        themeFile = "themes\dark_theme.css"

        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

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

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

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


class LoginWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")

        self.ui.pushButton_2.clicked.connect(self.go_to_register)
        self.ui.pushButton.clicked.connect(self.login)

    def go_to_register(self):
        widget.setCurrentWidget(register)

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if username and password:
            http = HttpHandle()
            token, error = http.login(username, password)
            if token is None:
                self.ui.error_label.setText(error)
            else:
                widget.currentWidget(main)
        else:
            self.ui.error_label.setText("Please fill all fields!")


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
            http = HttpHandle()
            token, error = http.register(username, password, display_name)
            if token is None:
                self.ui.error_label.setText(error)
            else:
                widget.currentWidget(login)
        else:
            self.ui.error_label.setText("Please fill all fields!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    app.setWindowIcon(QIcon("icon.ico"))

    main = MainWindow()
    login = LoginWindow()
    register = RegisterWindow()

    widget.addWidget(login)
    widget.addWidget(main)
    widget.addWidget(register)

    widget.setCurrentWidget(login)

    widget.show()
    sys.exit(app.exec())
