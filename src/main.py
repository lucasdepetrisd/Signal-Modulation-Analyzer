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
from PySide2 import QtCore, QtGui, QtWidgets
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
myappid = 'nexusteam.ComSysTrainer.gui.version1' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Libraries that do the heavy lifting
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        UIFunctions.addNewMenu(self, "INICIO", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "ASK", "btn_ASK", "url(:/16x16/icons/16x16/cil-ask.png)", True)
        UIFunctions.addNewMenu(self, "FSK", "btn_FSK", "url(:/16x16/icons/16x16/cil-fsk.png)", True)
        UIFunctions.addNewMenu(self, "PSK", "btn_PSK", "url(:/16x16/icons/16x16/cil-psk.png)", True)

        # UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        UIFunctions.labelPage(self, "INICIO")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "LD", "", True)
        UIFunctions.labelCredits(self, "Desarrollado por: Lucas Depetris")
        UIFunctions.labelVersion(self, "v0.5")
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

        self.ui.modulateBtnASK.clicked.connect(lambda: self.modulateASK())
        self.ui.clearBtnASK.clicked.connect(lambda: self.clearASK())
        self.ui.modulateBtnFSK.clicked.connect(lambda: self.modulateFSK())
        self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())
        self.ui.modulateBtnPSK.clicked.connect(lambda: self.modulatePSK())
        self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELOW                                               ##
        ########################################################################



        ## ==> QTableWidget PARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
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
        self.ui.MplWidgetFSK.canvas.ax4 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[2,:])
        self.ui.MplWidgetFSK.canvas.ax1 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[0,0],sharex = self.ui.MplWidgetFSK.canvas.ax4)
        self.ui.MplWidgetFSK.canvas.ax2 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[0,1],sharex = self.ui.MplWidgetFSK.canvas.ax4)
        self.ui.MplWidgetFSK.canvas.ax3 = self.ui.MplWidgetFSK.canvas.figure.add_subplot(gdspec_fsk[1,:],sharex = self.ui.MplWidgetFSK.canvas.ax4)
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
        if btnWidget.objectName() == "btn_ASK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ask)
            UIFunctions.resetStyle(self, "btn_ASK")
            UIFunctions.labelPage(self, "MODULACIÓN ASK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        # PAGE FSK
        if btnWidget.objectName() == "btn_FSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_fsk)
            UIFunctions.resetStyle(self, "btn_FSK")
            UIFunctions.labelPage(self, "MODULACIÓN FSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        # PAGE PSK
        if btnWidget.objectName() == "btn_PSK":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_psk)
            UIFunctions.resetStyle(self, "btn_PSK")
            UIFunctions.labelPage(self, "MODULACIÓN PSK")
            UIFunctions.labelDescription(self, 'Ingrese los valores de las señales')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

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
    def checkMessage(self,message: str, messagebox: QTextEdit):
        if((len(message) in [2**i for i in range(1,5)])):
            for bit in message:
                if(int(bit) not in [0,1]):
                    messagebox.setStyleSheet("border: 2px solid #ff0000;")
                    return False
            messagebox.setStyleSheet("border: 2px solid #00ff00;")
            return True
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
            Fs = 64 * Fc # Sampling freq must be >>> 2 * fc (Nyquist rate)
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
            self.ui.MplWidgetASK.canvas.ax1.plot(t,data_signal,color='red',label=f' Frecuencia: {Fs} Hz\nCadena: {message}')
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

            if self.ui.MplWidgetFSK.canvas.ax1:
                self.ui.MplWidgetFSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetFSK.canvas.axes.set_visible(False)

            # Clear the previous plots if any
            self.ui.MplWidgetFSK.canvas.axes.clear()

            # Plotting carrier signal 1
            self.ui.MplWidgetFSK.canvas.ax1.clear()
            self.ui.MplWidgetFSK.canvas.ax1.plot(t,carrier_signal_1,color='cyan',label=f'Carrier 1 \nFreq :{Fc1} Hz')
            self.ui.MplWidgetFSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal 2
            self.ui.MplWidgetFSK.canvas.ax2.clear()
            self.ui.MplWidgetFSK.canvas.ax2.plot(t,carrier_signal_2,color='skyblue',label=f'Carrier 2 \nFreq :{Fc2} Hz')
            self.ui.MplWidgetFSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting Data Signal
            self.ui.MplWidgetFSK.canvas.ax3.clear()
            self.ui.MplWidgetFSK.canvas.ax3.plot(t,data_signal,color='lime',label=f'Fs: {Fs} Hz\nMessage : {message}')
            self.ui.MplWidgetFSK.canvas.ax3.legend(loc = 'lower right')

            # Plotting FSK modulated signal
            self.ui.MplWidgetFSK.canvas.ax4.clear()
            self.ui.MplWidgetFSK.canvas.ax4.plot(t,fsk_signal,color='orange',label=f'FSK Signal \nFreq = {Fc1} Hz: Data(0)\nFreq = {Fc2} Hz: Data(1)')
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
            self.ui.MplWidgetFSK.canvas.figure.suptitle(f'FSK signal plot')
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
            self.ui.MplWidgetPSK.canvas.ax1.plot(t,data_signal,color='cyan',label=f'Sampling Freq: {Fs} Hz\n Message: {message}')
            self.ui.MplWidgetPSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal
            self.ui.MplWidgetPSK.canvas.ax2.clear()
            self.ui.MplWidgetPSK.canvas.ax2.plot(t,carrier_signal,color='lime',label=f'Carrier Freq: {Fc} Hz')
            self.ui.MplWidgetPSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal
            self.ui.MplWidgetPSK.canvas.ax3.clear()
            self.ui.MplWidgetPSK.canvas.ax3.plot(t,psk_signal,color='orange',label=f'PSK Signal')
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
            self.ui.MplWidgetPSK.canvas.ax1.set_title(f'PSK signal plot')
            self.ui.MplWidgetPSK.canvas.draw()

    ########################################################################
    ## END ==> MODULATION EVENTS
    ########################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Black.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Light.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Regular.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
