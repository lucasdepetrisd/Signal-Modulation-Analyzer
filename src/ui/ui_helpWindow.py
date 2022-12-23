# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpWindowxdcyvl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.files_rc

class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        if not helpWindow.objectName():
            helpWindow.setObjectName(u"helpWindow")
        helpWindow.resize(800, 740)
        helpWindow.setMinimumSize(QSize(800, 740))
        helpWindow.setMaximumSize(QSize(800, 740))
        font = QFont()
        font.setFamily(u"Satoshi Black")
        helpWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/bigSize/icons/bigSize/sigma-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        helpWindow.setWindowIcon(icon)
        helpWindow.setStyleSheet(u"/* LINE EDIT */\n"
"QMainWindow {\n"
"	font-family: \"Satoshi Black\"\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color: rgb(255,255,255);\n"
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
"QScrollBar::sub-lin"
                        "e:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
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
"     subcontrol-origin: ma"
                        "rgin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
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
"QRadioButton::indicator {"
                        "\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
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
"	background-position: ce"
                        "nter;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
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
"QSlid"
                        "er::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
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
        helpWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(helpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 64))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setMaximumSize(QSize(16777215, 52))
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
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
"background-image: url(:/16x16/icons/16x16/sigma-logo.png);\n"
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
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.btn_home = QPushButton(self.frame_label_top_btns)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(30, 30))
        self.btn_home.setMaximumSize(QSize(30, 16777215))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(11, 11, 11);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/icons/20x20/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.horizontalLayout_10.addWidget(self.btn_home)

        self.btn_prev = QPushButton(self.frame_label_top_btns)
        self.btn_prev.setObjectName(u"btn_prev")
        self.btn_prev.setMinimumSize(QSize(30, 30))
        self.btn_prev.setMaximumSize(QSize(30, 16777215))
        self.btn_prev.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(11, 11, 11);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/20x20/icons/20x20/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev.setIcon(icon2)

        self.horizontalLayout_10.addWidget(self.btn_prev)

        self.btn_next = QPushButton(self.frame_label_top_btns)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(30, 30))
        self.btn_next.setMaximumSize(QSize(30, 16777215))
        self.btn_next.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(11, 11, 11);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.btn_next)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
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
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
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
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setMinimumSize(QSize(0, 680))
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy3)
        self.frame_content.setMinimumSize(QSize(0, 0))
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.horizontalLayout_34 = QHBoxLayout(self.page_main)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(6, 6, 6, 6)
        self.frame_32 = QFrame(self.page_main)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(150, 0))
        self.frame_32.setMaximumSize(QSize(250, 16777215))
        self.frame_32.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_32)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_title_bar_top_5 = QLabel(self.frame_32)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_5.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_5.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_5.setMaximumSize(QSize(16777214, 45))
        font2 = QFont()
        font2.setFamily(u"Satoshi Black")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.label_title_bar_top_5.setFont(font2)
        self.label_title_bar_top_5.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_5.setScaledContents(True)
        self.label_title_bar_top_5.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_5.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_title_bar_top_5)

        self.label_top_info_16 = QLabel(self.frame_32)
        self.label_top_info_16.setObjectName(u"label_top_info_16")
        self.label_top_info_16.setMinimumSize(QSize(0, 35))
        self.label_top_info_16.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setFamily(u"Satoshi")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_16.setFont(font3)
        self.label_top_info_16.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_16)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(300, 40))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_34)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(20, 20))
        self.label_20.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"Satoshi Black")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.messageInputASK_3 = QLineEdit(self.frame_34)
        self.messageInputASK_3.setObjectName(u"messageInputASK_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.messageInputASK_3.sizePolicy().hasHeightForWidth())
        self.messageInputASK_3.setSizePolicy(sizePolicy4)
        self.messageInputASK_3.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamily(u"Satoshi Black")
        font5.setPointSize(12)
        self.messageInputASK_3.setFont(font5)
        self.messageInputASK_3.setToolTipDuration(-1)
        self.messageInputASK_3.setAutoFillBackground(False)
        self.messageInputASK_3.setStyleSheet(u"QLineEdit {\n"
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
        self.messageInputASK_3.setInputMethodHints(Qt.ImhNone)
        self.messageInputASK_3.setMaxLength(16)
        self.messageInputASK_3.setFrame(True)
        self.messageInputASK_3.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_15.addWidget(self.messageInputASK_3)


        self.verticalLayout_23.addWidget(self.frame_34)

        self.frame_39 = QFrame(self.frame_32)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(300, 30))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_39)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(20, 20))
        self.label_24.setMaximumSize(QSize(25, 20))
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_32.addWidget(self.label_24)

        self.labelASK_3 = QLabel(self.frame_39)
        self.labelASK_3.setObjectName(u"labelASK_3")
        self.labelASK_3.setMinimumSize(QSize(0, 25))
        self.labelASK_3.setMaximumSize(QSize(16777215, 25))
        font6 = QFont()
        font6.setFamily(u"Satoshi Black")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.labelASK_3.setFont(font6)
        self.labelASK_3.setStyleSheet(u"color: rgb(63, 152, 90);")
        self.labelASK_3.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.labelASK_3)


        self.verticalLayout_23.addWidget(self.frame_39)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 150))
        self.frame_36.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_36)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(300, 50))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_35.setSpacing(4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_41)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(20, 20))
        self.label_26.setMaximumSize(QSize(25, 20))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_35.addWidget(self.label_26)

        self.label_top_info_17 = QLabel(self.frame_41)
        self.label_top_info_17.setObjectName(u"label_top_info_17")
        self.label_top_info_17.setMinimumSize(QSize(0, 10))
        self.label_top_info_17.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_17.setFont(font6)
        self.label_top_info_17.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"}")
        self.label_top_info_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_top_info_17)


        self.verticalLayout_16.addWidget(self.frame_41)

        self.label_top_info_18 = QLabel(self.frame_36)
        self.label_top_info_18.setObjectName(u"label_top_info_18")
        self.label_top_info_18.setMinimumSize(QSize(0, 20))
        self.label_top_info_18.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_18.setFont(font3)
        self.label_top_info_18.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_top_info_18)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(300, 50))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_30.setSpacing(4)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_37)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(20, 20))
        self.label_22.setMaximumSize(QSize(25, 20))
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.label_22)

        self.carrierFreqInputASK_4 = QSpinBox(self.frame_37)
        self.carrierFreqInputASK_4.setObjectName(u"carrierFreqInputASK_4")
        self.carrierFreqInputASK_4.setMinimumSize(QSize(0, 25))
        font7 = QFont()
        font7.setFamily(u"Satoshi")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.carrierFreqInputASK_4.setFont(font7)
        self.carrierFreqInputASK_4.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"color: white;\n"
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
""
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
        self.carrierFreqInputASK_4.setMinimum(1)
        self.carrierFreqInputASK_4.setMaximum(200)

        self.horizontalLayout_30.addWidget(self.carrierFreqInputASK_4)


        self.verticalLayout_16.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(300, 50))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setSpacing(4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_38)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(20, 20))
        self.label_23.setMaximumSize(QSize(25, 20))
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.label_23)

        self.sliderASK_4 = QSlider(self.frame_38)
        self.sliderASK_4.setObjectName(u"sliderASK_4")
        self.sliderASK_4.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderASK_4.setMinimum(1)
        self.sliderASK_4.setMaximum(200)
        self.sliderASK_4.setTracking(False)
        self.sliderASK_4.setOrientation(Qt.Horizontal)
        self.sliderASK_4.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_31.addWidget(self.sliderASK_4)


        self.verticalLayout_16.addWidget(self.frame_38)


        self.verticalLayout_23.addWidget(self.frame_36)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(300, 50))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setSpacing(4)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_35)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(20, 20))
        self.label_21.setMaximumSize(QSize(25, 20))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_29.addWidget(self.label_21)

        self.modulateBtnASK_2 = QPushButton(self.frame_35)
        self.modulateBtnASK_2.setObjectName(u"modulateBtnASK_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.modulateBtnASK_2.sizePolicy().hasHeightForWidth())
        self.modulateBtnASK_2.setSizePolicy(sizePolicy5)
        self.modulateBtnASK_2.setMinimumSize(QSize(150, 30))
        self.modulateBtnASK_2.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnASK_2.setFont(font4)
        self.modulateBtnASK_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"color: white;\n"
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
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-ask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnASK_2.setIcon(icon6)

        self.horizontalLayout_29.addWidget(self.modulateBtnASK_2)


        self.verticalLayout_23.addWidget(self.frame_35)

        self.frame_40 = QFrame(self.frame_32)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(300, 50))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_33.setSpacing(4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_40)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(20, 20))
        self.label_25.setMaximumSize(QSize(25, 20))
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_33.addWidget(self.label_25)

        self.Btn_pauseASK_2 = QPushButton(self.frame_40)
        self.Btn_pauseASK_2.setObjectName(u"Btn_pauseASK_2")
        sizePolicy5.setHeightForWidth(self.Btn_pauseASK_2.sizePolicy().hasHeightForWidth())
        self.Btn_pauseASK_2.setSizePolicy(sizePolicy5)
        self.Btn_pauseASK_2.setMinimumSize(QSize(150, 30))
        self.Btn_pauseASK_2.setMaximumSize(QSize(16777215, 50))
        self.Btn_pauseASK_2.setFont(font4)
        self.Btn_pauseASK_2.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_pauseASK_2.setIcon(icon7)

        self.horizontalLayout_33.addWidget(self.Btn_pauseASK_2)


        self.verticalLayout_23.addWidget(self.frame_40)

        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(300, 50))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_28.setSpacing(4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(20, 20))
        self.label_19.setMaximumSize(QSize(25, 20))
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_28.addWidget(self.label_19)

        self.clearBtnASK_2 = QPushButton(self.frame_33)
        self.clearBtnASK_2.setObjectName(u"clearBtnASK_2")
        sizePolicy5.setHeightForWidth(self.clearBtnASK_2.sizePolicy().hasHeightForWidth())
        self.clearBtnASK_2.setSizePolicy(sizePolicy5)
        self.clearBtnASK_2.setMinimumSize(QSize(150, 30))
        self.clearBtnASK_2.setMaximumSize(QSize(16777215, 50))
        self.clearBtnASK_2.setFont(font4)
        self.clearBtnASK_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(235, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(207, 59, 72);\n"
"color: white;\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtnASK_2.setIcon(icon8)

        self.horizontalLayout_28.addWidget(self.clearBtnASK_2)


        self.verticalLayout_23.addWidget(self.frame_33)

        self.frame_42 = QFrame(self.frame_32)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(300, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_36.setSpacing(4)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_42)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(20, 20))
        self.label_27.setMaximumSize(QSize(25, 20))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_36.addWidget(self.label_27)

        self.Btn_helpFSK = QPushButton(self.frame_42)
        self.Btn_helpFSK.setObjectName(u"Btn_helpFSK")
        sizePolicy3.setHeightForWidth(self.Btn_helpFSK.sizePolicy().hasHeightForWidth())
        self.Btn_helpFSK.setSizePolicy(sizePolicy3)
        self.Btn_helpFSK.setMinimumSize(QSize(100, 30))
        self.Btn_helpFSK.setMaximumSize(QSize(103, 30))
        self.Btn_helpFSK.setFont(font4)
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
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_helpFSK.setIcon(icon9)

        self.horizontalLayout_36.addWidget(self.Btn_helpFSK)


        self.verticalLayout_23.addWidget(self.frame_42)


        self.verticalLayout_15.addLayout(self.verticalLayout_23)


        self.horizontalLayout_34.addWidget(self.frame_32)

        self.frame_10 = QFrame(self.page_main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textASK_4 = QFrame(self.frame_10)
        self.textASK_4.setObjectName(u"textASK_4")
        self.textASK_4.setMaximumSize(QSize(500, 16777215))
        self.textASK_4.setFrameShape(QFrame.StyledPanel)
        self.textASK_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.textASK_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.textASK_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(450, 0))
        font8 = QFont()
        font8.setFamily(u"Satoshi")
        font8.setPointSize(13)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setIndent(0)

        self.verticalLayout_13.addWidget(self.label_18, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.textASK_4)


        self.horizontalLayout_34.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_main)
        self.page_ask = QWidget()
        self.page_ask.setObjectName(u"page_ask")
        self.horizontalLayout_14 = QHBoxLayout(self.page_ask)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(6, 6, 6, 6)
        self.frame_4 = QFrame(self.page_ask)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(180, 385))
        self.frame_4.setMaximumSize(QSize(280, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_title_bar_top_2 = QLabel(self.frame_4)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_2.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_2.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_2.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_2.setFont(font2)
        self.label_title_bar_top_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_2.setScaledContents(True)
        self.label_title_bar_top_2.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_2.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_title_bar_top_2)

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
        self.label_top_info_4.setFont(font6)
        self.label_top_info_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"}")
        self.label_top_info_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_4)

        self.label_top_info_5 = QLabel(self.frame_5)
        self.label_top_info_5.setObjectName(u"label_top_info_5")
        self.label_top_info_5.setMinimumSize(QSize(0, 20))
        self.label_top_info_5.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_5.setFont(font3)
        self.label_top_info_5.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_5)

        self.frame_17 = QFrame(self.frame_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(300, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.carrierFreqInputASK = QSpinBox(self.frame_17)
        self.carrierFreqInputASK.setObjectName(u"carrierFreqInputASK")
        self.carrierFreqInputASK.setMinimumSize(QSize(0, 25))
        self.carrierFreqInputASK.setFont(font7)
        self.carrierFreqInputASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"color: white;\n"
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
""
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
        self.carrierFreqInputASK.setMinimum(1)
        self.carrierFreqInputASK.setMaximum(200)

        self.horizontalLayout_12.addWidget(self.carrierFreqInputASK)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(300, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.sliderASK = QSlider(self.frame_19)
        self.sliderASK.setObjectName(u"sliderASK")
        self.sliderASK.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderASK.setMinimum(1)
        self.sliderASK.setMaximum(200)
        self.sliderASK.setTracking(False)
        self.sliderASK.setOrientation(Qt.Horizontal)
        self.sliderASK.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_17.addWidget(self.sliderASK)


        self.verticalLayout_14.addWidget(self.frame_19)


        self.verticalLayout_25.addWidget(self.frame_5)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy6)
        self.frame_13.setMinimumSize(QSize(0, 100))
        self.frame_13.setMaximumSize(QSize(16777215, 100))
        self.frame_13.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(9, -1, -1, -1)
        self.label_top_info_13 = QLabel(self.frame_13)
        self.label_top_info_13.setObjectName(u"label_top_info_13")
        self.label_top_info_13.setMinimumSize(QSize(0, 20))
        self.label_top_info_13.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_13.setFont(font6)
        self.label_top_info_13.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_top_info_13)

        self.frame_43 = QFrame(self.frame_13)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(300, 50))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_37.setSpacing(4)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_top_info_15 = QLabel(self.frame_43)
        self.label_top_info_15.setObjectName(u"label_top_info_15")
        self.label_top_info_15.setMinimumSize(QSize(0, 20))
        self.label_top_info_15.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_15.setFont(font3)
        self.label_top_info_15.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_top_info_15)

        self.label_resultFSK_2 = QLabel(self.frame_43)
        self.label_resultFSK_2.setObjectName(u"label_resultFSK_2")
        self.label_resultFSK_2.setMinimumSize(QSize(0, 20))
        self.label_resultFSK_2.setMaximumSize(QSize(16777215, 30))
        self.label_resultFSK_2.setFont(font3)
        self.label_resultFSK_2.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_resultFSK_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_resultFSK_2)


        self.verticalLayout_30.addWidget(self.frame_43)


        self.verticalLayout_25.addWidget(self.frame_13)


        self.verticalLayout_12.addLayout(self.verticalLayout_25)


        self.horizontalLayout_14.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame = QFrame(self.page_ask)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textASK = QFrame(self.frame)
        self.textASK.setObjectName(u"textASK")
        self.textASK.setMaximumSize(QSize(500, 16777215))
        self.textASK.setFrameShape(QFrame.StyledPanel)
        self.textASK.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.textASK)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.textASK)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(450, 0))
        font9 = QFont()
        font9.setFamily(u"Satoshi")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.textASK)


        self.horizontalLayout_14.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_ask)
        self.page_fsk = QWidget()
        self.page_fsk.setObjectName(u"page_fsk")
        self.horizontalLayout_13 = QHBoxLayout(self.page_fsk)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.frame_6 = QFrame(self.page_fsk)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(180, 540))
        self.frame_6.setMaximumSize(QSize(280, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setMaximumSize(QSize(16777215, 100))
        self.frame_9.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, -1, -1, -1)
        self.label_top_info_11 = QLabel(self.frame_9)
        self.label_top_info_11.setObjectName(u"label_top_info_11")
        self.label_top_info_11.setMinimumSize(QSize(0, 20))
        self.label_top_info_11.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_11.setFont(font6)
        self.label_top_info_11.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_top_info_11)

        self.frame_31 = QFrame(self.frame_9)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(300, 50))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_27.setSpacing(4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_top_info_12 = QLabel(self.frame_31)
        self.label_top_info_12.setObjectName(u"label_top_info_12")
        self.label_top_info_12.setMinimumSize(QSize(0, 20))
        self.label_top_info_12.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_12.setFont(font3)
        self.label_top_info_12.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_top_info_12)

        self.label_resultFSK = QLabel(self.frame_31)
        self.label_resultFSK.setObjectName(u"label_resultFSK")
        self.label_resultFSK.setMinimumSize(QSize(0, 20))
        self.label_resultFSK.setMaximumSize(QSize(16777215, 30))
        self.label_resultFSK.setFont(font3)
        self.label_resultFSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_resultFSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_resultFSK)


        self.verticalLayout_20.addWidget(self.frame_31)


        self.gridLayout_4.addWidget(self.frame_9, 4, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 150))
        self.frame_7.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setSpacing(4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(6, 6, 6, 6)
        self.label_top_info_6 = QLabel(self.frame_7)
        self.label_top_info_6.setObjectName(u"label_top_info_6")
        self.label_top_info_6.setMinimumSize(QSize(0, 20))
        self.label_top_info_6.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_6.setFont(font6)
        self.label_top_info_6.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_top_info_6)

        self.label_top_info_7 = QLabel(self.frame_7)
        self.label_top_info_7.setObjectName(u"label_top_info_7")
        self.label_top_info_7.setMinimumSize(QSize(0, 20))
        self.label_top_info_7.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_7.setFont(font3)
        self.label_top_info_7.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_top_info_7)

        self.frame_27 = QFrame(self.frame_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(300, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.carrierFreqInputASK_2 = QSpinBox(self.frame_27)
        self.carrierFreqInputASK_2.setObjectName(u"carrierFreqInputASK_2")
        self.carrierFreqInputASK_2.setMinimumSize(QSize(0, 25))
        self.carrierFreqInputASK_2.setFont(font7)
        self.carrierFreqInputASK_2.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"color: white;\n"
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
""
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
        self.carrierFreqInputASK_2.setMinimum(1)
        self.carrierFreqInputASK_2.setMaximum(200)

        self.horizontalLayout_23.addWidget(self.carrierFreqInputASK_2)


        self.verticalLayout_18.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(300, 50))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.sliderASK_2 = QSlider(self.frame_28)
        self.sliderASK_2.setObjectName(u"sliderASK_2")
        self.sliderASK_2.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderASK_2.setMinimum(1)
        self.sliderASK_2.setMaximum(200)
        self.sliderASK_2.setTracking(False)
        self.sliderASK_2.setOrientation(Qt.Horizontal)
        self.sliderASK_2.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_24.addWidget(self.sliderASK_2)


        self.verticalLayout_18.addWidget(self.frame_28)


        self.gridLayout_4.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy6.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy6)
        self.frame_8.setMinimumSize(QSize(0, 120))
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(6, 6, 6, 6)
        self.label_top_info_9 = QLabel(self.frame_8)
        self.label_top_info_9.setObjectName(u"label_top_info_9")
        self.label_top_info_9.setMinimumSize(QSize(0, 20))
        self.label_top_info_9.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_9.setFont(font6)
        self.label_top_info_9.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_top_info_9)

        self.label_top_info_10 = QLabel(self.frame_8)
        self.label_top_info_10.setObjectName(u"label_top_info_10")
        self.label_top_info_10.setMinimumSize(QSize(0, 20))
        self.label_top_info_10.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_10.setFont(font3)
        self.label_top_info_10.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_top_info_10)

        self.frame_29 = QFrame(self.frame_8)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(300, 50))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.carrierFreqInputASK_3 = QSpinBox(self.frame_29)
        self.carrierFreqInputASK_3.setObjectName(u"carrierFreqInputASK_3")
        self.carrierFreqInputASK_3.setMinimumSize(QSize(0, 25))
        self.carrierFreqInputASK_3.setFont(font7)
        self.carrierFreqInputASK_3.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"color: white;\n"
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
""
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
        self.carrierFreqInputASK_3.setMinimum(1)
        self.carrierFreqInputASK_3.setMaximum(200)

        self.horizontalLayout_25.addWidget(self.carrierFreqInputASK_3)


        self.verticalLayout_19.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_8)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(300, 50))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.sliderASK_3 = QSlider(self.frame_30)
        self.sliderASK_3.setObjectName(u"sliderASK_3")
        self.sliderASK_3.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderASK_3.setMinimum(1)
        self.sliderASK_3.setMaximum(200)
        self.sliderASK_3.setTracking(False)
        self.sliderASK_3.setOrientation(Qt.Horizontal)
        self.sliderASK_3.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_26.addWidget(self.sliderASK_3)


        self.verticalLayout_19.addWidget(self.frame_30)


        self.gridLayout_4.addWidget(self.frame_8, 3, 0, 1, 1)

        self.label_title_bar_top_7 = QLabel(self.frame_6)
        self.label_title_bar_top_7.setObjectName(u"label_title_bar_top_7")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_7.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_7.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_7.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_7.setFont(font2)
        self.label_title_bar_top_7.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_7.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_7.setScaledContents(True)
        self.label_title_bar_top_7.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_7.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_title_bar_top_7, 0, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_13.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.page_fsk)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textASK_2 = QFrame(self.frame_2)
        self.textASK_2.setObjectName(u"textASK_2")
        self.textASK_2.setMaximumSize(QSize(500, 16777215))
        self.textASK_2.setFrameShape(QFrame.StyledPanel)
        self.textASK_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.textASK_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.textASK_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(450, 0))
        self.label_2.setMaximumSize(QSize(16777215, 650))
        self.label_2.setFont(font9)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.textASK_2)


        self.horizontalLayout_13.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_fsk)
        self.page_psk = QWidget()
        self.page_psk.setObjectName(u"page_psk")
        self.horizontalLayout_16 = QHBoxLayout(self.page_psk)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(6, 6, 6, 6)
        self.frame_11 = QFrame(self.page_psk)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(180, 385))
        self.frame_11.setMaximumSize(QSize(280, 16777215))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_title_bar_top_4 = QLabel(self.frame_11)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_4.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_4.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_4.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_4.setFont(font2)
        self.label_title_bar_top_4.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_4.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_4.setScaledContents(True)
        self.label_title_bar_top_4.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_4.setWordWrap(False)

        self.verticalLayout_29.addWidget(self.label_title_bar_top_4)

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
        self.label_top_info_8.setFont(font6)
        self.label_top_info_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_top_info_8)

        self.label_top_info_14 = QLabel(self.frame_12)
        self.label_top_info_14.setObjectName(u"label_top_info_14")
        self.label_top_info_14.setMinimumSize(QSize(0, 20))
        self.label_top_info_14.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_14.setFont(font3)
        self.label_top_info_14.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_top_info_14)

        self.carrierFreqInputPSK = QSpinBox(self.frame_12)
        self.carrierFreqInputPSK.setObjectName(u"carrierFreqInputPSK")
        self.carrierFreqInputPSK.setFont(font7)
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

        self.verticalLayout_22.addWidget(self.carrierFreqInputPSK)

        self.sliderPSK = QSlider(self.frame_12)
        self.sliderPSK.setObjectName(u"sliderPSK")
        self.sliderPSK.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}")
        self.sliderPSK.setMinimum(1)
        self.sliderPSK.setMaximum(200)
        self.sliderPSK.setTracking(False)
        self.sliderPSK.setOrientation(Qt.Horizontal)
        self.sliderPSK.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_22.addWidget(self.sliderPSK)


        self.verticalLayout_29.addWidget(self.frame_12)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy6.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy6)
        self.frame_15.setMaximumSize(QSize(16777215, 100))
        self.frame_15.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, -1, -1, -1)
        self.label_top_info_19 = QLabel(self.frame_15)
        self.label_top_info_19.setObjectName(u"label_top_info_19")
        self.label_top_info_19.setMinimumSize(QSize(0, 20))
        self.label_top_info_19.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_19.setFont(font6)
        self.label_top_info_19.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_top_info_19)

        self.frame_44 = QFrame(self.frame_15)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(300, 50))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_top_info_20 = QLabel(self.frame_44)
        self.label_top_info_20.setObjectName(u"label_top_info_20")
        self.label_top_info_20.setMinimumSize(QSize(0, 20))
        self.label_top_info_20.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_20.setFont(font3)
        self.label_top_info_20.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_top_info_20)

        self.label_resultFSK_3 = QLabel(self.frame_44)
        self.label_resultFSK_3.setObjectName(u"label_resultFSK_3")
        self.label_resultFSK_3.setMinimumSize(QSize(0, 20))
        self.label_resultFSK_3.setMaximumSize(QSize(16777215, 30))
        self.label_resultFSK_3.setFont(font3)
        self.label_resultFSK_3.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_resultFSK_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_resultFSK_3)


        self.verticalLayout_31.addWidget(self.frame_44)


        self.verticalLayout_29.addWidget(self.frame_15)


        self.verticalLayout_21.addLayout(self.verticalLayout_29)


        self.horizontalLayout_16.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.page_psk)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textASK_3 = QFrame(self.frame_3)
        self.textASK_3.setObjectName(u"textASK_3")
        self.textASK_3.setMaximumSize(QSize(500, 16777215))
        self.textASK_3.setFrameShape(QFrame.StyledPanel)
        self.textASK_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.textASK_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.textASK_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(450, 0))
        self.label_3.setFont(font9)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_3, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.textASK_3)


        self.horizontalLayout_16.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_psk)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_11 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.frame_18 = QFrame(self.page_settings)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(220, 425))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(6)
        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setMinimumSize(QSize(0, 200))
        self.frame_21.setMaximumSize(QSize(16777215, 400))
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
        self.label_top_info_22.setFont(font6)
        self.label_top_info_22.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_22)

        self.label_top_info_23 = QLabel(self.frame_21)
        self.label_top_info_23.setObjectName(u"label_top_info_23")
        self.label_top_info_23.setMinimumSize(QSize(0, 40))
        self.label_top_info_23.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_23.setFont(font3)
        self.label_top_info_23.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_23.setAlignment(Qt.AlignCenter)
        self.label_top_info_23.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.label_top_info_23)

        self.maxCarrierFSK1 = QSpinBox(self.frame_21)
        self.maxCarrierFSK1.setObjectName(u"maxCarrierFSK1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.maxCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK1.setSizePolicy(sizePolicy7)
        self.maxCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.maxCarrierFSK1.setFont(font7)
        self.maxCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
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
        self.maxCarrierFSK1.setMinimum(1)
        self.maxCarrierFSK1.setMaximum(10000)
        self.maxCarrierFSK1.setValue(200)

        self.verticalLayout_26.addWidget(self.maxCarrierFSK1, 0, Qt.AlignHCenter)

        self.label_top_info_21 = QLabel(self.frame_21)
        self.label_top_info_21.setObjectName(u"label_top_info_21")
        self.label_top_info_21.setMinimumSize(QSize(0, 40))
        self.label_top_info_21.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_21.setFont(font3)
        self.label_top_info_21.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_21.setAlignment(Qt.AlignCenter)
        self.label_top_info_21.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.label_top_info_21)

        self.minCarrierFSK1 = QSpinBox(self.frame_21)
        self.minCarrierFSK1.setObjectName(u"minCarrierFSK1")
        sizePolicy7.setHeightForWidth(self.minCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK1.setSizePolicy(sizePolicy7)
        self.minCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.minCarrierFSK1.setFont(font7)
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

        self.line = QFrame(self.frame_21)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line)

        self.btn_AplicarASK = QPushButton(self.frame_21)
        self.btn_AplicarASK.setObjectName(u"btn_AplicarASK")
        sizePolicy5.setHeightForWidth(self.btn_AplicarASK.sizePolicy().hasHeightForWidth())
        self.btn_AplicarASK.setSizePolicy(sizePolicy5)
        self.btn_AplicarASK.setMinimumSize(QSize(150, 30))
        self.btn_AplicarASK.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarASK.setFont(font4)
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
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_AplicarASK.setIcon(icon10)

        self.verticalLayout_26.addWidget(self.btn_AplicarASK)

        self.frame_20 = QFrame(self.frame_21)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 40))
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_top_info_31 = QLabel(self.frame_20)
        self.label_top_info_31.setObjectName(u"label_top_info_31")
        self.label_top_info_31.setMinimumSize(QSize(0, 20))
        self.label_top_info_31.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_31.setFont(font3)
        self.label_top_info_31.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_top_info_31)

        self.label_maxASK = QLabel(self.frame_20)
        self.label_maxASK.setObjectName(u"label_maxASK")
        self.label_maxASK.setMinimumSize(QSize(0, 20))
        self.label_maxASK.setMaximumSize(QSize(16777215, 30))
        self.label_maxASK.setFont(font3)
        self.label_maxASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_maxASK, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_20)

        self.frame_16 = QFrame(self.frame_21)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_top_info_27 = QLabel(self.frame_16)
        self.label_top_info_27.setObjectName(u"label_top_info_27")
        self.label_top_info_27.setMinimumSize(QSize(0, 20))
        self.label_top_info_27.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_27.setFont(font3)
        self.label_top_info_27.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_top_info_27)

        self.label_minASK = QLabel(self.frame_16)
        self.label_minASK.setObjectName(u"label_minASK")
        self.label_minASK.setMinimumSize(QSize(0, 20))
        self.label_minASK.setMaximumSize(QSize(16777215, 30))
        self.label_minASK.setFont(font3)
        self.label_minASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_minASK, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_16)


        self.gridLayout_7.addWidget(self.frame_21, 2, 0, 1, 1, Qt.AlignTop)

        self.label_title_bar_top_6 = QLabel(self.frame_18)
        self.label_title_bar_top_6.setObjectName(u"label_title_bar_top_6")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_6.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_6.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_6.setMinimumSize(QSize(0, 50))
        self.label_title_bar_top_6.setMaximumSize(QSize(16777215, 50))
        self.label_title_bar_top_6.setFont(font2)
        self.label_title_bar_top_6.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_6.setScaledContents(True)
        self.label_title_bar_top_6.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_6.setWordWrap(False)

        self.gridLayout_7.addWidget(self.label_title_bar_top_6, 1, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.horizontalLayout_11.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.page_settings)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(200, 0))
        self.frame_24.setMaximumSize(QSize(450, 650))
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_14 = QFrame(self.frame_24)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_14)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamily(u"Satoshi")
        font10.setPointSize(18)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_5.setFont(font10)
        self.label_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"padding: 10px\n"
