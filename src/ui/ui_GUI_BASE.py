# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget
from mplwidgetfsk import MplWidgetFSK
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
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
        font.setFamilies([u"Satoshi Black"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
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
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
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
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

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
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

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
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

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
        self.label_top_info_1.setStyleSheet(u"color: rgb(118, 125, 134)")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
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
        font2.setFamilies([u"Segoe UI"])
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
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(40)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(15)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
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
        self.messageInputASK = QLineEdit(self.frame_4)
        self.messageInputASK.setObjectName(u"messageInputASK")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.messageInputASK.sizePolicy().hasHeightForWidth())
        self.messageInputASK.setSizePolicy(sizePolicy5)
        self.messageInputASK.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setFamilies([u"Satoshi Black"])
        font6.setPointSize(10)
        self.messageInputASK.setFont(font6)
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
"}\n"
"\n"
"QLineEdit::Text {\n"
"width: parent.width\n"
"height: parent.height\n"
"font.pointSize: 100\n"
"minimumPointSize: 10\n"
"fontSizeMode: Text.Fit\n"
"}")
        self.messageInputASK.setInputMethodHints(Qt.ImhNone)
        self.messageInputASK.setMaxLength(16)
        self.messageInputASK.setFrame(True)
        self.messageInputASK.setEchoMode(QLineEdit.Normal)

        self.gridLayout_3.addWidget(self.messageInputASK, 3, 0, 1, 1)

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
        font7 = QFont()
        font7.setFamilies([u"Satoshi Black"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_top_info_4.setFont(font7)
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
        font8 = QFont()
        font8.setFamilies([u"Satoshi"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_top_info_5.setFont(font8)
        self.label_top_info_5.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_top_info_5)

        self.carrierFreqInputASK = QSpinBox(self.frame_5)
        self.carrierFreqInputASK.setObjectName(u"carrierFreqInputASK")
        font9 = QFont()
        font9.setFamilies([u"Satoshi"])
        font9.setPointSize(10)
        font9.setBold(True)
        self.carrierFreqInputASK.setFont(font9)
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

        self.verticalLayout_14.addWidget(self.carrierFreqInputASK)

        self.horizontalSlider_2 = QSlider(self.frame_5)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(200)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_14.addWidget(self.horizontalSlider_2)


        self.gridLayout_3.addWidget(self.frame_5, 4, 0, 1, 1)

        self.label_title_bar_top_2 = QLabel(self.frame_4)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_2.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_2.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_2.setMaximumSize(QSize(16777215, 100))
        font10 = QFont()
        font10.setFamilies([u"Satoshi Black"])
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setUnderline(False)
        font10.setStrikeOut(False)
        font10.setKerning(True)
        self.label_title_bar_top_2.setFont(font10)
        self.label_title_bar_top_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_2.setScaledContents(True)
        self.label_title_bar_top_2.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_2.setWordWrap(False)

        self.gridLayout_3.addWidget(self.label_title_bar_top_2, 0, 0, 1, 1)

        self.label_top_info_3 = QLabel(self.frame_4)
        self.label_top_info_3.setObjectName(u"label_top_info_3")
        self.label_top_info_3.setMinimumSize(QSize(0, 25))
        self.label_top_info_3.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_3.setFont(font8)
        self.label_top_info_3.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_top_info_3, 1, 0, 1, 1)

        self.modulateBtnASK = QPushButton(self.frame_4)
        self.modulateBtnASK.setObjectName(u"modulateBtnASK")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.modulateBtnASK.sizePolicy().hasHeightForWidth())
        self.modulateBtnASK.setSizePolicy(sizePolicy6)
        self.modulateBtnASK.setMinimumSize(QSize(150, 30))
        self.modulateBtnASK.setMaximumSize(QSize(16777215, 50))
        font11 = QFont()
        font11.setFamilies([u"Satoshi Black"])
        font11.setPointSize(14)
        font11.setBold(True)
        self.modulateBtnASK.setFont(font11)
        self.modulateBtnASK.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-ask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modulateBtnASK.setIcon(icon3)

        self.gridLayout_3.addWidget(self.modulateBtnASK, 5, 0, 1, 1)

        self.clearBtnASK = QPushButton(self.frame_4)
        self.clearBtnASK.setObjectName(u"clearBtnASK")
        sizePolicy6.setHeightForWidth(self.clearBtnASK.sizePolicy().hasHeightForWidth())
        self.clearBtnASK.setSizePolicy(sizePolicy6)
        self.clearBtnASK.setMinimumSize(QSize(150, 30))
        self.clearBtnASK.setMaximumSize(QSize(16777215, 50))
        self.clearBtnASK.setFont(font11)
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
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtnASK.setIcon(icon4)

        self.gridLayout_3.addWidget(self.clearBtnASK, 6, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_3)


        self.horizontalLayout_14.addWidget(self.frame_4)

        self.ASK_graph_layout = QFrame(self.page_ask)
        self.ASK_graph_layout.setObjectName(u"ASK_graph_layout")
        sizePolicy3.setHeightForWidth(self.ASK_graph_layout.sizePolicy().hasHeightForWidth())
        self.ASK_graph_layout.setSizePolicy(sizePolicy3)
        self.ASK_graph_layout.setMinimumSize(QSize(700, 585))
        self.ASK_graph_layout.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.ASK_graph_layout)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetASK = MplWidget(self.ASK_graph_layout)
        self.MplWidgetASK.setObjectName(u"MplWidgetASK")
        sizePolicy3.setHeightForWidth(self.MplWidgetASK.sizePolicy().hasHeightForWidth())
        self.MplWidgetASK.setSizePolicy(sizePolicy3)
        self.MplWidgetASK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.verticalLayout_13.addWidget(self.MplWidgetASK)


        self.horizontalLayout_14.addWidget(self.ASK_graph_layout)

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
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy7)
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
        self.label_top_info_9.setFont(font7)
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
        self.carrierFreq2InputFSK.setFont(font9)
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

        self.verticalLayout_19.addWidget(self.carrierFreq2InputFSK)

        self.horizontalSlider_4 = QSlider(self.frame_8)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(200)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_19.addWidget(self.horizontalSlider_4)


        self.gridLayout_4.addWidget(self.frame_8, 4, 0, 1, 1)

        self.clearBtnFSK = QPushButton(self.frame_6)
        self.clearBtnFSK.setObjectName(u"clearBtnFSK")
        sizePolicy6.setHeightForWidth(self.clearBtnFSK.sizePolicy().hasHeightForWidth())
        self.clearBtnFSK.setSizePolicy(sizePolicy6)
        self.clearBtnFSK.setMinimumSize(QSize(150, 30))
        self.clearBtnFSK.setMaximumSize(QSize(16777215, 50))
        self.clearBtnFSK.setFont(font11)
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
        self.clearBtnFSK.setIcon(icon4)

        self.gridLayout_4.addWidget(self.clearBtnFSK, 7, 0, 1, 1)

        self.messageInputFSK = QLineEdit(self.frame_6)
        self.messageInputFSK.setObjectName(u"messageInputFSK")
        sizePolicy5.setHeightForWidth(self.messageInputFSK.sizePolicy().hasHeightForWidth())
        self.messageInputFSK.setSizePolicy(sizePolicy5)
        self.messageInputFSK.setMinimumSize(QSize(0, 40))
        self.messageInputFSK.setFont(font6)
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
        self.label_top_info_13.setFont(font8)
        self.label_top_info_13.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_13.setAlignment(Qt.AlignCenter)
        self.label_top_info_13.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_top_info_13, 1, 0, 1, 1)

        self.modulateBtnFSK = QPushButton(self.frame_6)
        self.modulateBtnFSK.setObjectName(u"modulateBtnFSK")
        sizePolicy6.setHeightForWidth(self.modulateBtnFSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnFSK.setSizePolicy(sizePolicy6)
        self.modulateBtnFSK.setMinimumSize(QSize(150, 30))
        self.modulateBtnFSK.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnFSK.setFont(font11)
        self.modulateBtnFSK.setStyleSheet(u"QPushButton {\n"
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
        self.modulateBtnFSK.setIcon(icon3)

        self.gridLayout_4.addWidget(self.modulateBtnFSK, 6, 0, 1, 1)

        self.label_title_bar_top_3 = QLabel(self.frame_6)
        self.label_title_bar_top_3.setObjectName(u"label_title_bar_top_3")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_3.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_3.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_3.setMinimumSize(QSize(0, 25))
        self.label_title_bar_top_3.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_3.setFont(font10)
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
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
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
        self.label_top_info_6.setFont(font7)
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
        self.carrierFreq1InputFSK.setFont(font9)
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

        self.verticalLayout_18.addWidget(self.carrierFreq1InputFSK)

        self.horizontalSlider_3 = QSlider(self.frame_7)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(200)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_18.addWidget(self.horizontalSlider_3)


        self.gridLayout_4.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy7.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy7)
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
        self.label_top_info_11.setFont(font7)
        self.label_top_info_11.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
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
        self.label_top_info_12.setFont(font8)
        self.label_top_info_12.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_top_info_12)

        self.label_resultFSK = QLabel(self.frame_10)
        self.label_resultFSK.setObjectName(u"label_resultFSK")
        self.label_resultFSK.setMinimumSize(QSize(0, 20))
        self.label_resultFSK.setMaximumSize(QSize(16777215, 30))
        self.label_resultFSK.setFont(font8)
        self.label_resultFSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_resultFSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_resultFSK)


        self.verticalLayout_20.addWidget(self.frame_10)


        self.gridLayout_4.addWidget(self.frame_9, 5, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_13.addWidget(self.frame_6)

        self.FSK_graph_layout = QFrame(self.page_fsk)
        self.FSK_graph_layout.setObjectName(u"FSK_graph_layout")
        sizePolicy3.setHeightForWidth(self.FSK_graph_layout.sizePolicy().hasHeightForWidth())
        self.FSK_graph_layout.setSizePolicy(sizePolicy3)
        self.FSK_graph_layout.setMinimumSize(QSize(700, 585))
        self.FSK_graph_layout.setStyleSheet(u"")
        self.graph_layout_4 = QVBoxLayout(self.FSK_graph_layout)
        self.graph_layout_4.setSpacing(0)
        self.graph_layout_4.setObjectName(u"graph_layout_4")
        self.graph_layout_4.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetFSK = MplWidgetFSK(self.FSK_graph_layout)
        self.MplWidgetFSK.setObjectName(u"MplWidgetFSK")
        sizePolicy3.setHeightForWidth(self.MplWidgetFSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetFSK.setSizePolicy(sizePolicy3)
        self.MplWidgetFSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_4.addWidget(self.MplWidgetFSK)


        self.horizontalLayout_13.addWidget(self.FSK_graph_layout)

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
        self.messageInputPSK.setFont(font6)
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
        self.label_top_info_8.setFont(font7)
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
        self.carrierFreqInputPSK.setFont(font9)
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

        self.horizontalSlider_5 = QSlider(self.frame_12)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setStyleSheet(u"QSlider::handle:horizontal{\n"
"	background: rgb(33, 46, 112);\n"
"}")
        self.horizontalSlider_5.setMinimum(1)
        self.horizontalSlider_5.setMaximum(200)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_22.addWidget(self.horizontalSlider_5)


        self.gridLayout_5.addWidget(self.frame_12, 4, 0, 1, 1)

        self.label_title_bar_top_4 = QLabel(self.frame_11)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_4.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_4.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_4.setMaximumSize(QSize(16777215, 100))
        self.label_title_bar_top_4.setFont(font10)
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

        self.label_top_info_15 = QLabel(self.frame_11)
        self.label_top_info_15.setObjectName(u"label_top_info_15")
        self.label_top_info_15.setMinimumSize(QSize(0, 25))
        self.label_top_info_15.setMaximumSize(QSize(16777215, 80))
        self.label_top_info_15.setFont(font8)
        self.label_top_info_15.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_top_info_15, 1, 0, 1, 1)

        self.modulateBtnPSK = QPushButton(self.frame_11)
        self.modulateBtnPSK.setObjectName(u"modulateBtnPSK")
        sizePolicy6.setHeightForWidth(self.modulateBtnPSK.sizePolicy().hasHeightForWidth())
        self.modulateBtnPSK.setSizePolicy(sizePolicy6)
        self.modulateBtnPSK.setMinimumSize(QSize(150, 30))
        self.modulateBtnPSK.setMaximumSize(QSize(16777215, 50))
        self.modulateBtnPSK.setFont(font11)
        self.modulateBtnPSK.setStyleSheet(u"QPushButton {\n"
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
        self.modulateBtnPSK.setIcon(icon3)

        self.gridLayout_5.addWidget(self.modulateBtnPSK, 5, 0, 1, 1)

        self.clearBtnPSK = QPushButton(self.frame_11)
        self.clearBtnPSK.setObjectName(u"clearBtnPSK")
        sizePolicy6.setHeightForWidth(self.clearBtnPSK.sizePolicy().hasHeightForWidth())
        self.clearBtnPSK.setSizePolicy(sizePolicy6)
        self.clearBtnPSK.setMinimumSize(QSize(150, 30))
        self.clearBtnPSK.setMaximumSize(QSize(16777215, 50))
        self.clearBtnPSK.setFont(font11)
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
        self.clearBtnPSK.setIcon(icon4)

        self.gridLayout_5.addWidget(self.clearBtnPSK, 6, 0, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_5)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.PSK_graph_layout = QFrame(self.page_psk)
        self.PSK_graph_layout.setObjectName(u"PSK_graph_layout")
        self.PSK_graph_layout.setMinimumSize(QSize(700, 585))
        self.PSK_graph_layout.setStyleSheet(u"")
        self.graph_layout_5 = QVBoxLayout(self.PSK_graph_layout)
        self.graph_layout_5.setSpacing(0)
        self.graph_layout_5.setObjectName(u"graph_layout_5")
        self.graph_layout_5.setContentsMargins(0, 0, 0, 0)
        self.MplWidgetPSK = MplWidget(self.PSK_graph_layout)
        self.MplWidgetPSK.setObjectName(u"MplWidgetPSK")
        sizePolicy3.setHeightForWidth(self.MplWidgetPSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetPSK.setSizePolicy(sizePolicy3)
        self.MplWidgetPSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_5.addWidget(self.MplWidgetPSK)


        self.horizontalLayout_16.addWidget(self.PSK_graph_layout)

        self.stackedWidget.addWidget(self.page_psk)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(10)
        font12.setBold(True)
        self.labelBoxBlenderInstalation.setFont(font12)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(9)
        self.pushButton.setFont(font13)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font13)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon6)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
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
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font14);
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
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
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

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

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
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
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
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_2.sliderMoved.connect(self.carrierFreqInputASK.setValue)
        self.carrierFreqInputASK.valueChanged.connect(self.horizontalSlider_2.setValue)
        self.carrierFreq1InputFSK.valueChanged.connect(self.horizontalSlider_3.setValue)
        self.horizontalSlider_3.valueChanged.connect(self.carrierFreq1InputFSK.setValue)
        self.carrierFreq2InputFSK.valueChanged.connect(self.horizontalSlider_4.setValue)
        self.horizontalSlider_4.valueChanged.connect(self.carrierFreq2InputFSK.setValue)
        self.carrierFreqInputPSK.valueChanged.connect(self.horizontalSlider_5.setValue)
        self.horizontalSlider_5.valueChanged.connect(self.carrierFreqInputPSK.setValue)

        self.stackedWidget.setCurrentIndex(3)


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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Empyt Page - By: Wanderson M. Pimenta", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
#if QT_CONFIG(tooltip)
        self.messageInputASK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputASK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputASK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputASK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese cadena de bits", None))
        self.label_top_info_4.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_5.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_2.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Amplitud", None))
        self.label_top_info_3.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
        self.modulateBtnASK.setText(QCoreApplication.translate("MainWindow", u"Modular", None))
        self.clearBtnASK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_top_info_9.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 2", None))
        self.label_top_info_10.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq2InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.clearBtnFSK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
