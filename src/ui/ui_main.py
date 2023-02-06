# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASEprRSFk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from modulation.mplwidget import MplWidget
from pyqtgraph import GraphicsLayoutWidget
from modulation.mplwidget import MplWidgetFSK

import ui.files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QSize(1000, 800))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Satoshi Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/bigSize/icons/bigSize/sigma-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background: transparent; \n"
"/*font-family: \"Satoshi Black\"*/\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLineEdit::Text {\n"
"	width: parent.width\n"
"	height: parent.height\n"
"	font.pointSize: 100\n"
"	minimumPointSize: 10\n"
"	fontSizeMode: Text.Fit\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QSpinBox {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QWidget {\n"
"	background: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
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
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
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
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/20x20/icons/20x20/sigma-logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Satoshi Black")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(189, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 88, 88);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet(u"color: rgb(159, 165, 177);")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_user_icon.setFont(font2)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_22 = QFrame(self.page_home)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 150))
        self.frame_22.setMaximumSize(QSize(16777215, 204))
        self.frame_22.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 95))
        self.frame_25.setMaximumSize(QSize(16777215, 190))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid ;\n"
"	border-radius: 12px;\n"
"	padding: 4px\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_25)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(80, 80))
        self.label.setMaximumSize(QSize(16777215, 89))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_17.addWidget(self.label)

        self.label_6 = QLabel(self.frame_25)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 150))
        font3 = QFont()
        font3.setFamily(u"Satoshi Black")
        font3.setPointSize(40)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_25)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 80))
        self.label_2.setMaximumSize(QSize(16777215, 90))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_17.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_26)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_7.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setFamily(u"Satoshi Black")
        font4.setPointSize(22)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.label_7)


        self.verticalLayout_15.addWidget(self.frame_26)

        self.Btn_helpMain = QPushButton(self.frame_22)
        self.Btn_helpMain.setObjectName(u"Btn_helpMain")
        sizePolicy3.setHeightForWidth(self.Btn_helpMain.sizePolicy().hasHeightForWidth())
        self.Btn_helpMain.setSizePolicy(sizePolicy3)
        self.Btn_helpMain.setMinimumSize(QSize(220, 35))
        self.Btn_helpMain.setMaximumSize(QSize(300, 70))
        font5 = QFont()
        font5.setFamily(u"Satoshi Black")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.Btn_helpMain.setFont(font5)
        self.Btn_helpMain.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_helpMain.setIcon(icon4)

        self.verticalLayout_15.addWidget(self.Btn_helpMain, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_22)

        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 10))
        self.frame_15.setMaximumSize(QSize(16777215, 250))
        self.frame_15.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/bigSize/icons/bigSize/cil-ask.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	width: 20px;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_6.addWidget(self.frame_15)

        self.Btn_ASK = QPushButton(self.frame_2)
        self.Btn_ASK.setObjectName(u"Btn_ASK")
        font6 = QFont()
        font6.setFamily(u"Satoshi Black")
        font6.setPointSize(26)
        font6.setBold(True)
        font6.setWeight(75)
        self.Btn_ASK.setFont(font6)
        self.Btn_ASK.setAutoFillBackground(False)
        self.Btn_ASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 12px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.Btn_ASK.setFlat(False)

        self.verticalLayout_6.addWidget(self.Btn_ASK)


        self.horizontalLayout_9.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 10))
        self.frame_17.setMaximumSize(QSize(16777215, 250))
        self.frame_17.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/bigSize/icons/bigSize/cil-fsk.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.verticalLayout_7.addWidget(self.frame_17)

        self.Btn_FSK = QPushButton(self.frame_3)
        self.Btn_FSK.setObjectName(u"Btn_FSK")
        self.Btn_FSK.setFont(font6)
        self.Btn_FSK.setAutoFillBackground(False)
        self.Btn_FSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 12px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_FSK)


        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 10))
        self.frame_19.setMaximumSize(QSize(16777215, 250))
        self.frame_19.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/bigSize/icons/bigSize/cil-psk.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	width: 20px;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.verticalLayout_8.addWidget(self.frame_19)

        self.Btn_PSK = QPushButton(self.frame_13)
        self.Btn_PSK.setObjectName(u"Btn_PSK")
        self.Btn_PSK.setFont(font6)
        self.Btn_PSK.setAutoFillBackground(False)
        self.Btn_PSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 12px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_PSK)


        self.horizontalLayout_9.addWidget(self.frame_13)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_home)
        self.page_ask = QWidget()
        self.page_ask.setObjectName(u"page_ask")
        self.horizontalLayout_14 = QHBoxLayout(self.page_ask)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_4 = QFrame(self.page_ask)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_title_bar_top_2 = QLabel(self.frame_4)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_2.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_2.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_2.setMaximumSize(QSize(16777215, 100))
        font7 = QFont()
        font7.setFamily(u"Satoshi Black")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        self.label_title_bar_top_2.setFont(font7)
        self.label_title_bar_top_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_2.setScaledContents(True)
        self.label_title_bar_top_2.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_2.setWordWrap(False)

        self.verticalLayout_32.addWidget(self.label_title_bar_top_2)

        self.label_top_info_3 = QLabel(self.frame_4)
        self.label_top_info_3.setObjectName(u"label_top_info_3")
        self.label_top_info_3.setMinimumSize(QSize(0, 25))
        self.label_top_info_3.setMaximumSize(QSize(16777215, 80))
        font8 = QFont()
        font8.setFamily(u"Satoshi")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_top_info_3.setFont(font8)
        self.label_top_info_3.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_top_info_3)

        self.messageInputASK = QLineEdit(self.frame_4)
        self.messageInputASK.setObjectName(u"messageInputASK")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.messageInputASK.sizePolicy().hasHeightForWidth())
        self.messageInputASK.setSizePolicy(sizePolicy5)
        self.messageInputASK.setMinimumSize(QSize(0, 40))
        self.messageInputASK.setFont(font)
        self.messageInputASK.setToolTipDuration(-1)
        self.messageInputASK.setAutoFillBackground(False)
        self.messageInputASK.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.messageInputASK.setInputMethodHints(Qt.ImhNone)
        self.messageInputASK.setMaxLength(16)
        self.messageInputASK.setFrame(True)
        self.messageInputASK.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_32.addWidget(self.messageInputASK)

        self.labelASK = QLabel(self.frame_4)
        self.labelASK.setObjectName(u"labelASK")
        self.labelASK.setMinimumSize(QSize(0, 25))
        self.labelASK.setMaximumSize(QSize(16777215, 25))
        self.labelASK.setFont(font)
        self.labelASK.setStyleSheet(u"color: rgb(63, 152, 90);")
        self.labelASK.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.labelASK)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_top_info_4 = QLabel(self.frame_5)
        self.label_top_info_4.setObjectName(u"label_top_info_4")
        self.label_top_info_4.setMinimumSize(QSize(0, 10))
        self.label_top_info_4.setMaximumSize(QSize(16777215, 25))
        font9 = QFont()
        font9.setFamily(u"Satoshi Black")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_top_info_4.setFont(font9)
        self.label_top_info_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_4)

        self.label_top_info_5 = QLabel(self.frame_5)
        self.label_top_info_5.setObjectName(u"label_top_info_5")
        self.label_top_info_5.setMinimumSize(QSize(0, 20))
        self.label_top_info_5.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_5.setFont(font8)
        self.label_top_info_5.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_5)

        self.carrierFreqInputASK = QSpinBox(self.frame_5)
        self.carrierFreqInputASK.setObjectName(u"carrierFreqInputASK")
        self.carrierFreqInputASK.setMinimumSize(QSize(0, 25))
        font10 = QFont()
        font10.setFamily(u"Satoshi")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.carrierFreqInputASK.setFont(font10)
        self.carrierFreqInputASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.carrierFreqInputASK.setMinimum(1)
        self.carrierFreqInputASK.setMaximum(200)
        self.carrierFreqInputASK.setValue(25)

        self.verticalLayout_14.addWidget(self.carrierFreqInputASK)

        self.sliderASK = QSlider(self.frame_5)
        self.sliderASK.setObjectName(u"sliderASK")
        self.sliderASK.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderASK.setMinimum(1)
        self.sliderASK.setMaximum(200)
        self.sliderASK.setValue(25)
        self.sliderASK.setTracking(False)
        self.sliderASK.setOrientation(Qt.Horizontal)
        self.sliderASK.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_14.addWidget(self.sliderASK)


        self.verticalLayout_32.addWidget(self.frame_5)

        self.modulateBtnASK = QPushButton(self.frame_4)
        self.modulateBtnASK.setObjectName(u"modulateBtnASK")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.modulateBtnASK.sizePolicy().hasHeightForWidth())
        self.modulateBtnASK.setSizePolicy(sizePolicy6)
        self.modulateBtnASK.setMinimumSize(QSize(150, 25))
        self.modulateBtnASK.setMaximumSize(QSize(16777215, 40))
        self.modulateBtnASK.setFont(font5)
        self.modulateBtnASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 185, 78);\n"
