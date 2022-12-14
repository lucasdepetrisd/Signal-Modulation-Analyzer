# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
        helpWindow.resize(800, 700)
        helpWindow.setMinimumSize(QSize(800, 700))
        helpWindow.setMaximumSize(QSize(800, 700))
        font = QFont()
        font.setFamilies([u"Satoshi"])
        helpWindow.setFont(font)
        helpWindow.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color: white;\n"
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
""
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
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    b"
                        "ackground: rgb(55, 63, 77);\n"
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
"	height: 15p"
                        "x;\n"
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
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemVi"
                        "ew {\n"
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
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
""
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
        self.centralwidget = QWidget(helpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        font1.setFamilies([u"Satoshi Black"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


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
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

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
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)

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
        self.page_ask = QWidget()
        self.page_ask.setObjectName(u"page_ask")
        self.horizontalLayout_14 = QHBoxLayout(self.page_ask)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(6, 6, 6, 6)
        self.frame_4 = QFrame(self.page_ask)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(180, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        font2 = QFont()
        font2.setFamilies([u"Satoshi Black"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_top_info_4.setFont(font2)
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
        font3 = QFont()
        font3.setFamilies([u"Satoshi"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_top_info_5.setFont(font3)
        self.label_top_info_5.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_5)

        self.carrierFreqInputASK = QSpinBox(self.frame_5)
        self.carrierFreqInputASK.setObjectName(u"carrierFreqInputASK")
        font4 = QFont()
        font4.setFamilies([u"Satoshi"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.carrierFreqInputASK.setFont(font4)
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

        self.verticalLayout_14.addWidget(self.carrierFreqInputASK)

        self.sliderASK = QSlider(self.frame_5)
        self.sliderASK.setObjectName(u"sliderASK")
        self.sliderASK.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.sliderASK.setMinimum(1)
        self.sliderASK.setMaximum(200)
        self.sliderASK.setTracking(False)
        self.sliderASK.setOrientation(Qt.Horizontal)
        self.sliderASK.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_14.addWidget(self.sliderASK)


        self.gridLayout_3.addWidget(self.frame_5, 4, 0, 1, 1)

        self.label_title_bar_top_2 = QLabel(self.frame_4)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_2.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_2.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_2.setMaximumSize(QSize(16777215, 100))
        font5 = QFont()
        font5.setFamilies([u"Satoshi Black"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.label_title_bar_top_2.setFont(font5)
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

        self.gridLayout_3.addWidget(self.label_title_bar_top_2, 0, 0, 1, 1)

        self.clearBtnASK = QPushButton(self.frame_4)
        self.clearBtnASK.setObjectName(u"clearBtnASK")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.clearBtnASK.sizePolicy().hasHeightForWidth())
        self.clearBtnASK.setSizePolicy(sizePolicy4)
        self.clearBtnASK.setMinimumSize(QSize(150, 30))
        self.clearBtnASK.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamilies([u"Satoshi Black"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.clearBtnASK.setFont(font6)
        self.clearBtnASK.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtnASK.setIcon(icon2)

        self.gridLayout_3.addWidget(self.clearBtnASK, 6, 0, 1, 1)

        self.label_top_info_3 = QLabel(self.frame_4)
        self.label_top_info_3.setObjectName(u"label_top_info_3")
        self.label_top_info_3.setMinimumSize(QSize(0, 25))
        self.label_top_info_3.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_3.setFont(font3)
        self.label_top_info_3.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_top_info_3, 1, 0, 1, 1)

        self.messageInputASK = QLineEdit(self.frame_4)
        self.messageInputASK.setObjectName(u"messageInputASK")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.messageInputASK.sizePolicy().hasHeightForWidth())
        self.messageInputASK.setSizePolicy(sizePolicy5)
        self.messageInputASK.setMinimumSize(QSize(0, 40))
        font7 = QFont()
        font7.setFamilies([u"Satoshi Black"])
        font7.setPointSize(10)
        self.messageInputASK.setFont(font7)
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

        self.gridLayout_3.addWidget(self.messageInputASK, 3, 0, 1, 1)

        self.modulateBtnASK = QPushButton(self.frame_4)
        self.modulateBtnASK.setObjectName(u"modulateBtnASK")
        sizePolicy4.setHeightForWidth(self.modulateBtnASK.sizePolicy().hasHeightForWidth())
        self.modulateBtnASK.setSizePolicy(sizePolicy4)
        self.modulateBtnASK.setMinimumSize(QSize(150, 30))
        self.modulateBtnASK.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnASK.setFont(font6)
        self.modulateBtnASK.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-ask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnASK.setIcon(icon3)

        self.gridLayout_3.addWidget(self.modulateBtnASK, 5, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_3)


        self.horizontalLayout_14.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_ask)
        self.page_fsk = QWidget()
        self.page_fsk.setObjectName(u"page_fsk")
        self.horizontalLayout_13 = QHBoxLayout(self.page_fsk)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.frame_6 = QFrame(self.page_fsk)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(180, 0))
        self.frame_6.setMaximumSize(QSize(300, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy6)
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
        self.label_top_info_9.setFont(font2)
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

        self.carrierFreq2InputFSK = QSpinBox(self.frame_8)
        self.carrierFreq2InputFSK.setObjectName(u"carrierFreq2InputFSK")
        self.carrierFreq2InputFSK.setFont(font4)
        self.carrierFreq2InputFSK.setStyleSheet(u"QSpinBox{\n"
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
        self.carrierFreq2InputFSK.setMinimum(1)
        self.carrierFreq2InputFSK.setMaximum(200)

        self.verticalLayout_19.addWidget(self.carrierFreq2InputFSK)

        self.sliderFSK2 = QSlider(self.frame_8)
        self.sliderFSK2.setObjectName(u"sliderFSK2")
        self.sliderFSK2.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.sliderFSK2.setMinimum(1)
        self.sliderFSK2.setMaximum(200)
        self.sliderFSK2.setTracking(False)
        self.sliderFSK2.setOrientation(Qt.Horizontal)
        self.sliderFSK2.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_19.addWidget(self.sliderFSK2)


        self.gridLayout_4.addWidget(self.frame_8, 4, 0, 1, 1)

        self.clearBtnFSK = QPushButton(self.frame_6)
        self.clearBtnFSK.setObjectName(u"clearBtnFSK")
        sizePolicy4.setHeightForWidth(self.clearBtnFSK.sizePolicy().hasHeightForWidth())
        self.clearBtnFSK.setSizePolicy(sizePolicy4)
        self.clearBtnFSK.setMinimumSize(QSize(150, 30))
        self.clearBtnFSK.setMaximumSize(QSize(16777215, 50))
        self.clearBtnFSK.setFont(font6)
        self.clearBtnFSK.setStyleSheet(u"QPushButton {\n"
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
        self.clearBtnFSK.setIcon(icon2)

        self.gridLayout_4.addWidget(self.clearBtnFSK, 7, 0, 1, 1)

        self.messageInputFSK = QLineEdit(self.frame_6)
        self.messageInputFSK.setObjectName(u"messageInputFSK")
        sizePolicy5.setHeightForWidth(self.messageInputFSK.sizePolicy().hasHeightForWidth())
        self.messageInputFSK.setSizePolicy(sizePolicy5)
        self.messageInputFSK.setMinimumSize(QSize(0, 40))
        self.messageInputFSK.setFont(font7)
        self.messageInputFSK.setToolTipDuration(-1)
        self.messageInputFSK.setAutoFillBackground(False)
        self.messageInputFSK.setStyleSheet(u"QLineEdit {\n"
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
        self.messageInputFSK.setInputMethodHints(Qt.ImhNone)
        self.messageInputFSK.setMaxLength(16)
        self.messageInputFSK.setFrame(True)
        self.messageInputFSK.setEchoMode(QLineEdit.Normal)

        self.gridLayout_4.addWidget(self.messageInputFSK, 2, 0, 1, 1)

        self.label_top_info_13 = QLabel(self.frame_6)
        self.label_top_info_13.setObjectName(u"label_top_info_13")
        self.label_top_info_13.setMinimumSize(QSize(0, 25))
        self.label_top_info_13.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_13.setFont(font3)
        self.label_top_info_13.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_13.setAlignment(Qt.AlignCenter)
        self.label_top_info_13.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_top_info_13, 1, 0, 1, 1)

        self.modulateBtnFSK = QPushButton(self.frame_6)
        self.modulateBtnFSK.setObjectName(u"modulateBtnFSK")
        sizePolicy4.setHeightForWidth(self.modulateBtnFSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnFSK.setSizePolicy(sizePolicy4)
        self.modulateBtnFSK.setMinimumSize(QSize(150, 30))
        self.modulateBtnFSK.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnFSK.setFont(font6)
        self.modulateBtnFSK.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-fsk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnFSK.setIcon(icon4)

        self.gridLayout_4.addWidget(self.modulateBtnFSK, 6, 0, 1, 1)

        self.label_title_bar_top_3 = QLabel(self.frame_6)
        self.label_title_bar_top_3.setObjectName(u"label_title_bar_top_3")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_3.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_3.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_3.setMinimumSize(QSize(0, 25))
        self.label_title_bar_top_3.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_3.setFont(font5)
        self.label_title_bar_top_3.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_3.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_title_bar_top_3.setScaledContents(True)
        self.label_title_bar_top_3.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_3.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_title_bar_top_3, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
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
        self.label_top_info_6.setFont(font2)
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

        self.carrierFreq1InputFSK = QSpinBox(self.frame_7)
        self.carrierFreq1InputFSK.setObjectName(u"carrierFreq1InputFSK")
        self.carrierFreq1InputFSK.setFont(font4)
        self.carrierFreq1InputFSK.setStyleSheet(u"QSpinBox{\n"
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
        self.carrierFreq1InputFSK.setMinimum(1)
        self.carrierFreq1InputFSK.setMaximum(200)

        self.verticalLayout_18.addWidget(self.carrierFreq1InputFSK)

        self.sliderFSK1 = QSlider(self.frame_7)
        self.sliderFSK1.setObjectName(u"sliderFSK1")
        self.sliderFSK1.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.sliderFSK1.setMinimum(1)
        self.sliderFSK1.setMaximum(200)
        self.sliderFSK1.setTracking(False)
        self.sliderFSK1.setOrientation(Qt.Horizontal)
        self.sliderFSK1.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_18.addWidget(self.sliderFSK1)


        self.gridLayout_4.addWidget(self.frame_7, 3, 0, 1, 1)

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
        self.label_top_info_11.setFont(font2)
        self.label_top_info_11.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_top_info_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_top_info_12 = QLabel(self.frame_10)
        self.label_top_info_12.setObjectName(u"label_top_info_12")
        self.label_top_info_12.setMinimumSize(QSize(0, 20))
        self.label_top_info_12.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_12.setFont(font3)
        self.label_top_info_12.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_top_info_12)

        self.label_resultFSK = QLabel(self.frame_10)
        self.label_resultFSK.setObjectName(u"label_resultFSK")
        self.label_resultFSK.setMinimumSize(QSize(0, 20))
        self.label_resultFSK.setMaximumSize(QSize(16777215, 30))
        self.label_resultFSK.setFont(font3)
        self.label_resultFSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_resultFSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_resultFSK)


        self.verticalLayout_20.addWidget(self.frame_10)


        self.gridLayout_4.addWidget(self.frame_9, 5, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_13.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_fsk)
        self.page_psk = QWidget()
        self.page_psk.setObjectName(u"page_psk")
        self.horizontalLayout_16 = QHBoxLayout(self.page_psk)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_11 = QFrame(self.page_psk)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(180, 0))
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.messageInputPSK = QLineEdit(self.frame_11)
        self.messageInputPSK.setObjectName(u"messageInputPSK")
        sizePolicy5.setHeightForWidth(self.messageInputPSK.sizePolicy().hasHeightForWidth())
        self.messageInputPSK.setSizePolicy(sizePolicy5)
        self.messageInputPSK.setMinimumSize(QSize(0, 40))
        self.messageInputPSK.setFont(font7)
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
        self.label_top_info_8.setFont(font2)
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
        self.carrierFreqInputPSK.setFont(font4)
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
"	background: rgb(33, 46, 112);\n"
"}")
        self.sliderPSK.setMinimum(1)
        self.sliderPSK.setMaximum(200)
        self.sliderPSK.setTracking(False)
        self.sliderPSK.setOrientation(Qt.Horizontal)
        self.sliderPSK.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_22.addWidget(self.sliderPSK)


        self.gridLayout_5.addWidget(self.frame_12, 4, 0, 1, 1)

        self.label_title_bar_top_4 = QLabel(self.frame_11)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_4.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_4.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_4.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_4.setFont(font5)
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

        self.gridLayout_5.addWidget(self.label_title_bar_top_4, 0, 0, 1, 1)

        self.label_top_info_15 = QLabel(self.frame_11)
        self.label_top_info_15.setObjectName(u"label_top_info_15")
        self.label_top_info_15.setMinimumSize(QSize(0, 25))
        self.label_top_info_15.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_15.setFont(font3)
        self.label_top_info_15.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_top_info_15, 1, 0, 1, 1)

        self.modulateBtnPSK = QPushButton(self.frame_11)
        self.modulateBtnPSK.setObjectName(u"modulateBtnPSK")
        sizePolicy4.setHeightForWidth(self.modulateBtnPSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnPSK.setSizePolicy(sizePolicy4)
        self.modulateBtnPSK.setMinimumSize(QSize(150, 30))
        self.modulateBtnPSK.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnPSK.setFont(font6)
        self.modulateBtnPSK.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-psk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnPSK.setIcon(icon5)

        self.gridLayout_5.addWidget(self.modulateBtnPSK, 5, 0, 1, 1)

        self.clearBtnPSK = QPushButton(self.frame_11)
        self.clearBtnPSK.setObjectName(u"clearBtnPSK")
        sizePolicy4.setHeightForWidth(self.clearBtnPSK.sizePolicy().hasHeightForWidth())
        self.clearBtnPSK.setSizePolicy(sizePolicy4)
        self.clearBtnPSK.setMinimumSize(QSize(150, 30))
        self.clearBtnPSK.setMaximumSize(QSize(16777215, 50))
        self.clearBtnPSK.setFont(font6)
        self.clearBtnPSK.setStyleSheet(u"QPushButton {\n"
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
        self.clearBtnPSK.setIcon(icon2)

        self.gridLayout_5.addWidget(self.clearBtnPSK, 6, 0, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_5)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_psk)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_11 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_14 = QFrame(self.page_settings)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(180, 0))
        self.frame_14.setMaximumSize(QSize(300, 16777215))
        self.frame_14.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_title_bar_top_5 = QLabel(self.frame_14)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_5.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_5.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_5.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_5.setFont(font5)
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

        self.gridLayout_6.addWidget(self.label_title_bar_top_5, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 150))
        self.frame_16.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_top_info_16 = QLabel(self.frame_16)
        self.label_top_info_16.setObjectName(u"label_top_info_16")
        self.label_top_info_16.setMinimumSize(QSize(0, 25))
        self.label_top_info_16.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_16.setFont(font2)
        self.label_top_info_16.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_16)

        self.label_top_info_17 = QLabel(self.frame_16)
        self.label_top_info_17.setObjectName(u"label_top_info_17")
        self.label_top_info_17.setMinimumSize(QSize(0, 20))
        self.label_top_info_17.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_17.setFont(font3)
        self.label_top_info_17.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_17)

        self.maxCarrierASK = QSpinBox(self.frame_16)
        self.maxCarrierASK.setObjectName(u"maxCarrierASK")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.maxCarrierASK.sizePolicy().hasHeightForWidth())
        self.maxCarrierASK.setSizePolicy(sizePolicy7)
        self.maxCarrierASK.setMinimumSize(QSize(150, 25))
        self.maxCarrierASK.setFont(font4)
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
        self.maxCarrierASK.setMaximum(10000)
        self.maxCarrierASK.setValue(200)

        self.verticalLayout_23.addWidget(self.maxCarrierASK, 0, Qt.AlignHCenter)

        self.label_top_info_18 = QLabel(self.frame_16)
        self.label_top_info_18.setObjectName(u"label_top_info_18")
        self.label_top_info_18.setMinimumSize(QSize(0, 20))
        self.label_top_info_18.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_18.setFont(font3)
        self.label_top_info_18.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_18)

        self.minCarrierASK = QSpinBox(self.frame_16)
        self.minCarrierASK.setObjectName(u"minCarrierASK")
        sizePolicy7.setHeightForWidth(self.minCarrierASK.sizePolicy().hasHeightForWidth())
        self.minCarrierASK.setSizePolicy(sizePolicy7)
        self.minCarrierASK.setMinimumSize(QSize(150, 25))
        self.minCarrierASK.setFont(font4)
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


        self.gridLayout_6.addWidget(self.frame_16, 2, 0, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_6)


        self.horizontalLayout_11.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.page_settings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(180, 0))
        self.frame_18.setMaximumSize(QSize(300, 16777215))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy6.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy6)
        self.frame_21.setMaximumSize(QSize(16777215, 150))
        self.frame_21.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_21)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_top_info_22 = QLabel(self.frame_21)
        self.label_top_info_22.setObjectName(u"label_top_info_22")
        self.label_top_info_22.setMinimumSize(QSize(0, 25))
        self.label_top_info_22.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_22.setFont(font2)
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
        self.label_top_info_23.setMinimumSize(QSize(0, 20))
        self.label_top_info_23.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_23.setFont(font3)
        self.label_top_info_23.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_23)

        self.maxCarrierFSK1 = QSpinBox(self.frame_21)
        self.maxCarrierFSK1.setObjectName(u"maxCarrierFSK1")
        sizePolicy7.setHeightForWidth(self.maxCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK1.setSizePolicy(sizePolicy7)
        self.maxCarrierFSK1.setMinimumSize(QSize(150, 25))
        self.maxCarrierFSK1.setFont(font4)
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
        self.maxCarrierFSK1.setMaximum(10000)
        self.maxCarrierFSK1.setValue(200)

        self.verticalLayout_26.addWidget(self.maxCarrierFSK1, 0, Qt.AlignHCenter)

        self.label_top_info_21 = QLabel(self.frame_21)
        self.label_top_info_21.setObjectName(u"label_top_info_21")
        self.label_top_info_21.setMinimumSize(QSize(0, 20))
        self.label_top_info_21.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_21.setFont(font3)
        self.label_top_info_21.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_21)

        self.minCarrierFSK1 = QSpinBox(self.frame_21)
        self.minCarrierFSK1.setObjectName(u"minCarrierFSK1")
        sizePolicy7.setHeightForWidth(self.minCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK1.setSizePolicy(sizePolicy7)
        self.minCarrierFSK1.setMinimumSize(QSize(150, 25))
        self.minCarrierFSK1.setFont(font4)
        self.minCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
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
        self.minCarrierFSK1.setMinimum(1)
        self.minCarrierFSK1.setMaximum(1000)

        self.verticalLayout_26.addWidget(self.minCarrierFSK1, 0, Qt.AlignHCenter)


        self.gridLayout_7.addWidget(self.frame_21, 1, 0, 1, 1)

        self.label_title_bar_top_6 = QLabel(self.frame_18)
        self.label_title_bar_top_6.setObjectName(u"label_title_bar_top_6")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_6.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_6.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_6.setMinimumSize(QSize(0, 50))
        self.label_title_bar_top_6.setMaximumSize(QSize(16777215, 125))
        self.label_title_bar_top_6.setFont(font5)
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

        self.gridLayout_7.addWidget(self.label_title_bar_top_6, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy6.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy6)
        self.frame_23.setMaximumSize(QSize(16777215, 150))
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
        self.label_top_info_24.setFont(font2)
        self.label_top_info_24.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_24)

        self.label_top_info_25 = QLabel(self.frame_23)
        self.label_top_info_25.setObjectName(u"label_top_info_25")
        self.label_top_info_25.setMinimumSize(QSize(0, 20))
        self.label_top_info_25.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_25.setFont(font3)
        self.label_top_info_25.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_25)

        self.maxCarrierFSK2 = QSpinBox(self.frame_23)
        self.maxCarrierFSK2.setObjectName(u"maxCarrierFSK2")
        sizePolicy7.setHeightForWidth(self.maxCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK2.setSizePolicy(sizePolicy7)
        self.maxCarrierFSK2.setMinimumSize(QSize(150, 25))
        self.maxCarrierFSK2.setFont(font4)
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
        self.maxCarrierFSK2.setMaximum(10000)
        self.maxCarrierFSK2.setValue(200)

        self.verticalLayout_27.addWidget(self.maxCarrierFSK2, 0, Qt.AlignHCenter)

        self.label_top_info_28 = QLabel(self.frame_23)
        self.label_top_info_28.setObjectName(u"label_top_info_28")
        self.label_top_info_28.setMinimumSize(QSize(0, 20))
        self.label_top_info_28.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_28.setFont(font3)
        self.label_top_info_28.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_28)

        self.minCarrierFSK2 = QSpinBox(self.frame_23)
        self.minCarrierFSK2.setObjectName(u"minCarrierFSK2")
        sizePolicy7.setHeightForWidth(self.minCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK2.setSizePolicy(sizePolicy7)
        self.minCarrierFSK2.setMinimumSize(QSize(150, 25))
        self.minCarrierFSK2.setFont(font4)
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


        self.gridLayout_7.addWidget(self.frame_23, 2, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.horizontalLayout_11.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.page_settings)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(180, 0))
        self.frame_24.setMaximumSize(QSize(300, 16777215))
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_title_bar_top_7 = QLabel(self.frame_24)
        self.label_title_bar_top_7.setObjectName(u"label_title_bar_top_7")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_7.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_7.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_7.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_7.setFont(font5)
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

        self.gridLayout_8.addWidget(self.label_title_bar_top_7, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_24)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 150))
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
        self.label_top_info_19.setFont(font2)
        self.label_top_info_19.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"color: white;\n"
