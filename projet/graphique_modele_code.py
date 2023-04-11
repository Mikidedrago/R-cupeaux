import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphique de données")
        
        # Se connecter à la base de données et récupérer les données
        conn = psycopg2.connect(user="postgres", 
                                password="admin", 
                                host="172.20.10.3", 
                                port="5432", 
                                database="eaux")
        cur = conn.cursor()
        cur.execute("SELECT temperature, hauteur FROM mesure")
        data = cur.fetchall()
        
        # Créer une figure Matplotlib et ajouter un axe
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        # Tracer la courbe avec les données de la base de données
        x = [row[0] for row in data]
        y = [row[1] for row in data]
        ax.plot(x, y)
        ax.set_title("Données de mesure")
        ax.set_xlabel("Température")
        ax.set_ylabel("Hauteur")
        
        # Créer un objet FigureCanvas pour afficher la figure
        canvas = FigureCanvas(fig)
        canvas.setParent(self)
        
        # Ajouter le FigureCanvas à la fenêtre principale
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(canvas)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()