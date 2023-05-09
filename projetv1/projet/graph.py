from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow


class Graphique(QMainWindow):
    def __init__(self):
        super(Graphique, self).__init__()
        self.test()

    def test(self):
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphWidget = pg.PlotWidget()
        self.scene.addWidget(self.graphWidget)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

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
        
"""def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Graphique()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
        
"""
