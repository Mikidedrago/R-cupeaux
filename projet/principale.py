# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principale.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import resPrincipale
from PyQt5 import QtCore, QtGui, QtWidgets
from graph import Graphique


class Principale(object):
    def setupUi3(self, Form):
        Form.setObjectName("Form")
        Form.resize(1925, 1120)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1920, 50))
        self.frame.setStyleSheet("background-color: #BFBFBF;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(880, 0, 291, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(1880, 14, 27, 27))
        self.frame_3.setStyleSheet("background-image: url(:/images/image/parametre.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.graphics = QtWidgets.QGraphicsView(Form)
        self.graphics.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.testest = QtWidgets.QLabel(Form)
        self.testest.setGeometry(20, 20, 300,300)
        self.testest.setObjectName("testest")
        
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 50, 50))
        self.frame_2.setStyleSheet("background-image: url(:/iconesMeteo/image/iconesMeteo/soleil.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 70, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 480, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(50, 180, 470, 281))
        self.frame_4.setStyleSheet("background-image: url(:/images/image/courbes.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1930, 1101))
        self.frame_5.setStyleSheet("QPushButton#boutonDeconnexion, {    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#boutonDeconnexion, :hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#boutonDeconnexion, :pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:(255, 255, 255, 210);\n"
"}\n"
"\n"
"\n"
"QPushButton#bouton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#bouton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#bouton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.boutonDeconnexion = QtWidgets.QPushButton(self.frame_5)
        self.boutonDeconnexion.setGeometry(QtCore.QRect(1530, 950, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boutonDeconnexion.setFont(font)
        self.boutonDeconnexion.setObjectName("boutonDeconnexion")
        self.boutonSeConnecter_2 = QtWidgets.QPushButton(self.frame_5)
        self.boutonSeConnecter_2.setGeometry(QtCore.QRect(1530, 1000, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boutonSeConnecter_2.setFont(font)
        self.boutonSeConnecter_2.setObjectName("boutonSeConnecter_2")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(5, 5, 1920, 1080))
        self.label_5.setStyleSheet("background-color: #FFFFFF;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        
        
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView.setGeometry(340, 610, 800, 600)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView = Graphique()
        
        
        self.label_5.raise_()
        self.boutonDeconnexion.raise_()
        self.boutonSeConnecter_2.raise_()
        self.graphicsView.raise_()
        self.frame_5.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.frame_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Date"))
        self.label_4.setText(_translate("Form", "Localisation cuve"))
        self.label.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "°C"))
        self.testest.setText(_translate("Form", "TESTEST"))
        self.boutonDeconnexion.setText(_translate("Form", "Deconnexion"))
        self.boutonSeConnecter_2.setText(_translate("Form", "Quitter"))


