# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsive_app_login.ui'
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
import ressource_rc

class Ui_page_login(object):
    def setupUi(self, page_login):
        if not page_login.objectName():
            page_login.setObjectName(u"page_login")
        page_login.resize(600, 720)
        page_login.setMinimumSize(QSize(600, 720))
        page_login.setMaximumSize(QSize(16777215, 16777215))
        page_login.setStyleSheet(u"background:white;\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(page_login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer_4)

        self.image = QLabel(page_login)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(150, 152))
        self.image.setMaximumSize(QSize(150, 152))
        self.image.setStyleSheet(u"background-image: url(:/images/images/compte.png);")
        self.image.setPixmap(QPixmap(u":/images/images/compte.png"))
        self.image.setScaledContents(True)

        self.horizontalLayout1.addWidget(self.image)

        self.frame_2 = QFrame(page_login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout1.addWidget(self.frame_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer_6)

        self.frame = QFrame(page_login)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.connexion = QLabel(self.frame)
        self.connexion.setObjectName(u"connexion")
        self.connexion.setMinimumSize(QSize(0, 0))
        self.connexion.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.connexion.setFont(font)

        self.horizontalLayout.addWidget(self.connexion)


        self.horizontalLayout1.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout1)

        self.verticalLayout2_lineEdit = QVBoxLayout()
        self.verticalLayout2_lineEdit.setObjectName(u"verticalLayout2_lineEdit")
        self.usernameFrame = QFrame(page_login)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.usernameFrame.setMinimumSize(QSize(500, 0))
        self.usernameFrame.setMaximumSize(QSize(16777215, 100))
        self.usernameFrame.setFrameShape(QFrame.StyledPanel)
        self.usernameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.usernameFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.username = QLineEdit(self.usernameFrame)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setBold(True)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"font-weight: bold;\n"
"padding-bottom:7px")

        self.verticalLayout_5.addWidget(self.username)


        self.verticalLayout2_lineEdit.addWidget(self.usernameFrame, 0, Qt.AlignHCenter)

        self.passwordFrame = QFrame(page_login)
        self.passwordFrame.setObjectName(u"passwordFrame")
        self.passwordFrame.setMinimumSize(QSize(500, 0))
        self.passwordFrame.setMaximumSize(QSize(16777215, 100))
        self.passwordFrame.setFrameShape(QFrame.StyledPanel)
        self.passwordFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.passwordFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.password = QLineEdit(self.passwordFrame)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(16777215, 50))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"padding-bottom:7px;\n"
