from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from pyqtgraph import PlotWidget
import pyqtgraph as pg


class Graphique(QWidget):
    def __init__(self):
        super(Graphique, self).__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)    

        # changer couleur de l'arrière plan 
        self.graphWidget = pg.PlotWidget() 
        self.graphWidget.setBackground('w')
        layout.addWidget(self.graphWidget)
        
        
        pen = pg.mkPen(color=(255, 0, 0), width=10, style=QtCore.Qt.DotLine)

        x = [1, 2, 3, 4, 5]
        y = [30, 32, 34, 32, 33]

        # plot data: x, y values
        self.graphWidget.plot(x, y, pen=pen)

        """styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volume (m³)', **styles)
        self.graphWidget.setLabel('bottom', 'Heure (H)', **styles)
"""
        

"""def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()"""