"	border: 2px solid rgb(54, 177, 64);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-ask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnASK.setIcon(icon5)

        self.verticalLayout_32.addWidget(self.modulateBtnASK)

        self.Btn_pauseASK = QPushButton(self.frame_4)
        self.Btn_pauseASK.setObjectName(u"Btn_pauseASK")
        sizePolicy6.setHeightForWidth(self.Btn_pauseASK.sizePolicy().hasHeightForWidth())
        self.Btn_pauseASK.setSizePolicy(sizePolicy6)
        self.Btn_pauseASK.setMinimumSize(QSize(150, 30))
        self.Btn_pauseASK.setMaximumSize(QSize(16777215, 40))
        self.Btn_pauseASK.setFont(font5)
        self.Btn_pauseASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(29, 29, 29);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color:  rgb(45, 45, 45);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_pauseASK.setIcon(icon6)

        self.verticalLayout_32.addWidget(self.Btn_pauseASK)

        self.clearBtnASK = QPushButton(self.frame_4)
        self.clearBtnASK.setObjectName(u"clearBtnASK")
        sizePolicy6.setHeightForWidth(self.clearBtnASK.sizePolicy().hasHeightForWidth())
        self.clearBtnASK.setSizePolicy(sizePolicy6)
        self.clearBtnASK.setMinimumSize(QSize(150, 30))
        self.clearBtnASK.setMaximumSize(QSize(16777215, 40))
        self.clearBtnASK.setFont(font5)
        self.clearBtnASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(235, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(207, 59, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 67, 84);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtnASK.setIcon(icon7)

        self.verticalLayout_32.addWidget(self.clearBtnASK)

        self.Btn_helpASK = QPushButton(self.frame_4)
        self.Btn_helpASK.setObjectName(u"Btn_helpASK")
        sizePolicy3.setHeightForWidth(self.Btn_helpASK.sizePolicy().hasHeightForWidth())
        self.Btn_helpASK.setSizePolicy(sizePolicy3)
        self.Btn_helpASK.setMinimumSize(QSize(100, 30))
        self.Btn_helpASK.setMaximumSize(QSize(103, 30))
        self.Btn_helpASK.setFont(font5)
        self.Btn_helpASK.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        self.Btn_helpASK.setIcon(icon4)

        self.verticalLayout_32.addWidget(self.Btn_helpASK, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_12.addLayout(self.verticalLayout_32)


        self.horizontalLayout_14.addWidget(self.frame_4)

        self.stackedWidgetASK = QStackedWidget(self.page_ask)
        self.stackedWidgetASK.setObjectName(u"stackedWidgetASK")
        self.stackedWidgetASK.setMinimumSize(QSize(676, 585))
        self.mplask = QWidget()
        self.mplask.setObjectName(u"mplask")
        self.verticalLayout_20 = QVBoxLayout(self.mplask)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetASK = MplWidget(self.mplask)
        self.MplWidgetASK.setObjectName(u"MplWidgetASK")
        sizePolicy3.setHeightForWidth(self.MplWidgetASK.sizePolicy().hasHeightForWidth())
        self.MplWidgetASK.setSizePolicy(sizePolicy3)
        self.MplWidgetASK.setMinimumSize(QSize(0, 0))
        self.MplWidgetASK.setBaseSize(QSize(0, 0))
        self.MplWidgetASK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_20.addWidget(self.MplWidgetASK)

        self.stackedWidgetASK.addWidget(self.mplask)
        self.pqgask = QWidget()
        self.pqgask.setObjectName(u"pqgask")
        self.verticalLayout_13 = QVBoxLayout(self.pqgask)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PyQtGraphASK = GraphicsLayoutWidget(self.pqgask)
        self.PyQtGraphASK.setObjectName(u"PyQtGraphASK")
        self.PyQtGraphASK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_13.addWidget(self.PyQtGraphASK)

        self.frame_35 = QFrame(self.pqgask)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 50))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(1, 6, 0, 0)
        self.Btn_antialiasASK = QPushButton(self.frame_35)
        self.Btn_antialiasASK.setObjectName(u"Btn_antialiasASK")
        sizePolicy6.setHeightForWidth(self.Btn_antialiasASK.sizePolicy().hasHeightForWidth())
        self.Btn_antialiasASK.setSizePolicy(sizePolicy6)
        self.Btn_antialiasASK.setMinimumSize(QSize(140, 30))
        self.Btn_antialiasASK.setMaximumSize(QSize(16777215, 40))
        font11 = QFont()
        font11.setFamily(u"Satoshi Black")
        font11.setPointSize(13)
        font11.setBold(False)
        font11.setWeight(50)
        self.Btn_antialiasASK.setFont(font11)
        self.Btn_antialiasASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-double-quote-sans-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_antialiasASK.setIcon(icon8)
        self.Btn_antialiasASK.setCheckable(True)
        self.Btn_antialiasASK.setChecked(True)
        self.Btn_antialiasASK.setAutoRepeat(False)
        self.Btn_antialiasASK.setFlat(False)

        self.horizontalLayout_25.addWidget(self.Btn_antialiasASK)

        self.Btn_autoajustadoASK = QPushButton(self.frame_35)
        self.Btn_autoajustadoASK.setObjectName(u"Btn_autoajustadoASK")
        sizePolicy6.setHeightForWidth(self.Btn_autoajustadoASK.sizePolicy().hasHeightForWidth())
        self.Btn_autoajustadoASK.setSizePolicy(sizePolicy6)
        self.Btn_autoajustadoASK.setMinimumSize(QSize(140, 30))
        self.Btn_autoajustadoASK.setMaximumSize(QSize(16777215, 40))
        self.Btn_autoajustadoASK.setFont(font11)
        self.Btn_autoajustadoASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-cursor-move.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_autoajustadoASK.setIcon(icon9)
        self.Btn_autoajustadoASK.setCheckable(False)
        self.Btn_autoajustadoASK.setChecked(False)

        self.horizontalLayout_25.addWidget(self.Btn_autoajustadoASK)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy6.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy6)
        self.frame_36.setMinimumSize(QSize(260, 25))
        self.frame_36.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_velASK = QLabel(self.frame_36)
        self.label_velASK.setObjectName(u"label_velASK")
        self.label_velASK.setMinimumSize(QSize(90, 10))
        self.label_velASK.setMaximumSize(QSize(16777215, 25))
        self.label_velASK.setFont(font9)
        self.label_velASK.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_velASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_velASK)

        self.velocidadInputASK = QSpinBox(self.frame_36)
        self.velocidadInputASK.setObjectName(u"velocidadInputASK")
        sizePolicy6.setHeightForWidth(self.velocidadInputASK.sizePolicy().hasHeightForWidth())
        self.velocidadInputASK.setSizePolicy(sizePolicy6)
        self.velocidadInputASK.setMinimumSize(QSize(0, 15))
        self.velocidadInputASK.setFont(font10)
        self.velocidadInputASK.setLayoutDirection(Qt.LeftToRight)
        self.velocidadInputASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.velocidadInputASK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.velocidadInputASK.setMinimum(1)
        self.velocidadInputASK.setMaximum(5000)
        self.velocidadInputASK.setValue(1)

        self.horizontalLayout_26.addWidget(self.velocidadInputASK)

        self.label_velASK_3 = QLabel(self.frame_36)
        self.label_velASK_3.setObjectName(u"label_velASK_3")
        self.label_velASK_3.setMinimumSize(QSize(80, 10))
        self.label_velASK_3.setMaximumSize(QSize(16777215, 25))
        self.label_velASK_3.setFont(font9)
        self.label_velASK_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_velASK_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_velASK_3)

        self.samplesInputASK = QSpinBox(self.frame_36)
        self.samplesInputASK.setObjectName(u"samplesInputASK")
        sizePolicy6.setHeightForWidth(self.samplesInputASK.sizePolicy().hasHeightForWidth())
        self.samplesInputASK.setSizePolicy(sizePolicy6)
        self.samplesInputASK.setMinimumSize(QSize(0, 15))
        self.samplesInputASK.setFont(font10)
        self.samplesInputASK.setLayoutDirection(Qt.LeftToRight)
        self.samplesInputASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.samplesInputASK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.samplesInputASK.setMinimum(2)
        self.samplesInputASK.setMaximum(5000)
        self.samplesInputASK.setValue(2)

        self.horizontalLayout_26.addWidget(self.samplesInputASK)


        self.horizontalLayout_25.addWidget(self.frame_36, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_35, 0, Qt.AlignLeft)

        self.stackedWidgetASK.addWidget(self.pqgask)

        self.horizontalLayout_14.addWidget(self.stackedWidgetASK)

        self.stackedWidget.addWidget(self.page_ask)
        self.page_fsk = QWidget()
        self.page_fsk.setObjectName(u"page_fsk")
        self.horizontalLayout_13 = QHBoxLayout(self.page_fsk)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.frame_6 = QFrame(self.page_fsk)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setMaximumSize(QSize(300, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(4)
        self.Btn_helpFSK = QPushButton(self.frame_6)
        self.Btn_helpFSK.setObjectName(u"Btn_helpFSK")
        sizePolicy3.setHeightForWidth(self.Btn_helpFSK.sizePolicy().hasHeightForWidth())
        self.Btn_helpFSK.setSizePolicy(sizePolicy3)
        self.Btn_helpFSK.setMinimumSize(QSize(100, 30))
        self.Btn_helpFSK.setMaximumSize(QSize(103, 30))
        self.Btn_helpFSK.setFont(font5)
        self.Btn_helpFSK.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        self.Btn_helpFSK.setIcon(icon4)

        self.gridLayout_4.addWidget(self.Btn_helpFSK, 10, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.labelFSK = QLabel(self.frame_6)
        self.labelFSK.setObjectName(u"labelFSK")
        self.labelFSK.setMinimumSize(QSize(0, 25))
        self.labelFSK.setMaximumSize(QSize(16777215, 25))
        self.labelFSK.setFont(font)
        self.labelFSK.setStyleSheet(u"color: rgb(63, 152, 90);")
        self.labelFSK.setWordWrap(True)

        self.gridLayout_4.addWidget(self.labelFSK, 3, 0, 1, 1)

        self.label_title_bar_top_3 = QLabel(self.frame_6)
        self.label_title_bar_top_3.setObjectName(u"label_title_bar_top_3")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_3.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_3.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_3.setMinimumSize(QSize(0, 25))
        self.label_title_bar_top_3.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_3.setFont(font7)
        self.label_title_bar_top_3.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_3.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_3.setScaledContents(True)
        self.label_title_bar_top_3.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_3.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_title_bar_top_3, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setMinimumSize(QSize(0, 110))
        self.frame_7.setMaximumSize(QSize(16777215, 150))
        self.frame_7.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_top_info_6 = QLabel(self.frame_7)
        self.label_top_info_6.setObjectName(u"label_top_info_6")
        self.label_top_info_6.setMinimumSize(QSize(0, 20))
        self.label_top_info_6.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_6.setFont(font9)
        self.label_top_info_6.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_top_info_6)

        self.label_top_info_7 = QLabel(self.frame_7)
        self.label_top_info_7.setObjectName(u"label_top_info_7")
        self.label_top_info_7.setMinimumSize(QSize(0, 20))
        self.label_top_info_7.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_7.setFont(font8)
        self.label_top_info_7.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_top_info_7)

        self.carrierFreq1InputFSK = QSpinBox(self.frame_7)
        self.carrierFreq1InputFSK.setObjectName(u"carrierFreq1InputFSK")
        self.carrierFreq1InputFSK.setMinimumSize(QSize(0, 25))
        self.carrierFreq1InputFSK.setFont(font10)
        self.carrierFreq1InputFSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.carrierFreq1InputFSK.setMinimum(1)
        self.carrierFreq1InputFSK.setMaximum(200)
        self.carrierFreq1InputFSK.setValue(25)

        self.verticalLayout_18.addWidget(self.carrierFreq1InputFSK)

        self.sliderFSK1 = QSlider(self.frame_7)
        self.sliderFSK1.setObjectName(u"sliderFSK1")
        self.sliderFSK1.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderFSK1.setMinimum(1)
        self.sliderFSK1.setMaximum(200)
        self.sliderFSK1.setValue(25)
        self.sliderFSK1.setTracking(False)
        self.sliderFSK1.setOrientation(Qt.Horizontal)
        self.sliderFSK1.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_18.addWidget(self.sliderFSK1)


        self.gridLayout_4.addWidget(self.frame_7, 4, 0, 1, 1)

        self.messageInputFSK = QLineEdit(self.frame_6)
        self.messageInputFSK.setObjectName(u"messageInputFSK")
        sizePolicy5.setHeightForWidth(self.messageInputFSK.sizePolicy().hasHeightForWidth())
        self.messageInputFSK.setSizePolicy(sizePolicy5)
        self.messageInputFSK.setMinimumSize(QSize(0, 40))
        font12 = QFont()
        font12.setFamily(u"Satoshi Black")
        font12.setPointSize(10)
        self.messageInputFSK.setFont(font12)
        self.messageInputFSK.setToolTipDuration(-1)
        self.messageInputFSK.setAutoFillBackground(False)
        self.messageInputFSK.setStyleSheet(u"QMainWindow > *{\n"
"	backgroung-color: red;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLineEdit::Text {\n"
"	width: parent.width\n"
"	height: parent.height\n"
"	font.pointSize: 100\n"
"	minimumPointSize: 10\n"
"	fontSizeMode: Text.Fit\n"
"}")
        self.messageInputFSK.setInputMethodHints(Qt.ImhNone)
        self.messageInputFSK.setMaxLength(16)
        self.messageInputFSK.setFrame(True)
        self.messageInputFSK.setEchoMode(QLineEdit.Normal)

        self.gridLayout_4.addWidget(self.messageInputFSK, 2, 0, 1, 1)

        self.Btn_pauseFSK = QPushButton(self.frame_6)
        self.Btn_pauseFSK.setObjectName(u"Btn_pauseFSK")
        sizePolicy6.setHeightForWidth(self.Btn_pauseFSK.sizePolicy().hasHeightForWidth())
        self.Btn_pauseFSK.setSizePolicy(sizePolicy6)
        self.Btn_pauseFSK.setMinimumSize(QSize(150, 25))
        self.Btn_pauseFSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_pauseFSK.setFont(font5)
        self.Btn_pauseFSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(29, 29, 29);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color:  rgb(45, 45, 45);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        self.Btn_pauseFSK.setIcon(icon6)

        self.gridLayout_4.addWidget(self.Btn_pauseFSK, 8, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy7.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy7)
        self.frame_8.setMinimumSize(QSize(0, 110))
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_top_info_9 = QLabel(self.frame_8)
        self.label_top_info_9.setObjectName(u"label_top_info_9")
        self.label_top_info_9.setMinimumSize(QSize(0, 20))
        self.label_top_info_9.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_9.setFont(font9)
        self.label_top_info_9.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_top_info_9)

        self.label_top_info_10 = QLabel(self.frame_8)
        self.label_top_info_10.setObjectName(u"label_top_info_10")
        self.label_top_info_10.setMinimumSize(QSize(0, 20))
        self.label_top_info_10.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_10.setFont(font8)
        self.label_top_info_10.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_top_info_10)

        self.carrierFreq2InputFSK = QSpinBox(self.frame_8)
        self.carrierFreq2InputFSK.setObjectName(u"carrierFreq2InputFSK")
        self.carrierFreq2InputFSK.setMinimumSize(QSize(0, 25))
        self.carrierFreq2InputFSK.setFont(font10)
        self.carrierFreq2InputFSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.carrierFreq2InputFSK.setMinimum(1)
        self.carrierFreq2InputFSK.setMaximum(200)
        self.carrierFreq2InputFSK.setValue(50)

        self.verticalLayout_19.addWidget(self.carrierFreq2InputFSK)

        self.sliderFSK2 = QSlider(self.frame_8)
        self.sliderFSK2.setObjectName(u"sliderFSK2")
        self.sliderFSK2.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderFSK2.setMinimum(1)
        self.sliderFSK2.setMaximum(200)
        self.sliderFSK2.setValue(50)
        self.sliderFSK2.setTracking(False)
        self.sliderFSK2.setOrientation(Qt.Horizontal)
        self.sliderFSK2.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_19.addWidget(self.sliderFSK2)


        self.gridLayout_4.addWidget(self.frame_8, 6, 0, 1, 1)

        self.clearBtnFSK = QPushButton(self.frame_6)
        self.clearBtnFSK.setObjectName(u"clearBtnFSK")
        sizePolicy6.setHeightForWidth(self.clearBtnFSK.sizePolicy().hasHeightForWidth())
        self.clearBtnFSK.setSizePolicy(sizePolicy6)
        self.clearBtnFSK.setMinimumSize(QSize(150, 25))
        self.clearBtnFSK.setMaximumSize(QSize(16777215, 40))
        self.clearBtnFSK.setFont(font5)
        self.clearBtnFSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(235, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(207, 59, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 67, 84);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        self.clearBtnFSK.setIcon(icon7)

        self.gridLayout_4.addWidget(self.clearBtnFSK, 9, 0, 1, 1)

        self.label_top_info_13 = QLabel(self.frame_6)
        self.label_top_info_13.setObjectName(u"label_top_info_13")
        self.label_top_info_13.setMinimumSize(QSize(0, 25))
        self.label_top_info_13.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_13.setFont(font8)
        self.label_top_info_13.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_13.setAlignment(Qt.AlignCenter)
        self.label_top_info_13.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_top_info_13, 1, 0, 1, 1)

        self.modulateBtnFSK = QPushButton(self.frame_6)
        self.modulateBtnFSK.setObjectName(u"modulateBtnFSK")
        sizePolicy6.setHeightForWidth(self.modulateBtnFSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnFSK.setSizePolicy(sizePolicy6)
        self.modulateBtnFSK.setMinimumSize(QSize(150, 25))
        self.modulateBtnFSK.setMaximumSize(QSize(16777215, 40))
        self.modulateBtnFSK.setFont(font5)
        self.modulateBtnFSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 185, 78);\n"
