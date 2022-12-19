################################################################################
##
## SIGMA BY: LUCAS DEPETRIS
## BASED ON WANDERSON M. PIMENTA'S PROJECT AND COMSYS-TRAINER BY SOUMADIP DEY
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
# from PySide2 import QtCore, QtGui, QtWidgets, QtTest
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QColor, QFont
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *

# MODULATIONS
from matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
from PySide2.QtWidgets import *
import sys

# ANIMATION
from matplotlib.animation import FuncAnimation

# Telling windows to let me make my own taskbar icons
# import ctypes
# myappid = 'lucasdepetris.SigMA.gui.v1'
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Libraries that do the heavy lifting
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.setWindowIcon(QtGui.QIcon("url(:/16x16/icons/16x16/cil-home.png)"))

        self.ventana = HelpWindow()
        self.ventana.hide()

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('SigMA')
        UIFunctions.labelTitle(self, 'SigMA: Signal Modulation Analyzer')
        UIFunctions.labelDescription(self, 'Seleccione una opción')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Inicio", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "ASK", "btn_ASK", "url(:/16x16/icons/16x16/cil-ask.png)", True)
        UIFunctions.addNewMenu(self, "FSK", "btn_FSK", "url(:/16x16/icons/16x16/cil-fsk.png)", True)
        UIFunctions.addNewMenu(self, "PSK", "btn_PSK", "url(:/16x16/icons/16x16/cil-psk.png)", True)

        UIFunctions.addNewMenu(self, "Ajustes", "btn_ajustes", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        UIFunctions.labelPage(self, "Inicio")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "LD", "url(:/24x24/icons/24x24/sigma-logo.png)", True)
        UIFunctions.labelCredits(self, "Desarrollado por: Lucas Depetris")
        UIFunctions.labelVersion(self, "v1.0")
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        # ASK MODULATION CONNECTORS
        self.ui.messageInputASK.textChanged.connect(lambda: self.modulateASK())
        self.ui.carrierFreqInputASK.valueChanged.connect(lambda: self.modulateASK())
        self.ui.clearBtnASK.clicked.connect(lambda: self.clearASK())
        # ASK ANIMATION CONNECTORS
        self.ui.modulateBtnASK.clicked.connect(lambda: self.animateModulation("ask"))
        self.ui.Btn_pauseASK.clicked.connect(lambda: self.ui.MplWidgetASK.switchAnimation(True))

        # FSK MODULATION CONNECTORS
        self.ui.messageInputFSK.textChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq1InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq2InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())
        # FSK ANIMATION CONNECTORS
        self.ui.modulateBtnFSK.clicked.connect(lambda: self.animateModulation("fsk"))
        self.ui.Btn_pauseFSK.clicked.connect(lambda: self.ui.MplWidgetFSK.switchAnimation(True))

        # PSK MODULATION CONNECTORS
        self.ui.messageInputPSK.textChanged.connect(lambda: self.modulatePSK())
        self.ui.carrierFreqInputPSK.valueChanged.connect(lambda: self.modulatePSK())
        self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())
        # PSK ANIMATION CONNECTORS
        self.ui.modulateBtnPSK.clicked.connect(lambda: self.animateModulation("psk"))
        self.ui.Btn_pausePSK.clicked.connect(lambda: self.ui.MplWidgetPSK.switchAnimation(True))

        self.ui.Btn_helpASK.clicked.connect(lambda: self.helpPage("ask"))
        self.ui.Btn_helpFSK.clicked.connect(lambda: self.helpPage("fsk"))
        self.ui.Btn_helpPSK.clicked.connect(lambda: self.helpPage("psk"))
        self.ui.Btn_helpSettings.clicked.connect(lambda: self.helpPage("settings"))
        self.ui.Btn_helpMain.clicked.connect(lambda: self.helpPage("main"))

        self.ui.Btn_ASK.clicked.connect(self.Button)
        self.ui.Btn_FSK.clicked.connect(self.Button)
        self.ui.Btn_PSK.clicked.connect(self.Button)
        
        # SETTINGS
        self.ui.btn_AplicarASK.clicked.connect(lambda: self.valueChanged(self.ui.maxCarrierASK, self.ui.minCarrierASK, self.ui.sliderASK, self.ui.carrierFreqInputASK, self.ui.label_maxASK, self.ui.label_minASK))
        self.ui.btn_AplicarFSK1.clicked.connect(lambda: self.valueChanged(self.ui.maxCarrierFSK1, self.ui.minCarrierFSK1, self.ui.sliderFSK1, self.ui.carrierFreq1InputFSK, self.ui.label_maxFSK_1, self.ui.label_minFSK_1))
        self.ui.btn_AplicarFSK2.clicked.connect(lambda: self.valueChanged(self.ui.maxCarrierFSK2, self.ui.minCarrierFSK2, self.ui.sliderFSK2, self.ui.carrierFreq2InputFSK, self.ui.label_maxFSK_2, self.ui.label_minFSK_2))
        self.ui.btn_AplicarPSK.clicked.connect(lambda: self.valueChanged(self.ui.maxCarrierPSK, self.ui.minCarrierPSK, self.ui.sliderPSK, self.ui.carrierFreqInputPSK, self.ui.label_maxPSK, self.ui.label_minPSK))
        
        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELOW                                               ##
        ########################################################################

        ## ==> QTableWidget PARAMETERS
        ########################################################################
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        ## PLOTS ==> SUBPLOTS FUNCTIONS
        ########################################################################
        # Creating subplots and a blank canvas for ASK
        self.ui.MplWidgetASK.canvas.ax3 = self.ui.MplWidgetASK.canvas.figure.add_subplot(313)
        self.ui.MplWidgetASK.canvas.ax1 = self.ui.MplWidgetASK.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetASK.canvas.ax3)
        self.ui.MplWidgetASK.canvas.ax2 = self.ui.MplWidgetASK.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetASK.canvas.ax3)
        self.ui.MplWidgetASK.canvas.ax1.set_xticks([])

        # Creating subplots and a blank canvas for FSK
        gdspec_fsk = self.ui.MplWidgetFSK.gridspec
        self.ui.MplWidgetFSK.canvas.ax4 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[3,:])
        self.ui.MplWidgetFSK.canvas.ax1 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[0,:],sharex = self.ui.MplWidgetFSK.canvas.ax4)
        self.ui.MplWidgetFSK.canvas.ax2 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[1,:],sharex = self.ui.MplWidgetFSK.canvas.ax4)
        self.ui.MplWidgetFSK.canvas.ax3 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[2,:],sharex = self.ui.MplWidgetFSK.canvas.ax4)
        self.ui.MplWidgetFSK.canvas.ax2.set_xticks([])
        self.ui.MplWidgetFSK.canvas.ax3.set_xticks([])

        # Creating Subplots and a blank canvas for PSK
        self.ui.MplWidgetPSK.canvas.ax3 = self.ui.MplWidgetPSK.canvas.figure.add_subplot(313)
        self.ui.MplWidgetPSK.canvas.ax1 = self.ui.MplWidgetPSK.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetPSK.canvas.ax3)
        self.ui.MplWidgetPSK.canvas.ax2 = self.ui.MplWidgetPSK.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetPSK.canvas.ax3)
        self.ui.MplWidgetPSK.canvas.ax1.set_xticks([])

        self.ui.ASK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetASK.canvas,self))
        self.ui.FSK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetFSK.canvas,self))
        self.ui.PSK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetPSK.canvas,self))

        self.ui.MplWidgetASK.canvas.axes.set_visible(False)
        self.ui.MplWidgetFSK.canvas.axes.set_visible(False)
        self.ui.MplWidgetPSK.canvas.axes.set_visible(False)


        ## END ==> SUBPLOTS FUNCTIONS

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        
    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "INICIO")
            UIFunctions.labelDescription(self, 'Seleccione una opción')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ASK
        if btnWidget.objectName() == "btn_ASK" or btnWidget.objectName() == "Btn_ASK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ask)
            UIFunctions.resetStyle(self, "btn_ASK")
            UIFunctions.labelPage(self, "MODULACIÓN ASK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            if btnWidget.objectName() == "btn_ASK": btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        # PAGE FSK
        if btnWidget.objectName() == "btn_FSK" or btnWidget.objectName() == "Btn_FSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_fsk)
            UIFunctions.resetStyle(self, "btn_FSK")
            UIFunctions.labelPage(self, "MODULACIÓN FSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            if btnWidget.objectName() == "btn_FSK": btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        # PAGE PSK
        if btnWidget.objectName() == "btn_PSK" or btnWidget.objectName() == "Btn_PSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_psk)
            UIFunctions.resetStyle(self, "btn_PSK")
            UIFunctions.labelPage(self, "MODULACIÓN PSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            if btnWidget.objectName() == "btn_PSK": btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_ajustes":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            UIFunctions.resetStyle(self, "btn_ajustes")
            UIFunctions.labelPage(self, "AJUSTES")
            UIFunctions.labelDescription(self, 'Modifique los valores máximos y mínimos de frecuencia. Valores en rojo no seran considerados')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> CHANGE SETTINGS
    ########################################################################
    def valueChanged(self, inputMax: QSpinBox, inputMin: QSpinBox, slider: QSlider, input: QSpinBox, labelMax: QLabel, labelMin: QLabel):
        newMax = inputMax.value()
        newMin = inputMin.value()
        if (newMax - newMin) > 0:
            slider.setMaximum(newMax)
            input.setMaximum(newMax)
            slider.setMinimum(newMin)
            input.setMinimum(newMin)
            labelMax.setText("{0} Hz".format(newMax))
            labelMin.setText("{0} Hz".format(newMin))
            inputMax.setStyleSheet(Style.style_spinbox_ok)
            inputMin.setStyleSheet(Style.style_spinbox_ok)
        else:
            inputMax.setStyleSheet(Style.style_spinbox_error)
            inputMin.setStyleSheet(Style.style_spinbox_error)
            # print("No se puede cambiar: MaxAct={0} MaxIng={1}".format())
        # if (mod == "ask"):
        #     if (self.ui.carrierFreqInputASK.minimum() > value) :
        #         # self.ui.maxCarrierASK.setStyleSheet("border: 2px solid #ff0000;")
        #         self.ui.maxCarrierASK.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreqInputASK.maximum(),value))
        #     else:
        #         self.ui.maxCarrierASK.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreqInputASK.setMaximum(value)
        #         self.ui.sliderASK.setMaximum(value)
        # elif (mod == "askmin"):
        #     if (self.ui.carrierFreqInputASK.maximum() < value) :
        #         self.ui.minCarrierASK.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreqInputASK.minimum(),value))
        #     else:
        #         self.ui.minCarrierASK.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreqInputASK.setMinimum(value)
        #         self.ui.sliderASK.setMinimum(value)
        # elif (mod == "fsk1max"):
        #     if (self.ui.carrierFreq1InputFSK.minimum() > value) :
        #         self.ui.maxCarrierFSK1.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreq1InputFSK.maximum(),value))
        #     else:
        #         self.ui.maxCarrierFSK1.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreq1InputFSK.setMaximum(value)
        #         self.ui.sliderFSK1.setMaximum(value)
        # elif (mod == "fsk1min"):
        #     if (self.ui.carrierFreq1InputFSK.maximum() < value) :
        #         self.ui.minCarrierFSK1.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreq1InputFSK.minimum(),value))
        #     else:
        #         self.ui.minCarrierFSK1.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreq1InputFSK.setMinimum(value)
        #         self.ui.sliderFSK1.setMinimum(value)
        # elif (mod == "fsk2max"):
        #     if (self.ui.carrierFreq2InputFSK.minimum() > value) :
        #         self.ui.maxCarrierFSK2.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreq2InputFSK.maximum(),value))
        #     else:
        #         self.ui.maxCarrierFSK2.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreq2InputFSK.setMaximum(value)
        #         self.ui.sliderFSK2.setMaximum(value)
        # elif (mod == "fsk2min"):
        #     if (self.ui.carrierFreq2InputFSK.maximum() < value) :
        #         self.ui.minCarrierFSK2.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreq2InputFSK.minimum(),value))
        #     else:
        #         self.ui.minCarrierFSK2.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreq2InputFSK.setMinimum(value)
        #         self.ui.sliderFSK2.setMinimum(value)
        # elif (mod == "pskmax"):
        #     if (self.ui.carrierFreqInputPSK.minimum() > value) :
        #         self.ui.maxCarrierPSK.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreqInputPSK.maximum(),value))
        #     else:
        #         self.ui.maxCarrierPSK.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreqInputPSK.setMaximum(value)
        #         self.ui.sliderPSK.setMaximum(value)
        # elif (mod == "pskmin"):
        #     if (self.ui.carrierFreqInputPSK.maximum() < value) :
        #         self.ui.maxCarrierPSK.setStyleSheet(Style.style_spinbox_error)
        #         print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreqInputPSK.minimum(),value))
        #     else:
        #         self.ui.maxCarrierPSK.setStyleSheet(Style.style_spinbox_ok)
        #         self.ui.carrierFreqInputPSK.setMinimum(value)
        #         self.ui.sliderPSK.setMinimum(value)

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START ==> MODULATION EVENTS
    ########################################################################

    def checkMessage(self, message: str, messagebox: QTextEdit, label: QLabel, button: QPushButton):
        length = len(message)
        if length == 0:
            label.setText(str.format("{0}/16. Ingrese bits.",length))
            label.setStyleSheet("color: rgb(255, 255, 255);")
            messagebox.setStyleSheet("border: 2px solid rgb(255, 255, 255);")
            return False
        for bit in message:
            if(bit not in ["0","1"]):
                label.setText(str.format("{0}/16. Ingrese sólo 1 o 0.",length))
                label.setStyleSheet("color: rgb(207, 59, 72);")
                messagebox.setStyleSheet("border: 2px solid #ff0000;")
                button.click()
                return False
        if((length in [2**i for i in range(1,6)])):
            messagebox.setStyleSheet("border: 2px solid #00ff00;")
            label.setText(str.format("{0}/16",length))
            label.setStyleSheet("color: rgb(63, 152, 90);")
            return True
        button.click()
        messagebox.setStyleSheet("border: 2px solid #ff0000;")
        label.setText(str.format("{0}/16. Cantidad Incorrecta.",length))
        label.setStyleSheet("color: rgb(207, 59, 72);")
        return False        
    
    def clearASK(self):
        if hasattr(self.ui.MplWidgetASK, 'ani1'):
            self.ui.MplWidgetASK.pauseAnimation()
        self.ui.MplWidgetASK.canvas.ax1.clear()
        self.ui.MplWidgetASK.canvas.ax2.clear()
        self.ui.MplWidgetASK.canvas.ax3.clear()
        self.ui.MplWidgetASK.canvas.draw()
        
    def modulateASK(self):
        message = self.ui.messageInputASK.text()
        if(self.checkMessage(message,self.ui.messageInputASK, self.ui.labelASK, self.ui.clearBtnASK)):
            
            Fc = int(float(self.ui.carrierFreqInputASK.text()))
            Fs = 64 * Fc # Sampling freq must be >>> 2 * fc (Nyquist rate)
            Fs = Fs + (Fs % len(message))
            t = np.arange(0,1,1/Fs)
            samples = Fs // len(message)

            BG = BinaryGenerator(message,samples)

            data_signal = BG.generate()
            carrier_signal = np.cos(2 * np.pi * Fc * t)

            if len(t) > len(data_signal):
                dif = len(t) - len(data_signal)
                for i in range(dif):
                    data_signal = np.append(data_signal, data_signal[-1])
                    
            ask_signal = carrier_signal * data_signal

            arrays = [data_signal, carrier_signal, ask_signal]

            bandWidth = len(message)

            if self.ui.MplWidgetASK.canvas.ax1:
                self.ui.MplWidgetASK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetASK.canvas.axes.set_visible(False)

            # Clear the previous plots and/or animation if any
            if hasattr(self.ui.MplWidgetASK, 'ani1'):
                self.ui.MplWidgetASK.pauseAnimation()
            if hasattr(self.ui.MplWidgetPSK, 'ani1'):
                self.ui.MplWidgetPSK.pauseAnimation()
            if hasattr(self.ui.MplWidgetFSK, 'ani1'):
                self.ui.MplWidgetFSK.pauseAnimation()
            self.ui.MplWidgetASK.canvas.axes.clear()

            # Plotting data signal and asigning line
            self.ui.MplWidgetASK.canvas.ax1.clear()
            lin1, = self.ui.MplWidgetASK.canvas.ax1.plot(t,data_signal,color='red',label=f'Frec Muestreo = {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetASK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal and asigning line
            self.ui.MplWidgetASK.canvas.ax2.clear()
            lin2, = self.ui.MplWidgetASK.canvas.ax2.plot(t,carrier_signal,color='blue',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetASK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal and asigning line
            self.ui.MplWidgetASK.canvas.ax3.clear()
            lin3, = self.ui.MplWidgetASK.canvas.ax3.plot(t,ask_signal,color='purple',label=f'Señal ASK\n(0): Frec = 0 Hz\n(1): Frec = {Fc} Hz\nAB = {bandWidth} Hz')
            self.ui.MplWidgetASK.canvas.ax3.legend(loc = 'lower right')

            line = [lin1, lin2, lin3]

            # Removing intermediate xtick labels for a cleaner plot
            self.ui.MplWidgetASK.canvas.ax1.tick_params(
                                axis='x',          # changes apply to the x-axis
                                which='both',      # both major and minor ticks are affected
                                bottom='on',      # ticks along the bottom edge are off
                                top='off',         # ticks along the top edge are off
                                labelbottom='off'  # labels along the bottom edge are off)
                            )
            self.ui.MplWidgetASK.canvas.ax2.tick_params(
                                axis='x',          
                                which='both',      
                                bottom='on',      
                                top='off',         
                                labelbottom='off'  
                            )
            
            # Set Title and Show Plot
            self.ui.MplWidgetASK.canvas.ax1.set_title(f'Señal ASK')
            self.ui.MplWidgetASK.canvas.draw()
            return [arrays, t, line, self.ui.MplWidgetASK]
    
    def clearFSK(self):
        if hasattr(self.ui.MplWidgetFSK, 'ani1'):
            self.ui.MplWidgetFSK.pauseAnimation()
        self.ui.MplWidgetFSK.canvas.ax1.clear()
        self.ui.MplWidgetFSK.canvas.ax2.clear()
        self.ui.MplWidgetFSK.canvas.ax3.clear()
        self.ui.MplWidgetFSK.canvas.ax4.clear()
        self.ui.MplWidgetFSK.canvas.draw()
        
    def modulateFSK(self):
        message = self.ui.messageInputFSK.text()
        if(self.checkMessage(message,self.ui.messageInputFSK, self.ui.labelFSK, self.ui.clearBtnFSK)):
            Fc1 = int(float(self.ui.carrierFreq1InputFSK.text())) # Carrier freq 1
            Fc2 = int(float(self.ui.carrierFreq2InputFSK.text())) # Carrier freq 2
            Fs = 64 * max( Fc1, Fc2 ) # Sampling freq must be >>> 2 * fc (Nyquist rate)
            Fs = Fs + (Fs % len(message))
            t = np.arange(0, 1, 1/Fs)
            samples = Fs // len(message)

            BG = BinaryGenerator(message,samples)

            data_signal = BG.generate()
            data_signal_inverse = BG.generateInverse()
            carrier_signal_1 = np.cos(2 * np.pi * Fc1 * t)
            carrier_signal_2 = np.cos(2 * np.pi * Fc2 * t)

            if len(t) > len(data_signal_inverse):
                dif = len(t) - len(data_signal_inverse)
                for _ in range(dif):
                    data_signal_inverse = np.append(data_signal_inverse, data_signal_inverse[-1])
            
            if len(t) > len(data_signal):
                dif = len(t) - len(data_signal)
                for _ in range(dif):
                    data_signal = np.append(data_signal, data_signal[-1])

            fsk_signal = (carrier_signal_2 * data_signal) + (carrier_signal_1 * data_signal_inverse)

            arrays = [carrier_signal_1, carrier_signal_2, data_signal, fsk_signal]

            # T = 1/bps seconds 
            # B = 1/(2T)
            # 2B = 1/T
            # 2B = 1/(1/bps) = bps
            # 2B = bps Hz

            bandWidth = (len(message))+(2*abs(Fc2-Fc1))

            if self.ui.MplWidgetFSK.canvas.ax1:
                self.ui.MplWidgetFSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetFSK.canvas.axes.set_visible(False)

            # Clear the previous plots and animation if any
            if hasattr(self.ui.MplWidgetASK, 'ani1'):
                self.ui.MplWidgetASK.pauseAnimation()
            if hasattr(self.ui.MplWidgetPSK, 'ani1'):
                self.ui.MplWidgetPSK.pauseAnimation()
            if hasattr(self.ui.MplWidgetFSK, 'ani1'):
                self.ui.MplWidgetFSK.pauseAnimation()
            self.ui.MplWidgetFSK.canvas.axes.clear()

            # Plotting carrier signal 1 and asigning line
            self.ui.MplWidgetFSK.canvas.ax1.clear()
            lin1, = self.ui.MplWidgetFSK.canvas.ax1.plot(t,carrier_signal_1,color='cyan',label=f'Señal 1 \nFrecuencia: {Fc1} Hz')
            self.ui.MplWidgetFSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal 2 and asigning line
            self.ui.MplWidgetFSK.canvas.ax2.clear()
            lin2, = self.ui.MplWidgetFSK.canvas.ax2.plot(t,carrier_signal_2,color='yellow',label=f'Señal 2 \nFrecuencia:{Fc2} Hz')
            self.ui.MplWidgetFSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting Data Signal and asigning line
            self.ui.MplWidgetFSK.canvas.ax3.clear()
            lin3, = self.ui.MplWidgetFSK.canvas.ax3.plot(t,data_signal,color='lightcoral',label=f'Frec de Muestreo: {Fs} Hz\nBits : {message}')
            self.ui.MplWidgetFSK.canvas.ax3.legend(loc = 'lower right')

            # Plotting FSK modulated signal and asigning line
            self.ui.MplWidgetFSK.canvas.ax4.clear()
            lin4, = self.ui.MplWidgetFSK.canvas.ax4.plot(t,fsk_signal,color='white',label=f'Señal FSK \n(0): Frec = {Fc1} Hz\n(1): Frec = {Fc2} Hz\nAB = {bandWidth} Hz')
            self.ui.MplWidgetFSK.canvas.ax4.legend(loc = 'lower right')

            line = [lin1, lin2, lin3, lin4]

            # Removing intermediate xtick labels for a cleaner plot
            self.ui.MplWidgetFSK.canvas.ax1.tick_params(
                                axis='x',          # changes apply to the x-axis
                                which='both',      # both major and minor ticks are affected
                                bottom='on',      # ticks along the bottom edge are off
                                top='off',         # ticks along the top edge are off
                                labelbottom='off'  # labels along the bottom edge are off)
                            )
            self.ui.MplWidgetFSK.canvas.ax2.tick_params(
                                axis='x',          
                                which='both',      
                                bottom='on',      
                                top='off',         
                                labelbottom='off'  
                            )
            
            # Set Title and Show Plot
            self.ui.MplWidgetFSK.canvas.figure.suptitle(f'Señal FSK')
            self.ui.MplWidgetFSK.canvas.draw()
            return [arrays, t, line, self.ui.MplWidgetFSK]
            
    def clearPSK(self):
        if hasattr(self.ui.MplWidgetPSK, 'ani1'):
            self.ui.MplWidgetPSK.pauseAnimation()
        self.ui.MplWidgetPSK.canvas.ax1.clear()
        self.ui.MplWidgetPSK.canvas.ax2.clear()
        self.ui.MplWidgetPSK.canvas.ax3.clear()
        self.ui.MplWidgetPSK.canvas.draw()

    def modulatePSK(self):
        message = self.ui.messageInputPSK.text()
        if(self.checkMessage(message,self.ui.messageInputPSK, self.ui.labelPSK, self.ui.clearBtnPSK)):
            Fc = int(float(self.ui.carrierFreqInputPSK.text()))
            Fs = len(message) * 64
            t = np.arange(0, 1, 1/Fs)
            samples = len(t) // len(message)
            
            BG = BinaryGenerator(message,samples)

            data_signal = BG.generateBipolar()
            carrier_signal = np.sin(2 * np.pi * Fc * t)

            if len(t) > len(data_signal):
                dif = len(t) - len(data_signal)
                for i in range(dif):
                    data_signal = np.append(data_signal, data_signal[-1])

            psk_signal = data_signal * carrier_signal

            bandWidth = len(message)

            arrays = [data_signal, carrier_signal, psk_signal]

            if self.ui.MplWidgetPSK.canvas.ax1:
                self.ui.MplWidgetPSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetPSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetPSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetPSK.canvas.axes.set_visible(False)

            # Clear the previous plots if any
            if hasattr(self.ui.MplWidgetASK, 'ani1'):
                self.ui.MplWidgetASK.pauseAnimation()
            if hasattr(self.ui.MplWidgetPSK, 'ani1'):
                self.ui.MplWidgetPSK.pauseAnimation()
            if hasattr(self.ui.MplWidgetFSK, 'ani1'):
                self.ui.MplWidgetFSK.pauseAnimation()
            self.ui.MplWidgetPSK.canvas.axes.clear()

            # Plotting data signal and asigning line
            self.ui.MplWidgetPSK.canvas.ax1.clear()
            lin1, = self.ui.MplWidgetPSK.canvas.ax1.plot(t,data_signal,color='red',label=f'Frec de Muestreo: {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetPSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal and asigning line
            self.ui.MplWidgetPSK.canvas.ax2.clear()
            lin2, = self.ui.MplWidgetPSK.canvas.ax2.plot(t,carrier_signal,color='yellow',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetPSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal and asigning line
            self.ui.MplWidgetPSK.canvas.ax3.clear()
            lin3, = self.ui.MplWidgetPSK.canvas.ax3.plot(t,psk_signal,color='darkorange',label=f'Señal PSK\nAB = {bandWidth} Hz')
            self.ui.MplWidgetPSK.canvas.ax3.legend(loc = 'lower right')

            line = [lin1, lin2, lin3]

            # Removing intermediate xtick labels for a cleaner plot
            self.ui.MplWidgetPSK.canvas.ax1.tick_params(
                                axis='x',          # changes apply to the x-axis
                                which='both',      # both major and minor ticks are affected
                                bottom='on',      # ticks along the bottom edge are off
                                top='off',         # ticks along the top edge are off
                                labelbottom='off'  # labels along the bottom edge are off)
                            )
            self.ui.MplWidgetPSK.canvas.ax2.tick_params(
                                axis='x',          
                                which='both',      
                                bottom='on',      
                                top='off',         
                                labelbottom='off'  
                            )
            
            # Set Title and Show Plot
            self.ui.MplWidgetPSK.canvas.ax1.set_title(f'Señal PSK')
            self.ui.MplWidgetPSK.canvas.draw()
            return [arrays, t, line, self.ui.MplWidgetPSK]

    ########################################################################
    ## END ==> MODULATION EVENTS
    ########################################################################

    ########################################################################
    ## START ==> ANIMATION EVENTS
    ########################################################################

    def animateModulation(self, mod="nofsk"):
        if (mod != "fsk"):
            if(mod == "ask"):
                data = self.modulateASK()
            elif(mod == "psk"):
                data = self.modulatePSK()
            else: data = 0

            data_signal = data[0][0]
            carrier_signal = data[0][1]
            modulated_signal = data[0][2]
            t = data[1]
            line1 = data[2][0]
            line2 = data[2][1]
            line3 = data[2][2]
            mplwidget = data[3]

            anim1 = self.animateWave(mplwidget.canvas.figure, data_signal, line1, t)
            anim2 = self.animateWave(mplwidget.canvas.figure, carrier_signal, line2, t)
            anim3 = self.animateWave(mplwidget.canvas.figure, modulated_signal, line3, t)

            mplwidget.updateAnimation([anim1, anim2, anim3])
        else:
            data = self.modulateFSK()
            data_signal = data[0][0]
            carrier_signal_1 = data[0][1]
            carrier_signal_2 = data[0][2]
            modulated_signal = data[0][3]
            t = data[1]
            line1 = data[2][0]
            line2 = data[2][1]
            line3 = data[2][2]
            line4 = data[2][3]
            mplwidget = data[3]

            anim1 = self.animateWave(mplwidget.canvas.figure, data_signal, line1, t)
            anim2 = self.animateWave(mplwidget.canvas.figure, carrier_signal_1, line2, t)
            anim3 = self.animateWave(mplwidget.canvas.figure, carrier_signal_2, line3, t)
            anim4 = self.animateWave(mplwidget.canvas.figure, modulated_signal, line4, t)

            mplwidget.updateAnimation([anim1, anim2, anim3, anim4])

    def animateWave(self, mplwidget, wave, line, t):
        
        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            # x = np.linspace(0, 5, 500)
            y = np.roll(wave, -i) 
            line.set_data(t, y)
            return line,

        anim = FuncAnimation(mplwidget, animate, init_func=init, frames=len(t), interval=10, blit=True)
        return anim

    ########################################################################
    ## END ==> ANIMATION EVENT
    ########################################################################

    ########################################################################
    ## START ==> HELP EVENTS
    ########################################################################

    def helpPage(self, mod):
        if (mod == "ask"):
            self.ventana.changeWidget(self.ventana.ui.page_ask)
            UIFunctionsHelp.labelTitle(self.ventana,'Ayuda ASK')
        elif (mod == "fsk"):
            self.ventana.changeWidget(self.ventana.ui.page_fsk)
            UIFunctionsHelp.labelTitle(self.ventana,'Ayuda FSK')
        elif (mod == "psk"):
            self.ventana.changeWidget(self.ventana.ui.page_psk)
            UIFunctionsHelp.labelTitle(self.ventana,'Ayuda PSK')
        elif (mod == "settings"):
            self.ventana.changeWidget(self.ventana.ui.page_settings)
            UIFunctionsHelp.labelTitle(self.ventana, 'Ayuda Ajustes')
        elif (mod == "main"):
            self.ventana.changeWidget(self.ventana.ui.page_main)
            UIFunctionsHelp.labelTitle(self.ventana, 'Manual de Usuario')
        self.ventana.show()
        
    ########################################################################
    ## END ==> HELP EVENTS
    ########################################################################

class HelpWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_helpWindow()
        self.ui.setupUi(self)
        # self.setWindowIcon(QtGui.QIcon('sigma-logo.ico'))

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctionsHelp.removeTitleBar(True)
        ## ==> END ##

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Manual de Usuario')
        UIFunctionsHelp.labelTitle(self, 'Manual de Usuario')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        # startSize = QSize(1000, 800)
        # self.resize(startSize)
        # self.setMinimumSize(startSize)
        # UIFunctionsHelp.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctionsHelp.uiDefinitions(self)
        ## ==> END ##

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_main))
        self.ui.btn_home.clicked.connect(lambda: UIFunctionsHelp.labelTitle(self, 'Manual de Usuario'))

        self.ui.btn_prev.clicked.connect(lambda: self.pageHandler(self.ui.stackedWidget.currentIndex(), -1))
        self.ui.btn_next.clicked.connect(lambda: self.pageHandler(self.ui.stackedWidget.currentIndex(), 1))

        self.show()

    def changeWidget(self, widget):
        self.ui.stackedWidget.setCurrentWidget(widget)

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    # def resizeEvent(self, event):
    #     self.resizeFunction()
    #     return super(MainWindow, self).resizeEvent(event)

    # def resizeFunction(self):
    #     print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##
    
    def pageHandler(self, index, offset):
        index += offset
        self.ui.stackedWidget.setCurrentIndex(index)
        print(self.ui.stackedWidget.currentIndex())
        if index == 0:
            UIFunctionsHelp.labelTitle(self, 'Manual de Usuario')
        elif index == 1:
            UIFunctionsHelp.labelTitle(self, 'Ayuda ASK')
        elif index == 2:
            UIFunctionsHelp.labelTitle(self, 'Ayuda FSK')
        elif index == 3:
            UIFunctionsHelp.labelTitle(self, 'Ayuda PSK')
        elif index == 4:
            UIFunctionsHelp.labelTitle(self, 'Ayuda Ajustes')

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Black.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Light.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Regular.ttf')
    window = MainWindow()
    sys.exit(app.exec_())