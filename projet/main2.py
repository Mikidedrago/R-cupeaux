from aaaa import create_graph
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma fenêtre PyQt")
        self.resize(1920, 1120)

        # Créer un widget QLabel pour le graphique
        graph_widget = QLabel(self)
        
        # Appeler la fonction create_graph pour créer le graphique et récupérer le widget FigureCanvas
        graph_canvas = create_graph()

        # Ajouter le widget FigureCanvas au widget QLabel
        graph_widget.setLayout(QVBoxLayout())
        graph_widget.layout().addWidget(graph_canvas)

        # Ajouter le widget QLabel à la fenêtre
        self.setCentralWidget(graph_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())