#if QT_CONFIG(tooltip)
        self.messageInputFSK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputFSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputFSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputFSK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese cadena de bits", None))
        self.label_top_info_13.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
        self.modulateBtnFSK.setText(QCoreApplication.translate("MainWindow", u"Modular", None))
        self.label_title_bar_top_3.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Frecuencias", None))
        self.label_top_info_6.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 1", None))
        self.label_top_info_7.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreq1InputFSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_11.setText(QCoreApplication.translate("MainWindow", u"Resultante", None))
        self.label_top_info_12.setText(QCoreApplication.translate("MainWindow", u"f1 + f2 =", None))
        self.label_resultFSK.setText("")
#if QT_CONFIG(tooltip)
        self.messageInputPSK.setToolTip(QCoreApplication.translate("MainWindow", u"Ingrese cadenas de 2, 4, 8 o 16 bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.messageInputPSK.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.messageInputPSK.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.messageInputPSK.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese cadena de bits", None))
        self.label_top_info_8.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_14.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz)", None))
#if QT_CONFIG(tooltip)
        self.carrierFreqInputPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title_bar_top_4.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n\n"
"de Fase", None))
        self.label_top_info_15.setText(QCoreApplication.translate("MainWindow", u"Ingrese una cadena\n"
"cadena de bits de\n"
"2 / 4 / 8 / 16 bits", None))
        self.modulateBtnPSK.setText(QCoreApplication.translate("MainWindow", u"Modular", None))
        self.clearBtnPSK.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
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

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Desarrollado por: Lucas Depetris", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

