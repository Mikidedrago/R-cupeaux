# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsive_app_formulaire.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import ressources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 623)
        Form.setMinimumSize(QSize(460, 500))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_17.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(500, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(30, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 30))
        self.frame_8.setStyleSheet(u"background-image: url(:/icones/icones/utilisateur.png);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.nom_2 = QLineEdit(self.frame)
        self.nom_2.setObjectName(u"nom_2")
        self.nom_2.setMinimumSize(QSize(150, 0))
        self.nom_2.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.nom_2.setFont(font1)
        self.nom_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")

        self.horizontalLayout_8.addWidget(self.nom_2)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(30, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setStyleSheet(u"background-image: url(:/icones/icones/utilisateur.png);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_9)

        self.prenom_2 = QLineEdit(self.frame_4)
        self.prenom_2.setObjectName(u"prenom_2")
        self.prenom_2.setFont(font1)
        self.prenom_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")

        self.horizontalLayout_9.addWidget(self.prenom_2)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(32, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setStyleSheet(u"background-image: url(:/icones/icones/enveloppe.png)")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_10)

        self.mail_2 = QLineEdit(self.frame_5)
        self.mail_2.setObjectName(u"mail_2")
        self.mail_2.setFont(font1)
        self.mail_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")

        self.horizontalLayout_10.addWidget(self.mail_2)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(Form)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(400, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 60))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(30, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setStyleSheet(u"background-image: url(:/icones/icones/cadenas-verrouille.png);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_11)

        self.motDePasse_2 = QLineEdit(self.frame_12)
        self.motDePasse_2.setObjectName(u"motDePasse_2")
        self.motDePasse_2.setFont(font1)
        self.motDePasse_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")
        self.motDePasse_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_11.addWidget(self.motDePasse_2)


        self.verticalLayout.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(400, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(30, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setStyleSheet(u"background-image: url(:/icones/icones/cadenas-verrouille.png);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_7)

        self.confirmationMotdePasse_2 = QLineEdit(self.frame_6)
        self.confirmationMotdePasse_2.setObjectName(u"confirmationMotdePasse_2")
        self.confirmationMotdePasse_2.setFont(font1)
        self.confirmationMotdePasse_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")
        self.confirmationMotdePasse_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_12.addWidget(self.confirmationMotdePasse_2)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"color: red;\n"
"font-size: 16px")

        self.horizontalLayout_14.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignRight)

        self.frame_13 = QFrame(Form)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 60))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.mailIncohrent_2 = QLabel(self.frame_13)
        self.mailIncohrent_2.setObjectName(u"mailIncohrent_2")
        self.mailIncohrent_2.setMaximumSize(QSize(16777215, 50))
        self.mailIncohrent_2.setStyleSheet(u"color: red;\n"
"font-size: 16px")

        self.horizontalLayout_13.addWidget(self.mailIncohrent_2)


        self.horizontalLayout.addWidget(self.frame_13, 0, Qt.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame_14 = QFrame(Form)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(200, 60))
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.sinscrire = QPushButton(self.frame_14)
        self.sinscrire.setObjectName(u"sinscrire")
        self.sinscrire.setMinimumSize(QSize(0, 40))
        self.sinscrire.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.sinscrire.setFont(font2)
        self.sinscrire.setStyleSheet(u"QPushButton#sinscrire{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#sinscrire:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#sinscrire:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:(255, 255, 255, 210);\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.sinscrire)


        self.horizontalLayout_2.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(Form)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(200, 60))
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.retour = QPushButton(self.frame_15)
        self.retour.setObjectName(u"retour")
        self.retour.setMinimumSize(QSize(0, 40))
        self.retour.setMaximumSize(QSize(16777215, 40))
        self.retour.setFont(font2)
        self.retour.setStyleSheet(u"QPushButton#retour{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#retour:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#retour:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:(255, 255, 255, 210);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.retour)


        self.horizontalLayout_2.addWidget(self.frame_15, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Cr\u00e9ation de votre compte", None))
        self.nom_2.setPlaceholderText(QCoreApplication.translate("Form", u" Nom", None))
        self.prenom_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Prenom", None))
        self.mail_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Mail", None))
        self.motDePasse_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Mot de Passe", None))
        self.confirmationMotdePasse_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Confirmation", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Mot de passe diff\u00e9rent", None))
        self.mailIncohrent_2.setText(QCoreApplication.translate("Form", u"Adresse incoh\u00e9rente", None))
        self.sinscrire.setText(QCoreApplication.translate("Form", u"S'inscrire", None))
        self.retour.setText(QCoreApplication.translate("Form", u"Retour", None))
    # retranslateUi

