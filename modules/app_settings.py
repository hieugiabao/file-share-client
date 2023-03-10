from sys import platform

class Settings:
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """

    # SERVER ORIGIN
    SERVER_ORIGIN = 'http://localhost:8000'
    if platform == 'win32':
        TOKEN_CACHE_FILE = 'C:\\Users\\%s\\.fileshare\\token.txt' % os.getlogin()
    elif platform == 'linux' or platform == 'linux2':
        TOKEN_CACHE_FILE = '/home/hieu/.fileshare/token.txt'
    else:
        TOKEN_CACHE_FILE = 'token.txt'