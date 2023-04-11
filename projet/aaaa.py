import psycopg2
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def create_graph():
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
    
    # Ajouter les données au graphique
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    ax.plot(x, y)

    # Créer un widget FigureCanvas et ajouter la figure
    canvas = FigureCanvas(fig)
    canvas.draw()
    
    # Retourner le widget FigureCanvas
    return canvas
