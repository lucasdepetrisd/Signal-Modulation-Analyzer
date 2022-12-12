# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt

class MplWidget(QWidget):
    
    def __init__(self, parent = None):

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