"}")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_5)


        self.verticalLayout_28.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_24)

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
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        helpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(helpWindow)
        self.carrierFreqInputASK_4.valueChanged.connect(self.sliderASK_4.setValue)
        self.sliderASK_4.valueChanged.connect(self.carrierFreqInputASK_4.setValue)
        self.carrierFreqInputASK.valueChanged.connect(self.sliderASK.setValue)
        self.sliderASK.valueChanged.connect(self.carrierFreqInputASK.setValue)
        self.carrierFreqInputASK_2.valueChanged.connect(self.sliderASK_2.setValue)
        self.sliderASK_2.valueChanged.connect(self.carrierFreqInputASK_2.setValue)
        self.carrierFreqInputASK_3.valueChanged.connect(self.sliderASK_3.setValue)
        self.sliderASK_3.valueChanged.connect(self.carrierFreqInputASK_3.setValue)
        self.carrierFreqInputPSK.valueChanged.connect(self.sliderPSK.setValue)
        self.sliderPSK.valueChanged.connect(self.carrierFreqInputPSK.setValue)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(helpWindow)
    # setupUi

    def retranslateUi(self, helpWindow):
        helpWindow.setWindowTitle(QCoreApplication.translate("helpWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("helpWindow", u"Main Window - Base", None))
        self.btn_home.setText("")
        self.btn_prev.setText("")
        self.btn_next.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("helpWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("helpWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_title_bar_top_5.setText(QCoreApplication.translate("helpWindow", u"Panel de Control", None))
        self.label_top_info_16.setText(QCoreApplication.translate("helpWindow", u"Ingrese una cadena\n"
" de 2 / 4 / 8 / 16 bits", None))
        self.label_20.setText(QCoreApplication.translate("helpWindow", u"(1)", None))
#if QT_CONFIG(tooltip)
        self.messageInputASK_3.setToolTip(QCoreApplication.translate("helpWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputASK_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputASK_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputASK_3.setText("")
        self.messageInputASK_3.setPlaceholderText(QCoreApplication.translate("helpWindow", u"Ingrese cadena de bits", None))
        self.label_24.setText(QCoreApplication.translate("helpWindow", u"(2)", None))
        self.labelASK_3.setText(QCoreApplication.translate("helpWindow", u"16/16", None))
        self.label_26.setText(QCoreApplication.translate("helpWindow", u"(3)", None))
        self.label_top_info_17.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_18.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
        self.label_22.setText(QCoreApplication.translate("helpWindow", u"(4)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("helpWindow", u"(5)", None))
        self.label_21.setText(QCoreApplication.translate("helpWindow", u"(6)", None))
        self.modulateBtnASK_2.setText(QCoreApplication.translate("helpWindow", u"Animar", None))
        self.label_25.setText(QCoreApplication.translate("helpWindow", u"(7)", None))
#if QT_CONFIG(tooltip)
        self.Btn_pauseASK_2.setToolTip(QCoreApplication.translate("helpWindow", u"Pausa la animaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_pauseASK_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_pauseASK_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_pauseASK_2.setText(QCoreApplication.translate("helpWindow", u"Pausar", None))
        self.label_19.setText(QCoreApplication.translate("helpWindow", u"(8)", None))
        self.clearBtnASK_2.setText(QCoreApplication.translate("helpWindow", u"Limpiar", None))
        self.label_27.setText(QCoreApplication.translate("helpWindow", u"(9)", None))
#if QT_CONFIG(tooltip)
        self.Btn_helpFSK.setToolTip(QCoreApplication.translate("helpWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpFSK.setText(QCoreApplication.translate("helpWindow", u"Ayuda", None))
        self.label_18.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">\u00a1Bienvenido a SigMA!</span></p><p>A la izquierda se tiene un modelo como el que encontrar\u00e1 en cada tipo de modulaci\u00f3n. La simulaci\u00f3n se actualizar\u00e1 autom\u00e1ticamente a medida que cambie estos valores.</p><p><span style=\" font-size:18pt; text-decoration: underline;\">Ingresar el Mensaje</span></p><p>En (1) puede cambiar la cadena que se enviar\u00e1 como mensaje, en (2) se indicar\u00e1 si coincide con la longitud y los caracteres. SigMA soporta cadenas de bits (0 o 1) de longitudes en potencias de 2 (2, 4, 8 y 16 bits).</p><p><span style=\" font-size:18pt; text-decoration: underline;\">Modificar la Se\u00f1al</span></p><p>En (3) se muestra la se\u00f1al a modificar. Podr\u00e1 ingresar en (4) o deslizar en (5) para cambiar la frecuencia de la se\u00f1al.</p><p><span style=\" font-size:18pt; text-decoration: underline;\">Animar el Resultado</span></p><p>Finalmente para mostrar una ani"
                        "maci\u00f3n de la se\u00f1al presione en el bot\u00f3n Modular (6). Puede Pausar la animaci\u00f3n con (7) o limpiar la pantalla utilizando Limpiar en (8).</p><p><span style=\" font-size:18pt; text-decoration: underline;\">Ayuda</span></p><p>Desde cualquier men\u00fa utilice el bot\u00f3n de ayuda (9) para mostrar m\u00e1s informaci\u00f3n sobre la ventana actual.</p><p align=\"center\"><img src=\":/24x24/icons/24x24/sigma-logo.png\"/></p></body></html>", None))
        self.label_title_bar_top_2.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Amplitud", None))
        self.label_top_info_4.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_5.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_13.setText(QCoreApplication.translate("helpWindow", u"Resultante", None))
        self.label_top_info_15.setText(QCoreApplication.translate("helpWindow", u"AB =", None))
        self.label_resultFSK_2.setText(QCoreApplication.translate("helpWindow", u"longitudCadena (Hz)", None))
        self.label.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>La modulaci\u00f3n por desplazamiento de Amplitud es un tipo de modulaci\u00f3n digital que mediante la variaci\u00f3n de amplitud de la se\u00f1al portadora anal\u00f3gica permite transmitir el mensaje contenido en la se\u00f1al moduladora digital.</p><p>Este cambio de amplitud depende del c\u00f3digo binario de entrada y mantiene constante la frecuencia y fase.</p><p>En la simulaci\u00f3n se utiliza una frecuencia de muestreo para la se\u00f1al digital equivalente a 64 veces la portadora para una mayor precisi\u00f3n al momento de calcular.</p><p>El Ancho de Banda (AB) se calcula mediante la siguiente formula:</p><p align=\"center\">AB = 2B con B = (1/2T)</p><p>Siendo T = 1/longitudCadena entonces:</p><p align=\"center\">AB = longitudCadena (Hz)</p></body></html>", None))
        self.label_top_info_11.setText(QCoreApplication.translate("helpWindow", u"Resultante", None))
        self.label_top_info_12.setText(QCoreApplication.translate("helpWindow", u"AB =", None))
        self.label_resultFSK.setText(QCoreApplication.translate("helpWindow", u"longitudCadena + \u0394f (Hz)", None))
        self.label_top_info_6.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 1", None))
        self.label_top_info_7.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_9.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 2", None))
        self.label_top_info_10.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_7.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Frecuencias", None))
        self.label_2.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>La modulaci\u00f3n por desplazamiento de Frecuencia es un tipo de modulaci\u00f3n digital que utiliza dos se\u00f1ales con frecuencias distintas para enviar el mensaje de la se\u00f1al moduladora digital. Dependiendo del bit de la moduladora se enviara una se\u00f1al u otra.</p><p>Se mantiene constante la amplitud y fase.</p><p>En la simulaci\u00f3n se utiliza una frecuencia de muestreo para la se\u00f1al digital equivalente a 64 veces a la mayor frecuencia entre las se\u00f1ales de entrada para una mayor precisi\u00f3n al momento de hacer los calculos.</p><p>El Ancho de Banda (AB) se calcula mediante la siguiente formula:</p><p align=\"center\">AB = 2B + 2<span style=\" font-weight:400;\">\u0394</span>f </p><p align=\"center\">B = (1/2T) y <span style=\" font-weight:400;\">\u0394</span>f = |f1 - f2|</p><p>Siendo T = 1/longitudCadena entonces:</p><p align=\"center\">AB = longitudCadena + <span style=\" font-weight:400;\">\u0394</span>f (Hz)</p></body></html>", None))
        self.label_title_bar_top_4.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Fase", None))
        self.label_top_info_8.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_14.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_19.setText(QCoreApplication.translate("helpWindow", u"Resultante", None))
        self.label_top_info_20.setText(QCoreApplication.translate("helpWindow", u"AB =", None))
        self.label_resultFSK_3.setText(QCoreApplication.translate("helpWindow", u"longitudCadena (Hz)", None))
        self.label_3.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>La modulaci\u00f3n por desplazamiento de Fase es un tipo de modulaci\u00f3n digital que utiliza una se\u00f1al portadora a la que se le aplica defasajes para enviar el mensaje de la se\u00f1al moduladora digital. Dependiendo del bit de la moduladora se enviara una se\u00f1al u otra.</p><p>Se mantiene constante la amplitud y frecuencia.</p><p>En la simulaci\u00f3n se utiliza una frecuencia de muestreo para la se\u00f1al digital equivalente a 64 veces a la frecuencia de la portadora para una mayor precisi\u00f3n al momento de hacer los calculos.</p><p>El Ancho de Banda (AB) se calcula mediante la siguiente formula:</p><p align=\"center\">AB = 2B</p><p align=\"center\">B = (1/2T)</p><p>Siendo T = 1/longitudCadena entonces:</p><p align=\"center\">AB = longitudCadena (Hz)</p></body></html>", None))
        self.label_top_info_22.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 1", None))
        self.label_top_info_23.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>Frecuencia M\u00e1xima (Hz) 1-10.000</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_21.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>Frecuencia M\u00ednima (Hz) 1-1000</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarASK.setText(QCoreApplication.translate("helpWindow", u"Aplicar", None))
        self.label_top_info_31.setText(QCoreApplication.translate("helpWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxASK.setText(QCoreApplication.translate("helpWindow", u"200 Hz", None))
        self.label_top_info_27.setText(QCoreApplication.translate("helpWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minASK.setText(QCoreApplication.translate("helpWindow", u"1 Hz", None))
        self.label_title_bar_top_6.setText(QCoreApplication.translate("helpWindow", u"Configuraci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p>Desde el menu de Ajustes se puede cambiar los valores m\u00e1ximos y m\u00ednimos de simulaci\u00f3n.</p><p>Los cambios aplicados se mostrar\u00e1n en verde, si se utilizan valores m\u00e1ximos menores a los m\u00ednimos o viceversa no se guardar\u00e1 el cambio.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("helpWindow", u"<html><head/><body><p><img src=\":/20x20/icons/20x20/cil-danger.png\"/><span style=\" color:#ffffff;\"> \u00a1CUIDADO! </span><img src=\":/20x20/icons/20x20/cil-danger.png\"/></p><p><span style=\" color:#e70000;\">LOS VALORES DEMASIADO ALTOS PUEDEN CONGELAR LA APLICACI\u00d3N. SOLO CAMBIAR SI SABE LO QUE HACE.</span></p></body></html>", None))
    # retranslateUi

