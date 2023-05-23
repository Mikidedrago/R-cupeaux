import psycopg2

def connexion_bdd():
    conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "192.168.1.17", #172.20.10.3
            port = "5432",
            database = "eaux"
            )
    return conn