# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        plt.style.use(('dark_background'))
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        
        # self.toolbar = NavigationToolbar(self.canvas, self)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.ax = self.canvas.axes
        self.setLayout(vertical_layout)
        plt.tight_layout(pad = 1)
        
        # self.canvas.axes.plot(linewidth=1.0)
        
        # self.toolbar.setStyleSheet("background-color: white;")
        # self.toolbar.update()

class MplWidgetFSK(QWidget):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        plt.style.use(('dark_background'))
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.gridspec = self.canvas.figure.add_gridspec(4,3)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.ax = self.canvas.axes
        self.setLayout(vertical_layout)
        plt.tight_layout(pad = 1)
