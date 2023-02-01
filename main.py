import sys

from modules import *
from widgets import *

from core.http.http import HttpHandle

widgets = None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_Login()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.pushButton.clicked.connect(self.login)
        widgets.pushButton_2.clicked.connect(self.go_to_register)

        self.show()
        """ Settings.ENABLE_CUSTOM_TITLE_BAR = True

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
        self.show()

        widgets.pushButton.clicked.connect(self.login) """

    def login(self):
        global widgets

        username = widgets.lineEdit.text()
        password = widgets.lineEdit_2.text()
        token = HttpHandle.login(username, password)
        if token is not None:

            self.destroy()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

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
        else:
            print("error")

    def go_to_register(self):
        self.destroy()
        self.ui = Ui_Register()
        self.ui.setupUi(self)

        global widgets
        widgets = self.ui

        self.show()

    def go_to_login(self):
        self.destroy()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.show()

        global widgets
        widgets = self.ui

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
