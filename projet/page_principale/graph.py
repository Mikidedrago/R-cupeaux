import sys
import psycopg2
from datetime import datetime
from psycopg2 import Error
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QApplication
from PyQt5 import QtCore
import pyqtgraph as pg
import time

class Graphique(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.resize(750, 450)
        self.scene.addWidget(self.graphWidget)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.update_graph()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(10000)  # Update graph every 5 seconds (5000 milliseconds)

    def update_graph(self):
        try:
            conn = psycopg2.connect(
                host="192.168.1.17",#172.20.10.3
                database="eaux",
                user="postgres",
                password="admin",
                port="5432"
            )

            cursor = conn.cursor()
            cursor.execute("SELECT date, volume FROM mesure")
            records = cursor.fetchall()
            self.volume = []
            self.date = []
            for row in records:
                self.volume.append(row[1])
                self.date.append(row[0])

            cursor.close()
            conn.close()

            self.graphWidget.clear()
            self.graphWidget.setBackground('w')
            axis = pg.DateAxisItem(orientation='bottom')
            self.graphWidget.setAxisItems({"bottom": axis})
            pen = pg.mkPen(color=(0, 0, 255), width=10, style=QtCore.Qt.DotLine)
            self.graphWidget.plot(x=[x.timestamp() for x in self.date], y=self.volume, pen=pen, symbol='o')
            styles = {'color': 'r', 'font-size': '20px'}
            self.graphWidget.setLabel('left', 'Volume (L)', **styles)
            self.graphWidget.setLabel('bottom', 'Date (H)', **styles)

        except Error as e:
            print("Error de connexion", e)


