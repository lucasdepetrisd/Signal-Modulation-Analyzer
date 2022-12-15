# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MplWidget(QWidget):
    
    def __init__(self, parent = None):
        self.state = 0
        QWidget.__init__(self, parent)
        plt.style.use(('dark_background'))
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure) #FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.ax = self.canvas.axes
        self.setLayout(vertical_layout)
        plt.tight_layout(pad = 2)
    
    def updateAnimation(self, animations):
        if len(animations) < 4:
            self.ani1 = animations[0]
            self.ani2 = animations[1]
            self.ani3 = animations[2]
        self.canvas.draw()
    def switchAnimation(self, pause):
        self.state += 1
        if pause and (self.state % 2):
            self.ani1.event_source.stop()
            self.ani2.event_source.stop()
            self.ani3.event_source.stop()
        else: 
            self.ani1.event_source.start()
            self.ani2.event_source.start()
            self.ani3.event_source.start()
    def pauseAnimation(self):
        self.ani1.event_source.stop()
        self.ani2.event_source.stop()
        self.ani3.event_source.stop()