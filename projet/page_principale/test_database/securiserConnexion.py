import psycopg2

def test():
    return row[0]

try:
    conn = psycopg2.connect(
                user="postgres",
                password="admin",
                host="172.20.10.3",
                port="5432",
                database="eaux"
    )
    cur = conn.cursor()
    sql = "SELECT * FROM utilisateur"
    cur.execute(sql)
    print("Sélectionner des lignes dans la table person")
    res = cur.fetchall()

    for row in res:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Address  = ", row[2], "\n")

    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    
    print("La connexion PostgreSQL est fermée")
    test()
except (Exception, psycopg2.Error) as error :
    print ("Erreur lors du sélection à partir de la table person", error)
    
