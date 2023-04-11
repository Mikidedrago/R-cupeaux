import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from graphique import Graphique

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Création d'une scène et d'une vue QGraphicsView
    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    # Création de l'instance du graphique
    graphique = Graphique()

    # Ajout du graphique à la scène
    scene.addWidget(graphique)

    # Affichage de la vue QGraphicsView
    view.show()

    sys.exit(app.exec_())





