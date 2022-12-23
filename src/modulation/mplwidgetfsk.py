# ------------------------------------------------------
# ----------------- mplwidgetfsk.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MplWidgetFSK(QWidget):
    
    def __init__(self, parent = None):
        
        self.state = 0
        QWidget.__init__(self, parent)
        plt.style.use(('dark_background'))
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure) #FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.gridspec = self.canvas.figure.add_gridspec(4,3)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.ax = self.canvas.axes
        self.setLayout(vertical_layout)
        plt.tight_layout(pad = 1)

    def updateAnimation(self, animations):
        self.ani1 = animations[0]
        self.ani2 = animations[1]
        self.ani3 = animations[2]
        self.ani4 = animations[3]
        self.canvas.draw()
    
    def switchAnimation(self, pause):
        if hasattr(self, 'ani1'):
            self.state += 1
            if pause and (self.state % 2):
                self.ani1.event_source.stop()
                self.ani2.event_source.stop()
                self.ani3.event_source.stop()
                self.ani4.event_source.stop()
            else: 
                self.ani1.event_source.start()
                self.ani2.event_source.start()
                self.ani3.event_source.start()
                self.ani4.event_source.start()
    
    def pauseAnimation(self):
        if hasattr(self, 'ani1'):
            self.ani1.event_source.stop()
            self.ani2.event_source.stop()
            self.ani3.event_source.stop()
            self.ani4.event_source.stop()
