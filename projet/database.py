import psycopg2

def connexion_bdd():
    conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "172.20.10.3",
            port = "5432",
            database = "eaux"
            )
    return conn


# ssh Jason@172.20.10.3
# psql eaux;
# select * from utilisateur
# delete from utilisateur where id = (x, x, x, x)