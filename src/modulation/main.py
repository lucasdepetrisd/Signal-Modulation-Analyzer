# GUI FILE
from ui_ComSysTrainerUI import Ui_ComSys
from matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
from PySide2.QtWidgets import *
import sys

#Telling windows to let me make my own taskbar icons
import ctypes
myappid = 'nexusteam.ComSysTrainer.gui.version1' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Libraries that do the heavy lifting
import numpy as np
from BGen import BinaryGenerator

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ComSys()
        self.ui.setupUi(self)
        
        # Connecting methods to Button clicks / Actions
        self.ui.modulateBtnAM.clicked.connect(lambda: self.modulateAM())
        self.ui.clearBtnAM.clicked.connect(lambda: self.clearAM())
        self.ui.modulateBtnFM.clicked.connect(lambda: self.modulateFM())
        self.ui.clearBtnFM.clicked.connect(lambda: self.clearFM())
        self.ui.modulateBtnASK.clicked.connect(lambda: self.modulateASK())
        self.ui.clearBtnASK.clicked.connect(lambda: self.clearASK())
        self.ui.modulateBtnFSK.clicked.connect(lambda: self.modulateFSK())
        self.ui.clearBtnFSK.clicked.connect(lambda: self.clearFSK())
        self.ui.modulateBtnPSK.clicked.connect(lambda: self.modulatePSK())
        self.ui.clearBtnPSK.clicked.connect(lambda: self.clearPSK())
        self.ui.modulateBtnPAM.clicked.connect(lambda: self.modulatePAM())
        self.ui.clearBtnPAM.clicked.connect(lambda: self.clearPAM())
        self.ui.modulateBtnPWM.clicked.connect(lambda: self.modulatePWM())
        self.ui.clearBtnPWM.clicked.connect(lambda: self.clearPWM())
        self.show()

        # Creating subplots and a blank canvas for AM
        self.ui.MplWidgetAM.canvas.ax3 = self.ui.MplWidgetAM.canvas.figure.add_subplot(313)
        self.ui.MplWidgetAM.canvas.ax1 = self.ui.MplWidgetAM.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetAM.canvas.ax3)
        self.ui.MplWidgetAM.canvas.ax2 = self.ui.MplWidgetAM.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetAM.canvas.ax3)
        self.ui.MplWidgetAM.canvas.ax1.set_xticks([])

        # Creating subplots and a blank canvas for FM
        self.ui.MplWidgetFM.canvas.ax3 = self.ui.MplWidgetFM.canvas.figure.add_subplot(313)
        self.ui.MplWidgetFM.canvas.ax1 = self.ui.MplWidgetFM.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetFM.canvas.ax3)
        self.ui.MplWidgetFM.canvas.ax2 = self.ui.MplWidgetFM.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetFM.canvas.ax3)
        self.ui.MplWidgetFM.canvas.ax1.set_xticks([])

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

        # Creating Subplots and a blank canvas for PAM
        self.ui.MplWidgetPAM.canvas.ax3 = self.ui.MplWidgetPAM.canvas.figure.add_subplot(313)
        self.ui.MplWidgetPAM.canvas.ax1 = self.ui.MplWidgetPAM.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetPAM.canvas.ax3)
        self.ui.MplWidgetPAM.canvas.ax2 = self.ui.MplWidgetPAM.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetPAM.canvas.ax3)
        self.ui.MplWidgetPAM.canvas.ax1.set_xticks([])

        # Creating Subplots and a blank canvas for PWM
        self.ui.MplWidgetPWM.canvas.ax3 = self.ui.MplWidgetPWM.canvas.figure.add_subplot(313)
        self.ui.MplWidgetPWM.canvas.ax1 = self.ui.MplWidgetPWM.canvas.figure.add_subplot(311,sharex = self.ui.MplWidgetPWM.canvas.ax3)
        self.ui.MplWidgetPWM.canvas.ax2 = self.ui.MplWidgetPWM.canvas.figure.add_subplot(312,sharex = self.ui.MplWidgetPWM.canvas.ax3)
        self.ui.MplWidgetPWM.canvas.ax1.set_xticks([])

        #Setting Matplotlib toolbars form the various MplWidgets used
        self.ui.AM_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetAM.canvas,self))
        self.ui.FM_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetFM.canvas,self))
        self.ui.ASK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetASK.canvas,self))
        self.ui.FSK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetFSK.canvas,self))
        self.ui.PSK_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetPSK.canvas,self))
        self.ui.PAM_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetPAM.canvas,self))
        self.ui.PWM_graph_layout.layout().addWidget(NavigationToolbar(self.ui.MplWidgetPWM.canvas,self))
        self.ui.MplWidgetAM.canvas.axes.set_visible(False)
        self.ui.MplWidgetFM.canvas.axes.set_visible(False)
        self.ui.MplWidgetASK.canvas.axes.set_visible(False)
        self.ui.MplWidgetFSK.canvas.axes.set_visible(False)
        self.ui.MplWidgetPSK.canvas.axes.set_visible(False)
        self.ui.MplWidgetPAM.canvas.axes.set_visible(False)
        self.ui.MplWidgetPWM.canvas.axes.set_visible(False)

    def clearAM(self):
        self.ui.MplWidgetAM.canvas.ax1.clear()
        self.ui.MplWidgetAM.canvas.ax2.clear()
        self.ui.MplWidgetAM.canvas.ax3.clear()
        self.ui.MplWidgetAM.canvas.draw()

    def modulateAM(self):
        fc = float(self.ui.carrierFreqInput.text().replace(',','.'))
        fm = float(self.ui.msgFreqInput.text().replace(',','.'))
        t  =  np .arange(44100.0)/44100.0

        ac = float(self.ui.carrierAmpInput.text().replace(',','.'))
        am = float(self.ui.msgAmpInput.text().replace(',','.'))
        mod_index = float(am/ac)

        message_signal  =  am*(np . cos( 2 * np . pi * fm * t ))
        carrier_signal  =  ac*(np . cos( 2 * np . pi * fc * t ))
        am_product = np.zeros_like(message_signal)

        for i,j in enumerate(t):
            am_product[i] = ac*(np.cos(2*np.pi*fc*j)+mod_index*(np.cos(2*np.pi*fm*j)*np.cos(2*np.pi*fc*j)))

        if self.ui.MplWidgetAM.canvas.ax1:
            self.ui.MplWidgetAM.canvas.ax2.set_visible(True)
            self.ui.MplWidgetAM.canvas.ax3.set_visible(True)
            self.ui.MplWidgetAM.canvas.ax1.set_visible(True)
            self.ui.MplWidgetAM.canvas.axes.set_visible(False)

        # Clear the previous plots if any
        self.ui.MplWidgetAM.canvas.axes.clear()
        
        # Plotting message signal
        self.ui.MplWidgetAM.canvas.ax1.clear()
        self.ui.MplWidgetAM.canvas.ax1.plot(t,message_signal,color='red',label=f'Moduladora\nAmp: {am} Frec: {fm} Hz')
        self.ui.MplWidgetAM.canvas.ax1.legend(loc = 'lower right')
        
        # Plotting carrier signal
        self.ui.MplWidgetAM.canvas.ax2.clear()
        self.ui.MplWidgetAM.canvas.ax2.plot(t,carrier_signal,color='blue',label=f'Portadora\nAmp: {ac} Frec: {fc} Hz')
        self.ui.MplWidgetAM.canvas.ax2.legend(loc = 'lower right')
        
        # Plotting AM modulated signal
        self.ui.MplWidgetAM.canvas.ax3.clear()
        self.ui.MplWidgetAM.canvas.ax3.plot(t,am_product,color='purple',label=f'VMax/Vmin = {ac+am}/{ac-am}')
        self.ui.MplWidgetAM.canvas.ax3.legend(loc = 'lower right')

        # Removing intermediate xtick labels for a cleaner plot
        self.ui.MplWidgetAM.canvas.ax1.tick_params(
                            axis='x',          # changes apply to the x-axis
                            which='both',      # both major and minor ticks are affected
                            bottom='on',      # ticks along the bottom edge are off
                            top='off',         # ticks along the top edge are off
                            labelbottom='off'  # labels along the bottom edge are off)
                        )
        self.ui.MplWidgetAM.canvas.ax2.tick_params(
                            axis='x',          
                            which='both',      
                            bottom='on',      
                            top='off',         
                            labelbottom='off'  
                        )

        # Set Title and Show Plot
        self.ui.MplWidgetAM.canvas.ax1.set_title(f'Señal AM')
        # self.ui.MplWidgetAM.canvas.ax1.set_title(f'Señal AM : Mod Index = {mod_index}')
        self.ui.MplWidgetAM.canvas.draw()

    def clearFM(self):
        self.ui.MplWidgetFM.canvas.ax1.clear()
        self.ui.MplWidgetFM.canvas.ax2.clear()
        self.ui.MplWidgetFM.canvas.ax3.clear()
        self.ui.MplWidgetFM.canvas.draw()

    def modulateFM(self):
        fc = float(self.ui.carrierFreqInputFM.text())
        fm = float(self.ui.msgFreqInputFM.text())
        mod_index = float(self.ui.modIndexInputFM.text())
        t  = np.arange(44100.0)/44100.0

        message_signalA = np.cos( 2 * np.pi * fm * t ) * mod_index
        message_signalB = np.cos( 2 * np.pi * fm * t )
        carrier_signal  = np.cos( 2 * np.pi * fc * t )

        del_f = mod_index * fm
        fm_product = np.zeros_like(message_signalA)

        for i,j in enumerate(t):
            fm_product[i] = np.cos(2 * np.pi * (fc * j + message_signalA[i]))
        
        if self.ui.MplWidgetFM.canvas.ax1:
            self.ui.MplWidgetFM.canvas.ax2.set_visible(True)
            self.ui.MplWidgetFM.canvas.ax3.set_visible(True)
            self.ui.MplWidgetFM.canvas.ax1.set_visible(True)
            self.ui.MplWidgetFM.canvas.axes.set_visible(False)
        
        # Clear the previous plots if any
        self.ui.MplWidgetFM.canvas.axes.clear()

        # Plotting message signal
        self.ui.MplWidgetFM.canvas.ax1.clear()
        self.ui.MplWidgetFM.canvas.ax1.plot(t,message_signalB,color='cyan',label=f'Message Freq: {fm} Hz')
        self.ui.MplWidgetFM.canvas.ax1.legend(loc = 'lower right')

        # Plotting carrier signal
        self.ui.MplWidgetFM.canvas.ax2.clear()
        self.ui.MplWidgetFM.canvas.ax2.plot(t,carrier_signal,color='lime',label=f'Carrier Freq: {fc} Hz')
        self.ui.MplWidgetFM.canvas.ax2.legend(loc = 'lower right')
        
        # Plotting FM modulated signal
        self.ui.MplWidgetFM.canvas.ax3.clear()
        self.ui.MplWidgetFM.canvas.ax3.plot(t,fm_product,color='orange',label=f'FM Signal \nDel F: {del_f} Hz')
        self.ui.MplWidgetFM.canvas.ax3.legend(loc = 'lower right')

        # Removing intermediate xtick labels for a cleaner plot
        self.ui.MplWidgetFM.canvas.ax1.tick_params(
                            axis='x',          # changes apply to the x-axis
                            which='both',      # both major and minor ticks are affected
                            bottom='on',      # ticks along the bottom edge are off
                            top='off',         # ticks along the top edge are off
                            labelbottom='off'  # labels along the bottom edge are off)
                        )
        self.ui.MplWidgetFM.canvas.ax2.tick_params(
                            axis='x',          
                            which='both',      
                            bottom='on',      
                            top='off',         
                            labelbottom='off'  
                        )
        
        # Set Title and Show Plot
        self.ui.MplWidgetFM.canvas.ax1.set_title(f'FM signal plot: mod Index = {mod_index}')
        self.ui.MplWidgetFM.canvas.draw()

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
        message = self.ui.messageInputASK.toPlainText()
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
        message = self.ui.messageInputFSK.toPlainText()
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
        message = self.ui.messageInputPSK.toPlainText()
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
    
    def clearPAM(self):
        self.ui.MplWidgetPAM.canvas.ax1.clear()
        self.ui.MplWidgetPAM.canvas.ax2.clear()
        self.ui.MplWidgetPAM.canvas.ax3.clear()
        self.ui.MplWidgetPAM.canvas.draw()

    def modulatePAM(self):
        Fm = int(float(self.ui.msgFreqInputPAM.text()))
        Am = float(self.ui.msgAmpInputPAM.text())
        Fs = 1000 * Fm
        t = np.arange(0, 1, 1/Fs)

        clock_signal = BinaryGenerator.generateClock(t,20)
        message_signal = Am * np.sin(2 * np.pi * Fm * t)
        pam_signal = np.array([clock_signal[i] if(clock_signal[i] == 0) else message_signal[i] for i in range(len(t))])

        if self.ui.MplWidgetPAM.canvas.ax1:
                self.ui.MplWidgetPAM.canvas.ax2.set_visible(True)
                self.ui.MplWidgetPAM.canvas.ax3.set_visible(True)
                self.ui.MplWidgetPAM.canvas.ax1.set_visible(True)
                self.ui.MplWidgetPAM.canvas.axes.set_visible(False)

        # Clear the previous plots if any
        self.ui.MplWidgetPAM.canvas.axes.clear()

        # Plotting data signal
        self.ui.MplWidgetPAM.canvas.ax1.clear()
        self.ui.MplWidgetPAM.canvas.ax1.plot(t,clock_signal,color='cyan',label=f'Impulse Signal')
        self.ui.MplWidgetPAM.canvas.ax1.legend(loc = 'lower right')

        # Plotting carrier signal
        self.ui.MplWidgetPAM.canvas.ax2.clear()
        self.ui.MplWidgetPAM.canvas.ax2.plot(t,message_signal,color='lime',label=f'Message Freq: {Fm} Hz\nMessage Amp.: {Am} V')
        self.ui.MplWidgetPAM.canvas.ax2.legend(loc = 'lower right')
            
        # Plotting PAM modulated signal
        self.ui.MplWidgetPAM.canvas.ax3.clear()
        self.ui.MplWidgetPAM.canvas.ax3.plot(t,pam_signal,color='orange',label=f'PAM Signal')
        self.ui.MplWidgetPAM.canvas.ax3.legend(loc = 'lower right')

        # Removing intermediate xtick labels for a cleaner plot
        self.ui.MplWidgetPAM.canvas.ax1.tick_params(
                            axis='x',          # changes apply to the x-axis
                            which='both',      # both major and minor ticks are affected
                            bottom='on',      # ticks along the bottom edge are off
                            top='off',         # ticks along the top edge are off
                            labelbottom='off'  # labels along the bottom edge are off)
                        )
        self.ui.MplWidgetPAM.canvas.ax2.tick_params(
                            axis='x',          
                            which='both',      
                            bottom='on',      
                            top='off',         
                            labelbottom='off'  
                        )
            
        # Set Title and Show Plot
        self.ui.MplWidgetPAM.canvas.ax1.set_title(f'PAM signal plot')
        self.ui.MplWidgetPAM.canvas.draw()
        
    def clearPWM(self):
        self.ui.MplWidgetPWM.canvas.ax1.clear()
        self.ui.MplWidgetPWM.canvas.ax2.clear()
        self.ui.MplWidgetPWM.canvas.ax3.clear()
        self.ui.MplWidgetPWM.canvas.draw()

    def modulatePWM(self):
        Fm = int(float(self.ui.msgFreqInputPWM.text()))
        Am = float(self.ui.msgAmpInputPWM.text())
        Fs = 1000 * Fm
        t = np.arange(0, 1, 1/Fs)
        swt_freq = Fm * 10

        sawtooth_signal = BinaryGenerator.generateSawtooth(t,swt_freq,Am)
        message_signal = Am * np.sin(2 * np.pi * Fm * t)
        pwm_signal = np.array([1 if(message_signal[i] >= sawtooth_signal[i]) else 0 for i in range(len(t))])

        if self.ui.MplWidgetPWM.canvas.ax1:
                self.ui.MplWidgetPWM.canvas.ax2.set_visible(True)
                self.ui.MplWidgetPWM.canvas.ax3.set_visible(True)
                self.ui.MplWidgetPWM.canvas.ax1.set_visible(True)
                self.ui.MplWidgetPWM.canvas.axes.set_visible(False)

        # Clear the previous plots if any
        self.ui.MplWidgetPWM.canvas.axes.clear()

        # Plotting sawtooth signal
        self.ui.MplWidgetPWM.canvas.ax1.clear()
        self.ui.MplWidgetPWM.canvas.ax1.plot(t,sawtooth_signal,color='cyan',label=f'Sawtooth Signal: \nFreq: {swt_freq} Hz')
        self.ui.MplWidgetPWM.canvas.ax1.legend(loc = 'lower right')

        # Plotting message signal
        self.ui.MplWidgetPWM.canvas.ax2.clear()
        self.ui.MplWidgetPWM.canvas.ax2.plot(t,message_signal,color='lime',label=f'Message Freq: {Fm} Hz\nMessage Amp.: {Am} V')
        self.ui.MplWidgetPWM.canvas.ax2.legend(loc = 'lower right')
            
        # Plotting PWM modulated signal
        self.ui.MplWidgetPWM.canvas.ax3.clear()
        self.ui.MplWidgetPWM.canvas.ax3.plot(t,pwm_signal,color='orange',label=f'PWM Signal')
        self.ui.MplWidgetPWM.canvas.ax3.legend(loc = 'lower right')

        # Removing intermediate xtick labels for a cleaner plot
        self.ui.MplWidgetPWM.canvas.ax1.tick_params(
                            axis='x',          # changes apply to the x-axis
                            which='both',      # both major and minor ticks are affected
                            bottom='on',      # ticks along the bottom edge are off
                            top='off',         # ticks along the top edge are off
                            labelbottom='off'  # labels along the bottom edge are off)
                        )
        self.ui.MplWidgetPWM.canvas.ax2.tick_params(
                            axis='x',          
                            which='both',      
                            bottom='on',      
                            top='off',         
                            labelbottom='off'  
                        )
            
        # Set Title and Show Plot
        self.ui.MplWidgetPWM.canvas.ax1.set_title(f'PWM signal plot')
        self.ui.MplWidgetPWM.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())