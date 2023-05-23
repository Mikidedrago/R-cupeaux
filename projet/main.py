import sys
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

import psycopg2

# I M P O R T A T I O N -- F I C H I E R S
from page_login.responsive_app_login import Login
from page_principale.page_principale import Principale
from page_formulaire.responsive_app_formulaire import Formulaire
from page_mdpoublie.responsive_app_mdpOublie import Password

from database import connexion_bdd


from alerte import alerte_create_account, alerte_deconnexion

class Application(QtWidgets.QMainWindow):
    # Point de commancement
    def __init__(self):
        super(Application, self).__init__()
        self.login = Login()
        self.principal = Principale()
        self.formulaire = Formulaire()
        self.motdepasse = Password()
        self.initialisationLogin()
        
    # Au démarrage de l'application on veut afficher la fenetre de Login
    # Fonction pour afficher cette fenetre
    def initialisationLogin(self):
        
        # Processus pour afficher la fenetre de connexion
        self.design_page_login = QtWidgets.QWidget()
        # Pour donner un nom à la classe login 
        """self.login = Login()"""
        self.login.page_Login(self.design_page_login)
    
        #bouton pour les actions
        self.login.boutonSeConnecter.clicked.connect(self.systeme_Login)

        self.login.boutonCreerCompte.clicked.connect(self.initialisationFormulaire)
        self.login.boutonMotDePasseOublie.clicked.connect(self.loosePassword)
        
        # Création du raccourci clavier pour la touche "Entrée"
        shortcut = QtWidgets.QShortcut(QKeySequence(QtCore.Qt.Key_Return), self.login.boutonSeConnecter)
        shortcut.activated.connect(self.systeme_Login)
        
        #afficher la page connexion
        self.design_page_login.show()
        
    def systeme_Login(self):
        
        # ------------------------------------
        #Sans la BDD
        """
        username = self.login.username.text() 
        password = self.login.password.text()
        
        if username and password == "admin":
            self.succesLogin()
            
        else:
            self.erreurLogin()
        """
        # -----------------------------------
    
        """-------------------------------------------------------"""
        try:
            # Connexion à la base de données
            conn = connexion_bdd()
            cur = conn.cursor()

            # Fonction pour vérifier les informations de connexion de l'utilisateur
            def verify_login(username, password):
                # vérifier avec les mots de passe crypté
                cur.execute("SELECT (motdepasse = crypt(%s,motdepasse)) AS pswmatch FROM utilisateur WHERE nom = %s ;", (password, username))
                return cur.fetchone() is not None

            # Exemple d'utilisation de la fonction de vérification de connexion
            # récupérer les valeurs dans les lineEdit
            username = self.login.username.text() 
            password = self.login.password.text()
            # si le mail et le password sont correct connexion
            if verify_login(username, password):
                print("Connexion reussie.")
                self.succesLogin()
                
            # sinon non
            else:
                print("Echec de la connexion.")
                self.erreurLogin()

            # Fermer la connexion à la base de données
            cur.close()
            conn.close()

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors du selection a partir de la table person", error)    


        """-------------------------------------------------------"""
        
    def succesLogin(self):
        
        # Pour fermer la page de connexion 
        self.design_page_login.close()
        # pouvoir afficher la page principale
        self.design_page_principale = QtWidgets.QWidget()
        # Pour donner un nom à la classe login 
        self.principal.page_Principale(self.design_page_principale)
        # l'afficher en full screen
        self.design_page_principale.showFullScreen()
        
        # actions des boutons
        self.principal.boutonQuitter.clicked.connect(self.boutonquittez)
        self.principal.boutonDeconnexion.clicked.connect(self.deconnexion) #boutonDeconnexion
    
        
        print("fin")
        
    
    def erreurLogin(self):

        print("Adresse e-mail ou mot de passe incorrect")
        self.login.username.clear()
        self.login.password.clear()
        self.login.icone.show()
        self.login.information.show()

    def deconnexion(self):
        self.design_page_principal.close()
        self.initialisationLogin()
        
        alerte_deconnexion()
     
    
    def boutonquittez(self):
        exit()      
    """--------------------------------------------------------"""  
    """ ------ changement de bouton (partie formulaire) ------ """ 
    """--------------------------------------------------------"""   
    
    def initialisationFormulaire(self):
        self.design_page_login.close()
        self.design_page_formulaire = QtWidgets.QWidget()
        self.formulaire.page_Formulaire(self.design_page_formulaire)
        self.design_page_formulaire.show()
        
        self.formulaire.sinscrire.clicked.connect(self.createAccount)
        self.formulaire.retour.clicked.connect(self.back)
    
    def createAccount(self):
         
        # ------------------------------------
        #Sans la BDD
        
        nom = self.formulaire.nom_2.text()
        prenom = self.formulaire.prenom_2.text()
        mail = self.formulaire.mail_2.text()
        password = self.formulaire.motDePasse_2.text()
        confirmation = self.formulaire.confirmationMotdePasse_2.text()    
    
        print(f"compte {mail} cree !")


        #BDD
        conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "192.168.1.17",#172.20.10.3
            port = "5432",
            database = "eaux"
            )
        # création de l'utilisateur
        cur = conn.cursor()
        sql = f"CREATE USER {mail} WITH PASSWORD '{password}'"
        sql1 = f"GRANT SELECT ON ALL TABLES IN SCHEMA public TO {mail};"
        #identifiants = (mail,password)
        cur.execute(sql, sql1)
            
        # insertion de l'utilisateur dans la base de donnée
        cur = conn.cursor()
        sql = "INSERT INTO utilisateur (nom, prenom, email, motdepasse) VALUES (%s,%s,%s, crypt(%s,gen_salt('bf')))"
        values = (nom,prenom,mail,password)
        cur.execute(sql,values)
            
        # Vérification si l'utilisateur à été créé
        conn.commit()
        count = cur.rowcount
        print (count, "creation du compte.")
            
        cur.close()
        conn.close()
        
        alerte_create_account()
        self.design_page_formulaire.close()
        self.initialisationLogin()
        # ------------------------------------
        
    def back(self):
        self.design_page_formulaire.close()
        self.initialisationLogin()
        
        
    """----------------------------------------------------------------""" 
    """ ------ changement de bouton (partie mot de passe perdu) ------ """    
    """----------------------------------------------------------------"""

    def loosePassword(self):
        self.design_page_login.close()
        self.design_page_Motpasseoublie = QtWidgets.QWidget()
        self.motdepasse.page_PerteMdp(self.design_page_Motpasseoublie)
        
        self.motdepasse.retour.clicked.connect(self.back2)
        #self.motdepasse.boutonSeConnecter.clicked.connect[self.recuperation]

        self.design_page_Motpasseoublie.show()
        
    def back2(self):
        self.design_page_Motpasseoublie.close()
        self.initialisationLogin()
    
    
    
        
    
if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QtWidgets.QApplication(sys.argv)
        
    # On instancie une fenêtre graphique et l'affiche.
    application = Application()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())