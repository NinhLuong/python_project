
from PyQt5 import QtCore, QtGui, QtWidgets
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QtCore.QSize(940, 560))
        self.styleSheet = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet("/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(255, 121, 198);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {    \n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {    \n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-image: url(:/images/images/images/PyDracula.png);\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: rgb(37, 41, 48);\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {    \n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{    \n"
"    background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"    border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{    \n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color:transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {    \n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(33, 37, 43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 121, 198);    \n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {    \n"
"    color: rgb(255, 121, 198);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {    \n"
"    color: rgb(255, 170, 255);\n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {    \n"
"    color: rgb(189, 147, 249);\n"
"    background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.styleSheet.setObjectName("styleSheet")
        self.appMargins = QtWidgets.QVBoxLayout(self.styleSheet)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName("appMargins")
        self.bgApp = QtWidgets.QFrame(self.styleSheet)
        self.bgApp.setStyleSheet("")
        self.bgApp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bgApp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgApp.setObjectName("bgApp")
        self.appLayout = QtWidgets.QHBoxLayout(self.bgApp)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName("appLayout")
        self.leftMenuBg = QtWidgets.QFrame(self.bgApp)
        self.leftMenuBg.setMinimumSize(QtCore.QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuBg.setObjectName("leftMenuBg")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.topLogoInfo = QtWidgets.QFrame(self.leftMenuBg)
        self.topLogoInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet("image: url(:/images/images/images/topLogo.jpg);")
        self.topLogoInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topLogoInfo.setObjectName("topLogoInfo")
        self.titleLeftApp = QtWidgets.QLabel(self.topLogoInfo)
        self.titleLeftApp.setGeometry(QtCore.QRect(70, 8, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLeftApp.setObjectName("titleLeftApp")
        self.titleLeftDescription = QtWidgets.QLabel(self.topLogoInfo)
        self.titleLeftDescription.setGeometry(QtCore.QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titleLeftDescription.setFont(font)
        self.titleLeftDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLeftDescription.setObjectName("titleLeftDescription")
        self.verticalLayout_3.addWidget(self.topLogoInfo)
        self.leftMenuFrame = QtWidgets.QFrame(self.leftMenuBg)
        self.leftMenuFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuFrame.setObjectName("leftMenuFrame")
        self.verticalMenuLayout = QtWidgets.QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName("verticalMenuLayout")
        self.toggleBox = QtWidgets.QFrame(self.leftMenuFrame)
        self.toggleBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.toggleBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggleBox.setObjectName("toggleBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toggleButton = QtWidgets.QPushButton(self.toggleBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setObjectName("toggleButton")
        self.verticalLayout_4.addWidget(self.toggleButton)
        self.verticalMenuLayout.addWidget(self.toggleBox)
        self.topMenu = QtWidgets.QFrame(self.leftMenuFrame)
        self.topMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topMenu.setObjectName("topMenu")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_home = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_home.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_home.setStyleSheet("background-image: url(:/icons/images/icons/cil-home.png);")
        self.btn_home.setIconSize(QtCore.QSize(40, 40))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_8.addWidget(self.btn_home)
        self.btn_widgets = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_widgets.setStyleSheet("background-image: url(:/icons/images/icons/cil-gamepad.png);")
        self.btn_widgets.setObjectName("btn_widgets")
        self.verticalLayout_8.addWidget(self.btn_widgets)
        self.btn_new = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_new.setStyleSheet("background-image: url(:/icons/images/icons/cil-file.png);")
        self.btn_new.setObjectName("btn_new")
        self.verticalLayout_8.addWidget(self.btn_new)
        self.btn_save = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save.setStyleSheet("background-image: url(:/icons/images/icons/cil-save.png)")
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_8.addWidget(self.btn_save)
        self.verticalMenuLayout.addWidget(self.topMenu, 0, QtCore.Qt.AlignTop)
        self.bottomMenu = QtWidgets.QFrame(self.leftMenuFrame)
        self.bottomMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomMenu.setObjectName("bottomMenu")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.toggleLeftBox = QtWidgets.QPushButton(self.bottomMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet("background-image: url(:/icons/images/icons/icon_settings.png);")
        self.toggleLeftBox.setObjectName("toggleLeftBox")
        self.verticalLayout_9.addWidget(self.toggleLeftBox)
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.leftMenuFrame)
        self.appLayout.addWidget(self.leftMenuBg)
        self.extraLeftBox = QtWidgets.QFrame(self.bgApp)
        self.extraLeftBox.setMinimumSize(QtCore.QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraLeftBox.setObjectName("extraLeftBox")
        self.extraColumLayout = QtWidgets.QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName("extraColumLayout")
        self.extraTopBg = QtWidgets.QFrame(self.extraLeftBox)
        self.extraTopBg.setMinimumSize(QtCore.QSize(0, 50))
        self.extraTopBg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraTopBg.setObjectName("extraTopBg")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.extraTopLayout = QtWidgets.QGridLayout()
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setObjectName("extraTopLayout")
        self.extraIcon = QtWidgets.QFrame(self.extraTopBg)
        self.extraIcon.setMinimumSize(QtCore.QSize(20, 0))
        self.extraIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.extraIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraIcon.setObjectName("extraIcon")
        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)
        self.extraLabel = QtWidgets.QLabel(self.extraTopBg)
        self.extraLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.extraLabel.setObjectName("extraLabel")
        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)
        self.extraCloseColumnBtn = QtWidgets.QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QtCore.QSize(20, 20))
        self.extraCloseColumnBtn.setObjectName("extraCloseColumnBtn")
        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.extraTopLayout)
        self.extraColumLayout.addWidget(self.extraTopBg)
        self.extraContent = QtWidgets.QFrame(self.extraLeftBox)
        self.extraContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraContent.setObjectName("extraContent")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.extraTopMenu = QtWidgets.QFrame(self.extraContent)
        self.extraTopMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraTopMenu.setObjectName("extraTopMenu")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_share = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_share.setStyleSheet("background-image: url(:/icons/images/icons/cil-share-boxed.png);")
        self.btn_share.setObjectName("btn_share")
        self.verticalLayout_11.addWidget(self.btn_share)
        self.btn_adjustments = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet("background-image: url(:/icons/images/icons/cil-equalizer.png);")
        self.btn_adjustments.setObjectName("btn_adjustments")
        self.verticalLayout_11.addWidget(self.btn_adjustments)
        self.btn_more = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_more.setStyleSheet("background-image: url(:/icons/images/icons/cil-layers.png);")
        self.btn_more.setObjectName("btn_more")
        self.verticalLayout_11.addWidget(self.btn_more)
        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, QtCore.Qt.AlignTop)
        self.extraCenter = QtWidgets.QFrame(self.extraContent)
        self.extraCenter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraCenter.setObjectName("extraCenter")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textEdit = QtWidgets.QTextEdit(self.extraCenter)
        self.textEdit.setMinimumSize(QtCore.QSize(222, 0))
        self.textEdit.setStyleSheet("background: transparent;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.verticalLayout_12.addWidget(self.extraCenter)
        self.extraBottom = QtWidgets.QFrame(self.extraContent)
        self.extraBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraBottom.setObjectName("extraBottom")
        self.verticalLayout_12.addWidget(self.extraBottom)
        self.extraColumLayout.addWidget(self.extraContent)
        self.appLayout.addWidget(self.extraLeftBox)
        self.contentBox = QtWidgets.QFrame(self.bgApp)
        self.contentBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBox.setObjectName("contentBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentTopBg = QtWidgets.QFrame(self.contentBox)
        self.contentTopBg.setMinimumSize(QtCore.QSize(0, 50))
        self.contentTopBg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentTopBg.setObjectName("contentTopBg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftBox = QtWidgets.QFrame(self.contentTopBg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftBox.setObjectName("leftBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titleRightInfo = QtWidgets.QLabel(self.leftBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleRightInfo.setObjectName("titleRightInfo")
        self.horizontalLayout_3.addWidget(self.titleRightInfo)
        self.horizontalLayout.addWidget(self.leftBox)
        self.rightButtons = QtWidgets.QFrame(self.contentTopBg)
        self.rightButtons.setMinimumSize(QtCore.QSize(0, 28))
        self.rightButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightButtons.setObjectName("rightButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimizeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.minimizeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeAppBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeAppBtn.setObjectName("minimizeAppBtn")
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        self.maximizeRestoreAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.maximizeRestoreAppBtn.setObjectName("maximizeRestoreAppBtn")
        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)
        self.closeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.closeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeAppBtn.setText("")
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.horizontalLayout_2.addWidget(self.closeAppBtn)
        self.horizontalLayout.addWidget(self.rightButtons, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.contentTopBg)
        self.contentBottom = QtWidgets.QFrame(self.contentBox)
        self.contentBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBottom.setObjectName("contentBottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(self.contentBottom)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pagesContainer = QtWidgets.QFrame(self.content)
        self.pagesContainer.setStyleSheet("")
        self.pagesContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pagesContainer.setObjectName("pagesContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pagesContainer)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("background-position: center;\n"
"background-repeat: no-repeat;")
        self.home.setObjectName("home")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QtWidgets.QWidget()
        self.widgets.setStyleSheet("b")
        self.widgets.setObjectName("widgets")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgets)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row_1 = QtWidgets.QFrame(self.widgets)
        self.row_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_1.setObjectName("row_1")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.row_1)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_div_content_1 = QtWidgets.QFrame(self.row_1)
        self.frame_div_content_1.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_div_content_1.setObjectName("frame_div_content_1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_title_wid_1 = QtWidgets.QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_wid_1.setObjectName("frame_title_wid_1")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.labelBoxBlenderInstalation = QtWidgets.QLabel(self.frame_title_wid_1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet("")
        self.labelBoxBlenderInstalation.setObjectName("labelBoxBlenderInstalation")
        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)
        self.verticalLayout_17.addWidget(self.frame_title_wid_1)
        self.frame_content_wid_1 = QtWidgets.QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_wid_1.setObjectName("frame_content_wid_1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_content_wid_1)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(52, 59, 72);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.labelVersion_3 = QtWidgets.QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setStyleSheet("color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelVersion_3.setObjectName("labelVersion_3")
        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)
        self.horizontalLayout_9.addLayout(self.gridLayout)
        self.verticalLayout_17.addWidget(self.frame_content_wid_1)
        self.verticalLayout_16.addWidget(self.frame_div_content_1)
        self.verticalLayout.addWidget(self.row_1)
        self.row_2 = QtWidgets.QFrame(self.widgets)
        self.row_2.setMinimumSize(QtCore.QSize(0, 150))
        self.row_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_2.setObjectName("row_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.row_2)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.row_2)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.row_2)
        self.verticalSlider.setStyleSheet("")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.row_2)
        self.verticalScrollBar.setStyleSheet(" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.row_2)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 278, 222))
        self.scrollAreaWidgetContents.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 200))
        self.plainTextEdit.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_11.addWidget(self.plainTextEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)
        self.comboBox = QtWidgets.QComboBox(self.row_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.row_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.row_2)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon4)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.row_2)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)
        self.verticalLayout_19.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.row_2)
        self.row_3 = QtWidgets.QFrame(self.widgets)
        self.row_3.setMinimumSize(QtCore.QSize(0, 150))
        self.row_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_3.setObjectName("row_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget = QtWidgets.QTableWidget(self.row_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_12.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.row_3)
        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QtWidgets.QWidget()
        self.new_page.setObjectName("new_page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.stackedWidget.addWidget(self.new_page)
        self.verticalLayout_15.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.pagesContainer)
        self.extraRightBox = QtWidgets.QFrame(self.content)
        self.extraRightBox.setMinimumSize(QtCore.QSize(0, 0))
        self.extraRightBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraRightBox.setObjectName("extraRightBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.themeSettingsTopDetail = QtWidgets.QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setMaximumSize(QtCore.QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.themeSettingsTopDetail.setObjectName("themeSettingsTopDetail")
        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)
        self.contentSettings = QtWidgets.QFrame(self.extraRightBox)
        self.contentSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentSettings.setObjectName("contentSettings")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.topMenus = QtWidgets.QFrame(self.contentSettings)
        self.topMenus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topMenus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topMenus.setObjectName("topMenus")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_message = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_message.setStyleSheet("background-image: url(:/icons/images/icons/cil-envelope-open.png);")
        self.btn_message.setObjectName("btn_message")
        self.verticalLayout_14.addWidget(self.btn_message)
        self.btn_print = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_print.setStyleSheet("background-image: url(:/icons/images/icons/cil-print.png);")
        self.btn_print.setObjectName("btn_print")
        self.verticalLayout_14.addWidget(self.btn_print)
        self.btn_logout = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_logout.setStyleSheet("background-image: url(:/icons/images/icons/cil-account-logout.png);")
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_14.addWidget(self.btn_logout)
        self.verticalLayout_13.addWidget(self.topMenus, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.contentSettings)
        self.horizontalLayout_4.addWidget(self.extraRightBox)
        self.verticalLayout_6.addWidget(self.content)
        self.verticalLayout_2.addWidget(self.contentBottom)
        self.appLayout.addWidget(self.contentBox)
        self.appMargins.addWidget(self.bgApp)
        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLeftApp.setText(_translate("MainWindow", "PyDracula"))
        self.titleLeftDescription.setText(_translate("MainWindow", "Modern GUI / Flat Style"))
        self.toggleButton.setText(_translate("MainWindow", "Hide"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_widgets.setText(_translate("MainWindow", "Widgets"))
        self.btn_new.setText(_translate("MainWindow", "New"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.toggleLeftBox.setText(_translate("MainWindow", "Left Box"))
        self.extraLabel.setText(_translate("MainWindow", "Left Box"))
        self.extraCloseColumnBtn.setToolTip(_translate("MainWindow", "Close left box"))
        self.btn_share.setText(_translate("MainWindow", "Share"))
        self.btn_adjustments.setText(_translate("MainWindow", "Adjustments"))
        self.btn_more.setText(_translate("MainWindow", "More"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>"))
        self.titleRightInfo.setText(_translate("MainWindow", "XỬ LÝ TÌNH HUỐNG KHẨN CẤP"))
        self.minimizeAppBtn.setToolTip(_translate("MainWindow", "Minimize"))
        self.maximizeRestoreAppBtn.setToolTip(_translate("MainWindow", "Maximize"))
        self.closeAppBtn.setToolTip(_translate("MainWindow", "Close"))
        self.labelBoxBlenderInstalation.setText(_translate("MainWindow", "FILE BOX"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type here"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.labelVersion_3.setText(_translate("MainWindow", "Label description"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Test 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Test 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Test 3"))
        self.commandLinkButton.setText(_translate("MainWindow", "Link Button"))
        self.commandLinkButton.setDescription(_translate("MainWindow", "Link description"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Test"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Text"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Cell"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Line"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_message.setText(_translate("MainWindow", "Message"))
        self.btn_print.setText(_translate("MainWindow", "Print"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
