import psycopg2

def bdd():
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
                    