"	border: 2px solid rgb(54, 177, 64);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-fsk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnFSK.setIcon(icon10)

        self.gridLayout_4.addWidget(self.modulateBtnFSK, 7, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_13.addWidget(self.frame_6)

        self.stackedWidgetFSK = QStackedWidget(self.page_fsk)
        self.stackedWidgetFSK.setObjectName(u"stackedWidgetFSK")
        self.stackedWidgetFSK.setMinimumSize(QSize(676, 585))
        self.mplfsk = QWidget()
        self.mplfsk.setObjectName(u"mplfsk")
        self.verticalLayout_29 = QVBoxLayout(self.mplfsk)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetFSK = MplWidgetFSK(self.mplfsk)
        self.MplWidgetFSK.setObjectName(u"MplWidgetFSK")
        sizePolicy3.setHeightForWidth(self.MplWidgetFSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetFSK.setSizePolicy(sizePolicy3)
        self.MplWidgetFSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;\n"
"color: rgb(210, 210, 210);")

        self.verticalLayout_29.addWidget(self.MplWidgetFSK)

        self.stackedWidgetFSK.addWidget(self.mplfsk)
        self.pqgfsk = QWidget()
        self.pqgfsk.setObjectName(u"pqgfsk")
        self.verticalLayout_30 = QVBoxLayout(self.pqgfsk)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.PyQtGraphFSK = GraphicsLayoutWidget(self.pqgfsk)
        self.PyQtGraphFSK.setObjectName(u"PyQtGraphFSK")
        self.PyQtGraphFSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_30.addWidget(self.PyQtGraphFSK)

        self.frame_42 = QFrame(self.pqgfsk)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 0))
        self.frame_42.setMaximumSize(QSize(16777215, 50))
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(1, 6, 0, 0)
        self.Btn_antialiasFSK = QPushButton(self.frame_42)
        self.Btn_antialiasFSK.setObjectName(u"Btn_antialiasFSK")
        sizePolicy6.setHeightForWidth(self.Btn_antialiasFSK.sizePolicy().hasHeightForWidth())
        self.Btn_antialiasFSK.setSizePolicy(sizePolicy6)
        self.Btn_antialiasFSK.setMinimumSize(QSize(140, 30))
        self.Btn_antialiasFSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_antialiasFSK.setFont(font11)
        self.Btn_antialiasFSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        self.Btn_antialiasFSK.setIcon(icon8)
        self.Btn_antialiasFSK.setCheckable(True)
        self.Btn_antialiasFSK.setChecked(True)
        self.Btn_antialiasFSK.setAutoRepeat(False)
        self.Btn_antialiasFSK.setFlat(False)

        self.horizontalLayout_36.addWidget(self.Btn_antialiasFSK)

        self.Btn_autoajustadoFSK = QPushButton(self.frame_42)
        self.Btn_autoajustadoFSK.setObjectName(u"Btn_autoajustadoFSK")
        sizePolicy6.setHeightForWidth(self.Btn_autoajustadoFSK.sizePolicy().hasHeightForWidth())
        self.Btn_autoajustadoFSK.setSizePolicy(sizePolicy6)
        self.Btn_autoajustadoFSK.setMinimumSize(QSize(140, 30))
        self.Btn_autoajustadoFSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_autoajustadoFSK.setFont(font11)
        self.Btn_autoajustadoFSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        self.Btn_autoajustadoFSK.setIcon(icon9)
        self.Btn_autoajustadoFSK.setCheckable(False)
        self.Btn_autoajustadoFSK.setChecked(False)

        self.horizontalLayout_36.addWidget(self.Btn_autoajustadoFSK)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy6.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy6)
        self.frame_44.setMinimumSize(QSize(260, 25))
        self.frame_44.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_velFSK = QLabel(self.frame_44)
        self.label_velFSK.setObjectName(u"label_velFSK")
        self.label_velFSK.setMinimumSize(QSize(90, 10))
        self.label_velFSK.setMaximumSize(QSize(16777215, 25))
        self.label_velFSK.setFont(font9)
        self.label_velFSK.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_velFSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_velFSK)

        self.velocidadInputFSK = QSpinBox(self.frame_44)
        self.velocidadInputFSK.setObjectName(u"velocidadInputFSK")
        sizePolicy6.setHeightForWidth(self.velocidadInputFSK.sizePolicy().hasHeightForWidth())
        self.velocidadInputFSK.setSizePolicy(sizePolicy6)
        self.velocidadInputFSK.setMinimumSize(QSize(0, 15))
        self.velocidadInputFSK.setFont(font10)
        self.velocidadInputFSK.setLayoutDirection(Qt.LeftToRight)
        self.velocidadInputFSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.velocidadInputFSK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.velocidadInputFSK.setMinimum(1)
        self.velocidadInputFSK.setMaximum(5000)
        self.velocidadInputFSK.setValue(1)

        self.horizontalLayout_37.addWidget(self.velocidadInputFSK)

        self.label_samFSK = QLabel(self.frame_44)
        self.label_samFSK.setObjectName(u"label_samFSK")
        self.label_samFSK.setMinimumSize(QSize(80, 10))
        self.label_samFSK.setMaximumSize(QSize(16777215, 25))
        self.label_samFSK.setFont(font9)
        self.label_samFSK.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_samFSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_samFSK)

        self.samplesInputFSK = QSpinBox(self.frame_44)
        self.samplesInputFSK.setObjectName(u"samplesInputFSK")
        sizePolicy6.setHeightForWidth(self.samplesInputFSK.sizePolicy().hasHeightForWidth())
        self.samplesInputFSK.setSizePolicy(sizePolicy6)
        self.samplesInputFSK.setMinimumSize(QSize(0, 15))
        self.samplesInputFSK.setFont(font10)
        self.samplesInputFSK.setLayoutDirection(Qt.LeftToRight)
        self.samplesInputFSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.samplesInputFSK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.samplesInputFSK.setMinimum(2)
        self.samplesInputFSK.setMaximum(5000)
        self.samplesInputFSK.setValue(2)

        self.horizontalLayout_37.addWidget(self.samplesInputFSK)


        self.horizontalLayout_36.addWidget(self.frame_44, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.frame_42, 0, Qt.AlignLeft)

        self.stackedWidgetFSK.addWidget(self.pqgfsk)

        self.horizontalLayout_13.addWidget(self.stackedWidgetFSK)

        self.stackedWidget.addWidget(self.page_fsk)
        self.page_psk = QWidget()
        self.page_psk.setObjectName(u"page_psk")
        self.horizontalLayout_16 = QHBoxLayout(self.page_psk)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_11 = QFrame(self.page_psk)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(200, 0))
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.modulateBtnPSK = QPushButton(self.frame_11)
        self.modulateBtnPSK.setObjectName(u"modulateBtnPSK")
        sizePolicy6.setHeightForWidth(self.modulateBtnPSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnPSK.setSizePolicy(sizePolicy6)
        self.modulateBtnPSK.setMinimumSize(QSize(150, 30))
        self.modulateBtnPSK.setMaximumSize(QSize(16777215, 40))
        self.modulateBtnPSK.setFont(font5)
        self.modulateBtnPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 185, 78);\n"
