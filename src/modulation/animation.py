# ------------------------------------------------------
# -------------------- animation.py --------------------
# ------------------------------------------------------
# PyQtGraph Libraries
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

#Libraries that do the heavy lifting
from main import *
# import numpy as np
# import modulation.modulation as mod

#Timer FPS
from time import perf_counter

class DynPlotter:
    
    def __init__(self, win, speedBox: QtWidgets.QSpinBox, samplesBox: QtWidgets.QSpinBox):        
        # Attributes Declarations
        self.running = False
        self.antiAliasing = False
        
        self.step = 1
        self.speed = 1
        self.totalSpeed = 1000
        self.speedPercent = 0
        self.speedBox = speedBox

        self.samples = 0
        self.totalSamples = 0
        self.samplesPercent = 0
        self.samplesBox = samplesBox

        self.counter = 0
        self.axisOffset = 0
        
        self.plotList = []
        self.dataList = []
        self.curveList = [None] * 3
                
        self.samplesText = ""
        self.warnText = ""
        
        self.brcount = 0
        self.lastUpdate = perf_counter()
        self.avgFps = 0.0

        pg.setConfigOptions(antialias = False)

        self.win = win
        self.win.clear()

        self.labelTitle = pg.LabelItem(justify='center')
        self.labelTitle.setText("Modulación", color='#ffffff', size='12pt', bold=True)
        self.win.addItem(self.labelTitle)
        self.win.nextRow()
        self.labelInfo = pg.LabelItem(justify='right')
        self.win.addItem(self.labelInfo)
        self.win.nextRow()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(self.update)

    ########################################################################
    ## DATA METHODS
    ########################################################################
    def createPlot(self):
        p = self.win.addPlot()
        p.showAxes(True, True)
        self.win.nextRow()
        self.plotList.append(p)

        if len(self.plotList) > 1:
            self.plotList[-2].setXLink(self.plotList[-1])
        return p

    def loadData(self):
        pass

    ########################################################################
    ## ANIMATION CONTROL METHODS
    ########################################################################
    def start(self):
        self.running = True
        self.counter = 0
        self.axisOffset = 0
        self.labelInfo.setText("{}Muestras Totales: {} Mostrando: {} | Ejecutando a {:.2f} fps".format(self.warnText, self.totalSamples, self.samples, self.avgFps), color='#ffffff', size='8pt')
        self.timer.start()

    def stop(self):
        self.running = False
        self.timer.stop()

    def resume(self):
        self.running = True
        self.timer.start()

    def switchPause(self):
        if self.running == True:
            self.stop()
        elif (self.running == False) & (self.samples != 0):
            self.resume()

    def update(self):
        # zip the lists to use their elements, enumerate to get index 
        # and finally assign each dataList[x] to update its value outside the for loop
        for x, (data, curve) in enumerate(zip(self.dataList, self.curveList)):
            self.dataList[x] = np.roll(data, -self.step)
            curve.setData(data[0:self.samples])
        
        self.axisOffset += self.step
        self.counter += 1

        for c in self.curveList:
            c.setPos(self.axisOffset, 0)

        # QtCore.QCoreApplication.processEvents()

        now = perf_counter()
        fps = 1.0 / (now - self.lastUpdate)
        self.lastUpdate = now
        self.avgFps = self.avgFps * 0.8 + fps * 0.2
        self.labelInfo.setText("{}Muestras Totales: {} Mostrando: {} | Ejecutando a {:.2f} fps".format(self.warnText, self.totalSamples, self.samples, self.avgFps), color='#ffffff', size='8pt')
        if self.avgFps < 5:
            self.brcount += 1
        if self.avgFps < 10:
            self.warnText = "(Desactive Anti-aliasing o disminuya las muestras) | "
        else: self.warnText = ""

        if self.brcount > 10:
            self.stop()
            self.brcount = 0
            self.clearPlots()
            self.labelInfo.setText("¡Simulación detenida por bajo rendimiento! Reduzca el número de muestras y desactive Anti-aliasing", color='r', size='12pt')

    ########################################################################
    ## SETTERS METHODS
    ########################################################################
    def setSpeed(self, nv):
        self.step = nv
        self.updateSpeedBox()
    
    def setSamples(self, ns):
        self.samples = ns
        if (self.samples > int(self.totalSamples/2)) | self.antiAliasing:
            self.warnText = "(Desactive Anti-aliasing o disminuya las muestras) | "
        else: self.warnText = ""
        self.updateSamplesBox()

    ########################################################################
    ## UI METHODS
    ########################################################################
    def setAntialising(self, aa: bool):
        aa = not aa
        self.antiAliasing = aa
        if pg.getConfigOption("antialias") != self.antiAliasing:
            self.clearPlots()
            pg.setConfigOptions(antialias = self.antiAliasing)

    def speedChanged(self):
        percentage = int(self.speedBox.text()[:-1])
        if percentage == 0:
            self.setSpeed(1)
        elif percentage != self.speedPercent:
            speed = int((percentage * self.totalSpeed) / 100)
            self.setSpeed(speed)

    def samplesChanged(self):
        percentage = int(self.samplesBox.text()[:-1])
        print(percentage)
        if percentage != self.samplesPercent:
            self.samplesPercent = percentage
            samples = int((percentage * self.totalSamples) / 100)
            self.setSamples(samples)

    def updateSpeedBox(self):
        self.speedBox.setMaximum(self.totalSpeed)
        self.speedPercent = int((self.step * 100) / self.totalSpeed)
        self.speedBox.setValue(self.speedPercent)

    def updateSamplesBox(self):
        # self.samplesBox.setMaximum(100)
        self.samplesBox.setValue(self.samplesPercent)
        print(self.samplesPercent)

    def adjustPlot(self):
        for ps in self.plotList:
            ps.enableAutoRange(axis='y')
            ps.enableAutoRange(axis='x')
            ps.setAutoVisible(x=True, y=True)
    
    def clearPlots(self):
        self.stop()
        # self.setSamples(1)
        for ps in self.plotList:
            ps.clear()
            ps.setAutoVisible(x=True)