"font-weight: bold;")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password)


        self.verticalLayout2_lineEdit.addWidget(self.passwordFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout2_lineEdit)

        self.horizontalLayout3_icone_info_bouton = QHBoxLayout()
        self.horizontalLayout3_icone_info_bouton.setObjectName(u"horizontalLayout3_icone_info_bouton")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout3_icone_info_bouton.addItem(self.horizontalSpacer)

        self.iconeFrame = QFrame(page_login)
        self.iconeFrame.setObjectName(u"iconeFrame")
        self.iconeFrame.setMinimumSize(QSize(35, 35))
        self.iconeFrame.setMaximumSize(QSize(35, 35))
        self.iconeFrame.setStyleSheet(u"")
        self.iconeFrame.setFrameShape(QFrame.StyledPanel)
        self.iconeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.iconeFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.icone = QLabel(self.iconeFrame)
        self.icone.setObjectName(u"icone")
        self.icone.setMinimumSize(QSize(20, 20))
        self.icone.setMaximumSize(QSize(20, 20))
        self.icone.setStyleSheet(u"background-image: url(:/images/images/attention.png);")

        self.verticalLayout_8.addWidget(self.icone)


        self.horizontalLayout3_icone_info_bouton.addWidget(self.iconeFrame, 0, Qt.AlignHCenter)

        self.info_fausseFrame = QFrame(page_login)
        self.info_fausseFrame.setObjectName(u"info_fausseFrame")
        self.info_fausseFrame.setMaximumSize(QSize(16777215, 50))
        self.info_fausseFrame.setFrameShape(QFrame.StyledPanel)
        self.info_fausseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.info_fausseFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.information = QLabel(self.info_fausseFrame)
        self.information.setObjectName(u"information")
        self.information.setMaximumSize(QSize(16777215, 40))
        self.information.setStyleSheet(u"color: red;\n"
"font-size: 16px")

        self.verticalLayout_9.addWidget(self.information)


        self.horizontalLayout3_icone_info_bouton.addWidget(self.info_fausseFrame, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout3_icone_info_bouton.addItem(self.horizontalSpacer_2)

        self.motdepasseFrame = QFrame(page_login)
        self.motdepasseFrame.setObjectName(u"motdepasseFrame")
        self.motdepasseFrame.setMinimumSize(QSize(170, 0))
        self.motdepasseFrame.setMaximumSize(QSize(16777215, 50))
        self.motdepasseFrame.setFrameShape(QFrame.StyledPanel)
        self.motdepasseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.motdepasseFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.boutonMotDePasseOublie = QPushButton(self.motdepasseFrame)
        self.boutonMotDePasseOublie.setObjectName(u"boutonMotDePasseOublie")
        self.boutonMotDePasseOublie.setMinimumSize(QSize(200, 20))
        self.boutonMotDePasseOublie.setMaximumSize(QSize(200, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.boutonMotDePasseOublie.setFont(font2)
        self.boutonMotDePasseOublie.setStyleSheet(u"\n"
"QPushButton#boutonMotDePasseOublie{	\n"
"\n"
"	color: black;\n"
"	border:1px solid rgba(0, 0, 0, 0);\n"
"	border-bottom-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"")

        self.verticalLayout_10.addWidget(self.boutonMotDePasseOublie)


        self.horizontalLayout3_icone_info_bouton.addWidget(self.motdepasseFrame, 0, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout3_icone_info_bouton.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout3_icone_info_bouton)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.seConnecterFrame = QFrame(page_login)
        self.seConnecterFrame.setObjectName(u"seConnecterFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seConnecterFrame.sizePolicy().hasHeightForWidth())
        self.seConnecterFrame.setSizePolicy(sizePolicy)
        self.seConnecterFrame.setMinimumSize(QSize(400, 40))
        self.seConnecterFrame.setMaximumSize(QSize(16777215, 60))
        self.seConnecterFrame.setFrameShape(QFrame.StyledPanel)
        self.seConnecterFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.seConnecterFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.boutonSeConnecter = QPushButton(self.seConnecterFrame)
        self.boutonSeConnecter.setObjectName(u"boutonSeConnecter")
        self.boutonSeConnecter.setMinimumSize(QSize(0, 40))
        self.boutonSeConnecter.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(12)
        self.boutonSeConnecter.setFont(font3)
        self.boutonSeConnecter.setStyleSheet(u"QPushButton#boutonSeConnecter{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#boutonSeConnecter:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#boutonSeConnecter:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:(255, 255, 255, 210);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.boutonSeConnecter)


        self.verticalLayout_2.addWidget(self.seConnecterFrame, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(page_login)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.boutonCreerCompte = QPushButton(self.frame_4)
        self.boutonCreerCompte.setObjectName(u"boutonCreerCompte")
        self.boutonCreerCompte.setMinimumSize(QSize(0, 40))
        self.boutonCreerCompte.setMaximumSize(QSize(16777215, 40))
        self.boutonCreerCompte.setFont(font3)
        self.boutonCreerCompte.setStyleSheet(u"QPushButton#boutonCreerCompte{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#boutonCreerCompte:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#boutonCreerCompte:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")

        self.verticalLayout_7.addWidget(self.boutonCreerCompte)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(page_login)

        QMetaObject.connectSlotsByName(page_login)
    # setupUi

    def retranslateUi(self, page_login):
        page_login.setWindowTitle(QCoreApplication.translate("page_login", u"Form", None))
        self.image.setText("")
        self.connexion.setText(QCoreApplication.translate("page_login", u"Connexion", None))
        self.username.setPlaceholderText(QCoreApplication.translate("page_login", u"  Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("page_login", u"  Password", None))
        self.icone.setText("")
        self.information.setText(QCoreApplication.translate("page_login", u"Informations incorrectes", None))
        self.boutonMotDePasseOublie.setText(QCoreApplication.translate("page_login", u"Mot de passe oubli\u00e9", None))
        self.boutonSeConnecter.setText(QCoreApplication.translate("page_login", u"Se connecter", None))
        self.boutonCreerCompte.setText(QCoreApplication.translate("page_login", u"Cr\u00e9er un compte", None))
    # retranslateUi

