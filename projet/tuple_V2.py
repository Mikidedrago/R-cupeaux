import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import psycopg2
from datetime import datetime
from principale import Principale
from database_Mesure import bdd


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # titre de la fenetre 
        self.setWindowTitle("PyQtGraph")
        
        # Taille de la fenêtre 
        self.setGeometry(100,100, 800, 600)
        
        # appel du graphique
        self.graphique()
        
        # afficher la fenetre
        self.show()
        
    # méthode création du graphique
    def graphique(self):
       
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

        self.bdd = bdd()
        date = bdd.date
        volume = bdd.volume
    
        # plot data: x, y values
        self.graphWidget.plot(x=[x.timestamp() for x in date], y=volume, pen=pen, symbol='o')

        #x, y, pen=pen

        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volume (m³)', **styles)
        self.graphWidget.setLabel('bottom', 'Date (H)', **styles)
        
        

 
"""# créer l'application 
App = QApplication(sys.argv)

# créer une instance de la fenetre 
graphique = Window()

# lancer l'app
sys.exit(App.exec())"""
