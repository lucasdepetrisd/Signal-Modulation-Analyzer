# ------------------------------------------------------
# -------------------- animation.py --------------------
# ------------------------------------------------------
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pyqtgraph as pg 
from pyqtgraph import PlotWidget
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, QEventLoop
import numpy as np
import modulation.modulation as mod
import threading
import time

class DynPlotter:
    
    def __init__(self, win):
        self.running = False
        self.step = 1
        self.counter = 0
        self.axisOffset = 0
        self.plotList = []
        self.dataList = []
        self.curveList = [None] * 3
        
        pg.setConfigOptions(antialias=False)

        self.win = win
        self.win.clear()
        # self.plot = plot
        # self.plot.setTitle('Hola')

        self.timer = QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(self.update)

    def createPlot(self):
        p = self.win.addPlot()
        self.win.nextRow()
        self.plotList.append(p)
        if len(self.plotList) > 1:
            self.plotList[-2].setXLink(self.plotList[-1])
        return p

    def loadData(self):
        pass

    def start(self):
        self.running = True
        self.timer.start()
        # self.dataCollectionThread = DataCaptureThread(self.update)
        # self.dataCollectionThread.start()

    def stop(self):
        self.running = False
        self.timer.stop()

    def resume(self):
        self.running = True
        self.timer.start()

    def update(self):
        for x, d in enumerate(self.dataList):
            self.dataList[x] = np.roll(d, -self.step)
            self.curveList[x].setData(d)
        
        self.axisOffset += self.step
        self.counter += 1

        for c in self.curveList:
            c.setPos(self.axisOffset, 0)

        QtCore.QCoreApplication.processEvents()

    def switchAnimation(self):
        if self.running == True:
            self.stop()
        elif self.running == False:
            self.resume()

    def clear(self):
        self.stop()
        for ps in self.plotList:
            ps.clear()
            ps.setAutoVisible(x=True)

    def speed(self, nv):
        self.v = nv
    
    def antialiasing(self, aa: bool):
        self.clear()
        pg.setConfigOptions(antialias=aa)

    def autoadjust(self):
        for ps in self.plotList:
            ps.enableAutoRange(axis='y')
            ps.enableAutoRange(axis='x')
            ps.setAutoVisible(x=True, y=True)

class ASKPlotter(DynPlotter):
    def __init__(self, win):
        super().__init__(win)

        self.createPlot()
        self.createPlot()
        self.createPlot()

        for ps in self.plotList:
            ps.hideButtons()
            # p.setMouseEnabled(x=False, y=False)
    
    def loadData(self, message, Fc):
        self.clear()

        data = mod.modulateASK(message, Fc)
        
        self.dataList = []
        self.dataList.extend(data[:3])

        self.step = int(len(data[4])/800)
        if self.step < 1: self.step = 1

        self.curveList[0] = self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('r', width=2))
        self.curveList[1] = self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('b', width=2))
        self.curveList[2] = self.plotList[2].plot(self.dataList[2], pen=pg.mkPen(color=(75,0,130), width=2))
        self.autoadjust()

class FSKPlotter(DynPlotter):
    def __init__(self, win):
        super().__init__(win)

        self.createPlot()
        self.createPlot()
        self.createPlot()
        self.createPlot()

        for ps in self.plotList:
            ps.hideButtons()
            # p.setMouseEnabled(x=False, y=False)
    
    def loadData(self, message, Fc, Fs):
        self.clear()

        data = mod.modulateFSK(message, Fc, Fs)
        
        self.dataList = []
        self.dataList.extend(data[:4])

        # self.step = int(len(data[0])/800)
        # if self.step < 1: self.step = 1

        self.curveList = []
        self.curveList.append(
            self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('r', width=2)))
        self.curveList.append(
            self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('b', width=2)))
        self.curveList.append(
            self.plotList[2].plot(self.dataList[2], pen=pg.mkPen(color=(75,0,130), width=2)))
        self.curveList.append(
            self.plotList[3].plot(self.dataList[3], pen=pg.mkPen(color=(75,0,130), width=2)))
        self.autoadjust()

class PSKPlotter(DynPlotter):
    def __init__(self, win):
        super().__init__(win)

        self.createPlot()
        self.createPlot()
        self.createPlot()

        for ps in self.plotList:
            ps.hideButtons()
            # p.setMouseEnabled(x=False, y=False)
    
    def loadData(self, message, Fc):
        self.clear()

        data = mod.modulatePSK(message, Fc)
        
        self.dataList = []
        self.dataList.extend(data[:3])

        self.step = int(len(data[4])/800)
        if self.step < 1: self.step = 1

        self.curveList[0] = self.plotList[0].plot(self.dataList[0], pen=pg.mkPen('r', width=2))
        self.curveList[1] = self.plotList[1].plot(self.dataList[1], pen=pg.mkPen('b', width=2))
        self.curveList[2] = self.plotList[2].plot(self.dataList[2], pen=pg.mkPen(color=(75,0,130), width=2))
        self.autoadjust()

# elif tipo == 1:
#     data = mod.modulateFSK(message, Fc, Fs)
# elif tipo == 2:
#     data = mod.modulatePSK(message, Fc)