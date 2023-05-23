import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# ---------------------------------------------------------------------




class Graphique(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphWidget = pg.PlotWidget()
        self.scene.addWidget(self.graphWidget)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        
        # changer couleur de l'arrière plan
        self.graphWidget.setBackground('w')
        axis = pg.DateAxisItem(orientation='bottom')
        self.graphWidget.setAxisItems({"bottom": axis})
        pen = pg.mkPen(color=(255, 0, 0), width=10, style=QtCore.Qt.DotLine)

    
        # plot data: x, y values
        x = [1, 3, 5, 1, 3, 12, 34]
        y = [7, 34, 83, 21, 1, 34, 3]
        self.graphWidget.plot(x,y)
        # self.graphWidget.plot(x=[x.timestamp() for x in date], y=volume, pen=pen, symbol='o')

        #x, y, pen=pen

        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volume (m³)', **styles)
        self.graphWidget.setLabel('bottom', 'Date (H)', **styles)