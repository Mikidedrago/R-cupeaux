from database import connexion_bdd
import json

# Connexion à la base de donnée
conn = connexion_bdd()

# Exécution d'une requête SQL
cur = conn.cursor()

"""# valeur à ajouter
nom = input("nom : ")
prenom = input("prenom : ")
mail = input("mail : ")
password = input("password : ")"""


"""sql = "INSERT INTO utilisateur (nom, prenom, email, motdepasse) VALUES (%s,%s,%s,%s)"
values = (nom, prenom,mail,password)
cur.execute(sql,values)
"""
cur.execute("SELECT * FROM utilisateur")
res = cur.fetchall()


# Stocker les données extraites dans un dictionnaire
donnees_utilisateurs = {}
for ligne in res:
    donnees_utilisateurs[ligne[0]] = {
        "nom": ligne[1],
        "prenom": ligne[2],
        "email": ligne[3],
        "password": ligne[4]
    }

# Enregistrer les données dans un fichier JSON
with open("donnees_utilisateurs.json", "w") as fichier_json:
    json.dump(donnees_utilisateurs, fichier_json)

print("----------------------------------------")
print("----------------------------------------")


"""# Ouvrir le fichier JSON en mode lecture
with open("donnees_utilisateurs.json", "r") as fichier_json:
    donnees_utilisateurs = json.load(fichier_json)

# Itérer sur les étudiants et afficher leurs informations
for id_etudiant, etudiant in donnees_utilisateurs.items():
    print(f"Informations de l'étudiant {id_etudiant}:")
    print("- Prénom :", etudiant["prenom"])
    print("- Nom :", etudiant["nom"])
    print("- Email :", etudiant["email"])
    print("- Mot de passe :", etudiant["password"])"""

"""# Récupérer les informations de l'étudiant 1
etudiant_1 = donnees_utilisateurs["1"]
print("Informations de l'etudiant 1 :")
print("- Prenom :", etudiant_1["prenom"])
print("- Nom :", etudiant_1["nom"])
print("- Email :", etudiant_1["email"])
print("- Password :", etudiant_1["password"])

print("----------------------------------------")

# Récupérer les informations de l'étudiant 2
etudiant_2 = donnees_utilisateurs["2"]
print("Informations de l'etudiant 2 :")
print("- Prenom :", etudiant_2["prenom"])
print("- Nom :", etudiant_2["nom"])
print("- Email :", etudiant_2["email"])
print("- Password :", etudiant_2["password"])

print("----------------------------------------")

# Récupérer les informations de l'étudiant 3
etudiant_3 = donnees_utilisateurs["18"]
print("Informations de l'etudiant 3 :")
print("- Prenom :", etudiant_3["prenom"])
print("- Nom :", etudiant_3["nom"])
print("- Email :", etudiant_3["email"])
print("- Password :", etudiant_3["password"])
"""



"""# Ouvrir le fichier JSON en mode lecture
with open("donnees_utilisateurs.json", "r") as fichier_json:
    donnees_utilisateurs = json.load(fichier_json)

nombre_essaies = 0

# demander l'adresse mail
email_utilisateur = input("Entrez votre adresse e-mail : ")

while nombre_essaies < 3 :

    # Demander le mot de passe à l'utilisateur
    
    mot_de_passe_utilisateur = input("Entrez votre mot de passe : ")

    # Parcourir les utilisateurs pour trouver une correspondance adresse e-mail/mot de passe
    correspondance_trouvee = False
    for identifiant, utilisateur in donnees_utilisateurs.items():
        if utilisateur["email"] == email_utilisateur and utilisateur["password"] == mot_de_passe_utilisateur:
            print("Bienvenue,", utilisateur["prenom"])
            correspondance_trouvee = True
            break

    # Si aucune correspondance n'a été trouvée, afficher un message d'erreur
    if not correspondance_trouvee:
        print("Adresse e-mail ou mot de passe incorrect")
        
    nombre_essaies += 1
    if correspondance_trouvee == True:
        break"""