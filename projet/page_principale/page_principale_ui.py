# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_principale.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import ressources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1918, 1073)
        Form.setMaximumSize(QSize(1920, 1080))
        Form.setMouseTracking(False)
        Form.setStyleSheet(u"background: white;")
        self.barre_etat = QFrame(Form)
        self.barre_etat.setObjectName(u"barre_etat")
        self.barre_etat.setGeometry(QRect(0, 0, 1920, 50))
        self.barre_etat.setStyleSheet(u"background: #7F7F7F;")
        self.barre_etat.setFrameShape(QFrame.StyledPanel)
        self.barre_etat.setFrameShadow(QFrame.Raised)
        self.barre_avec_boutons = QFrame(self.barre_etat)
        self.barre_avec_boutons.setObjectName(u"barre_avec_boutons")
        self.barre_avec_boutons.setGeometry(QRect(0, 0, 1920, 50))
        self.barre_avec_boutons.setMaximumSize(QSize(1920, 16777215))
        self.barre_avec_boutons.setFrameShape(QFrame.StyledPanel)
        self.barre_avec_boutons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.barre_avec_boutons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boutonQuitter = QPushButton(self.barre_avec_boutons)
        self.boutonQuitter.setObjectName(u"boutonQuitter")
        self.boutonQuitter.setMinimumSize(QSize(0, 20))
        self.boutonQuitter.setMaximumSize(QSize(20, 16777215))
        self.boutonQuitter.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.boutonQuitter)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.boutonReduire = QPushButton(self.barre_avec_boutons)
        self.boutonReduire.setObjectName(u"boutonReduire")
        self.boutonReduire.setMinimumSize(QSize(0, 20))
        self.boutonReduire.setMaximumSize(QSize(20, 16777215))
        self.boutonReduire.setStyleSheet(u"border: none;\n"
"background-color: #F8A200;\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.boutonReduire)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.boutonAgrandir = QPushButton(self.barre_avec_boutons)
        self.boutonAgrandir.setObjectName(u"boutonAgrandir")
        self.boutonAgrandir.setMinimumSize(QSize(0, 20))
        self.boutonAgrandir.setMaximumSize(QSize(20, 16777215))
        self.boutonAgrandir.setStyleSheet(u"border: none;\n"
"background-color: rgb(0, 148, 0);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.boutonAgrandir)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.localisation = QLabel(self.barre_avec_boutons)
        self.localisation.setObjectName(u"localisation")
        self.localisation.setMinimumSize(QSize(0, 30))
        self.localisation.setStyleSheet(u"border : 2px solid black;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border-radius: 5px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.localisation)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.barre_avec_boutons)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 35))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.boutonDeconnexion = QPushButton(self.frame)
        self.boutonDeconnexion.setObjectName(u"boutonDeconnexion")
        self.boutonDeconnexion.setGeometry(QRect(40, 0, 30, 30))
        self.boutonDeconnexion.setMinimumSize(QSize(30, 30))
        self.boutonDeconnexion.setMaximumSize(QSize(30, 30))
        self.boutonDeconnexion.setStyleSheet(u"border: none;\n"
"background-image: url(:/autre/icones/log-out.png);\n"
"")

        self.horizontalLayout.addWidget(self.frame)

        self.main = QFrame(Form)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 51, 1920, 1030))
        self.main.setStyleSheet(u"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.mainFrame = QFrame(self.main)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(60, 50, 1820, 931))
        self.mainFrame.setStyleSheet(u"QFrame#mainFrame {\n"
"	\n"
"	background-color: #FEFEE2;\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.graphiqueFrame = QFrame(self.mainFrame)
        self.graphiqueFrame.setObjectName(u"graphiqueFrame")
        self.graphiqueFrame.setGeometry(QRect(970, 20, 811, 530))
        self.graphiqueFrame.setStyleSheet(u"background-color: #FEFEE2;")
        self.graphiqueFrame.setFrameShape(QFrame.StyledPanel)
        self.graphiqueFrame.setFrameShadow(QFrame.Raised)
        self.graphique = QGraphicsView(self.graphiqueFrame)
        self.graphique.setObjectName(u"graphique")
        self.graphique.setGeometry(QRect(20, 20, 771, 500))
        self.graphique.setStyleSheet(u"border: none;")
        self.informationFrame = QFrame(self.mainFrame)
        self.informationFrame.setObjectName(u"informationFrame")
        self.informationFrame.setGeometry(QRect(40, 560, 1730, 340))
        self.informationFrame.setStyleSheet(u"background-color: #FFE9B7;\n"
"border-radius: 8px;\n"
"box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.5);")
        self.informationFrame.setFrameShape(QFrame.StyledPanel)
        self.informationFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.informationFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 40, 1611, 252))
        self.horizontalLayout_infocuve_et_etatPompe = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_infocuve_et_etatPompe.setObjectName(u"horizontalLayout_infocuve_et_etatPompe")
        self.horizontalLayout_infocuve_et_etatPompe.setContentsMargins(0, 0, 0, 0)
        self.infoCuve = QFrame(self.horizontalLayoutWidget)
        self.infoCuve.setObjectName(u"infoCuve")
        self.infoCuve.setMinimumSize(QSize(0, 200))
        self.infoCuve.setMaximumSize(QSize(16777215, 300))
        self.infoCuve.setStyleSheet(u"QFrame#infoCuve {\n"
"	border: 2px solid red;\n"
"}")
        self.infoCuve.setFrameShape(QFrame.StyledPanel)
        self.infoCuve.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.infoCuve)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 631, 231))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)


        self.horizontalLayout_infocuve_et_etatPompe.addWidget(self.infoCuve)

        self.horizontalSpacer_5 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_infocuve_et_etatPompe.addItem(self.horizontalSpacer_5)

        self.etatPompe = QFrame(self.horizontalLayoutWidget)
        self.etatPompe.setObjectName(u"etatPompe")
        self.etatPompe.setMinimumSize(QSize(0, 200))
        self.etatPompe.setMaximumSize(QSize(16777215, 300))
        self.etatPompe.setStyleSheet(u"border: 2px solid blue")
        self.etatPompe.setFrameShape(QFrame.StyledPanel)
        self.etatPompe.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.etatPompe)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 631, 231))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)


        self.horizontalLayout_infocuve_et_etatPompe.addWidget(self.etatPompe)

        self.cuve = QFrame(self.mainFrame)
        self.cuve.setObjectName(u"cuve")
        self.cuve.setGeometry(QRect(470, 90, 196, 325))
        self.cuve.setMinimumSize(QSize(0, 0))
        self.cuve.setStyleSheet(u"QFrame#cuve {\n"
"	border: 2px solid black;\n"
"	border-radius: 30px;\n"
"}")
        self.cuve.setFrameShape(QFrame.StyledPanel)
        self.cuve.setFrameShadow(QFrame.Raised)
        self.niveau_0pourcent = QFrame(self.cuve)
        self.niveau_0pourcent.setObjectName(u"niveau_0pourcent")
        self.niveau_0pourcent.setGeometry(QRect(20, 303, 151, 20))
        self.niveau_0pourcent.setStyleSheet(u"border-bottom:5px solid blue;\n"
"")
        self.niveau_0pourcent.setFrameShape(QFrame.StyledPanel)
        self.niveau_0pourcent.setFrameShadow(QFrame.Raised)
        self.niveau_25pourcent = QFrame(self.cuve)
        self.niveau_25pourcent.setObjectName(u"niveau_25pourcent")
        self.niveau_25pourcent.setGeometry(QRect(0, 220, 200, 101))
        self.niveau_25pourcent.setStyleSheet(u"background-color: blue;\n"
"border-radius: 30px;\n"
"")
        self.niveau_25pourcent.setFrameShape(QFrame.StyledPanel)
        self.niveau_25pourcent.setFrameShadow(QFrame.Raised)
        self.niveau_50pourcent = QFrame(self.cuve)
        self.niveau_50pourcent.setObjectName(u"niveau_50pourcent")
        self.niveau_50pourcent.setGeometry(QRect(0, 140, 200, 181))
        self.niveau_50pourcent.setStyleSheet(u"background-color: blue;\n"
"border-radius: 30px;\n"
"")
        self.niveau_50pourcent.setFrameShape(QFrame.StyledPanel)
        self.niveau_50pourcent.setFrameShadow(QFrame.Raised)
        self.niveau_75pourcent = QFrame(self.cuve)
        self.niveau_75pourcent.setObjectName(u"niveau_75pourcent")
        self.niveau_75pourcent.setGeometry(QRect(0, 70, 200, 251))
        self.niveau_75pourcent.setStyleSheet(u"background-color: blue;\n"
"border-radius: 30px;\n"
"")
        self.niveau_75pourcent.setFrameShape(QFrame.StyledPanel)
        self.niveau_75pourcent.setFrameShadow(QFrame.Raised)
        self.niveau_100pourcent = QFrame(self.cuve)
        self.niveau_100pourcent.setObjectName(u"niveau_100pourcent")
        self.niveau_100pourcent.setGeometry(QRect(0, 0, 200, 320))
        self.niveau_100pourcent.setStyleSheet(u"background-color: blue;\n"
"border-radius: 30px;\n"
"")
        self.niveau_100pourcent.setFrameShape(QFrame.StyledPanel)
        self.niveau_100pourcent.setFrameShadow(QFrame.Raised)
        self.pourcentageCuve = QLabel(self.niveau_100pourcent)
        self.pourcentageCuve.setObjectName(u"pourcentageCuve")
        self.pourcentageCuve.setGeometry(QRect(60, 145, 100, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pourcentageCuve.setFont(font)
        self.pourcentageCuve.setStyleSheet(u"padding-left:6px;\n"
"border: none;\n"
"color:red;")
        self.label_2 = QLabel(self.mainFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 40, 191, 50))
        self.label_2.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: #FEFEE2;\n"
"magin-bottom: 40px;\n"
"word-wrap: break-word;\n"
"")
        self.main_frame_meteo = QFrame(self.mainFrame)
        self.main_frame_meteo.setObjectName(u"main_frame_meteo")
        self.main_frame_meteo.setGeometry(QRect(40, 40, 210, 421))
        self.main_frame_meteo.setStyleSheet(u"border: 1px solid;\n"
"background-color: rgb(240, 240, 220);")
        self.main_frame_meteo.setFrameShape(QFrame.StyledPanel)
        self.main_frame_meteo.setFrameShadow(QFrame.Raised)
        self.frameMeteo = QFrame(self.main_frame_meteo)
        self.frameMeteo.setObjectName(u"frameMeteo")
        self.frameMeteo.setGeometry(QRect(1, 1, 209, 50))
        self.frameMeteo.setFrameShape(QFrame.StyledPanel)
        self.frameMeteo.setFrameShadow(QFrame.Raised)
        self.titreMeteo = QLabel(self.frameMeteo)
        self.titreMeteo.setObjectName(u"titreMeteo")
        self.titreMeteo.setGeometry(QRect(55, 10, 111, 30))
        self.titreMeteo.setFont(font1)
        self.titreMeteo.setStyleSheet(u"border:none;\n"
"padding-left:15px;\n"
"")
        self.iconeOrage = QLabel(self.main_frame_meteo)
        self.iconeOrage.setObjectName(u"iconeOrage")
        self.iconeOrage.setGeometry(QRect(30, 80, 150, 150))
        self.iconeOrage.setStyleSheet(u"background-image: url(:/meteo/icones/pluie.png);\n"
"border:none;")
        self.iconeOrage.setPixmap(QPixmap(u":/meteo/icones/pluie.png"))
        self.iconeOrage.setScaledContents(True)
        self.iconeNeige = QLabel(self.main_frame_meteo)
        self.iconeNeige.setObjectName(u"iconeNeige")
        self.iconeNeige.setGeometry(QRect(30, 80, 150, 150))
        self.iconeNeige.setStyleSheet(u"background-image: url(:/meteo/icones/flocon-de-neige.png);\n"
"border:none;")
        self.iconeNeige.setPixmap(QPixmap(u":/meteo/icones/flocon-de-neige.png"))
        self.iconeNeige.setScaledContents(True)
        self.iconeNuage = QLabel(self.main_frame_meteo)
        self.iconeNuage.setObjectName(u"iconeNuage")
        self.iconeNuage.setGeometry(QRect(30, 80, 150, 150))
        self.iconeNuage.setStyleSheet(u"background-image: url(:/meteo/icones/nuage.png);\n"
"border:none;")
        self.iconeNuage.setPixmap(QPixmap(u":/meteo/icones/nuage.png"))
        self.iconeNuage.setScaledContents(True)
        self.iconePluie = QLabel(self.main_frame_meteo)
        self.iconePluie.setObjectName(u"iconePluie")
        self.iconePluie.setGeometry(QRect(30, 80, 150, 150))
        self.iconePluie.setStyleSheet(u"background-image: url(:/meteo/icones/pluie-abondante.png);\n"
"border:none;")
        self.iconePluie.setPixmap(QPixmap(u":/meteo/icones/pluie-abondante.png"))
        self.iconePluie.setScaledContents(True)
        self.iconeSoleil = QLabel(self.main_frame_meteo)
        self.iconeSoleil.setObjectName(u"iconeSoleil")
        self.iconeSoleil.setGeometry(QRect(30, 80, 150, 150))
        self.iconeSoleil.setStyleSheet(u"background-image: url(:/meteo/icones/soleil.png);\n"
"border:none;")
        self.iconeSoleil.setPixmap(QPixmap(u":/meteo/icones/soleil.png"))
        self.iconeSoleil.setScaledContents(True)
        self.iconeSoleilNuage = QLabel(self.main_frame_meteo)
        self.iconeSoleilNuage.setObjectName(u"iconeSoleilNuage")
        self.iconeSoleilNuage.setGeometry(QRect(30, 80, 150, 150))
        self.iconeSoleilNuage.setStyleSheet(u"background-image: url(:/meteo/icones/soleil_nuage.png);\n"
"border:none;")
        self.iconeSoleilNuage.setPixmap(QPixmap(u":/meteo/icones/soleil_nuage.png"))
        self.iconeSoleilNuage.setScaledContents(True)
        self.frameDescriptionTemps = QFrame(self.main_frame_meteo)
        self.frameDescriptionTemps.setObjectName(u"frameDescriptionTemps")
        self.frameDescriptionTemps.setGeometry(QRect(30, 230, 150, 111))
        self.frameDescriptionTemps.setStyleSheet(u"border: none;")
        self.frameDescriptionTemps.setFrameShape(QFrame.StyledPanel)
        self.frameDescriptionTemps.setFrameShadow(QFrame.Raised)
        self.descriptionTemps = QLabel(self.frameDescriptionTemps)
        self.descriptionTemps.setObjectName(u"descriptionTemps")
        self.descriptionTemps.setGeometry(QRect(35, 5, 80, 30))
        font2 = QFont()
        font2.setPointSize(8)
        self.descriptionTemps.setFont(font2)
        self.descriptionTemps.setStyleSheet(u"")
        self.chiffreTemperature = QLabel(self.frameDescriptionTemps)
        self.chiffreTemperature.setObjectName(u"chiffreTemperature")
        self.chiffreTemperature.setGeometry(QRect(35, 50, 40, 24))
        self.chiffreTemperature.setFont(font2)
        self.chiffreTemperature.setStyleSheet(u"")
        self.Unitee = QLabel(self.frameDescriptionTemps)
        self.Unitee.setObjectName(u"Unitee")
        self.Unitee.setGeometry(QRect(80, 50, 30, 20))
        self.Unitee.setFont(font2)
        self.Unitee.setStyleSheet(u"border:none;")
        self.ligne = QFrame(Form)
        self.ligne.setObjectName(u"ligne")
        self.ligne.setGeometry(QRect(0, 50, 1920, 2))
        self.ligne.setStyleSheet(u"background-color: black;")
        self.ligne.setFrameShape(QFrame.StyledPanel)
        self.ligne.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)
        self.boutonQuitter.clicked.connect(Form.close)
        self.boutonReduire.clicked.connect(Form.showMinimized)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Page Principale", None))
        self.boutonQuitter.setText("")
        self.boutonReduire.setText("")
        self.boutonAgrandir.setText("")
        self.localisation.setText(QCoreApplication.translate("Form", u"Cuve De ", None))
        self.boutonDeconnexion.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Niveau d'eau", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"D\u00e9bit", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Vide dans :", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Temp\u00e9ratuer de l'eau", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pourcentageCuve.setText(QCoreApplication.translate("Form", u"100%", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Niveau de la cuve", None))
        self.titreMeteo.setText(QCoreApplication.translate("Form", u"M\u00e9teo", None))
        self.iconeOrage.setText("")
        self.iconeNeige.setText("")
        self.iconeNuage.setText("")
        self.iconePluie.setText("")
        self.iconeSoleil.setText("")
        self.iconeSoleilNuage.setText("")
        self.descriptionTemps.setText("")
        self.chiffreTemperature.setText("")
        self.Unitee.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    page_login = QWidget()
    ui = Ui_Form()
    ui.setupUi(page_login)
    page_login.show()
    sys.exit(app.exec_())
