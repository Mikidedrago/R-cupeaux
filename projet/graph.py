from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Graphique(QWidget):
    def __init__(self):
        super(Graphique, self).__init__()
        self.test()

    def test(self):
        # Création d'un layout vertical pour le widget
        layout = QVBoxLayout()
        self.setLayout(layout)

        # changer couleur de l'arrière plan
        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0), width=10, style=QtCore.Qt.DotLine)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature, pen=pen)

        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

        

