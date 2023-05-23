from securiserConnexion import Test
import psycopg2

class ElementDatabase():
    def __init__(self):
        self.elements = Test()
        print(self.elements.row[0])
       