"	border: 2px solid rgb(54, 177, 64);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/16x16/icons/16x16/cil-psk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnPSK.setIcon(icon11)

        self.gridLayout_5.addWidget(self.modulateBtnPSK, 6, 0, 1, 1)

        self.Btn_helpPSK = QPushButton(self.frame_11)
        self.Btn_helpPSK.setObjectName(u"Btn_helpPSK")
        sizePolicy3.setHeightForWidth(self.Btn_helpPSK.sizePolicy().hasHeightForWidth())
        self.Btn_helpPSK.setSizePolicy(sizePolicy3)
        self.Btn_helpPSK.setMinimumSize(QSize(100, 30))
        self.Btn_helpPSK.setMaximumSize(QSize(103, 30))
        self.Btn_helpPSK.setFont(font5)
        self.Btn_helpPSK.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        self.Btn_helpPSK.setIcon(icon4)

        self.gridLayout_5.addWidget(self.Btn_helpPSK, 11, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.Btn_pausePSK = QPushButton(self.frame_11)
        self.Btn_pausePSK.setObjectName(u"Btn_pausePSK")
        sizePolicy6.setHeightForWidth(self.Btn_pausePSK.sizePolicy().hasHeightForWidth())
        self.Btn_pausePSK.setSizePolicy(sizePolicy6)
        self.Btn_pausePSK.setMinimumSize(QSize(0, 30))
        self.Btn_pausePSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_pausePSK.setFont(font5)
        self.Btn_pausePSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(29, 29, 29);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color:  rgb(45, 45, 45);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        self.Btn_pausePSK.setIcon(icon6)

        self.gridLayout_5.addWidget(self.Btn_pausePSK, 7, 0, 1, 1)

        self.label_title_bar_top_4 = QLabel(self.frame_11)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_4.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_4.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_4.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_4.setFont(font7)
        self.label_title_bar_top_4.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_4.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_4.setScaledContents(True)
        self.label_title_bar_top_4.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_4.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label_title_bar_top_4, 0, 0, 1, 1)

        self.messageInputPSK = QLineEdit(self.frame_11)
        self.messageInputPSK.setObjectName(u"messageInputPSK")
        sizePolicy5.setHeightForWidth(self.messageInputPSK.sizePolicy().hasHeightForWidth())
        self.messageInputPSK.setSizePolicy(sizePolicy5)
        self.messageInputPSK.setMinimumSize(QSize(0, 40))
        self.messageInputPSK.setFont(font12)
        self.messageInputPSK.setToolTipDuration(-1)
        self.messageInputPSK.setAutoFillBackground(False)
        self.messageInputPSK.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLineEdit::Text {\n"
"width: parent.width\n"
"height: parent.height\n"
"font.pointSize: 100\n"
"minimumPointSize: 10\n"
"fontSizeMode: Text.Fit\n"
"}")
        self.messageInputPSK.setInputMethodHints(Qt.ImhNone)
        self.messageInputPSK.setMaxLength(16)
        self.messageInputPSK.setFrame(True)
        self.messageInputPSK.setEchoMode(QLineEdit.Normal)

        self.gridLayout_5.addWidget(self.messageInputPSK, 3, 0, 1, 1)

        self.labelPSK = QLabel(self.frame_11)
        self.labelPSK.setObjectName(u"labelPSK")
        self.labelPSK.setMinimumSize(QSize(50, 25))
        self.labelPSK.setMaximumSize(QSize(16777215, 25))
        self.labelPSK.setFont(font)
        self.labelPSK.setStyleSheet(u"color: rgb(63, 152, 90);")
        self.labelPSK.setWordWrap(True)

        self.gridLayout_5.addWidget(self.labelPSK, 4, 0, 1, 1)

        self.clearBtnPSK = QPushButton(self.frame_11)
        self.clearBtnPSK.setObjectName(u"clearBtnPSK")
        sizePolicy6.setHeightForWidth(self.clearBtnPSK.sizePolicy().hasHeightForWidth())
        self.clearBtnPSK.setSizePolicy(sizePolicy6)
        self.clearBtnPSK.setMinimumSize(QSize(150, 30))
        self.clearBtnPSK.setMaximumSize(QSize(16777215, 40))
        self.clearBtnPSK.setFont(font5)
        self.clearBtnPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(235, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(207, 59, 72);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 67, 84);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(139, 37, 46);\n"
