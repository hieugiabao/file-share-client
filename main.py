import sys

from modules import *
from widgets import *
from typing import List

from core.model import *
from core.http import login as login_fn, register as register_fn, logout as logout_fn, init_data
from core.tftp import TFTPClient
from pathlib import Path

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
        widgets.pushButton_2.clicked.connect(self.create_directory)
        widgets.pushButton_5.clicked.connect(self.choose_file)
        widgets.pushButton.clicked.connect(self.upload_file)

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

        self.nodes = None
        self.directories = None
        self.files = None
        self.group_choosen = None
        self.directory_choosen = None
        self.file_choosen = None
        self.file = None

        self.setup_right_menu()

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
            self.rerender_file_list(
                self.nodes if self.nodes is not None else self.group_choosen.nodes, self.directory_choosen)

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
        self.group_choosen = groups[0] if len(groups) > 0 else None

        rows = len(groups) // 4 + 1
        cols = 4 if len(groups) >= 4 else len(groups)
        self.ui.scrollAreaWidgetContents_3.setFixedSize(
            QSize(1280, rows * 315))
        self.ui.gridLayoutWidget_2.setGeometry(
            QRect(0, 0, cols * 320, rows * 315))

        for idx, group in enumerate(groups):
            group_btn = QPushButton(self.ui.gridLayoutWidget_2)
            group_btn.setObjectName(f"groupbtn_{group.id}")
            group_btn.setEnabled(True)
            group_btn.setMaximumSize(QSize(265, 265))
            group_btn.setCursor(QCursor(Qt.PointingHandCursor))
            group_frame = QFrame(group_btn)
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
            group_name_label.setText(
                QCoreApplication.translate("MainWindow", f"{group.name}"))

            label_avatar = QLabel(group_frame)
            label_avatar.setObjectName(f"avatar_{group.id}")
            label_avatar.setGeometry(QRect(70, 70, 125, 125))
            label_avatar.setStyleSheet(u"border: none")
            label_avatar.setPixmap(
                QPixmap(u":/images/images/images/PyDracula.png"))
            label_avatar.setScaledContents(True)

            row = idx // 4
            col = idx % 4

            group_btn.pressed.connect(lambda val=group: self.go_to_group(val))

            self.ui.gridLayout_3.addWidget(group_btn, row, col, 1, 1)

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

    def go_to_group(self, group):
        self.group_choosen = group
        widgets.stackedWidget.setCurrentWidget(widgets.widgets)
        widgets.btn_widgets.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_widgets.styleSheet()))
        UIFunctions.resetStyle(self, "btn_widgets")
        self.rerender_file_list(group.nodes, None)

    def rerender_file_list(self, nodes, root_directory=None):
        if self.group_choosen is None:
            return
        # clear table
        widgets.tableWidget.clearContents()
        # disconnect event
        try:
            widgets.tableWidget.cellClicked.disconnect()
        except Exception as e:
            print(e)

        widgets.labelBoxBlenderInstalation.setText(
            self.group_choosen.name.upper() + "'s files")
        self.nodes = nodes
        self.offset = 1

        self.directory_choosen = root_directory
        if root_directory is not None:
            self.offset = 2
            icon = QIcon()
            icon.addFile(u":/icons/images/icons/cil-folder.png",
                         QSize(), QIcon.Active, QIcon.Off)
            __qtablewidgetitem = QTableWidgetItem()
            __qtablewidgetitem.setIcon(icon)
            __qtablewidgetitem.setText(QCoreApplication.translate(
                "MainWindow", f'..'))
            widgets.tableWidget.setItem(1, 0, __qtablewidgetitem)

        widgets.tableWidget.setRowCount(len(nodes) + 1 + self.offset)
        widgets.tableWidget.cellClicked.connect(self.item_clicked)
        self.directories = [node for node in nodes if type(node) == Directory]
        self.files = [node for node in nodes if type(node) == File]
        self.render_files()

    def render_files(self):
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter)
        widgets.tableWidget.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        __qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Size", None))
        __qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"Owner", None))
        __qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"Modify By", None))
        __qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"Created at", None))
        __qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"Updated at", None))
        for idx, _directory in enumerate(self.directories):
            icon = QIcon()
            icon.addFile(u":/icons/images/icons/cil-folder.png",
                         QSize(), QIcon.Active, QIcon.Off)
            __qtablewidgetitem1 = QTableWidgetItem()
            __qtablewidgetitem1.setIcon(icon)
            __qtablewidgetitem1.setText(QCoreApplication.translate(
                "MainWindow", f'{_directory.name}'))
            widgets.tableWidget.setItem(
                idx+self.offset, 0, __qtablewidgetitem1)
            __qtablewidgetitem3 = QTableWidgetItem()
            __qtablewidgetitem3.setText(QCoreApplication.translate(
                "MainWindow", f'{_directory.owner.display_name}'))
            widgets.tableWidget.setItem(
                idx+self.offset, 2, __qtablewidgetitem3)
            __qtablewidgetitem5 = QTableWidgetItem()
            __qtablewidgetitem5.setText(QCoreApplication.translate(
                "MainWindow", f'{_directory.created_at}'))
            widgets.tableWidget.setItem(
                idx+self.offset, 4, __qtablewidgetitem5)
            __qtablewidgetitem6 = QTableWidgetItem()

        offset = len(self.directories) + self.offset
        for idx, _file in enumerate(self.files):
            icon = QIcon()
            icon.addFile(u":/icons/images/icons/cil-file.png",
                         QSize(), QIcon.Active, QIcon.Off)
            __qtablewidgetitem1 = QTableWidgetItem()
            __qtablewidgetitem1.setIcon(icon)
            __qtablewidgetitem1.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.name}'))
            widgets.tableWidget.setItem(idx+offset, 0, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem()
            __qtablewidgetitem2.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.size} bytes'))
            widgets.tableWidget.setItem(idx+offset, 1, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem()
            __qtablewidgetitem3.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.owner.display_name}'))
            widgets.tableWidget.setItem(idx+offset, 2, __qtablewidgetitem3)
            __qtablewidgetitem4 = QTableWidgetItem()
            __qtablewidgetitem4.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.modified_by.display_name}'))
            widgets.tableWidget.setItem(idx+offset, 3, __qtablewidgetitem4)
            __qtablewidgetitem5 = QTableWidgetItem()
            __qtablewidgetitem5.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.created_at}'))
            widgets.tableWidget.setItem(idx+offset, 4, __qtablewidgetitem5)
            __qtablewidgetitem6 = QTableWidgetItem()
            __qtablewidgetitem6.setText(QCoreApplication.translate(
                "MainWindow", f'{_file.updated_at}'))
            widgets.tableWidget.setItem(idx+offset, 5, __qtablewidgetitem6)

    def item_clicked(self, row, col):
        offset = self.offset
        if self.directories is None or len(self.directories) + offset - 1 < row:
            return
        if offset == 2 and row == 1:
            directory_choosen = self.directory_choosen.parent
            if directory_choosen is None:
                self.rerender_file_list(self.group_choosen.nodes, None)
            else:
                self.rerender_file_list(
                    directory_choosen.nodes, directory_choosen)
        else:
            directory_choosen = self.directories[row-offset]
            self.rerender_file_list(directory_choosen.nodes, directory_choosen)

    def create_directory(self):
        name = widgets.lineEdit.text()
        if self.group_choosen is None:
            widgets.labelVersion_3.setText("Please choose a group")
            return
        if name.strip() == "":
            widgets.labelVersion_3.setText(
                "Please enter a name for the directory")
            return
        if any(x.name == name for x in self.directories):
            widgets.labelVersion_3.setText("Directory name already exists")
            return
        data = {
            'name': name,
            'group_id': self.group_choosen.id,
        }
        if self.directory_choosen is not None:
            data['parent_id'] = self.directory_choosen.id
        success, directory = Directory.create_one(data)
        if success:
            widgets.labelVersion_3.setText('')
            widgets.lineEdit.setText('')
            if self.directory_choosen is not None:
                self.directory_choosen.nodes.append(directory)
                self.rerender_file_list(self.directory_choosen.nodes,
                                        self.directory_choosen)
            else:
                self.group_choosen.nodes.append(directory)
                self.rerender_file_list(self.group_choosen.nodes, None)
        else:
            widgets.labelVersion_3.setText(directory)

    def choose_file(self):
        fpath = QFileDialog.getOpenFileUrl(
            widget,
            'Choose file'
        )
        self.file = fpath[0]
        widgets.lineEdit.setText(fpath[0].fileName())

    def upload_file(self):
        name = widgets.lineEdit.text()
        if self.file is None:
            widgets.labelVersion_3.setText("Please choose a file")
            return
        if self.group_choosen is None:
            widgets.labelVersion_3.setText("Please choose a group")
            return
        if any(x.name == name for x in self.files):
            widgets.labelVersion_3.setText("File name already exists")
            return

        data = {
            'name': name.encode('utf-8'),
            'group_id': self.group_choosen.id,
        }
        if self.directory_choosen is not None:
            data['directory_id'] = self.directory_choosen.id

        success, path = File.create_file(data)
        if success == False:
            widgets.labelVersion_3.setText(path)
            return
        try:
            with TFTPClient(Settings.FILE_HOST, Settings.FILE_PORT, Settings.BLOCKSIZE, Settings.WINDOWSIZE) as client:
                file_path = self.file.path()
                client.put_file(path, Path(file_path).read_bytes())
        except Exception as e:
            print(e)
            widgets.labelVersion_3.setText(
                "Error uploading file. Try again later")
            return

        data['size'] = Path(file_path).stat().st_size
        data['path'] = path
        success, file = File.save_file(data)
        if success:
            widgets.labelVersion_3.setText('')
            widgets.lineEdit.setText('')
            if self.directory_choosen is not None:
                self.directory_choosen.nodes.append(file)
                self.rerender_file_list(
                    self.directory_choosen.nodes, self.directory_choosen)
            else:
                self.group_choosen.nodes.append(directory)
                self.rerender_file_list(
                    self.group_choosen.nodes)
            widgets.labelVersion_3.setText('')
        else:
            widgets.labelVersion_3.setText(file)
            return

    def setup_right_menu(self):
        widgets.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        widgets.tableWidget.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self, pos):
        menu = QMenu(widgets.tableWidget)
        row = widgets.tableWidget.rowAt(pos.y())

        if row < self.offset or row == self.offset + len(self.nodes) - 1:
            return

        if row < len(self.directories) + self.offset:
            directory = self.directories[row-self.offset]
            if directory.owner_id == user.id or self.group_choosen.owner_id == user.id:
                icon1 = QIcon()
                icon1.addFile(u":/icons/images/icons/cil-cut.png",
                              QSize(), QIcon.Active, QIcon.Off)
                delete_action = QAction(icon1, "Delete", widgets.tableWidget)
                delete_action.triggered.connect(
                    lambda: self.delete_dir_action(directory))
                menu.addAction(delete_action)

                icon2 = QIcon()
                icon2.addFile(u":/icons/images/icons/cil-share.png",
                              QSize(), QIcon.Active, QIcon.Off)
                change_permission_action = QAction(icon2, "Change permission to " + (
                    'read' if directory.permission == 2 else 'write'), widgets.tableWidget)
                change_permission_action.triggered.connect(
                    lambda: self.change_dir_permission_action(directory))
                menu.addAction(change_permission_action)
        else:
            file = self.files[row-self.offset-len(self.directories)]
            if file.owner_id == user.id or self.group_choosen.owner_id == user.id:
                icon1 = QIcon()
                icon1.addFile(u":/icons/images/icons/cil-cut.png",
                              QSize(), QIcon.Active, QIcon.Off)
                delete_action = QAction(icon1, "Delete", widgets.tableWidget)
                delete_action.triggered.connect(
                    lambda: self.delete_file_action(file))
                menu.addAction(delete_action)

                icon2 = QIcon()
                icon2.addFile(u":/icons/images/icons/cil-share.png",
                              QSize(), QIcon.Active, QIcon.Off)
                change_permission_action = QAction(icon2, "Change permission to " + (
                    'read' if file.permission == 2 else 'write'), widgets.tableWidget)
                change_permission_action.triggered.connect(
                    lambda: self.change_file_permission_action(file))
                menu.addAction(change_permission_action)

                icon3 = QIcon()
                icon3.addFile(u":/icons/images/icons/cil-cloud-download.png",
                              QSize(), QIcon.Active, QIcon.Off)
                download_action = QAction(
                    icon3, "Download", widgets.tableWidget)
                download_action.triggered.connect(
                    lambda: self.download_file_action(file))
                menu.addAction(download_action)

        menu.exec(QCursor.pos())

    def delete_dir_action(self, directory):
        status, error = Directory.delete_one(directory.id)
        if status:
            if self.directory_choosen is None:
                self.group_choosen.nodes.remove(directory)
                self.rerender_file_list(self.group_choosen.nodes)
            else:
                self.directory_choosen.nodes.remove(directory)
                self.rerender_file_list(
                    self.directory_choosen.nodes, self.directory_choosen)
            widgets.labelVersion_3.setText('')
        else:
            widgets.labelVersion_3.setText(error)

    def change_dir_permission_action(self, directory):
        print(directory)

    def change_file_permission_action(self, file):
        print(file)

    def delete_file_action(self, file):
        status, error = File.delete_one(file.id)
        if status:
            if self.directory_choosen is None:
                self.group_choosen.nodes.remove(file)
                self.rerender_file_list(self.group_choosen.nodes)
            else:
                self.directory_choosen.nodes.remove(file)
                self.rerender_file_list(
                    self.directory_choosen.nodes, self.directory_choosen)
            widgets.labelVersion_3.setText('')
        else:
            widgets.labelVersion_3.setText(error)

    def download_file_action(self, file):
        if os.name == 'nt':
            path = QFileDialog.getSaveFileUrl(
                self, "Save file", os.path.join(os.path.expanduser('~'),
                                            "Desktop"), "All Files (*)")
         # type: (QUrl, str)
        else:
            path = QFileDialog.getSaveFileUrl(
                self, "Save file", '/', "All Files (*)")
        fPath = path[0].path()
        if fPath == '':
            return
        
        try:
            with TFTPClient(Settings.FILE_HOST, Settings.FILE_PORT, Settings.BLOCKSIZE, Settings.WINDOWSIZE) as client:
                Path(fPath).write_bytes(client.get_file(file.path))
            widgets.labelVersion_3.setText('')
        except Exception as e:
            print(e)
            widgets.labelVersion_3.setText("Error while downloading file")


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
    if status == True:  # if user is logged in
        user = User.from_dict(data)
        setupUiMain()
    else:
        setupUiLogin()

    # widget.show()
    sys.exit(app.exec())
