from PyQt5.QtWidgets import QApplication, QMainWindow
import psycopg2
from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys

from datetime import datetime

# établir une connexion à la base de données
conn = psycopg2.connect(
    user="postgres",
    password="admin",
    host="172.20.10.3",
    port="5432",
    database="eaux"
)

# créer un objet cursor pour exécuter des requêtes SQL
cur = conn.cursor()

# exécuter une requête SQL pour récupérer les données de la table "temperatures"
sql = "SELECT temperature, volume FROM mesure"
cur.execute(sql)

# récupérer toutes les lignes de résultats de la requête
rows = cur.fetchall()

# stocker les données dans des listes
x = [row[0] for row in rows] # hauteur
y = [row[1] for row in rows] # température

# fermer le curseur et la connexion à la base de données
cur.close()
conn.close()
    

# créer une application pyqtgraph


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphWidget = pg.PlotWidget()
        self.scene.addWidget(self.graphWidget)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        

        # changer couleur de l'arrière plan
        self.graphWidget.setBackground('w')
        w = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        w.showGrid(x=True, y=True)
        pen = pg.mkPen(color=(255, 0, 0), width=10, style=QtCore.Qt.DotLine)

        
        # plot data: x, y values
        self.graphWidget.plot(x, y, pen=pen)

        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volume (m³)', **styles)
        self.graphWidget.setLabel('bottom', 'Heure (H)', **styles)

        


# afficher la fenêtre
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())