class ASKPlotter(DynPlotter):
    def __init__(self, *args):
        super().__init__(*args)

        self.createPlot()
        self.createPlot()
        self.createPlot()

        self.plotList[0].setTitle("Señal Moduladora")
        self.plotList[1].setTitle("Señal Portadora")
        self.plotList[2].setTitle("Señal Modulada ASK")
        self.labelTitle.setText("Modulación ASK", color='#ffffff', size='12pt', bold=True)

        for ps in self.plotList:
            # ps.hideButtons()
            ps.setMouseEnabled(y=False)
    
    def loadData(self, message, Fc):
        self.clearPlots()

        data = mod.modulateASK(message, Fc)
        
        self.dataList = []
        self.dataList.extend(data[:3])
        
        self.totalSamples = len(data[3])
        if self.totalSamples > 8000:
            self.samplesPercent = 25
            self.samplesBox.setValue(self.samplesPercent)
        elif self.totalSamples > 5000:
            self.samplesPercent = 50
            self.samplesBox.setValue(self.samplesPercent)
        else: 
            self.samplesPercent = 100
            self.samplesBox.setValue(self.samplesPercent)
        
        samples = int((self.samplesPercent * self.totalSamples) / 100)
        self.setSamples(samples)

        self.setSpeed(int(len(data[3])/800))
        if self.step < 1: self.setSpeed(1)

        self.curveList[0] = self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('r', width=2))
        self.curveList[1] = self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('b', width=2))
        self.curveList[2] = self.plotList[2].plot(self.dataList[2], pen=pg.mkPen(color=(75,0,130), width=2))
        self.adjustPlot()

    def adjustPlot(self):
        super().adjustPlot()
        self.plotList[0].setYRange(0, 1, padding=0.1)
        self.plotList[1].setYRange(-1, 1, padding=0.1)
        self.plotList[2].setYRange(-1, 1, padding=0.1)

