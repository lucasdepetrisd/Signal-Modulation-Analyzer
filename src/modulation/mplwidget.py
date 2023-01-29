# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MplWidget(QWidget):
    
    def __init__(self, parent = None, dpi=1):
        self._running = True
        self.state = 1
        QWidget.__init__(self, parent)
        plt.style.use(('dark_background'))
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure) #FigureCanvas(Figure())
        
        # self.toolbar = NavigationToolbar(self.canvas, self)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.ax = self.canvas.axes
        self.setLayout(vertical_layout)
        plt.tight_layout(pad = 1)
        
        # self.toolbar.setStyleSheet("background-color: white;")
        # self.toolbar.update()
    
    def updateAnimation(self, animations):
        self.ani1 = animations[0]
        self.ani2 = animations[1]
        self.ani3 = animations[2]
        self.canvas.draw()
    
    def switchAnimation(self, pause):
        if hasattr(self, 'ani1'):
            if self._running == False:
                self._running = True
                self.ani1.event_source.start()
                self.ani2.event_source.start()
                self.ani3.event_source.start()
            elif self._running == True:
                self._running = False
                self.ani1.event_source.stop()
                self.ani2.event_source.stop()
                self.ani3.event_source.stop()
    
    def pauseAnimation(self):
        if hasattr(self, 'ani1'):
            self._running = False
            self.ani1.event_source.stop()
            self.ani2.event_source.stop()
            self.ani3.event_source.stop()