"	border: 2px solid rgb(207, 59, 72);\n"
"}")
        self.clearBtnPSK.setIcon(icon7)

        self.gridLayout_5.addWidget(self.clearBtnPSK, 8, 0, 1, 1)

        self.label_top_info_15 = QLabel(self.frame_11)
        self.label_top_info_15.setObjectName(u"label_top_info_15")
        self.label_top_info_15.setMinimumSize(QSize(0, 25))
        self.label_top_info_15.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_15.setFont(font8)
        self.label_top_info_15.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_top_info_15, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 150))
        self.frame_12.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_top_info_8 = QLabel(self.frame_12)
        self.label_top_info_8.setObjectName(u"label_top_info_8")
        self.label_top_info_8.setMinimumSize(QSize(0, 10))
        self.label_top_info_8.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_8.setFont(font9)
        self.label_top_info_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_top_info_8)

        self.label_top_info_14 = QLabel(self.frame_12)
        self.label_top_info_14.setObjectName(u"label_top_info_14")
        self.label_top_info_14.setMinimumSize(QSize(0, 20))
        self.label_top_info_14.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_14.setFont(font8)
        self.label_top_info_14.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_top_info_14)

        self.carrierFreqInputPSK = QSpinBox(self.frame_12)
        self.carrierFreqInputPSK.setObjectName(u"carrierFreqInputPSK")
        self.carrierFreqInputPSK.setMinimumSize(QSize(0, 25))
        self.carrierFreqInputPSK.setFont(font10)
        self.carrierFreqInputPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.carrierFreqInputPSK.setMinimum(1)
        self.carrierFreqInputPSK.setMaximum(200)
        self.carrierFreqInputPSK.setValue(25)

        self.verticalLayout_22.addWidget(self.carrierFreqInputPSK)

        self.sliderPSK = QSlider(self.frame_12)
        self.sliderPSK.setObjectName(u"sliderPSK")
        self.sliderPSK.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderPSK.setMinimum(1)
        self.sliderPSK.setMaximum(200)
        self.sliderPSK.setValue(15)
        self.sliderPSK.setTracking(False)
        self.sliderPSK.setOrientation(Qt.Horizontal)
        self.sliderPSK.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_22.addWidget(self.sliderPSK)


        self.gridLayout_5.addWidget(self.frame_12, 5, 0, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_5)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.stackedWidgetPSK = QStackedWidget(self.page_psk)
        self.stackedWidgetPSK.setObjectName(u"stackedWidgetPSK")
        self.stackedWidgetPSK.setMinimumSize(QSize(676, 585))
        self.mplpsk = QWidget()
        self.mplpsk.setObjectName(u"mplpsk")
        self.verticalLayout_31 = QVBoxLayout(self.mplpsk)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetPSK = MplWidget(self.mplpsk)
        self.MplWidgetPSK.setObjectName(u"MplWidgetPSK")
        sizePolicy3.setHeightForWidth(self.MplWidgetPSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetPSK.setSizePolicy(sizePolicy3)
        self.MplWidgetPSK.setMinimumSize(QSize(0, 0))
        self.MplWidgetPSK.setBaseSize(QSize(0, 0))
        self.MplWidgetPSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_31.addWidget(self.MplWidgetPSK)

        self.stackedWidgetPSK.addWidget(self.mplpsk)
        self.pqgpsk = QWidget()
        self.pqgpsk.setObjectName(u"pqgpsk")
        self.verticalLayout_33 = QVBoxLayout(self.pqgpsk)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.PyQtGraphPSK = GraphicsLayoutWidget(self.pqgpsk)
        self.PyQtGraphPSK.setObjectName(u"PyQtGraphPSK")
        self.PyQtGraphPSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_33.addWidget(self.PyQtGraphPSK)

        self.frame_45 = QFrame(self.pqgpsk)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 0))
        self.frame_45.setMaximumSize(QSize(16777215, 50))
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(1, 6, 0, 0)
        self.Btn_antialiasPSK = QPushButton(self.frame_45)
        self.Btn_antialiasPSK.setObjectName(u"Btn_antialiasPSK")
        sizePolicy6.setHeightForWidth(self.Btn_antialiasPSK.sizePolicy().hasHeightForWidth())
        self.Btn_antialiasPSK.setSizePolicy(sizePolicy6)
        self.Btn_antialiasPSK.setMinimumSize(QSize(140, 30))
        self.Btn_antialiasPSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_antialiasPSK.setFont(font11)
        self.Btn_antialiasPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        self.Btn_antialiasPSK.setIcon(icon8)
        self.Btn_antialiasPSK.setCheckable(True)
        self.Btn_antialiasPSK.setChecked(True)
        self.Btn_antialiasPSK.setAutoRepeat(False)
        self.Btn_antialiasPSK.setFlat(False)

        self.horizontalLayout_38.addWidget(self.Btn_antialiasPSK)

        self.Btn_autoajustadoPSK = QPushButton(self.frame_45)
        self.Btn_autoajustadoPSK.setObjectName(u"Btn_autoajustadoPSK")
        sizePolicy6.setHeightForWidth(self.Btn_autoajustadoPSK.sizePolicy().hasHeightForWidth())
        self.Btn_autoajustadoPSK.setSizePolicy(sizePolicy6)
        self.Btn_autoajustadoPSK.setMinimumSize(QSize(140, 30))
        self.Btn_autoajustadoPSK.setMaximumSize(QSize(16777215, 40))
        self.Btn_autoajustadoPSK.setFont(font11)
        self.Btn_autoajustadoPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(46, 139, 59);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(53, 128, 76);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 168, 71);\n"
