################################################################################
##
## SIGMA BY: LUCAS DEPETRIS
## BASED ON WANDERSON M. PIMENTA'S PROJECT AND COMSYS-TRAINER BY SOUMADIP DEY
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.2.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import numpy as np

# GUI FILE
from app_modules import *

# MODULATIONS
from matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import modulation.modulation as mod
import modulation.animation as anim

# SETTINGS FILE MANAGER
import json
from pathlib import Path

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
        self.ui.stackedWidgetASK.setCurrentIndex(0)
        self.ui.stackedWidgetFSK.setCurrentIndex(0)
        self.ui.stackedWidgetPSK.setCurrentIndex(0)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "LD", "url(:/24x24/icons/24x24/sigma-logo.png)", True)
        UIFunctions.labelCredits(self, "Desarrollado por: Lucas Depetris")
        UIFunctions.labelVersion(self, "v1.2")
        ## ==> END ##

        self.animASK = anim.ASKPlotter(self.ui.PyQtGraphASK, self.ui.velocidadInputASK, self.ui.samplesInputASK)
        self.animFSK = anim.FSKPlotter(self.ui.PyQtGraphFSK, self.ui.velocidadInputFSK, self.ui.samplesInputFSK)
        self.animPSK = anim.PSKPlotter(self.ui.PyQtGraphPSK, self.ui.velocidadInputPSK, self.ui.samplesInputPSK)

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
        self.ui.Btn_pauseASK.clicked.connect(lambda: self.animASK.switchPause())
        # ASK PLOT CONNECTORS
        self.ui.Btn_antialiasASK.clicked.connect(lambda: self.animASK.setAntialising(self.ui.Btn_antialiasASK.isChecked()))
        self.ui.Btn_autoajustadoASK.clicked.connect(lambda: self.animASK.adjustPlot())
        self.ui.velocidadInputASK.valueChanged.connect(lambda: self.animASK.setSpeed(int(self.ui.velocidadInputASK.text())))
        self.ui.samplesInputASK.valueChanged.connect(lambda: self.animASK.samplesChanged())

        # FSK MODULATION CONNECTORS
        self.ui.messageInputFSK.textChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq1InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.carrierFreq2InputFSK.valueChanged.connect(lambda: self.modulateFSK())
        self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())
        # FSK ANIMATION CONNECTORS
        self.ui.modulateBtnFSK.clicked.connect(lambda: self.animateModulation("fsk"))
        self.ui.Btn_pauseFSK.clicked.connect(lambda: self.animFSK.switchPause())
        # FSK PLOT CONNECTORS
        self.ui.Btn_antialiasFSK.clicked.connect(lambda: self.animFSK.setAntialising(self.ui.Btn_antialiasFSK.isChecked()))
        self.ui.Btn_autoajustadoFSK.clicked.connect(lambda: self.animFSK.adjustPlot())
        self.ui.velocidadInputFSK.valueChanged.connect(lambda: self.animFSK.setSpeed(int(self.ui.velocidadInputFSK.text())))
        self.ui.samplesInputFSK.valueChanged.connect(lambda: self.animFSK.setSamples(int(self.ui.samplesInputFSK.text())))

        # PSK MODULATION CONNECTORS
        self.ui.messageInputPSK.textChanged.connect(lambda: self.modulatePSK())
        self.ui.carrierFreqInputPSK.valueChanged.connect(lambda: self.modulatePSK())
        self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())
        # PSK ANIMATION CONNECTORS
        self.ui.modulateBtnPSK.clicked.connect(lambda: self.animateModulation("psk"))
        self.ui.Btn_pausePSK.clicked.connect(lambda: self.animPSK.switchPause())
        # PSK PLOT CONNECTORS
        self.ui.Btn_antialiasPSK.clicked.connect(lambda: self.animPSK.setAntialising(self.ui.Btn_antialiasPSK.isChecked()))
        self.ui.Btn_autoajustadoPSK.clicked.connect(lambda: self.animPSK.adjustPlot())
        self.ui.velocidadInputPSK.valueChanged.connect(lambda: self.animPSK.setSpeed(int(self.ui.velocidadInputPSK.text())))
        self.ui.samplesInputPSK.valueChanged.connect(lambda: self.animPSK.setSamples(int(self.ui.samplesInputPSK.text())))

        self.ui.Btn_helpASK.clicked.connect(lambda: self.helpPage("ask"))
        self.ui.Btn_helpFSK.clicked.connect(lambda: self.helpPage("fsk"))
        self.ui.Btn_helpPSK.clicked.connect(lambda: self.helpPage("psk"))
        self.ui.Btn_helpSettings.clicked.connect(lambda: self.helpPage("settings"))
        self.ui.Btn_helpMain.clicked.connect(lambda: self.helpPage("main"))

        self.ui.Btn_ASK.clicked.connect(self.Button)
        self.ui.Btn_FSK.clicked.connect(self.Button)
        self.ui.Btn_PSK.clicked.connect(self.Button)
        
        # SETTINGS
        self.ui.btn_AplicarASK.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierASK, self.ui.minCarrierASK, self.ui.sliderASK, self.ui.carrierFreqInputASK, self.ui.label_maxASK, self.ui.label_minASK))
        self.ui.btn_AplicarFSK1.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierFSK1, self.ui.minCarrierFSK1, self.ui.sliderFSK1, self.ui.carrierFreq1InputFSK, self.ui.label_maxFSK_1, self.ui.label_minFSK_1))
        self.ui.btn_AplicarFSK2.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierFSK2, self.ui.minCarrierFSK2, self.ui.sliderFSK2, self.ui.carrierFreq2InputFSK, self.ui.label_maxFSK_2, self.ui.label_minFSK_2))
        self.ui.btn_AplicarPSK.clicked.connect(lambda: self.settingsChanged(self.ui.maxCarrierPSK, self.ui.minCarrierPSK, self.ui.sliderPSK, self.ui.carrierFreqInputPSK, self.ui.label_maxPSK, self.ui.label_minPSK))

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

        #TODO: ADD FSK PSK
        self.ui.mplask.layout().addWidget(NavigationToolbar(self.ui.MplWidgetASK.canvas,self))
        self.ui.mplfsk.layout().addWidget(NavigationToolbar(self.ui.MplWidgetFSK.canvas,self))
        self.ui.mplpsk.layout().addWidget(NavigationToolbar(self.ui.MplWidgetPSK.canvas,self))

        self.ui.MplWidgetASK.canvas.axes.set_visible(False)
        self.ui.MplWidgetFSK.canvas.axes.set_visible(False)
        self.ui.MplWidgetPSK.canvas.axes.set_visible(False)

        ## END ==> SUBPLOTS FUNCTIONS

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        ## INITIALIZE SETTINGS
        self.loadSettings()

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
        self.animASK.stop()
        self.animFSK.stop()
        self.animPSK.stop()

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
    #TODO: SAVE ONLY CHANGED
    def settingsChanged(self, inputMax: QSpinBox, inputMin: QSpinBox, slider: QSlider, input: QSpinBox, labelMax: QLabel, labelMin: QLabel):
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
            self.saveSettings()
        else:
            inputMax.setStyleSheet(Style.style_spinbox_error)
            inputMin.setStyleSheet(Style.style_spinbox_error)
            # print("No se puede cambiar: MaxAct={0} MaxIng={1}".format())

    def saveSettings(self):
        print("saving")
        settings_json = {'maxASK' : self.ui.maxCarrierASK.value(),
                    'minASK' : self.ui.minCarrierASK.value(),
                    'maxFSK1' : self.ui.maxCarrierFSK1.value(),
                    'minFSK1' : self.ui.minCarrierFSK1.value(),
                    'maxFSK2' : self.ui.maxCarrierFSK2.value(),
                    'minFSK2' : self.ui.minCarrierFSK2.value(),
                    'maxPSK' : self.ui.maxCarrierPSK.value(),
                    'minPSK' : self.ui.minCarrierPSK.value()
                    }
        with open('settingSIGMA.json','w+') as fp:
            fp.seek(0)
            json.dump(settings_json, fp)#, indent=4)
            # fp.write(json.dumps(settings_json))

    def loadSettings(self):
        settingsFile = "./settingSIGMA.json"
        path = Path(settingsFile)
        if path.is_file():
            print("existe el archivo")
            if path.stat().st_size != 0:
                print("cargando archivo...")
                with open(settingsFile,'r') as json_file:
                    settings_json = json.load(json_file)

                self.ui.maxCarrierASK.setValue(settings_json["maxASK"])
                self.ui.minCarrierASK.setValue(settings_json["minASK"])
                self.ui.maxCarrierFSK1.setValue(settings_json["maxFSK1"])
                self.ui.minCarrierFSK1.setValue(settings_json["minFSK1"])
                self.ui.maxCarrierFSK2.setValue(settings_json["maxFSK2"])
                self.ui.minCarrierFSK2.setValue(settings_json["minFSK2"])
                self.ui.maxCarrierPSK.setValue(settings_json["maxPSK"])
                self.ui.minCarrierPSK.setValue(settings_json["minPSK"])

                self.ui.btn_AplicarASK.click()
                self.ui.btn_AplicarFSK1.click()
                self.ui.btn_AplicarFSK2.click()
                self.ui.btn_AplicarPSK.click()
            else:
                print("archivo vacio")
        else:
            print("no existe el archivo")
        

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
        if self.animASK.running:
            self.animASK.stop()
        if self.animFSK.running:
            self.animFSK.stop()
        if self.animPSK.running:
            self.animPSK.stop()
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START ==> MODULATION EVENTS
    ########################################################################

    def checkMessage(self, messagebox: QTextEdit, label: QLabel, button: QPushButton):
        message = messagebox.text()
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
        self.ui.MplWidgetASK.canvas.ax1.clear()
        self.ui.MplWidgetASK.canvas.ax2.clear()
        self.ui.MplWidgetASK.canvas.ax3.clear()
        self.ui.MplWidgetASK.canvas.axes.clear()
        self.ui.MplWidgetASK.canvas.draw()
        self.animASK.clearPlots()
        
    def modulateASK(self):
        self.ui.stackedWidgetASK.setCurrentIndex(0)
        message = self.ui.messageInputASK.text()
        Fc = int(float(self.ui.carrierFreqInputASK.text()))

        if self.checkMessage(self.ui.messageInputASK, self.ui.labelASK, self.ui.clearBtnASK):
            data_signal, carrier_signal, ask_signal, t, Fs, bandWidth = mod.modulateASK(message, Fc)

            if self.ui.MplWidgetASK.canvas.ax1:
                self.ui.MplWidgetASK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetASK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetASK.canvas.axes.set_visible(False)

            # Plotting data signal and asigning line
            self.ui.MplWidgetASK.canvas.ax1.clear()
            self.ui.MplWidgetASK.canvas.ax1.plot(t,data_signal,color='red',label=f'Frec Muestreo = {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetASK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal and asigning line
            self.ui.MplWidgetASK.canvas.ax2.clear()
            self.ui.MplWidgetASK.canvas.ax2.plot(t,carrier_signal,color='blue',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetASK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal and asigning line
            self.ui.MplWidgetASK.canvas.ax3.clear()
            self.ui.MplWidgetASK.canvas.ax3.plot(t,ask_signal,color='purple',label=f'Señal ASK\n(0): Frec = 0 Hz\n(1): Frec = {Fc} Hz\nAB = {bandWidth} Hz')
            self.ui.MplWidgetASK.canvas.ax3.legend(loc = 'lower right')

            # line.set_antialiased(False)

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
            self.ui.MplWidgetASK.canvas.ax3.tick_params(
                                axis='x',          
                                which='both',      
                                bottom='on',      
                                top='off',         
                                labelbottom='off'  
                            )
            
            # Set Title and Show Plot
            self.ui.MplWidgetASK.canvas.ax1.set_title(f'Señal ASK')
            self.ui.MplWidgetASK.canvas.axes.plot(linewidth=7.0)
            self.ui.MplWidgetASK.canvas.draw()
    
    def clearFSK(self):
        self.ui.MplWidgetFSK.canvas.ax1.clear()
        self.ui.MplWidgetFSK.canvas.ax2.clear()
        self.ui.MplWidgetFSK.canvas.ax3.clear()
        self.ui.MplWidgetFSK.canvas.ax4.clear()
        self.ui.MplWidgetFSK.canvas.axes.clear()
        self.ui.MplWidgetFSK.canvas.draw()
        self.animFSK.clearPlots()
        
    def modulateFSK(self):
        self.ui.stackedWidgetFSK.setCurrentIndex(0)
        message = self.ui.messageInputFSK.text()
        Fc1 = int(float(self.ui.carrierFreq1InputFSK.text()))
        Fc2 = int(float(self.ui.carrierFreq2InputFSK.text()))

        if self.checkMessage(self.ui.messageInputFSK, self.ui.labelFSK, self.ui.clearBtnFSK):
            data_signal, carrier_signal_1, carrier_signal_2, fsk_signal, t, Fs, bandWidth = mod.modulateFSK(message, Fc1, Fc2)

            if self.ui.MplWidgetFSK.canvas.ax1:
                self.ui.MplWidgetFSK.canvas.ax2.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax3.set_visible(True)
                self.ui.MplWidgetFSK.canvas.ax1.set_visible(True)
                self.ui.MplWidgetFSK.canvas.axes.set_visible(False)

            self.ui.MplWidgetFSK.canvas.axes.clear()

            # Plotting carrier signal 1 and asigning line
            self.ui.MplWidgetFSK.canvas.ax1.clear()
            lin1, = self.ui.MplWidgetFSK.canvas.ax1.plot(t,carrier_signal_1,color='green',label=f'Señal 1 \nFrecuencia: {Fc1} Hz')
            self.ui.MplWidgetFSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal 2 and asigning line
            self.ui.MplWidgetFSK.canvas.ax2.clear()
            lin2, = self.ui.MplWidgetFSK.canvas.ax2.plot(t,carrier_signal_2,color='lime',label=f'Señal 2 \nFrecuencia:{Fc2} Hz')
            self.ui.MplWidgetFSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting Data Signal and asigning line
            self.ui.MplWidgetFSK.canvas.ax3.clear()
            lin3, = self.ui.MplWidgetFSK.canvas.ax3.plot(t,data_signal,color='red',label=f'Frec de Muestreo: {Fs} Hz\nBits : {message}')
            self.ui.MplWidgetFSK.canvas.ax3.legend(loc = 'lower right')

            # Plotting FSK modulated signal and asigning line
            self.ui.MplWidgetFSK.canvas.ax4.clear()
            lin4, = self.ui.MplWidgetFSK.canvas.ax4.plot(t,fsk_signal,color='darkorange',label=f'Señal FSK \n(0): Frec = {Fc1} Hz\n(1): Frec = {Fc2} Hz\nAB = {bandWidth} Hz')
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
        self.ui.MplWidgetPSK.canvas.axes.clear()
        self.ui.MplWidgetPSK.canvas.draw()
        self.animPSK.clearPlots()

    def modulatePSK(self):
        self.ui.stackedWidgetPSK.setCurrentIndex(0)
        message = self.ui.messageInputPSK.text()
        Fc = int(float(self.ui.carrierFreqInputPSK.text()))

        if self.checkMessage(self.ui.messageInputPSK, self.ui.labelPSK, self.ui.clearBtnPSK):
            data_signal, carrier_signal, psk_signal, t, Fs, bandWidth = mod.modulatePSK(message, Fc)

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
            self.ui.MplWidgetPSK.canvas.ax1.plot(t,data_signal,color='red',label=f'Frec de Muestreo: {Fs} Hz\nBits: {message}')
            self.ui.MplWidgetPSK.canvas.ax1.legend(loc = 'lower right')

            # Plotting carrier signal and asigning line
            self.ui.MplWidgetPSK.canvas.ax2.clear()
            self.ui.MplWidgetPSK.canvas.ax2.plot(t,carrier_signal,color='yellow',label=f'Frecuencia Portadora: {Fc} Hz')
            self.ui.MplWidgetPSK.canvas.ax2.legend(loc = 'lower right')
            
            # Plotting ASK modulated signal and asigning line
            self.ui.MplWidgetPSK.canvas.ax3.clear()
            self.ui.MplWidgetPSK.canvas.ax3.plot(t,psk_signal,color='darkorange',label=f'Señal PSK\nAB = {bandWidth} Hz')
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
    ## START ==> ANIMATION EVENTS
    ########################################################################

    def animateModulation(self, modt="nofsk"):
        if self.animASK.running == True:
            self.animASK.stop()
        if self.animFSK.running == True:
            self.animFSK.stop()
        if self.animPSK.running == True:
            self.animPSK.stop()

        if(modt == "ask"):
            self.ui.stackedWidgetASK.setCurrentIndex(1)
            self.animASK.loadData(self.ui.messageInputASK.text(), int(float(self.ui.carrierFreqInputASK.text())))
            self.animASK.start()
        elif(modt == "fsk"):
            self.ui.stackedWidgetFSK.setCurrentIndex(1)
            self.animFSK.loadData(self.ui.messageInputFSK.text(), int(float(self.ui.carrierFreq1InputFSK.text())), int(float(self.ui.carrierFreq2InputFSK.text())))
            self.animFSK.start()
        elif(modt == "psk"):
            self.ui.stackedWidgetPSK.setCurrentIndex(1)
            self.animPSK.loadData(self.ui.messageInputPSK.text(), int(float(self.ui.carrierFreqInputPSK.text())))
            self.animPSK.start()

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
        # print(self.ui.stackedWidget.currentIndex())
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
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Light.ttf')
    QtGui.QFontDatabase.addApplicationFont('./ui/fonts/Satoshi-Regular.ttf')
    app.setFont("Segoe UI", "*")
    window = MainWindow()
    sys.exit(app.exec_())