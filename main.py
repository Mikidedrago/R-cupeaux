import psycopg2

try:
    # Connexion à la base de données
    conn = psycopg2.connect(
        user="postgres",
        password="admin",
        host="172.20.10.3",
        port="5432",
        database="eaux"
    )
    cur = conn.cursor()

    # Fonction pour vérifier les informations de connexion de l'utilisateur
    def verify_login(username, password):
        
        cur.execute("SELECT * FROM utilisateur WHERE nom = %s AND motdepasse = %s;", (username, password))
        return cur.fetchone() is not None

    # Exemple d'utilisation de la fonction de vérification de connexion
    username = 'jj' #un truc sous cette forme a peu près : self.formulaire.nom.text()
    password = 'jj'
    if verify_login(username, password):
        print("Connexion reussie.")
    else:
        print("Echec de la connexion.")

    # Fermer la connexion à la base de données
    cur.close()
    conn.close()

except (Exception, psycopg2.Error) as error :
    print ("Erreur lors du selection a partir de la table person", error)

