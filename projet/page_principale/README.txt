python -m PyQt5.uic.pyuic -x page_principale.ui -o page_principale2.py 

pyrcc5 ressources.qrc -o ressources_rc.py  


self.graph = Graphique()

self.scene = QtWidgets.QGraphicsScene()
self.scene.addWidget(self.graph)

# Définir la scène de la QGraphicsView
self.graphique.setScene(self.scene)

self.niveau_0pourcent.hide()
self.niveau_25pourcent.hide()
self.niveau_50pourcent.hide()
self.niveau_75pourcent.hide()
self.niveau_100pourcent.hide()


