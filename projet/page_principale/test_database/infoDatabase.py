import psycopg2

class ElementConnexionDatabase():
    def __init__(self):
        
        self.conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "172.20.10.3",
            port = "5432",
            database = "eaux"
            )
        return self.conn
    