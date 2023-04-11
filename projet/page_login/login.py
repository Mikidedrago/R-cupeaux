# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import resLogin
from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 672)
        # Masquer les contours blanc, le nom de la fenêtre et les boutons fermer, réduire etc
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 570, 670))
        self.frame.setStyleSheet("QPushButton#boutonSeConnecter{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#boutonSeConnecter:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#boutonSeConnecter:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:(255, 255, 255, 210);\n"
"}\n"
"\n"
"\n"
"QPushButton#boutonCreerCompte{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#boutonCreerCompte:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#boutonCreerCompte:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#boutonMotDePasseOublie{    \n"
"\n"
"    color: #FFFFFF;\n"
"    border:1px solid rgba(0, 0, 0, 0);\n"
"    border-bottom-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.fond = QtWidgets.QLabel(self.frame)
        self.fond.setGeometry(QtCore.QRect(10, 10, 550, 650))
        self.fond.setStyleSheet("border-radius : 20px;\n"
"background-image: url(:/images/Fond/fondA.png);")
        self.fond.setText("")
        self.fond.setObjectName("fond")
        self.boutonSeConnecter = QtWidgets.QPushButton(self.frame)
        self.boutonSeConnecter.setGeometry(QtCore.QRect(110, 480, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boutonSeConnecter.setFont(font)
        self.boutonSeConnecter.setObjectName("boutonSeConnecter")
        self.boutonCreerCompte = QtWidgets.QPushButton(self.frame)
        self.boutonCreerCompte.setGeometry(QtCore.QRect(110, 540, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boutonCreerCompte.setFont(font)
        self.boutonCreerCompte.setObjectName("boutonCreerCompte")
        self.boutonMotDePasseOublie = QtWidgets.QPushButton(self.frame)
        self.boutonMotDePasseOublie.setGeometry(QtCore.QRect(310, 390, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.boutonMotDePasseOublie.setFont(font)
        self.boutonMotDePasseOublie.setStyleSheet("")
        self.boutonMotDePasseOublie.setObjectName("boutonMotDePasseOublie")
        self.connexion = QtWidgets.QLabel(self.frame)
        self.connexion.setGeometry(QtCore.QRect(320, 80, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.connexion.setFont(font)
        self.connexion.setObjectName("connexion")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(80, 240, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"padding-bottom:7px")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(80, 320, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"font-weight: bold;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.image = QtWidgets.QLabel(self.frame)
        self.image.setGeometry(QtCore.QRect(100, 40, 150, 150))
        self.image.setStyleSheet("background-image: url(:/images/Fond/compte.png);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.information = QtWidgets.QLabel(self.frame)
        self.information.setGeometry(QtCore.QRect(120, 390, 180, 20))
        self.information.setStyleSheet("color: red;\n"
"font-size: 16px")
        self.information.setObjectName("information")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(93, 390, 21, 21))
        self.label_2.setStyleSheet("background-image: url(:/images/Fond/attention.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.fond.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.boutonSeConnecter.setText(_translate("Form", "Se connecter"))
        self.boutonCreerCompte.setText(_translate("Form", "Créer un compte"))
        self.boutonMotDePasseOublie.setText(_translate("Form", "Mot de passe oublié"))
        self.connexion.setText(_translate("Form", "Connexion"))
        self.username.setPlaceholderText(_translate("Form", "  Username"))
        self.password.setPlaceholderText(_translate("Form", "  Password"))
        self.information.setText(_translate("Form", "Informations incorrectes"))


