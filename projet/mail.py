import smtplib
from email.message import EmailMessage
from PyQt5.QtWidgets import QMessageBox


def recuperation(self):
        
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