import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from pyqtgraph import PlotWidget

class Graphique(QWidget):
    def __init__(self):
        super(Graphique, self).__init__()

        # Création d'un layout vertical pour le widget
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Création du widget de tracé
        self.graphWidget = PlotWidget()
        layout.addWidget(self.graphWidget)

        # Tracé du graphique
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        x = [1, 2, 3, 4, 5]
        y = [30, 32, 34, 32, 33]
        self.graphWidget.plot(x, y, pen=pen)