class FSKPlotter(DynPlotter):
    def __init__(self, *args):
        super().__init__(*args)
        
        self.createPlot()
        self.createPlot()
        self.createPlot()
        self.createPlot()

        self.plotList[0].setTitle("Señal 1")
        self.plotList[1].setTitle("Señal 2")
        self.plotList[2].setTitle("Señal Moduladora")
        self.plotList[3].setTitle("Señal Modulada FSK")
        self.labelTitle.setText("Modulación FSK", color='#ffffff', size='12pt', bold=True)

        for ps in self.plotList:
            # ps.hideButtons()
            ps.setMouseEnabled(y=False)
    
    def loadData(self, message, Fc, Fs):
        self.clearPlots()

        data = mod.modulateFSK(message, Fc, Fs)
        
        self.dataList = []
        self.dataList.extend(data[:4])
        self.dataList[0], self.dataList[2] = self.dataList[2], self.dataList[0]

        self.totalSamples = len(data[3])
        if self.totalSamples > 8000:
            self.samplesPercent = 25
            self.samplesBox.setValue(self.samplesPercent)
        elif self.totalSamples > 5000:
            self.samplesPercent = 50
            self.samplesBox.setValue(self.samplesPercent)
        else: 
            self.samplesPercent = 100
            self.samplesBox.setValue(self.samplesPercent)
        
        samples = int((self.samplesPercent * self.totalSamples) / 100)
        self.setSamples(samples)

        self.setSpeed(int(len(data[0])/800))
        if self.step < 1: self.setSpeed(1)

        self.curveList = []
        self.curveList.append(
            self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('#008000', width=2)))
        self.curveList.append(
            self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('#00C000', width=2)))
        self.curveList.append(
            self.plotList[2].plot(self.dataList[2], pen=pg.mkPen('#FF0000', width=2)))
        self.curveList.append(
            self.plotList[3].plot(self.dataList[3], pen=pg.mkPen('#FF8C00', width=2)))
        self.adjustPlot()
    
    def adjustPlot(self):
        super().adjustPlot()
        self.plotList[0].setYRange(-1, 1, padding=0.1)
        self.plotList[1].setYRange(-1, 1, padding=0.1)
        self.plotList[2].setYRange(0, 1, padding=0.1)
        self.plotList[3].setYRange(-1, 1, padding=0.1)

class PSKPlotter(DynPlotter):
    def __init__(self, *args):
        super().__init__(*args)

        self.createPlot()
        self.createPlot()
        self.createPlot()

        self.plotList[0].setTitle("Señal Moduladora")
        self.plotList[1].setTitle("Señal Portadora")
        self.plotList[2].setTitle("Señal Modulada PSK")
        self.labelTitle.setText("Modulación PSK", color='#ffffff', size='12pt', bold=True)

        for ps in self.plotList:
            # ps.hideButtons()
            ps.setMouseEnabled(y=False)
    
    def loadData(self, message, Fc):
        self.clearPlots()

        data = mod.modulatePSK(message, Fc)
        
        self.dataList = []
        self.dataList.extend(data[:3])

        self.setSpeed(int(len(data[3])/800))
        if self.step < 1: self.setSpeed(1)

        self.totalSamples = len(data[3])
        if self.totalSamples > 8000:
            self.samplesPercent = 25
            self.samplesBox.setValue(self.samplesPercent)
        elif self.totalSamples > 5000:
            self.samplesPercent = 50
            self.samplesBox.setValue(self.samplesPercent)
        else: 
            self.samplesPercent = 100
            self.samplesBox.setValue(self.samplesPercent)

        samples = int((self.samplesPercent * self.totalSamples) / 100)
        self.setSamples(samples)

        self.curveList[0] = self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('#FF0000', width=2))
        self.curveList[1] = self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('#FFFF00', width=2))
        self.curveList[2] = self.plotList[2].plot(self.dataList[2], pen=pg.mkPen('#FF8C00', width=2))
        self.adjustPlot()

    def adjustPlot(self):
        super().adjustPlot()
        self.plotList[0].setYRange(-1, 1, padding=0.1)
        self.plotList[1].setYRange(-1, 1, padding=0.1)
        self.plotList[2].setYRange(-1, 1, padding=0.1)