"	border: 2px solid rgb(48, 156, 57);\n"
"}\n"
"QPushButton:pressed, QPushButton:checked {	\n"
"	background-color: rgb(138, 26, 26);\n"
"	border: 2px solid rgb(163, 52, 52);\n"
"}\n"
"")
        self.Btn_autoajustadoPSK.setIcon(icon9)
        self.Btn_autoajustadoPSK.setCheckable(False)
        self.Btn_autoajustadoPSK.setChecked(False)

        self.horizontalLayout_38.addWidget(self.Btn_autoajustadoPSK)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy6.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy6)
        self.frame_46.setMinimumSize(QSize(260, 25))
        self.frame_46.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_velPSK = QLabel(self.frame_46)
        self.label_velPSK.setObjectName(u"label_velPSK")
        self.label_velPSK.setMinimumSize(QSize(90, 10))
        self.label_velPSK.setMaximumSize(QSize(16777215, 25))
        self.label_velPSK.setFont(font9)
        self.label_velPSK.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_velPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_velPSK)

        self.velocidadInputPSK = QSpinBox(self.frame_46)
        self.velocidadInputPSK.setObjectName(u"velocidadInputPSK")
        sizePolicy6.setHeightForWidth(self.velocidadInputPSK.sizePolicy().hasHeightForWidth())
        self.velocidadInputPSK.setSizePolicy(sizePolicy6)
        self.velocidadInputPSK.setMinimumSize(QSize(0, 15))
        self.velocidadInputPSK.setFont(font10)
        self.velocidadInputPSK.setLayoutDirection(Qt.LeftToRight)
        self.velocidadInputPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.velocidadInputPSK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.velocidadInputPSK.setMinimum(1)
        self.velocidadInputPSK.setMaximum(2000)
        self.velocidadInputPSK.setValue(1)

        self.horizontalLayout_39.addWidget(self.velocidadInputPSK)

        self.label_samPSK = QLabel(self.frame_46)
        self.label_samPSK.setObjectName(u"label_samPSK")
        self.label_samPSK.setMinimumSize(QSize(80, 10))
        self.label_samPSK.setMaximumSize(QSize(16777215, 25))
        self.label_samPSK.setFont(font9)
        self.label_samPSK.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_samPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_samPSK)

        self.samplesInputPSK = QSpinBox(self.frame_46)
        self.samplesInputPSK.setObjectName(u"samplesInputPSK")
        sizePolicy6.setHeightForWidth(self.samplesInputPSK.sizePolicy().hasHeightForWidth())
        self.samplesInputPSK.setSizePolicy(sizePolicy6)
        self.samplesInputPSK.setMinimumSize(QSize(0, 15))
        self.samplesInputPSK.setFont(font10)
        self.samplesInputPSK.setLayoutDirection(Qt.LeftToRight)
        self.samplesInputPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.samplesInputPSK.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.samplesInputPSK.setMinimum(2)
        self.samplesInputPSK.setMaximum(5000)
        self.samplesInputPSK.setValue(2)

        self.horizontalLayout_39.addWidget(self.samplesInputPSK)


        self.horizontalLayout_38.addWidget(self.frame_46, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_33.addWidget(self.frame_45, 0, Qt.AlignLeft)

        self.stackedWidgetPSK.addWidget(self.pqgpsk)

        self.horizontalLayout_16.addWidget(self.stackedWidgetPSK)

        self.stackedWidget.addWidget(self.page_psk)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_11 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.frame_43 = QFrame(self.page_settings)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_43)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_27)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(180, 0))
        self.frame_14.setMaximumSize(QSize(350, 16777215))
        self.frame_14.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_title_bar_top_5 = QLabel(self.frame_14)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_5.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_5.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_5.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_5.setMaximumSize(QSize(16777215, 200))
        self.label_title_bar_top_5.setFont(font7)
        self.label_title_bar_top_5.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_5.setScaledContents(True)
        self.label_title_bar_top_5.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_5.setWordWrap(False)

        self.gridLayout_6.addWidget(self.label_title_bar_top_5, 0, 0, 1, 1, Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 280))
        self.frame_16.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, -1, 9)
        self.label_top_info_16 = QLabel(self.frame_16)
        self.label_top_info_16.setObjectName(u"label_top_info_16")
        self.label_top_info_16.setMinimumSize(QSize(0, 25))
        self.label_top_info_16.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_16.setFont(font9)
        self.label_top_info_16.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_16)

        self.label_top_info_17 = QLabel(self.frame_16)
        self.label_top_info_17.setObjectName(u"label_top_info_17")
        self.label_top_info_17.setMinimumSize(QSize(250, 20))
        self.label_top_info_17.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_17.setFont(font8)
        self.label_top_info_17.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_17)

        self.maxCarrierASK = QSpinBox(self.frame_16)
        self.maxCarrierASK.setObjectName(u"maxCarrierASK")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.maxCarrierASK.sizePolicy().hasHeightForWidth())
        self.maxCarrierASK.setSizePolicy(sizePolicy8)
        self.maxCarrierASK.setMinimumSize(QSize(150, 30))
        self.maxCarrierASK.setFont(font10)
        self.maxCarrierASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierASK.setMinimum(1)
        self.maxCarrierASK.setMaximum(1000)
        self.maxCarrierASK.setValue(200)

        self.verticalLayout_23.addWidget(self.maxCarrierASK, 0, Qt.AlignHCenter)

        self.label_top_info_18 = QLabel(self.frame_16)
        self.label_top_info_18.setObjectName(u"label_top_info_18")
        self.label_top_info_18.setMinimumSize(QSize(250, 20))
        self.label_top_info_18.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_18.setFont(font8)
        self.label_top_info_18.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_18)

        self.minCarrierASK = QSpinBox(self.frame_16)
        self.minCarrierASK.setObjectName(u"minCarrierASK")
        sizePolicy8.setHeightForWidth(self.minCarrierASK.sizePolicy().hasHeightForWidth())
        self.minCarrierASK.setSizePolicy(sizePolicy8)
        self.minCarrierASK.setMinimumSize(QSize(150, 30))
        self.minCarrierASK.setFont(font10)
        self.minCarrierASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierASK.setMinimum(1)
        self.minCarrierASK.setMaximum(1000)

        self.verticalLayout_23.addWidget(self.minCarrierASK, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame_16)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line)

        self.btn_AplicarASK = QPushButton(self.frame_16)
        self.btn_AplicarASK.setObjectName(u"btn_AplicarASK")
        sizePolicy6.setHeightForWidth(self.btn_AplicarASK.sizePolicy().hasHeightForWidth())
        self.btn_AplicarASK.setSizePolicy(sizePolicy6)
        self.btn_AplicarASK.setMinimumSize(QSize(150, 30))
        self.btn_AplicarASK.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarASK.setFont(font5)
        self.btn_AplicarASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/16x16/icons/16x16/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_AplicarASK.setIcon(icon12)

        self.verticalLayout_23.addWidget(self.btn_AplicarASK)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_top_info_31 = QLabel(self.frame_10)
        self.label_top_info_31.setObjectName(u"label_top_info_31")
        self.label_top_info_31.setMinimumSize(QSize(0, 20))
        self.label_top_info_31.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_31.setFont(font8)
        self.label_top_info_31.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_top_info_31)

        self.label_maxASK = QLabel(self.frame_10)
        self.label_maxASK.setObjectName(u"label_maxASK")
        self.label_maxASK.setMinimumSize(QSize(0, 20))
        self.label_maxASK.setMaximumSize(QSize(16777215, 30))
        self.label_maxASK.setFont(font8)
        self.label_maxASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_maxASK, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_16)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_top_info_26 = QLabel(self.frame_9)
        self.label_top_info_26.setObjectName(u"label_top_info_26")
        self.label_top_info_26.setMinimumSize(QSize(0, 20))
        self.label_top_info_26.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_26.setFont(font8)
        self.label_top_info_26.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_top_info_26)

        self.label_minASK = QLabel(self.frame_9)
        self.label_minASK.setObjectName(u"label_minASK")
        self.label_minASK.setMinimumSize(QSize(0, 20))
        self.label_minASK.setMaximumSize(QSize(16777215, 30))
        self.label_minASK.setFont(font8)
        self.label_minASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_minASK, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_9)


        self.gridLayout_6.addWidget(self.frame_16, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_16.addLayout(self.gridLayout_6)


        self.horizontalLayout_18.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.frame_27)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(180, 0))
        self.frame_18.setMaximumSize(QSize(350, 16777215))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy7.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy7)
        self.frame_21.setMaximumSize(QSize(16777215, 280))
        self.frame_21.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_21)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_top_info_22 = QLabel(self.frame_21)
        self.label_top_info_22.setObjectName(u"label_top_info_22")
        self.label_top_info_22.setMinimumSize(QSize(0, 25))
        self.label_top_info_22.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_22.setFont(font9)
        self.label_top_info_22.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_22)

        self.label_top_info_23 = QLabel(self.frame_21)
        self.label_top_info_23.setObjectName(u"label_top_info_23")
        self.label_top_info_23.setMinimumSize(QSize(250, 20))
        self.label_top_info_23.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_23.setFont(font8)
        self.label_top_info_23.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_23)

        self.maxCarrierFSK1 = QSpinBox(self.frame_21)
        self.maxCarrierFSK1.setObjectName(u"maxCarrierFSK1")
        sizePolicy8.setHeightForWidth(self.maxCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK1.setSizePolicy(sizePolicy8)
        self.maxCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.maxCarrierFSK1.setFont(font10)
        self.maxCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierFSK1.setMinimum(1)
        self.maxCarrierFSK1.setMaximum(1000)
        self.maxCarrierFSK1.setValue(200)

        self.verticalLayout_26.addWidget(self.maxCarrierFSK1, 0, Qt.AlignHCenter)

        self.label_top_info_21 = QLabel(self.frame_21)
        self.label_top_info_21.setObjectName(u"label_top_info_21")
        self.label_top_info_21.setMinimumSize(QSize(250, 20))
        self.label_top_info_21.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_21.setFont(font8)
        self.label_top_info_21.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_21)

        self.minCarrierFSK1 = QSpinBox(self.frame_21)
        self.minCarrierFSK1.setObjectName(u"minCarrierFSK1")
        sizePolicy8.setHeightForWidth(self.minCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK1.setSizePolicy(sizePolicy8)
        self.minCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.minCarrierFSK1.setFont(font10)
        self.minCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
""
                        "}\n"
"\n"
"QSpinBox::down-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierFSK1.setMinimum(1)
        self.minCarrierFSK1.setMaximum(1000)

        self.verticalLayout_26.addWidget(self.minCarrierFSK1, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.frame_21)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_2)

        self.btn_AplicarFSK1 = QPushButton(self.frame_21)
        self.btn_AplicarFSK1.setObjectName(u"btn_AplicarFSK1")
        sizePolicy6.setHeightForWidth(self.btn_AplicarFSK1.sizePolicy().hasHeightForWidth())
        self.btn_AplicarFSK1.setSizePolicy(sizePolicy6)
        self.btn_AplicarFSK1.setMinimumSize(QSize(150, 30))
        self.btn_AplicarFSK1.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarFSK1.setFont(font5)
        self.btn_AplicarFSK1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarFSK1.setIcon(icon12)

        self.verticalLayout_26.addWidget(self.btn_AplicarFSK1)

        self.frame_30 = QFrame(self.frame_21)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_top_info_32 = QLabel(self.frame_30)
        self.label_top_info_32.setObjectName(u"label_top_info_32")
        self.label_top_info_32.setMinimumSize(QSize(0, 20))
        self.label_top_info_32.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_32.setFont(font8)
        self.label_top_info_32.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_top_info_32)

        self.label_maxFSK_1 = QLabel(self.frame_30)
        self.label_maxFSK_1.setObjectName(u"label_maxFSK_1")
        self.label_maxFSK_1.setMinimumSize(QSize(0, 20))
        self.label_maxFSK_1.setMaximumSize(QSize(16777215, 30))
        self.label_maxFSK_1.setFont(font8)
        self.label_maxFSK_1.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxFSK_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_maxFSK_1, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_top_info_27 = QLabel(self.frame_29)
        self.label_top_info_27.setObjectName(u"label_top_info_27")
        self.label_top_info_27.setMinimumSize(QSize(0, 20))
        self.label_top_info_27.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_27.setFont(font8)
        self.label_top_info_27.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_top_info_27)

        self.label_minFSK_1 = QLabel(self.frame_29)
        self.label_minFSK_1.setObjectName(u"label_minFSK_1")
        self.label_minFSK_1.setMinimumSize(QSize(0, 20))
        self.label_minFSK_1.setMaximumSize(QSize(16777215, 30))
        self.label_minFSK_1.setFont(font8)
        self.label_minFSK_1.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minFSK_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_minFSK_1, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_29)


        self.gridLayout_7.addWidget(self.frame_21, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy7.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy7)
        self.frame_23.setMaximumSize(QSize(16777215, 280))
        self.frame_23.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_top_info_24 = QLabel(self.frame_23)
        self.label_top_info_24.setObjectName(u"label_top_info_24")
        self.label_top_info_24.setMinimumSize(QSize(0, 25))
        self.label_top_info_24.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_24.setFont(font9)
        self.label_top_info_24.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_24)

        self.label_top_info_25 = QLabel(self.frame_23)
        self.label_top_info_25.setObjectName(u"label_top_info_25")
        self.label_top_info_25.setMinimumSize(QSize(250, 20))
        self.label_top_info_25.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_25.setFont(font8)
        self.label_top_info_25.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_25)

        self.maxCarrierFSK2 = QSpinBox(self.frame_23)
        self.maxCarrierFSK2.setObjectName(u"maxCarrierFSK2")
        sizePolicy8.setHeightForWidth(self.maxCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK2.setSizePolicy(sizePolicy8)
        self.maxCarrierFSK2.setMinimumSize(QSize(150, 30))
        self.maxCarrierFSK2.setFont(font10)
        self.maxCarrierFSK2.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierFSK2.setMinimum(1)
        self.maxCarrierFSK2.setMaximum(1000)
        self.maxCarrierFSK2.setValue(200)

        self.verticalLayout_27.addWidget(self.maxCarrierFSK2, 0, Qt.AlignHCenter)

        self.label_top_info_28 = QLabel(self.frame_23)
        self.label_top_info_28.setObjectName(u"label_top_info_28")
        self.label_top_info_28.setMinimumSize(QSize(250, 20))
        self.label_top_info_28.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_28.setFont(font8)
        self.label_top_info_28.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_28)

        self.minCarrierFSK2 = QSpinBox(self.frame_23)
        self.minCarrierFSK2.setObjectName(u"minCarrierFSK2")
        sizePolicy8.setHeightForWidth(self.minCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK2.setSizePolicy(sizePolicy8)
        self.minCarrierFSK2.setMinimumSize(QSize(150, 30))
        self.minCarrierFSK2.setFont(font10)
        self.minCarrierFSK2.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierFSK2.setMinimum(1)
        self.minCarrierFSK2.setMaximum(1000)

        self.verticalLayout_27.addWidget(self.minCarrierFSK2, 0, Qt.AlignHCenter)

        self.line_3 = QFrame(self.frame_23)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_3)

        self.btn_AplicarFSK2 = QPushButton(self.frame_23)
        self.btn_AplicarFSK2.setObjectName(u"btn_AplicarFSK2")
        sizePolicy6.setHeightForWidth(self.btn_AplicarFSK2.sizePolicy().hasHeightForWidth())
        self.btn_AplicarFSK2.setSizePolicy(sizePolicy6)
        self.btn_AplicarFSK2.setMinimumSize(QSize(150, 30))
        self.btn_AplicarFSK2.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarFSK2.setFont(font5)
        self.btn_AplicarFSK2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarFSK2.setIcon(icon12)

        self.verticalLayout_27.addWidget(self.btn_AplicarFSK2)

        self.frame_32 = QFrame(self.frame_23)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_top_info_35 = QLabel(self.frame_32)
        self.label_top_info_35.setObjectName(u"label_top_info_35")
        self.label_top_info_35.setMinimumSize(QSize(0, 20))
        self.label_top_info_35.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_35.setFont(font8)
        self.label_top_info_35.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_top_info_35)

        self.label_maxFSK_2 = QLabel(self.frame_32)
        self.label_maxFSK_2.setObjectName(u"label_maxFSK_2")
        self.label_maxFSK_2.setMinimumSize(QSize(0, 20))
        self.label_maxFSK_2.setMaximumSize(QSize(16777215, 30))
        self.label_maxFSK_2.setFont(font8)
        self.label_maxFSK_2.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxFSK_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_maxFSK_2, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_top_info_34 = QLabel(self.frame_31)
        self.label_top_info_34.setObjectName(u"label_top_info_34")
        self.label_top_info_34.setMinimumSize(QSize(0, 20))
        self.label_top_info_34.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_34.setFont(font8)
        self.label_top_info_34.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_top_info_34)

        self.label_minFSK_2 = QLabel(self.frame_31)
        self.label_minFSK_2.setObjectName(u"label_minFSK_2")
        self.label_minFSK_2.setMinimumSize(QSize(0, 20))
        self.label_minFSK_2.setMaximumSize(QSize(16777215, 30))
        self.label_minFSK_2.setFont(font8)
        self.label_minFSK_2.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minFSK_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_minFSK_2, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_31)


        self.gridLayout_7.addWidget(self.frame_23, 2, 0, 1, 1)

        self.label_title_bar_top_6 = QLabel(self.frame_18)
        self.label_title_bar_top_6.setObjectName(u"label_title_bar_top_6")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_6.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_6.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_6.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_6.setMaximumSize(QSize(16777215, 200))
        self.label_title_bar_top_6.setFont(font7)
        self.label_title_bar_top_6.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_6.setScaledContents(True)
        self.label_title_bar_top_6.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_6.setWordWrap(False)

        self.gridLayout_7.addWidget(self.label_title_bar_top_6, 0, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.horizontalLayout_18.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(180, 0))
        self.frame_24.setMaximumSize(QSize(350, 16777215))
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_title_bar_top_7 = QLabel(self.frame_24)
        self.label_title_bar_top_7.setObjectName(u"label_title_bar_top_7")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_7.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_7.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_7.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_7.setMaximumSize(QSize(16777215, 200))
        self.label_title_bar_top_7.setFont(font7)
        self.label_title_bar_top_7.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_7.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_7.setScaledContents(True)
        self.label_title_bar_top_7.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_7.setWordWrap(False)

        self.gridLayout_8.addWidget(self.label_title_bar_top_7, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_24)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 280))
        self.frame_20.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_top_info_19 = QLabel(self.frame_20)
        self.label_top_info_19.setObjectName(u"label_top_info_19")
        self.label_top_info_19.setMinimumSize(QSize(0, 25))
        self.label_top_info_19.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_19.setFont(font9)
        self.label_top_info_19.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_19)

        self.label_top_info_20 = QLabel(self.frame_20)
        self.label_top_info_20.setObjectName(u"label_top_info_20")
        self.label_top_info_20.setMinimumSize(QSize(250, 20))
        self.label_top_info_20.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_20.setFont(font8)
        self.label_top_info_20.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_20)

        self.maxCarrierPSK = QSpinBox(self.frame_20)
        self.maxCarrierPSK.setObjectName(u"maxCarrierPSK")
        sizePolicy8.setHeightForWidth(self.maxCarrierPSK.sizePolicy().hasHeightForWidth())
        self.maxCarrierPSK.setSizePolicy(sizePolicy8)
        self.maxCarrierPSK.setMinimumSize(QSize(150, 30))
        self.maxCarrierPSK.setFont(font10)
        self.maxCarrierPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierPSK.setMinimum(1)
        self.maxCarrierPSK.setMaximum(1000)
        self.maxCarrierPSK.setValue(200)

        self.verticalLayout_25.addWidget(self.maxCarrierPSK, 0, Qt.AlignHCenter)

        self.label_top_info_29 = QLabel(self.frame_20)
        self.label_top_info_29.setObjectName(u"label_top_info_29")
        self.label_top_info_29.setMinimumSize(QSize(250, 20))
        self.label_top_info_29.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_29.setFont(font8)
        self.label_top_info_29.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_29)

        self.minCarrierPSK = QSpinBox(self.frame_20)
        self.minCarrierPSK.setObjectName(u"minCarrierPSK")
        sizePolicy8.setHeightForWidth(self.minCarrierPSK.sizePolicy().hasHeightForWidth())
        self.minCarrierPSK.setSizePolicy(sizePolicy8)
        self.minCarrierPSK.setMinimumSize(QSize(150, 30))
        self.minCarrierPSK.setFont(font10)
        self.minCarrierPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierPSK.setMinimum(1)
        self.minCarrierPSK.setMaximum(1000)

        self.verticalLayout_25.addWidget(self.minCarrierPSK, 0, Qt.AlignHCenter)

        self.line_4 = QFrame(self.frame_20)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_4)

        self.btn_AplicarPSK = QPushButton(self.frame_20)
        self.btn_AplicarPSK.setObjectName(u"btn_AplicarPSK")
        sizePolicy6.setHeightForWidth(self.btn_AplicarPSK.sizePolicy().hasHeightForWidth())
        self.btn_AplicarPSK.setSizePolicy(sizePolicy6)
        self.btn_AplicarPSK.setMinimumSize(QSize(150, 30))
        self.btn_AplicarPSK.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarPSK.setFont(font5)
        self.btn_AplicarPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarPSK.setIcon(icon12)

        self.verticalLayout_25.addWidget(self.btn_AplicarPSK)

        self.frame_34 = QFrame(self.frame_20)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_top_info_37 = QLabel(self.frame_34)
        self.label_top_info_37.setObjectName(u"label_top_info_37")
        self.label_top_info_37.setMinimumSize(QSize(0, 20))
        self.label_top_info_37.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_37.setFont(font8)
        self.label_top_info_37.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_top_info_37)

        self.label_maxPSK = QLabel(self.frame_34)
        self.label_maxPSK.setObjectName(u"label_maxPSK")
        self.label_maxPSK.setMinimumSize(QSize(0, 20))
        self.label_maxPSK.setMaximumSize(QSize(16777215, 30))
        self.label_maxPSK.setFont(font8)
        self.label_maxPSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_maxPSK, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_top_info_36 = QLabel(self.frame_33)
        self.label_top_info_36.setObjectName(u"label_top_info_36")
        self.label_top_info_36.setMinimumSize(QSize(0, 20))
        self.label_top_info_36.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_36.setFont(font8)
        self.label_top_info_36.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_top_info_36)

        self.label_minPSK = QLabel(self.frame_33)
        self.label_minPSK.setObjectName(u"label_minPSK")
        self.label_minPSK.setMinimumSize(QSize(0, 20))
        self.label_minPSK.setMaximumSize(QSize(16777215, 30))
        self.label_minPSK.setFont(font8)
        self.label_minPSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_minPSK, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_33)


        self.gridLayout_8.addWidget(self.frame_20, 1, 0, 1, 1)


        self.verticalLayout_28.addLayout(self.gridLayout_8)


        self.horizontalLayout_18.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_36.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_43)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Btn_helpSettings = QPushButton(self.frame_28)
        self.Btn_helpSettings.setObjectName(u"Btn_helpSettings")
        sizePolicy3.setHeightForWidth(self.Btn_helpSettings.sizePolicy().hasHeightForWidth())
        self.Btn_helpSettings.setSizePolicy(sizePolicy3)
        self.Btn_helpSettings.setMinimumSize(QSize(100, 30))
        self.Btn_helpSettings.setMaximumSize(QSize(103, 30))
        self.Btn_helpSettings.setFont(font5)
        self.Btn_helpSettings.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        self.Btn_helpSettings.setIcon(icon4)

        self.horizontalLayout_21.addWidget(self.Btn_helpSettings)


        self.verticalLayout_36.addWidget(self.frame_28, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgb(159, 165, 177);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)
        self.carrierFreqInputPSK.valueChanged.connect(self.sliderPSK.setValue)
        self.carrierFreq1InputFSK.valueChanged.connect(self.sliderFSK1.setValue)
        self.carrierFreq2InputFSK.valueChanged.connect(self.sliderFSK2.setValue)
        self.sliderFSK2.valueChanged.connect(self.carrierFreq2InputFSK.setValue)
        self.sliderFSK1.valueChanged.connect(self.carrierFreq1InputFSK.setValue)
        self.sliderPSK.valueChanged.connect(self.carrierFreqInputPSK.setValue)
        self.carrierFreqInputASK.valueChanged.connect(self.sliderASK.setValue)
        self.sliderASK.valueChanged.connect(self.carrierFreqInputASK.setValue)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidgetASK.setCurrentIndex(1)
        self.stackedWidgetFSK.setCurrentIndex(1)
        self.stackedWidgetPSK.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| INICIO", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"LD", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/bigSize/icons/bigSize/sigma-logo.png\"/></p><p><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" Bienvenido/a a SigMA ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/bigSize/icons/bigSize/sigma-logo.png\"/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Seleccione una opci\u00f3n</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Btn_helpMain.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpMain.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpMain.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpMain.setText(QCoreApplication.translate("MainWindow", u"Manual de Usuario", None))
        self.Btn_ASK.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n\n"
