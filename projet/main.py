import sys
import requests
import json

import smtplib
from email.message import EmailMessage

import psycopg2

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *


from login import Login 
from formulaire import Inscription
from perteMdp import Password
from principale import Principale
from database import connexion_bdd
#from systeme_login_sql import systeme_sql





class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application,self).__init__()  
        self.initialisationLogin()
        
    
    
    def initialisationLogin(self):
        #affichage de la fenetre de connexion
        self.Form = QtWidgets.QWidget()
        self.login = Login()
        self.login.setupUi(self.Form)
        #bouton pour ouvrir la fenetre 2 aaprès la connexion réussi 
        self.login.boutonSeConnecter.clicked.connect(self.systeme_Login)
        self.login.boutonCreerCompte.clicked.connect(self.createAccount)
        self.login.boutonMotDePasseOublie.clicked.connect(self.loosePassword)
        self.Form.show()
        
    # ------------------------------------------------------------------------    
        
    def systeme_Login(self):
        
        
        #self.systeme_Login() # si utilisation d'un fichier
        try:
            # Connexion à la base de données
            conn = psycopg2.connect(
                user = "postgres", #postgres
                password="admin", #admin
                host="172.20.10.3",
                port="5432",
                database="eaux"
            )
            cur = conn.cursor()

            # Fonction pour vérifier les informations de connexion de l'utilisateur
            def verify_login(username, password):
                
                cur.execute("SELECT (motdepasse = crypt(%s,motdepasse)) AS pswmatch FROM utilisateur WHERE nom = %s ;", (password, username))
                return cur.fetchone() is not None

            # Exemple d'utilisation de la fonction de vérification de connexion
            username = self.login.username.text() 
            password = self.login.password.text()
            if verify_login(username, password):
                print("Connexion reussie.")
                self.succesLogin()
                
            else:
                print("Echec de la connexion.")
                self.erreurLogin()

            # Fermer la connexion à la base de données
            cur.close()
            conn.close()

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors du selection a partir de la table person", error)


        
        
        
    def succesLogin(self):
        self.close()
        self.Form = QtWidgets.QWidget()
        self.principale = Principale()
        self.principale.setupUi3(self.Form)
        self.Form.showMaximized()
        
        
        
            
        self.principale.boutonDeconnexion.clicked.connect(self.deconnexion)
        self.principale.boutonSeConnecter_2.clicked.connect(self.boutonquittez) 
    
    def erreurLogin(self):
        print("Adresse e-mail ou mot de passe incorrect")
        self.login.username.clear()
        self.login.password.clear()
        self.login.icone.show()
        self.login.information.show()
    
    def deconnexion(self):
        self.close()
        self.initialisationLogin()
        #self.login.label_4.hide()
    
    def boutonquittez(self):
        exit()        
        
    # ------------------------------------------------------------------------
            
    def createAccount(self):
        self.close()
        self.Form = QtWidgets.QWidget()
        self.formulaire = Inscription()
        self.formulaire.setupUi1(self.Form)
        self.Form.show()
        
        self.formulaire.boutonSeConnecter.clicked.connect(self.generer)
        
        self.close()
        self.login = Login()
        self.login.setupUi(self)
        #self.login.label_4.hide()
        
    def generer(self):
        nom = self.formulaire.nom.text()
        prenom = self.formulaire.prenom.text()
        mail = self.formulaire.mail.text()
        password = self.formulaire.motDePasse.text()
        #confirmation = self.formulaire.confirmationMotdePasse.text()
        
        # Insersion du compte dans le base de données
        conn = connexion_bdd()
        
        """# création de l'utilisateur
        cur = conn.cursor()
        sql = "CREATE USER %s WITH PASSWORD '%s'"
        identifiants = (mail,password)
        cur.execute(sql, identifiants)
        
        # insertion de l'utilisateur dans la base de donnée
        cur = conn.cursor()
        sql = "INSERT INTO utilisateur (nom, prenom, email, motdepasse) VALUES (%s,%s,%s, crypt(%s,gen_salt('bf')))"
        values = (nom,prenom,mail,password)
        cur.execute(sql,values)
        
        # Vérification si l'utilisateur à été créé
        conn.commit()
        count = cur.rowcount
        print (count, "création du compte.")
        
        cur.close()
        conn.close()
        
        connexion = psycopg2.connect(
            user = mail,
            password = password,
            host = "172.20.10.3",
            port = "5432",
            database = "eaux"
        )
        
        curseur = connexion.cursor()
        """
        
        
        cur = conn.cursor()
        sql = "INSERT INTO utilisateur (nom, prenom, email, motdepasse) VALUES (%s,%s,%s, crypt(%s,gen_salt('bf')))"
        values = (nom,prenom,mail,password)
        cur.execute(sql,values)
        
        # Vérification si le compte à été inséré
        conn.commit()
        count = cur.rowcount
        print (count, "enregistrement insere avec succes dans la table utilisateurs.")
        
        # Récupérer les données de la base de données
        cur.execute("SELECT * FROM utilisateur")
        donnees = cur.fetchall()

        # Stocker les données extraites dans un dictionnaire
        donnees_utilisateurs = {}
        for ligne in donnees:
            donnees_utilisateurs[ligne[0]] = {
                "nom": ligne[1],
                "prenom": ligne[2],
                "email": ligne[3],
                "password": ligne[4]
            }
        
        
        self.close()
        self.initialisationLogin()
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Inscription")
        msgBox.setMinimumSize(100,20)
        msgBox.setText("SUCCES !!                                         ")
        msgBox.setInformativeText("Votre compte a été crée")
        returnValue = msgBox.exec()
        
    # ------------------------------------------------------------------------
            
    def loosePassword(self):
        self.close()
        self.Form = QtWidgets.QWidget()
        self.password = Password()
        self.password.setupUi2(self.Form)
        self.Form.show()
        self.password.envoyer.clicked.connect(self.recuperermdp)
    
    def recuperermdp(self):
        
        msg = EmailMessage()
        msg.set_content("Votre mot de passe est : admin")

        msg['Subject'] = 'Récupération du mot de passe'
        msg['From'] = "testenvoyeur2@gmail.com"
        msg['To'] = "larroque064@gmail.com"

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("testenvoyeur2@gmail.com", "oxkiiilexfntzomy")
        server.send_message(msg)
        server.quit()

            
        self.close()
        self.initialisationLogin()
        #self.login.label_4.hide()
        
        msgBox1 = QMessageBox()
        msgBox1.setWindowTitle("Mail")
        msgBox1.setMinimumSize(100,20)
        msgBox1.setText("Un mail de récupération a été envoyé                                         ")
        returnValue = msgBox1.exec()
    
    
        # Ajouter du code pour enregistrer donnée dans la BDD
        

        
    def meteo(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=Gardanne,FR&appid=ac7c75b9937a495021393024d0a90c44&units=metric'

        res = requests.get(url)

        data = res.json()

        temp = data['main']['temp']
        win_speed = data['wind']['speed']

        latitude = data['coord']['lat']
        longitude = data['coord']['lon']

        description = data['weather'][0]['description']

        print("Temperature : {} °C".format(temp))
        print("Wind speed : {} m/s".format(win_speed))
        print("Latitude : {}".format(latitude))
        print("Longitude : {}".format(longitude))
        print("Description : {}".format(description))
        
    
       
    def maBdd(self):
        
        pass

        
        
     
if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QtWidgets.QApplication(sys.argv)
    
    # On instancie une fenêtre graphique et l'affiche.
    application = Application()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())