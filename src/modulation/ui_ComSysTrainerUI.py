# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ComSysTrainerUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget
from mplwidgetfsk import MplWidgetFSK

class Ui_ComSys(object):
    def setupUi(self, ComSys):
        if not ComSys.objectName():
            ComSys.setObjectName(u"ComSys")
        ComSys.setWindowModality(Qt.NonModal)
        ComSys.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComSys.sizePolicy().hasHeightForWidth())
        ComSys.setSizePolicy(sizePolicy)
        ComSys.setMinimumSize(QSize(1000, 600))
        ComSys.setMaximumSize(QSize(1000, 800))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        ComSys.setFont(font)
        icon = QIcon()
        icon.addFile(u"D:/Users/Lucas/Documents/Dise\u00f1o/Trabajos/Personal/Logos/1x/Recurso 1.png", QSize(), QIcon.Normal, QIcon.Off)
        ComSys.setWindowIcon(icon)
        ComSys.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(ComSys)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(800, 0))
        self.tabWidget.setMaximumSize(QSize(1000, 550))
        font1 = QFont()
        font1.setFamilies([u"Product Sans"])
        font1.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        font2 = QFont()
        font2.setFamilies([u"Product Sans"])
        font2.setBold(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.tab_1.setFont(font2)
        self.tab_1.setFocusPolicy(Qt.ClickFocus)
        self.tab_1.setToolTipDuration(1)
        self.AM_graph_layout = QFrame(self.tab_1)
        self.AM_graph_layout.setObjectName(u"AM_graph_layout")
        self.AM_graph_layout.setGeometry(QRect(240, 0, 741, 510))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AM_graph_layout.sizePolicy().hasHeightForWidth())
        self.AM_graph_layout.setSizePolicy(sizePolicy1)
        self.AM_graph_layout.setMaximumSize(QSize(880, 510))
        self.AM_graph_layout.setStyleSheet(u"")
        self.graph_layout = QVBoxLayout(self.AM_graph_layout)
        self.graph_layout.setObjectName(u"graph_layout")
        self.MplWidgetAM = MplWidget(self.AM_graph_layout)
        self.MplWidgetAM.setObjectName(u"MplWidgetAM")
        sizePolicy.setHeightForWidth(self.MplWidgetAM.sizePolicy().hasHeightForWidth())
        self.MplWidgetAM.setSizePolicy(sizePolicy)
        self.MplWidgetAM.setMaximumSize(QSize(800, 490))
        self.MplWidgetAM.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout.addWidget(self.MplWidgetAM)

        self.dataInpBox = QFrame(self.tab_1)
        self.dataInpBox.setObjectName(u"dataInpBox")
        self.dataInpBox.setGeometry(QRect(0, 60, 241, 221))
        self.verticalLayout_2 = QVBoxLayout(self.dataInpBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame_3 = QFrame(self.dataInpBox)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.horizontalFrame_3)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamilies([u"Product Sans"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label_7.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.msgFreqInput = QSpinBox(self.horizontalFrame_3)
        self.msgFreqInput.setObjectName(u"msgFreqInput")
        self.msgFreqInput.setMinimum(10)
        self.msgFreqInput.setMaximum(100)
        self.msgFreqInput.setValue(10)

        self.horizontalLayout_5.addWidget(self.msgFreqInput)


        self.verticalLayout_2.addWidget(self.horizontalFrame_3)

        self.horizontalFrame_2 = QFrame(self.dataInpBox)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 1, 9, 1)
        self.label_6 = QLabel(self.horizontalFrame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setIndent(-1)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.msgAmpInput = QDoubleSpinBox(self.horizontalFrame_2)
        self.msgAmpInput.setObjectName(u"msgAmpInput")
        self.msgAmpInput.setMinimum(1.000000000000000)
        self.msgAmpInput.setMaximum(3.000000000000000)
        self.msgAmpInput.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.msgAmpInput)


        self.verticalLayout_2.addWidget(self.horizontalFrame_2)

        self.horizontalFrame = QFrame(self.dataInpBox)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.horizontalFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.carrierFreqInput = QSpinBox(self.horizontalFrame)
        self.carrierFreqInput.setObjectName(u"carrierFreqInput")
        self.carrierFreqInput.setMinimum(200)
        self.carrierFreqInput.setMaximum(800)
        self.carrierFreqInput.setValue(200)

        self.horizontalLayout_3.addWidget(self.carrierFreqInput)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.horizontalFrame1 = QFrame(self.dataInpBox)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        sizePolicy.setHeightForWidth(self.horizontalFrame1.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1.setSizePolicy(sizePolicy)
        self.horizontalFrame1.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.horizontalFrame1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.carrierAmpInput = QDoubleSpinBox(self.horizontalFrame1)
        self.carrierAmpInput.setObjectName(u"carrierAmpInput")
        self.carrierAmpInput.setMinimum(2.000000000000000)
        self.carrierAmpInput.setMaximum(7.000000000000000)
        self.carrierAmpInput.setValue(2.000000000000000)

        self.horizontalLayout_2.addWidget(self.carrierAmpInput)


        self.verticalLayout_2.addWidget(self.horizontalFrame1)

        self.modulateBtnAM = QPushButton(self.tab_1)
        self.modulateBtnAM.setObjectName(u"modulateBtnAM")
        self.modulateBtnAM.setGeometry(QRect(50, 300, 150, 50))
        font4 = QFont()
        font4.setFamilies([u"Product Sans"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setKerning(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.modulateBtnAM.setFont(font4)
        self.modulateBtnAM.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnAM.setAcceptDrops(False)
        self.modulateBtnAM.setAutoFillBackground(False)
        self.modulateBtnAM.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnAM.setIconSize(QSize(16, 16))
        self.modulateBtnAM.setAutoDefault(False)
        self.modulateBtnAM.setFlat(False)
        self.clearBtnAM = QPushButton(self.tab_1)
        self.clearBtnAM.setObjectName(u"clearBtnAM")
        self.clearBtnAM.setGeometry(QRect(50, 360, 150, 50))
        self.clearBtnAM.setFont(font4)
        self.clearBtnAM.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnAM.setAcceptDrops(False)
        self.clearBtnAM.setAutoFillBackground(False)
        self.clearBtnAM.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnAM.setIconSize(QSize(16, 16))
        self.clearBtnAM.setAutoDefault(False)
        self.clearBtnAM.setFlat(False)
        self.label_8 = QLabel(self.tab_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(16, 20, 221, 31))
        font5 = QFont()
        font5.setFamilies([u"Product Sans"])
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(16, 20, 171, 31))
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.modulateBtnFM = QPushButton(self.tab_2)
        self.modulateBtnFM.setObjectName(u"modulateBtnFM")
        self.modulateBtnFM.setGeometry(QRect(25, 300, 150, 50))
        self.modulateBtnFM.setFont(font4)
        self.modulateBtnFM.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnFM.setAcceptDrops(False)
        self.modulateBtnFM.setAutoFillBackground(False)
        self.modulateBtnFM.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnFM.setIconSize(QSize(16, 16))
        self.modulateBtnFM.setAutoDefault(False)
        self.modulateBtnFM.setFlat(False)
        self.clearBtnFM = QPushButton(self.tab_2)
        self.clearBtnFM.setObjectName(u"clearBtnFM")
        self.clearBtnFM.setGeometry(QRect(25, 390, 150, 50))
        self.clearBtnFM.setFont(font4)
        self.clearBtnFM.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnFM.setAcceptDrops(False)
        self.clearBtnFM.setAutoFillBackground(False)
        self.clearBtnFM.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnFM.setIconSize(QSize(16, 16))
        self.clearBtnFM.setAutoDefault(False)
        self.clearBtnFM.setFlat(False)
        self.FM_graph_layout = QFrame(self.tab_2)
        self.FM_graph_layout.setObjectName(u"FM_graph_layout")
        self.FM_graph_layout.setGeometry(QRect(195, 0, 680, 510))
        sizePolicy1.setHeightForWidth(self.FM_graph_layout.sizePolicy().hasHeightForWidth())
        self.FM_graph_layout.setSizePolicy(sizePolicy1)
        self.FM_graph_layout.setMaximumSize(QSize(880, 510))
        self.FM_graph_layout.setStyleSheet(u"")
        self.graph_layout_2 = QVBoxLayout(self.FM_graph_layout)
        self.graph_layout_2.setObjectName(u"graph_layout_2")
        self.MplWidgetFM = MplWidget(self.FM_graph_layout)
        self.MplWidgetFM.setObjectName(u"MplWidgetFM")
        sizePolicy.setHeightForWidth(self.MplWidgetFM.sizePolicy().hasHeightForWidth())
        self.MplWidgetFM.setSizePolicy(sizePolicy)
        self.MplWidgetFM.setMaximumSize(QSize(880, 490))
        self.MplWidgetFM.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_2.addWidget(self.MplWidgetFM)

        self.dataInpBox_2 = QFrame(self.tab_2)
        self.dataInpBox_2.setObjectName(u"dataInpBox_2")
        self.dataInpBox_2.setGeometry(QRect(0, 60, 191, 221))
        self.verticalLayout_3 = QVBoxLayout(self.dataInpBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalFrame_4 = QFrame(self.dataInpBox_2)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.horizontalFrame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.msgFreqInputFM = QSpinBox(self.horizontalFrame_4)
        self.msgFreqInputFM.setObjectName(u"msgFreqInputFM")
        self.msgFreqInputFM.setFont(font2)
        self.msgFreqInputFM.setMinimum(10)
        self.msgFreqInputFM.setMaximum(50)
        self.msgFreqInputFM.setValue(10)

        self.horizontalLayout_6.addWidget(self.msgFreqInputFM)


        self.verticalLayout_3.addWidget(self.horizontalFrame_4)

        self.horizontalFrame_6 = QFrame(self.dataInpBox_2)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalFrame_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.horizontalFrame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.carrierFreqInputFM = QSpinBox(self.horizontalFrame_6)
        self.carrierFreqInputFM.setObjectName(u"carrierFreqInputFM")
        self.carrierFreqInputFM.setFont(font2)
        self.carrierFreqInputFM.setMinimum(100)
        self.carrierFreqInputFM.setMaximum(500)
        self.carrierFreqInputFM.setValue(200)

        self.horizontalLayout_8.addWidget(self.carrierFreqInputFM)


        self.verticalLayout_3.addWidget(self.horizontalFrame_6)

        self.horizontalFrame_7 = QFrame(self.dataInpBox_2)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        sizePolicy.setHeightForWidth(self.horizontalFrame_7.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_7.setSizePolicy(sizePolicy)
        self.horizontalFrame_7.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.horizontalFrame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.modIndexInputFM = QDoubleSpinBox(self.horizontalFrame_7)
        self.modIndexInputFM.setObjectName(u"modIndexInputFM")
        self.modIndexInputFM.setFont(font2)
        self.modIndexInputFM.setMinimum(1.000000000000000)
        self.modIndexInputFM.setMaximum(10.000000000000000)
        self.modIndexInputFM.setValue(2.000000000000000)

        self.horizontalLayout_9.addWidget(self.modIndexInputFM)


        self.verticalLayout_3.addWidget(self.horizontalFrame_7)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.ASK_graph_layout = QFrame(self.tab_3)
        self.ASK_graph_layout.setObjectName(u"ASK_graph_layout")
        self.ASK_graph_layout.setGeometry(QRect(220, 0, 761, 510))
        sizePolicy1.setHeightForWidth(self.ASK_graph_layout.sizePolicy().hasHeightForWidth())
        self.ASK_graph_layout.setSizePolicy(sizePolicy1)
        self.ASK_graph_layout.setMaximumSize(QSize(900, 510))
        self.ASK_graph_layout.setStyleSheet(u"")
        self.graph_layout_3 = QVBoxLayout(self.ASK_graph_layout)
        self.graph_layout_3.setObjectName(u"graph_layout_3")
        self.MplWidgetASK = MplWidget(self.ASK_graph_layout)
        self.MplWidgetASK.setObjectName(u"MplWidgetASK")
        sizePolicy.setHeightForWidth(self.MplWidgetASK.sizePolicy().hasHeightForWidth())
        self.MplWidgetASK.setSizePolicy(sizePolicy)
        self.MplWidgetASK.setMaximumSize(QSize(880, 490))
        self.MplWidgetASK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_3.addWidget(self.MplWidgetASK)

        self.modulateBtnASK = QPushButton(self.tab_3)
        self.modulateBtnASK.setObjectName(u"modulateBtnASK")
        self.modulateBtnASK.setGeometry(QRect(30, 290, 150, 50))
        self.modulateBtnASK.setFont(font4)
        self.modulateBtnASK.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnASK.setAcceptDrops(False)
        self.modulateBtnASK.setAutoFillBackground(False)
        self.modulateBtnASK.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnASK.setIconSize(QSize(16, 16))
        self.modulateBtnASK.setAutoDefault(False)
        self.modulateBtnASK.setFlat(False)
        self.dataInpBox_3 = QFrame(self.tab_3)
        self.dataInpBox_3.setObjectName(u"dataInpBox_3")
        self.dataInpBox_3.setGeometry(QRect(0, 90, 231, 161))
        self.verticalLayout_4 = QVBoxLayout(self.dataInpBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalFrame_5 = QFrame(self.dataInpBox_3)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_5 = QVBoxLayout(self.horizontalFrame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.horizontalFrame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)

        self.messageInputASK = QTextEdit(self.horizontalFrame_5)
        self.messageInputASK.setObjectName(u"messageInputASK")
        sizePolicy.setHeightForWidth(self.messageInputASK.sizePolicy().hasHeightForWidth())
        self.messageInputASK.setSizePolicy(sizePolicy)
        self.messageInputASK.setMaximumSize(QSize(16777215, 25))
        self.messageInputASK.setFont(font2)
        self.messageInputASK.setStyleSheet(u"")
        self.messageInputASK.setInputMethodHints(Qt.ImhDigitsOnly)
        self.messageInputASK.setFrameShape(QFrame.StyledPanel)
        self.messageInputASK.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.messageInputASK)


        self.verticalLayout_4.addWidget(self.horizontalFrame_5)

        self.horizontalFrame_8 = QFrame(self.dataInpBox_3)
        self.horizontalFrame_8.setObjectName(u"horizontalFrame_8")
        self.horizontalFrame_8.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.horizontalFrame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.carrierFreqInputASK = QSpinBox(self.horizontalFrame_8)
        self.carrierFreqInputASK.setObjectName(u"carrierFreqInputASK")
        self.carrierFreqInputASK.setFont(font2)
        self.carrierFreqInputASK.setMinimum(25)
        self.carrierFreqInputASK.setMaximum(100)
        self.carrierFreqInputASK.setValue(50)

        self.horizontalLayout_10.addWidget(self.carrierFreqInputASK)


        self.verticalLayout_4.addWidget(self.horizontalFrame_8)

        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 20, 171, 81))
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.clearBtnASK = QPushButton(self.tab_3)
        self.clearBtnASK.setObjectName(u"clearBtnASK")
        self.clearBtnASK.setGeometry(QRect(30, 350, 150, 50))
        self.clearBtnASK.setFont(font4)
        self.clearBtnASK.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnASK.setAcceptDrops(False)
        self.clearBtnASK.setAutoFillBackground(False)
        self.clearBtnASK.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnASK.setIconSize(QSize(16, 16))
        self.clearBtnASK.setAutoDefault(False)
        self.clearBtnASK.setFlat(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.clearBtnFSK = QPushButton(self.tab_4)
        self.clearBtnFSK.setObjectName(u"clearBtnFSK")
        self.clearBtnFSK.setGeometry(QRect(50, 380, 150, 50))
        self.clearBtnFSK.setFont(font4)
        self.clearBtnFSK.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnFSK.setAcceptDrops(False)
        self.clearBtnFSK.setAutoFillBackground(False)
        self.clearBtnFSK.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnFSK.setIconSize(QSize(16, 16))
        self.clearBtnFSK.setAutoDefault(False)
        self.clearBtnFSK.setFlat(False)
        self.label_17 = QLabel(self.tab_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 20, 171, 81))
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.modulateBtnFSK = QPushButton(self.tab_4)
        self.modulateBtnFSK.setObjectName(u"modulateBtnFSK")
        self.modulateBtnFSK.setGeometry(QRect(50, 320, 150, 50))
        self.modulateBtnFSK.setFont(font4)
        self.modulateBtnFSK.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnFSK.setAcceptDrops(False)
        self.modulateBtnFSK.setAutoFillBackground(False)
        self.modulateBtnFSK.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnFSK.setIconSize(QSize(16, 16))
        self.modulateBtnFSK.setAutoDefault(False)
        self.modulateBtnFSK.setFlat(False)
        self.dataInpBox_4 = QFrame(self.tab_4)
        self.dataInpBox_4.setObjectName(u"dataInpBox_4")
        self.dataInpBox_4.setGeometry(QRect(0, 110, 241, 201))
        self.verticalLayout_6 = QVBoxLayout(self.dataInpBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalFrame_9 = QFrame(self.dataInpBox_4)
        self.horizontalFrame_9.setObjectName(u"horizontalFrame_9")
        self.horizontalFrame_9.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_7 = QVBoxLayout(self.horizontalFrame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.horizontalFrame_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_15)

        self.messageInputFSK = QTextEdit(self.horizontalFrame_9)
        self.messageInputFSK.setObjectName(u"messageInputFSK")
        sizePolicy.setHeightForWidth(self.messageInputFSK.sizePolicy().hasHeightForWidth())
        self.messageInputFSK.setSizePolicy(sizePolicy)
        self.messageInputFSK.setMaximumSize(QSize(16777215, 25))
        self.messageInputFSK.setFont(font2)
        self.messageInputFSK.setStyleSheet(u"")
        self.messageInputFSK.setInputMethodHints(Qt.ImhDigitsOnly)
        self.messageInputFSK.setFrameShape(QFrame.StyledPanel)
        self.messageInputFSK.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.messageInputFSK)


        self.verticalLayout_6.addWidget(self.horizontalFrame_9)

        self.horizontalFrame_10 = QFrame(self.dataInpBox_4)
        self.horizontalFrame_10.setObjectName(u"horizontalFrame_10")
        self.horizontalFrame_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.horizontalFrame_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.carrierFreq1InputFSK = QSpinBox(self.horizontalFrame_10)
        self.carrierFreq1InputFSK.setObjectName(u"carrierFreq1InputFSK")
        self.carrierFreq1InputFSK.setFont(font2)
        self.carrierFreq1InputFSK.setMinimum(25)
        self.carrierFreq1InputFSK.setMaximum(150)
        self.carrierFreq1InputFSK.setValue(50)

        self.horizontalLayout_11.addWidget(self.carrierFreq1InputFSK)


        self.verticalLayout_6.addWidget(self.horizontalFrame_10)

        self.horizontalFrame_11 = QFrame(self.dataInpBox_4)
        self.horizontalFrame_11.setObjectName(u"horizontalFrame_11")
        self.horizontalFrame_11.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalFrame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.horizontalFrame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.carrierFreq2InputFSK = QSpinBox(self.horizontalFrame_11)
        self.carrierFreq2InputFSK.setObjectName(u"carrierFreq2InputFSK")
        self.carrierFreq2InputFSK.setFont(font2)
        self.carrierFreq2InputFSK.setMinimum(25)
        self.carrierFreq2InputFSK.setMaximum(150)
        self.carrierFreq2InputFSK.setValue(50)

        self.horizontalLayout_12.addWidget(self.carrierFreq2InputFSK)


        self.verticalLayout_6.addWidget(self.horizontalFrame_11)

        self.FSK_graph_layout = QFrame(self.tab_4)
        self.FSK_graph_layout.setObjectName(u"FSK_graph_layout")
        self.FSK_graph_layout.setGeometry(QRect(239, 10, 751, 510))
        sizePolicy1.setHeightForWidth(self.FSK_graph_layout.sizePolicy().hasHeightForWidth())
        self.FSK_graph_layout.setSizePolicy(sizePolicy1)
        self.FSK_graph_layout.setMaximumSize(QSize(880, 510))
        self.FSK_graph_layout.setStyleSheet(u"")
        self.graph_layout_4 = QVBoxLayout(self.FSK_graph_layout)
        self.graph_layout_4.setObjectName(u"graph_layout_4")
        self.MplWidgetFSK = MplWidgetFSK(self.FSK_graph_layout)
        self.MplWidgetFSK.setObjectName(u"MplWidgetFSK")
        sizePolicy.setHeightForWidth(self.MplWidgetFSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetFSK.setSizePolicy(sizePolicy)
        self.MplWidgetFSK.setMaximumSize(QSize(880, 490))
        self.MplWidgetFSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_4.addWidget(self.MplWidgetFSK)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.dataInpBox_5 = QFrame(self.tab_5)
        self.dataInpBox_5.setObjectName(u"dataInpBox_5")
        self.dataInpBox_5.setGeometry(QRect(0, 90, 191, 161))
        self.verticalLayout_8 = QVBoxLayout(self.dataInpBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalFrame_12 = QFrame(self.dataInpBox_5)
        self.horizontalFrame_12.setObjectName(u"horizontalFrame_12")
        self.horizontalFrame_12.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_9 = QVBoxLayout(self.horizontalFrame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.horizontalFrame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_20)

        self.messageInputPSK = QTextEdit(self.horizontalFrame_12)
        self.messageInputPSK.setObjectName(u"messageInputPSK")
        sizePolicy.setHeightForWidth(self.messageInputPSK.sizePolicy().hasHeightForWidth())
        self.messageInputPSK.setSizePolicy(sizePolicy)
        self.messageInputPSK.setMaximumSize(QSize(16777215, 25))
        self.messageInputPSK.setFont(font2)
        self.messageInputPSK.setStyleSheet(u"")
        self.messageInputPSK.setInputMethodHints(Qt.ImhDigitsOnly)
        self.messageInputPSK.setFrameShape(QFrame.StyledPanel)
        self.messageInputPSK.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_9.addWidget(self.messageInputPSK)


        self.verticalLayout_8.addWidget(self.horizontalFrame_12)

        self.horizontalFrame_13 = QFrame(self.dataInpBox_5)
        self.horizontalFrame_13.setObjectName(u"horizontalFrame_13")
        self.horizontalFrame_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalFrame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.horizontalFrame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.carrierFreqInputPSK = QSpinBox(self.horizontalFrame_13)
        self.carrierFreqInputPSK.setObjectName(u"carrierFreqInputPSK")
        self.carrierFreqInputPSK.setFont(font2)
        self.carrierFreqInputPSK.setMinimum(25)
        self.carrierFreqInputPSK.setMaximum(300)
        self.carrierFreqInputPSK.setValue(50)

        self.horizontalLayout_13.addWidget(self.carrierFreqInputPSK)


        self.verticalLayout_8.addWidget(self.horizontalFrame_13)

        self.modulateBtnPSK = QPushButton(self.tab_5)
        self.modulateBtnPSK.setObjectName(u"modulateBtnPSK")
        self.modulateBtnPSK.setGeometry(QRect(25, 300, 150, 50))
        self.modulateBtnPSK.setFont(font4)
        self.modulateBtnPSK.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnPSK.setAcceptDrops(False)
        self.modulateBtnPSK.setAutoFillBackground(False)
        self.modulateBtnPSK.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnPSK.setIconSize(QSize(16, 16))
        self.modulateBtnPSK.setAutoDefault(False)
        self.modulateBtnPSK.setFlat(False)
        self.clearBtnPSK = QPushButton(self.tab_5)
        self.clearBtnPSK.setObjectName(u"clearBtnPSK")
        self.clearBtnPSK.setGeometry(QRect(25, 390, 150, 50))
        self.clearBtnPSK.setFont(font4)
        self.clearBtnPSK.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnPSK.setAcceptDrops(False)
        self.clearBtnPSK.setAutoFillBackground(False)
        self.clearBtnPSK.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnPSK.setIconSize(QSize(16, 16))
        self.clearBtnPSK.setAutoDefault(False)
        self.clearBtnPSK.setFlat(False)
        self.label_22 = QLabel(self.tab_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(16, 20, 171, 61))
        self.label_22.setFont(font5)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.PSK_graph_layout = QFrame(self.tab_5)
        self.PSK_graph_layout.setObjectName(u"PSK_graph_layout")
        self.PSK_graph_layout.setGeometry(QRect(195, 0, 680, 510))
        sizePolicy1.setHeightForWidth(self.PSK_graph_layout.sizePolicy().hasHeightForWidth())
        self.PSK_graph_layout.setSizePolicy(sizePolicy1)
        self.PSK_graph_layout.setMaximumSize(QSize(880, 510))
        self.PSK_graph_layout.setStyleSheet(u"")
        self.graph_layout_5 = QVBoxLayout(self.PSK_graph_layout)
        self.graph_layout_5.setObjectName(u"graph_layout_5")
        self.MplWidgetPSK = MplWidget(self.PSK_graph_layout)
        self.MplWidgetPSK.setObjectName(u"MplWidgetPSK")
        sizePolicy.setHeightForWidth(self.MplWidgetPSK.sizePolicy().hasHeightForWidth())
        self.MplWidgetPSK.setSizePolicy(sizePolicy)
        self.MplWidgetPSK.setMaximumSize(QSize(880, 490))
        self.MplWidgetPSK.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_5.addWidget(self.MplWidgetPSK)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.modulateBtnPAM = QPushButton(self.tab_6)
        self.modulateBtnPAM.setObjectName(u"modulateBtnPAM")
        self.modulateBtnPAM.setGeometry(QRect(25, 300, 150, 50))
        self.modulateBtnPAM.setFont(font4)
        self.modulateBtnPAM.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnPAM.setAcceptDrops(False)
        self.modulateBtnPAM.setAutoFillBackground(False)
        self.modulateBtnPAM.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnPAM.setIconSize(QSize(16, 16))
        self.modulateBtnPAM.setAutoDefault(False)
        self.modulateBtnPAM.setFlat(False)
        self.clearBtnPAM = QPushButton(self.tab_6)
        self.clearBtnPAM.setObjectName(u"clearBtnPAM")
        self.clearBtnPAM.setGeometry(QRect(25, 390, 150, 50))
        self.clearBtnPAM.setFont(font4)
        self.clearBtnPAM.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnPAM.setAcceptDrops(False)
        self.clearBtnPAM.setAutoFillBackground(False)
        self.clearBtnPAM.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnPAM.setIconSize(QSize(16, 16))
        self.clearBtnPAM.setAutoDefault(False)
        self.clearBtnPAM.setFlat(False)
        self.label_25 = QLabel(self.tab_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(16, 20, 171, 61))
        self.label_25.setFont(font5)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.PAM_graph_layout = QFrame(self.tab_6)
        self.PAM_graph_layout.setObjectName(u"PAM_graph_layout")
        self.PAM_graph_layout.setGeometry(QRect(195, 0, 680, 510))
        sizePolicy1.setHeightForWidth(self.PAM_graph_layout.sizePolicy().hasHeightForWidth())
        self.PAM_graph_layout.setSizePolicy(sizePolicy1)
        self.PAM_graph_layout.setMaximumSize(QSize(880, 510))
        self.PAM_graph_layout.setStyleSheet(u"")
        self.graph_layout_6 = QVBoxLayout(self.PAM_graph_layout)
        self.graph_layout_6.setObjectName(u"graph_layout_6")
        self.MplWidgetPAM = MplWidget(self.PAM_graph_layout)
        self.MplWidgetPAM.setObjectName(u"MplWidgetPAM")
        sizePolicy.setHeightForWidth(self.MplWidgetPAM.sizePolicy().hasHeightForWidth())
        self.MplWidgetPAM.setSizePolicy(sizePolicy)
        self.MplWidgetPAM.setMaximumSize(QSize(880, 490))
        self.MplWidgetPAM.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_6.addWidget(self.MplWidgetPAM)

        self.dataInpBox_6 = QFrame(self.tab_6)
        self.dataInpBox_6.setObjectName(u"dataInpBox_6")
        self.dataInpBox_6.setGeometry(QRect(0, 90, 191, 131))
        self.verticalLayout_11 = QVBoxLayout(self.dataInpBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalFrame_18 = QFrame(self.dataInpBox_6)
        self.horizontalFrame_18.setObjectName(u"horizontalFrame_18")
        self.horizontalFrame_18.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalFrame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_28 = QLabel(self.horizontalFrame_18)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_28)

        self.msgFreqInputPAM = QSpinBox(self.horizontalFrame_18)
        self.msgFreqInputPAM.setObjectName(u"msgFreqInputPAM")
        self.msgFreqInputPAM.setMinimum(5)
        self.msgFreqInputPAM.setMaximum(100)
        self.msgFreqInputPAM.setValue(5)

        self.horizontalLayout_17.addWidget(self.msgFreqInputPAM)


        self.verticalLayout_11.addWidget(self.horizontalFrame_18)

        self.horizontalFrame_19 = QFrame(self.dataInpBox_6)
        self.horizontalFrame_19.setObjectName(u"horizontalFrame_19")
        sizePolicy.setHeightForWidth(self.horizontalFrame_19.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_19.setSizePolicy(sizePolicy)
        self.horizontalFrame_19.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalFrame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 1, 9, 1)
        self.label_29 = QLabel(self.horizontalFrame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setIndent(-1)

        self.horizontalLayout_18.addWidget(self.label_29)

        self.msgAmpInputPAM = QDoubleSpinBox(self.horizontalFrame_19)
        self.msgAmpInputPAM.setObjectName(u"msgAmpInputPAM")
        self.msgAmpInputPAM.setMinimum(1.000000000000000)
        self.msgAmpInputPAM.setMaximum(5.000000000000000)
        self.msgAmpInputPAM.setValue(1.000000000000000)

        self.horizontalLayout_18.addWidget(self.msgAmpInputPAM)


        self.verticalLayout_11.addWidget(self.horizontalFrame_19)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.clearBtnPWM = QPushButton(self.tab_7)
        self.clearBtnPWM.setObjectName(u"clearBtnPWM")
        self.clearBtnPWM.setGeometry(QRect(25, 390, 150, 50))
        self.clearBtnPWM.setFont(font4)
        self.clearBtnPWM.setFocusPolicy(Qt.StrongFocus)
        self.clearBtnPWM.setAcceptDrops(False)
        self.clearBtnPWM.setAutoFillBackground(False)
        self.clearBtnPWM.setStyleSheet(u"QPushButton {\n"
"background-color: #de122f;\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #ef344f;\n"
"}")
        self.clearBtnPWM.setIconSize(QSize(16, 16))
        self.clearBtnPWM.setAutoDefault(False)
        self.clearBtnPWM.setFlat(False)
        self.label_26 = QLabel(self.tab_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(16, 20, 171, 61))
        self.label_26.setFont(font5)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.modulateBtnPWM = QPushButton(self.tab_7)
        self.modulateBtnPWM.setObjectName(u"modulateBtnPWM")
        self.modulateBtnPWM.setGeometry(QRect(25, 300, 150, 50))
        self.modulateBtnPWM.setFont(font4)
        self.modulateBtnPWM.setFocusPolicy(Qt.StrongFocus)
        self.modulateBtnPWM.setAcceptDrops(False)
        self.modulateBtnPWM.setAutoFillBackground(False)
        self.modulateBtnPWM.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 85, 0);\n"
"border-radius: 5px;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        self.modulateBtnPWM.setIconSize(QSize(16, 16))
        self.modulateBtnPWM.setAutoDefault(False)
        self.modulateBtnPWM.setFlat(False)
        self.PWM_graph_layout = QFrame(self.tab_7)
        self.PWM_graph_layout.setObjectName(u"PWM_graph_layout")
        self.PWM_graph_layout.setGeometry(QRect(195, 0, 680, 510))
        sizePolicy1.setHeightForWidth(self.PWM_graph_layout.sizePolicy().hasHeightForWidth())
        self.PWM_graph_layout.setSizePolicy(sizePolicy1)
        self.PWM_graph_layout.setMaximumSize(QSize(880, 510))
        self.PWM_graph_layout.setStyleSheet(u"")
        self.graph_layout_7 = QVBoxLayout(self.PWM_graph_layout)
        self.graph_layout_7.setObjectName(u"graph_layout_7")
        self.MplWidgetPWM = MplWidget(self.PWM_graph_layout)
        self.MplWidgetPWM.setObjectName(u"MplWidgetPWM")
        sizePolicy.setHeightForWidth(self.MplWidgetPWM.sizePolicy().hasHeightForWidth())
        self.MplWidgetPWM.setSizePolicy(sizePolicy)
        self.MplWidgetPWM.setMaximumSize(QSize(880, 490))
        self.MplWidgetPWM.setStyleSheet(u"background-color: rgba(0,0,0,0.7);\n"
"border-radius: 5px;")

        self.graph_layout_7.addWidget(self.MplWidgetPWM)

        self.dataInpBox_7 = QFrame(self.tab_7)
        self.dataInpBox_7.setObjectName(u"dataInpBox_7")
        self.dataInpBox_7.setGeometry(QRect(0, 90, 191, 131))
        self.verticalLayout_12 = QVBoxLayout(self.dataInpBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalFrame_20 = QFrame(self.dataInpBox_7)
        self.horizontalFrame_20.setObjectName(u"horizontalFrame_20")
        self.horizontalFrame_20.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_30 = QLabel(self.horizontalFrame_20)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.msgFreqInputPWM = QSpinBox(self.horizontalFrame_20)
        self.msgFreqInputPWM.setObjectName(u"msgFreqInputPWM")
        self.msgFreqInputPWM.setMinimum(5)
        self.msgFreqInputPWM.setMaximum(100)
        self.msgFreqInputPWM.setValue(5)

        self.horizontalLayout_19.addWidget(self.msgFreqInputPWM)


        self.verticalLayout_12.addWidget(self.horizontalFrame_20)

        self.horizontalFrame_21 = QFrame(self.dataInpBox_7)
        self.horizontalFrame_21.setObjectName(u"horizontalFrame_21")
        sizePolicy.setHeightForWidth(self.horizontalFrame_21.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_21.setSizePolicy(sizePolicy)
        self.horizontalFrame_21.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalFrame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 1, 9, 1)
        self.label_31 = QLabel(self.horizontalFrame_21)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setIndent(-1)

        self.horizontalLayout_20.addWidget(self.label_31)

        self.msgAmpInputPWM = QDoubleSpinBox(self.horizontalFrame_21)
        self.msgAmpInputPWM.setObjectName(u"msgAmpInputPWM")
        self.msgAmpInputPWM.setMinimum(1.000000000000000)
        self.msgAmpInputPWM.setMaximum(5.000000000000000)
        self.msgAmpInputPWM.setValue(1.000000000000000)

        self.horizontalLayout_20.addWidget(self.msgAmpInputPWM)


        self.verticalLayout_12.addWidget(self.horizontalFrame_21)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)

        ComSys.setCentralWidget(self.centralwidget)

        self.retranslateUi(ComSys)

        self.tabWidget.setCurrentIndex(0)
        self.modulateBtnAM.setDefault(False)
        self.clearBtnAM.setDefault(False)
        self.modulateBtnFM.setDefault(False)
        self.clearBtnFM.setDefault(False)
        self.modulateBtnASK.setDefault(False)
        self.clearBtnASK.setDefault(False)
        self.clearBtnFSK.setDefault(False)
        self.modulateBtnFSK.setDefault(False)
        self.modulateBtnPSK.setDefault(False)
        self.clearBtnPSK.setDefault(False)
        self.modulateBtnPAM.setDefault(False)
        self.clearBtnPAM.setDefault(False)
        self.clearBtnPWM.setDefault(False)
        self.modulateBtnPWM.setDefault(False)


        QMetaObject.connectSlotsByName(ComSys)
    # setupUi

    def retranslateUi(self, ComSys):
        ComSys.setWindowTitle(QCoreApplication.translate("ComSys", u"Python QtDesigner", None))
#if QT_CONFIG(tooltip)
        self.tab_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tab_1.setWhatsThis(QCoreApplication.translate("ComSys", u"AM Tab", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("ComSys", u"Frecuencia Moduladora (Hz)     ", None))
        self.label_6.setText(QCoreApplication.translate("ComSys", u"Amplitud Moduladora(V)       ", None))
        self.label_5.setText(QCoreApplication.translate("ComSys", u"Frecuencia Portadora (Hz)  ", None))
        self.label_4.setText(QCoreApplication.translate("ComSys", u"Amplitud Portadora (V)   ", None))
        self.modulateBtnAM.setText(QCoreApplication.translate("ComSys", u"Modular", None))
        self.clearBtnAM.setText(QCoreApplication.translate("ComSys", u"Borrar", None))
        self.label_8.setText(QCoreApplication.translate("ComSys", u"Modulaci\u00f3n por Amplitud", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("ComSys", u"AM ", None))
        self.label_9.setText(QCoreApplication.translate("ComSys", u"Frequency Modulation", None))
        self.modulateBtnFM.setText(QCoreApplication.translate("ComSys", u"Modulate", None))
        self.clearBtnFM.setText(QCoreApplication.translate("ComSys", u"Clear", None))
        self.label_10.setText(QCoreApplication.translate("ComSys", u"Msg. Freq. (Hz)     ", None))
        self.label_12.setText(QCoreApplication.translate("ComSys", u"Carrier Freq (Hz)  ", None))
        self.label_13.setText(QCoreApplication.translate("ComSys", u"Modulation Index", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ComSys", u"FM", None))
        self.modulateBtnASK.setText(QCoreApplication.translate("ComSys", u"Modular", None))
        self.label_11.setText(QCoreApplication.translate("ComSys", u"Ingresar cadena de\n"
"2 / 8 / 16 / 32 bits", None))
        self.messageInputASK.setHtml(QCoreApplication.translate("ComSys", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Product Sans','Product Sans'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.messageInputASK.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("ComSys", u"Frecuencia Portadora (Hz)  ", None))
        self.label_16.setText(QCoreApplication.translate("ComSys", u"<html><head/><body><p>Modulaci\u00f3n por </p><p>Conmutaci\u00f3n </p><p>de Amplitud</p></body></html>", None))
        self.clearBtnASK.setText(QCoreApplication.translate("ComSys", u"Borrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ComSys", u"ASK", None))
        self.clearBtnFSK.setText(QCoreApplication.translate("ComSys", u"Borrar", None))
        self.label_17.setText(QCoreApplication.translate("ComSys", u"<html><head/><body><p>Modulaci\u00f3n por </p><p>Conmutaci\u00f3n </p><p>de Frecuencia</p></body></html>", None))
        self.modulateBtnFSK.setText(QCoreApplication.translate("ComSys", u"Modular", None))
        self.label_15.setText(QCoreApplication.translate("ComSys", u"Ingresar bits", None))
        self.messageInputFSK.setHtml(QCoreApplication.translate("ComSys", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Product Sans','Product Sans'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
        self.messageInputFSK.setPlaceholderText(QCoreApplication.translate("ComSys", u" Enter Binary String", None))
        self.label_18.setText(QCoreApplication.translate("ComSys", u"Frecuencia Portadora 1 (Hz)", None))
        self.label_19.setText(QCoreApplication.translate("ComSys", u"Frecuencia Portadora 2 (Hz)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ComSys", u"FSK", None))
        self.label_20.setText(QCoreApplication.translate("ComSys", u"Binary Message\n"
"Size 2 / 4 / 8 / 16 Only", None))
        self.messageInputPSK.setPlaceholderText(QCoreApplication.translate("ComSys", u" Enter Binary String", None))
        self.label_21.setText(QCoreApplication.translate("ComSys", u"Carrier Freq (Hz)  ", None))
        self.modulateBtnPSK.setText(QCoreApplication.translate("ComSys", u"Modulate", None))
        self.clearBtnPSK.setText(QCoreApplication.translate("ComSys", u"Clear", None))
        self.label_22.setText(QCoreApplication.translate("ComSys", u"<html><head/><body><p>Phase Shift </p><p>Keying</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("ComSys", u"PSK", None))
        self.modulateBtnPAM.setText(QCoreApplication.translate("ComSys", u"Modulate", None))
        self.clearBtnPAM.setText(QCoreApplication.translate("ComSys", u"Clear", None))
        self.label_25.setText(QCoreApplication.translate("ComSys", u"<html><head/><body><p>Pulse Amplitude </p><p>Modulation</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("ComSys", u"Msg. Freq. (Hz)     ", None))
        self.label_29.setText(QCoreApplication.translate("ComSys", u"Msg. Amp (V)       ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("ComSys", u"PAM", None))
        self.clearBtnPWM.setText(QCoreApplication.translate("ComSys", u"Clear", None))
        self.label_26.setText(QCoreApplication.translate("ComSys", u"<html><head/><body><p>Pulse Width </p><p>Modulation</p></body></html>", None))
        self.modulateBtnPWM.setText(QCoreApplication.translate("ComSys", u"Modulate", None))
        self.label_30.setText(QCoreApplication.translate("ComSys", u"Msg. Freq. (Hz)     ", None))
        self.label_31.setText(QCoreApplication.translate("ComSys", u"Msg. Amp (V)       ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("ComSys", u"PWM", None))
    # retranslateUi