"ASK", None))
        self.Btn_FSK.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n\n"
"FSK", None))
        self.Btn_PSK.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n\n"
"PSK", None))
        self.label_title_bar_top_2.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Amplitud", None))
        self.label_top_info_3.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
" de 2, 4, 8 o 16 bits", None))
#if QT_CONFIG(tooltip)
        self.messageInputASK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputASK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputASK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputASK.setText(QCoreApplication.translate("MainWindow", u"0110110001100100", None))
        self.messageInputASK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena de bits", None))
        self.labelASK.setText(QCoreApplication.translate("MainWindow", u"16/16", None))
        self.label_top_info_4.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_5.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.modulateBtnASK.setText(QCoreApplication.translate("MainWindow", u"Animar", None))
#if QT_CONFIG(tooltip)
        self.Btn_pauseASK.setToolTip(QCoreApplication.translate("MainWindow", u"Pausa la animaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_pauseASK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_pauseASK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_pauseASK.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
#if QT_CONFIG(shortcut)
        self.Btn_pauseASK.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.clearBtnASK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
#if QT_CONFIG(shortcut)
        self.clearBtnASK.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Btn_helpASK.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpASK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpASK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpASK.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.Btn_antialiasASK.setText(QCoreApplication.translate("MainWindow", u"Anti-aliasing", None))
        self.Btn_autoajustadoASK.setText(QCoreApplication.translate("MainWindow", u"Auto Ajustar", None))
        self.label_velASK.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
#if QT_CONFIG(tooltip)
        self.velocidadInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_velASK_3.setText(QCoreApplication.translate("MainWindow", u"Muestras", None))
#if QT_CONFIG(tooltip)
        self.samplesInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Btn_helpFSK.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpFSK.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.labelFSK.setText(QCoreApplication.translate("MainWindow", u"16/16", None))
        self.label_title_bar_top_3.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Frecuencias", None))
        self.label_top_info_6.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 1", None))
        self.label_top_info_7.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq1InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.messageInputFSK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputFSK.setText(QCoreApplication.translate("MainWindow", u"0110110001100100", None))
        self.messageInputFSK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese cadena de bits", None))
#if QT_CONFIG(tooltip)
        self.Btn_pauseFSK.setToolTip(QCoreApplication.translate("MainWindow", u"Pausa la animaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_pauseFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_pauseFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_pauseFSK.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
#if QT_CONFIG(shortcut)
        self.Btn_pauseFSK.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.label_top_info_9.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 2", None))
        self.label_top_info_10.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq2InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.clearBtnFSK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
#if QT_CONFIG(shortcut)
        self.clearBtnFSK.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.label_top_info_13.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
" de 2, 4, 8 o 16 bits", None))
        self.modulateBtnFSK.setText(QCoreApplication.translate("MainWindow", u"Animar", None))
        self.Btn_antialiasFSK.setText(QCoreApplication.translate("MainWindow", u"Anti-aliasing", None))
        self.Btn_autoajustadoFSK.setText(QCoreApplication.translate("MainWindow", u"Auto Ajustar", None))
        self.label_velFSK.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
#if QT_CONFIG(tooltip)
        self.velocidadInputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_samFSK.setText(QCoreApplication.translate("MainWindow", u"Muestras", None))
#if QT_CONFIG(tooltip)
        self.samplesInputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.modulateBtnPSK.setText(QCoreApplication.translate("MainWindow", u"Animar", None))
#if QT_CONFIG(tooltip)
        self.Btn_helpPSK.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpPSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpPSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpPSK.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#if QT_CONFIG(tooltip)
        self.Btn_pausePSK.setToolTip(QCoreApplication.translate("MainWindow", u"Pausa la animaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_pausePSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_pausePSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_pausePSK.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
#if QT_CONFIG(shortcut)
        self.Btn_pausePSK.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.label_title_bar_top_4.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Fase", None))
#if QT_CONFIG(tooltip)
        self.messageInputPSK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputPSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputPSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputPSK.setText(QCoreApplication.translate("MainWindow", u"0110110001100100", None))
        self.messageInputPSK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese cadena de bits", None))
        self.labelPSK.setText(QCoreApplication.translate("MainWindow", u"16/16", None))
        self.clearBtnPSK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
#if QT_CONFIG(shortcut)
        self.clearBtnPSK.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.label_top_info_15.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
" de 2, 4, 8 o 16 bits", None))
        self.label_top_info_8.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_14.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Btn_antialiasPSK.setText(QCoreApplication.translate("MainWindow", u"Anti-aliasing", None))
        self.Btn_autoajustadoPSK.setText(QCoreApplication.translate("MainWindow", u"Auto Ajustar", None))
        self.label_velPSK.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
#if QT_CONFIG(tooltip)
        self.velocidadInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_samPSK.setText(QCoreApplication.translate("MainWindow", u"Muestras", None))
#if QT_CONFIG(tooltip)
        self.samplesInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_5.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Amplitud\n"
"ASK", None))
        self.label_top_info_16.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_17.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_18.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarASK.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_31.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxASK.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_26.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minASK.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_top_info_22.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 1", None))
        self.label_top_info_23.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_21.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarFSK1.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_32.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxFSK_1.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_27.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minFSK_1.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_top_info_24.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 2", None))
        self.label_top_info_25.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_28.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarFSK2.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_35.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxFSK_2.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_34.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minFSK_2.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_title_bar_top_6.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Frecuencias\n"
"FSK", None))
        self.label_title_bar_top_7.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Fase\n"
"PSK", None))
        self.label_top_info_19.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_20.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_29.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 1.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarPSK.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_37.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxPSK.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_36.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minPSK.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
#if QT_CONFIG(tooltip)
        self.Btn_helpSettings.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpSettings.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpSettings.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpSettings.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Desarrollado por: Lucas Depetris", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

