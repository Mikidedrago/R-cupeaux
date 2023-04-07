import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import psycopg2
from datetime import datetime


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
        try:
            # Connexion à la base de données PostgreSQL
            conn = psycopg2.connect(
                host="172.20.10.3", 
                database="eaux", 
                user="postgres", 
                password="admin",
                port="5432")

            # Création du curseur pour exécuter les requêtes SQL
            cur = conn.cursor()

            # Exécution de la requête SQL pour récupérer les données timestamp
            cur.execute("SELECT volume, date FROM mesure LIMIT 3")

            res = cur.fetchall()

            # Stocker les données extraites dans un dictionnaire
            volume = []
            date = []
        
        
            for row in res:
                # ajouter les données dans la liste res_final
                volume.append(row[0])
                date.append(row[1])
                print(type(row[1]))
            #.strftime("%H:%M:%S")
            
                
            #print(volume)
            #print(date)
            
            
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()



        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors du sélection à partir de la table person", error)
                
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
        self.graphWidget.plot(x=[x.timestamp() for x in date], y=volume, pen=pen, symbol='o')

        #x, y, pen=pen

        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volume (m³)', **styles)
        self.graphWidget.setLabel('bottom', 'Date (H)', **styles)
        
        

 
# créer l'application 
App = QApplication(sys.argv)

# créer une instance de la fenetre 
graphique = Window()

# lancer l'app
sys.exit(App.exec())
