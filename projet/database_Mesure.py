import psycopg2
import json

#def connexion_mesure():
try:
    conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "172.20.10.3",
            port = "5432",
            database = "eaux"
        )

    #conn = connexion_mesure()
    cur = conn.cursor()
    sql = "SELECT * FROM mesure"
    cur.execute(sql)
    
    res = cur.fetchall() 
    # Stocker les données extraites dans un dictionnaire
    donnees_mesure = {}
    
    for row in res:
        donnees_mesure[row[0]] = {
            "Temperature de l'eau = ": row[1],
            "Volume  = " : row[2],
            "Hauteur  = " : row[3]
        }
       
  
    
        # Enregistrer les données dans un fichier JSON
        with open("donnees_mesure.json", "w") as fichier_json:
            json.dump(donnees_mesure, fichier_json)
    #fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    
except (Exception, psycopg2.Error) as error :
    print ("Erreur lors du sélection à partir de la table person", error)
    
    
    
# ouvrir le fichier json 
with open ("donnees_mesure.json", "r") as fichier_json:
    data = json.load(fichier_json)

donnees = []

for key in data.keys():
    donnees.append(data[key])

# Récupérer les variables
temperature_eau_1 = donnees[0]["Temperature de l'eau = "]
volume_1 = donnees[0]["Volume  = "]
hauteur_1 = donnees[0]["Hauteur  = "]

temperature_eau_2 = donnees[1]["Temperature de l'eau = "]
volume_2 = donnees[1]["Volume  = "]
hauteur_2 = donnees[1]["Hauteur  = "]

temperature_eau_3 = donnees[2]["Temperature de l'eau = "]
volume_3 = donnees[2]["Volume  = "]
hauteur_3 = donnees[2]["Hauteur  = "]


print(temperature_eau_1)
