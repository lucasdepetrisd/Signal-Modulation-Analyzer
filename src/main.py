################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
## EDITED BY: LUCAS DEPETRIS
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets, QtTest
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *

# MODULATIONS
from matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
from PySide2.QtWidgets import *
import sys

# Telling windows to let me make my own taskbar icons
import ctypes
myappid = 'lucasdepetris.SigMA.gui.v1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Libraries that do the heavy lifting
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('sigma-logo.ico'))

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
        UIFunctions.labelVersion(self, "v0.9")
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

        # self.ui.modulateBtnASK.clicked.connect(lambda: self.modulateASK())
        self.ui.messageInputASK.textChanged.connect(lambda: self.modulateASK())
        self.ui.carrierFreqInputASK.valueChanged.connect(lambda: self.modulateASK())
        self.ui.clearBtnASK.clicked.connect(lambda: self.clearASK())

        # self.ui.modulateBtnFSK.clicked.connect(lambda: self.modulateFSK())
        self.ui.messageInputFSK.textChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq1InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq2InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())

        # self.ui.modulateBtnPSK.clicked.connect(lambda: self.modulatePSK())
        self.ui.messageInputPSK.textChanged.connect(lambda: self.modulatePSK())
        self.ui.carrierFreqInputPSK.valueChanged.connect(lambda: self.modulatePSK())
        self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())

        self.ui.Btn_helpASK.clicked.connect(lambda: self.helpPage("ask"))
        self.ui.Btn_helpFSK.clicked.connect(lambda: self.helpPage("fsk"))
        self.ui.Btn_helpPSK.clicked.connect(lambda: self.helpPage("psk"))
        self.ui.Btn_helpSettings.clicked.connect(lambda: self.helpPage("settings"))

        self.ui.Btn_ASK.clicked.connect(self.Button)
        self.ui.Btn_FSK.clicked.connect(self.Button)
        self.ui.Btn_PSK.clicked.connect(self.Button)
        
        self.ui.maxCarrierASK.valueChanged.connect(lambda: self.valueChanged("askmax", self.ui.maxCarrierASK.value()))
        self.ui.minCarrierASK.valueChanged.connect(lambda: self.valueChanged("askmin", self.ui.minCarrierASK.value()))
        
        self.ui.maxCarrierFSK1.valueChanged.connect(lambda: self.valueChanged("fsk1max", self.ui.maxCarrierFSK1.value()))
        self.ui.minCarrierFSK1.valueChanged.connect(lambda: self.valueChanged("fsk1min", self.ui.minCarrierFSK1.value()))
        self.ui.maxCarrierFSK2.valueChanged.connect(lambda: self.valueChanged("fsk2max", self.ui.maxCarrierFSK2.value()))
        self.ui.minCarrierFSK2.valueChanged.connect(lambda: self.valueChanged("fsk2min", self.ui.minCarrierFSK2.value()))

        self.ui.maxCarrierPSK.valueChanged.connect(lambda: self.valueChanged("pskmax", self.ui.maxCarrierPSK.value()))
        self.ui.minCarrierPSK.valueChanged.connect(lambda: self.valueChanged("pskmin", self.ui.minCarrierPSK.value()))
        
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
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        # PAGE FSK
        if btnWidget.objectName() == "btn_FSK" or btnWidget.objectName() == "Btn_FSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_fsk)
            UIFunctions.resetStyle(self, "btn_FSK")
            UIFunctions.labelPage(self, "MODULACIÓN FSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        # PAGE PSK
        if btnWidget.objectName() == "btn_PSK" or btnWidget.objectName() == "Btn_PSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_psk)
            UIFunctions.resetStyle(self, "btn_PSK")
            UIFunctions.labelPage(self, "MODULACIÓN PSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

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
    def valueChanged(self, mod, value):
        if (mod == "askmax"):
            if (self.ui.carrierFreqInputASK.minimum() > value) :
                self.ui.maxCarrierASK.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreqInputASK.maximum(),value))
            else:
                self.ui.maxCarrierASK.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreqInputASK.setMaximum(value)
                self.ui.sliderASK.setMaximum(value)
        elif (mod == "askmin"):
            if (self.ui.carrierFreqInputASK.maximum() < value) :
                self.ui.minCarrierASK.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreqInputASK.minimum(),value))
            else:
                self.ui.minCarrierASK.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreqInputASK.setMinimum(value)
                self.ui.sliderASK.setMinimum(value)
        elif (mod == "fsk1max"):
            if (self.ui.carrierFreq1InputFSK.minimum() > value) :
                self.ui.maxCarrierFSK1.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreq1InputFSK.maximum(),value))
            else:
                self.ui.maxCarrierFSK1.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreq1InputFSK.setMaximum(value)
                self.ui.sliderFSK1.setMaximum(value)
        elif (mod == "fsk1min"):
            if (self.ui.carrierFreq1InputFSK.maximum() < value) :
                self.ui.minCarrierFSK1.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreq1InputFSK.minimum(),value))
            else:
                self.ui.minCarrierFSK1.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreq1InputFSK.setMinimum(value)
                self.ui.sliderFSK1.setMinimum(value)
        elif (mod == "fsk2max"):
            if (self.ui.carrierFreq2InputFSK.minimum() > value) :
                self.ui.maxCarrierFSK2.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreq2InputFSK.maximum(),value))
            else:
                self.ui.maxCarrierFSK2.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreq2InputFSK.setMaximum(value)
                self.ui.sliderFSK2.setMaximum(value)
        elif (mod == "fsk2min"):
            if (self.ui.carrierFreq2InputFSK.maximum() < value) :
                self.ui.minCarrierFSK2.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreq2InputFSK.minimum(),value))
            else:
                self.ui.minCarrierFSK2.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreq2InputFSK.setMinimum(value)
                self.ui.sliderFSK2.setMinimum(value)
        elif (mod == "pskmax"):
            if (self.ui.carrierFreqInputPSK.minimum() > value) :
                self.ui.maxCarrierPSK.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MaxAct={0} MaxIng={1}".format(self.ui.carrierFreqInputPSK.maximum(),value))
            else:
                self.ui.maxCarrierPSK.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreqInputPSK.setMaximum(value)
                self.ui.sliderPSK.setMaximum(value)
        elif (mod == "pskmin"):
            if (self.ui.carrierFreqInputPSK.maximum() < value) :
                self.ui.maxCarrierPSK.setStyleSheet("border: 2px solid #ff0000;")
                print("No se puede cambiar: MinAct={0} MinIng={1}".format(self.ui.carrierFreqInputPSK.minimum(),value))
            else:
                self.ui.maxCarrierPSK.setStyleSheet("border: 2px solid #098c04;")
                self.ui.carrierFreqInputPSK.setMinimum(value)
                self.ui.sliderPSK.setMinimum(value)

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

    def checkMessage(self, message: str, messagebox: QTextEdit):
        if((len(message) in [2**i for i in range(1,6)])):
            for bit in message:
                if(int(bit) not in [0,1]):
                    messagebox.setStyleSheet("border: 2px solid #ff0000;")
                    self.ui.clearBtnASK.click()
                    self.ui.clearBtnFSK.click()
                    self.ui.clearBtnPSK.click()
                    return False
            messagebox.setStyleSheet("border: 2px solid #00ff00;")
            return True
        self.ui.clearBtnASK.click()
        self.ui.clearBtnFSK.click()
        self.ui.clearBtnPSK.click()
        messagebox.setStyleSheet("border: 2px solid #ff0000;")
        return False
    
    def clearASK(self):
        self.ui.MplWidgetASK.canvas.ax1.clear()
        self.ui.MplWidgetASK.canvas.ax2.clear()
        self.ui.MplWidgetASK.canvas.ax3.clear()
        self.ui.MplWidgetASK.canvas.draw()
        
    def modulateASK(self):
        message = self.ui.messageInputASK.text()
        if(self.checkMessage(message,self.ui.messageInputASK)):
            
            Fc = int(float(self.ui.carrierFreqInputASK.text()))
            Fs = 1000 * Fc # Sampling freq must be >>> 2 * fc (Nyquist rate)
            Fs = Fs + (Fs % len(message))
            t = np.arange(0,1,1/Fs)
            samples = Fs // len(message)

            BG = BinaryGenerator(message,samples)

            data_signal = BG.generate()
            carrier_signal = np.cos(2 * np.pi * Fc * t)
            ask_signal = carrier_signal * data_signal

            if self.ui.MplWidgetASK.canvas.ax1:
                self.ui.MplWidgetASK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetASK.canvas.axes.set_visible(False)

            # Clear the previous plots if any
            self.ui.MplWidgetASK.canvas.axes.clear()

            # Plotting data signal
            self.ui.MplWidgetASK.canvas.ax1.clear()
            self.ui.MplWidgetASK.canvas.ax1.plot(t,data_signal,color='red',label=f'Frecuencia: {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetASK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal
            self.ui.MplWidgetASK.canvas.ax2.clear()
            self.ui.MplWidgetASK.canvas.ax2.plot(t,carrier_signal,color='blue',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetASK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal
            self.ui.MplWidgetASK.canvas.ax3.clear()
            self.ui.MplWidgetASK.canvas.ax3.plot(t,ask_signal,color='purple',label=f'Señal ASK\n(0): Frec = 0 Hz\n(1): Frec = {Fc} Hz')
            self.ui.MplWidgetASK.canvas.ax3.legend(loc = 'lower right')

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
    
    def clearFSK(self):
        self.ui.MplWidgetFSK.canvas.ax1.clear()
        self.ui.MplWidgetFSK.canvas.ax2.clear()
        self.ui.MplWidgetFSK.canvas.ax3.clear()
        self.ui.MplWidgetFSK.canvas.ax4.clear()
        self.ui.MplWidgetFSK.canvas.draw()
        
    def modulateFSK(self):
        message = self.ui.messageInputFSK.text()
        if(self.checkMessage(message,self.ui.messageInputFSK)):
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
            
            fsk_signal = (carrier_signal_2 * data_signal) + (carrier_signal_1 * data_signal_inverse)

            bandWidth = (2*len(message))+(2*abs(Fc2-Fc1))
            self.ui.label_resultFSK.setText(str.format("{0} Hz", bandWidth))

            if self.ui.MplWidgetFSK.canvas.ax1:
                self.ui.MplWidgetFSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetFSK.canvas.axes.set_visible(False)

            # Clear the previous plots if any
            self.ui.MplWidgetFSK.canvas.axes.clear()

            # Plotting carrier signal 1
            self.ui.MplWidgetFSK.canvas.ax1.clear()
            self.ui.MplWidgetFSK.canvas.ax1.plot(t,carrier_signal_1,color='cyan',label=f'Señal 1 \nFrecuencia: {Fc1} Hz')
            self.ui.MplWidgetFSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal 2
            self.ui.MplWidgetFSK.canvas.ax2.clear()
            self.ui.MplWidgetFSK.canvas.ax2.plot(t,carrier_signal_2,color='pink',label=f'Señal 2 \nFrecuencia:{Fc2} Hz')
            self.ui.MplWidgetFSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting Data Signal
            self.ui.MplWidgetFSK.canvas.ax3.clear()
            self.ui.MplWidgetFSK.canvas.ax3.plot(t,data_signal,color='lime',label=f'Frec de Muestreo: {Fs} Hz\nBits : {message}')
            self.ui.MplWidgetFSK.canvas.ax3.legend(loc = 'lower right')

            # Plotting FSK modulated signal
            self.ui.MplWidgetFSK.canvas.ax4.clear()
            self.ui.MplWidgetFSK.canvas.ax4.plot(t,fsk_signal,color='orange',label=f'Señal FSK \n(0): Frec = {Fc1} Hz\n(1): Frec = {Fc2} Hz')
            self.ui.MplWidgetFSK.canvas.ax4.legend(loc = 'lower right')

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
            
    def clearPSK(self):
        self.ui.MplWidgetPSK.canvas.ax1.clear()
        self.ui.MplWidgetPSK.canvas.ax2.clear()
        self.ui.MplWidgetPSK.canvas.ax3.clear()
        self.ui.MplWidgetPSK.canvas.draw()

    def modulatePSK(self):
        message = self.ui.messageInputPSK.text()
        if(self.checkMessage(message,self.ui.messageInputPSK)):
            Fc = int(float(self.ui.carrierFreqInputPSK.text()))
            Fs = len(message) * 1000
            t = np.arange(0, 1, 1/Fs)
            samples = len(t) // len(message)
            
            BG = BinaryGenerator(message,samples)

            data_signal = BG.generateBipolar()
            carrier_signal = np.sin(2 * np.pi * Fc * t)
            psk_signal = data_signal * carrier_signal

            if self.ui.MplWidgetPSK.canvas.ax1:
                self.ui.MplWidgetPSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetPSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetPSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetPSK.canvas.axes.set_visible(False)

            # Clear the previous plots if any
            self.ui.MplWidgetPSK.canvas.axes.clear()

            # Plotting data signal
            self.ui.MplWidgetPSK.canvas.ax1.clear()
            self.ui.MplWidgetPSK.canvas.ax1.plot(t,data_signal,color='cyan',label=f'Frec de Muestreo: {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetPSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal
            self.ui.MplWidgetPSK.canvas.ax2.clear()
            self.ui.MplWidgetPSK.canvas.ax2.plot(t,carrier_signal,color='lime',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetPSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal
            self.ui.MplWidgetPSK.canvas.ax3.clear()
            self.ui.MplWidgetPSK.canvas.ax3.plot(t,psk_signal,color='orange',label=f'Señal PSK')
            self.ui.MplWidgetPSK.canvas.ax3.legend(loc = 'lower right')

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

    ########################################################################
    ## END ==> MODULATION EVENTS
    ########################################################################

    ########################################################################
    ## START ==> HELP EVENTS
    ########################################################################

    def helpPage(self, mod):
        if (mod == "ask"):
            self.ventana.changeWidget(self.ventana.ui.page_ask)
        elif (mod == "fsk"):
            self.ventana.changeWidget(self.ventana.ui.page_fsk)
        elif (mod == "psk"):
            self.ventana.changeWidget(self.ventana.ui.page_psk)
        elif (mod == "settings"):
            self.ventana.changeWidget(self.ventana.ui.page_settings)
        self.ventana.show()
        
    ########################################################################
    ## END ==> HELP EVENTS
    ########################################################################

class HelpWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_helpWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('sigma-logo.ico'))

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctionsHelp.removeTitleBar(True)
        ## ==> END ##

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Ayuda')
        UIFunctionsHelp.labelTitle(self, 'Ayuda')
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