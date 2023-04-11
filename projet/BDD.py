import psycopg2

conn = psycopg2.connect(
        user = "postgres",
        password = "md53175bce1d3201d16594cebf9d7eb3f9d",
        host = "172.20.10.3",
        database = "eaux"
    )
cur = conn.cursor()
# Afficher la version de PostgreSQL 
cur.execute("SELECT version();")
version = cur.fetchone()
print("Version : ", version,"\n")
  
#fermeture de la connexion à la base de données
cur.close()
conn.close()
print("La connexion PostgreSQL est fermée")
