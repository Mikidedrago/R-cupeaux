from PyQt5.QtWidgets import QMessageBox


def alerte_create_account():
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Inscription")
    msgBox.setMinimumSize(100,20)
    msgBox.setText("SUCCES !!                                         ")
    msgBox.setInformativeText("Votre compte a été crée")
    returnValue = msgBox.exec()
    
def alerte_deconnexion():
    # Message de déconnexion
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Déconnexion")
    msgBox.setMinimumSize(100,20)
    msgBox.setText("Vous avez été déconnecté")
    returnValue = msgBox.exec()