"}")
        self.label_top_info_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_19)

        self.label_top_info_20 = QLabel(self.frame_20)
        self.label_top_info_20.setObjectName(u"label_top_info_20")
        self.label_top_info_20.setMinimumSize(QSize(0, 20))
        self.label_top_info_20.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_20.setFont(font3)
        self.label_top_info_20.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_20)

        self.maxCarrierPSK = QSpinBox(self.frame_20)
        self.maxCarrierPSK.setObjectName(u"maxCarrierPSK")
        sizePolicy7.setHeightForWidth(self.maxCarrierPSK.sizePolicy().hasHeightForWidth())
        self.maxCarrierPSK.setSizePolicy(sizePolicy7)
        self.maxCarrierPSK.setMinimumSize(QSize(150, 25))
        self.maxCarrierPSK.setFont(font4)
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
        self.maxCarrierPSK.setMaximum(10000)
        self.maxCarrierPSK.setValue(200)

        self.verticalLayout_25.addWidget(self.maxCarrierPSK, 0, Qt.AlignHCenter)

        self.label_top_info_29 = QLabel(self.frame_20)
        self.label_top_info_29.setObjectName(u"label_top_info_29")
        self.label_top_info_29.setMinimumSize(QSize(0, 20))
        self.label_top_info_29.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_29.setFont(font3)
        self.label_top_info_29.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_29)

        self.minCarrierPSK = QSpinBox(self.frame_20)
        self.minCarrierPSK.setObjectName(u"minCarrierPSK")
        sizePolicy7.setHeightForWidth(self.minCarrierPSK.sizePolicy().hasHeightForWidth())
        self.minCarrierPSK.setSizePolicy(sizePolicy7)
        self.minCarrierPSK.setMinimumSize(QSize(150, 25))
        self.minCarrierPSK.setFont(font4)
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


        self.gridLayout_8.addWidget(self.frame_20, 1, 0, 1, 1)


        self.verticalLayout_28.addLayout(self.gridLayout_8)


        self.horizontalLayout_11.addWidget(self.frame_24, 0, Qt.AlignTop)

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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(helpWindow)
    # setupUi

    def retranslateUi(self, helpWindow):
        helpWindow.setWindowTitle(QCoreApplication.translate("helpWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("helpWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("helpWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("helpWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_4.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_5.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_2.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Amplitud", None))
        self.clearBtnASK.setText(QCoreApplication.translate("helpWindow", u"Limpiar", None))
        self.label_top_info_3.setText(QCoreApplication.translate("helpWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
#if QT_CONFIG(tooltip)
        self.messageInputASK.setToolTip(QCoreApplication.translate("helpWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputASK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputASK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputASK.setPlaceholderText(QCoreApplication.translate("helpWindow", u"Ingrese cadena de bits", None))
        self.modulateBtnASK.setText(QCoreApplication.translate("helpWindow", u"Modular", None))
        self.label_top_info_9.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 2", None))
        self.label_top_info_10.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq2InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.clearBtnFSK.setText(QCoreApplication.translate("helpWindow", u"Limpiar", None))
#if QT_CONFIG(tooltip)
        self.messageInputFSK.setToolTip(QCoreApplication.translate("helpWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputFSK.setPlaceholderText(QCoreApplication.translate("helpWindow", u"Ingrese cadena de bits", None))
        self.label_top_info_13.setText(QCoreApplication.translate("helpWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
        self.modulateBtnFSK.setText(QCoreApplication.translate("helpWindow", u"Modular", None))
        self.label_title_bar_top_3.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Frecuencias", None))
        self.label_top_info_6.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 1", None))
        self.label_top_info_7.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq1InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_11.setText(QCoreApplication.translate("helpWindow", u"Resultante", None))
        self.label_top_info_12.setText(QCoreApplication.translate("helpWindow", u"AB =", None))
        self.label_resultFSK.setText("")
#if QT_CONFIG(tooltip)
        self.messageInputPSK.setToolTip(QCoreApplication.translate("helpWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputPSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputPSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputPSK.setPlaceholderText(QCoreApplication.translate("helpWindow", u"Ingrese cadena de bits", None))
        self.label_top_info_8.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_14.setText(QCoreApplication.translate("helpWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_4.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Fase", None))
        self.label_top_info_15.setText(QCoreApplication.translate("helpWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
        self.modulateBtnPSK.setText(QCoreApplication.translate("helpWindow", u"Modular", None))
        self.clearBtnPSK.setText(QCoreApplication.translate("helpWindow", u"Limpiar", None))
        self.label_title_bar_top_5.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Amplitud\n"
"ASK", None))
        self.label_top_info_16.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_17.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00e1xima (Hz) | 1-10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_18.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00ednima (Hz) | 1-1000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_22.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 1", None))
        self.label_top_info_23.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00e1xima (Hz) | 1-10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_21.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00ednima (Hz)| 1-1000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_6.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Frecuencias\n"
"FSK", None))
        self.label_top_info_24.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al 2", None))
        self.label_top_info_25.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00e1xima (Hz) | 1-10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_28.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00ednima (Hz) | 1-1000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_7.setText(QCoreApplication.translate("helpWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Fase\n"
"PSK", None))
        self.label_top_info_19.setText(QCoreApplication.translate("helpWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_20.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00e1xima (Hz) | 1-10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_29.setText(QCoreApplication.translate("helpWindow", u"Frecuencia M\u00ednima (Hz) | 1-1000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

