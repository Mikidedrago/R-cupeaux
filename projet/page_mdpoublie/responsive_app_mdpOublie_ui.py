# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responsive_app_mdpOublie.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(513, 303)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username = QLineEdit(self.frame_2)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(True)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:black;\n"
"font-weight: bold;\n"
"padding-bottom:7px")

        self.horizontalLayout_3.addWidget(self.username)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.boutonSeConnecter = QPushButton(self.frame_3)
        self.boutonSeConnecter.setObjectName(u"boutonSeConnecter")
        self.boutonSeConnecter.setGeometry(QRect(20, 30, 200, 40))
        self.boutonSeConnecter.setMinimumSize(QSize(200, 40))
        self.boutonSeConnecter.setMaximumSize(QSize(400, 1677215))
        font2 = QFont()
        font2.setPointSize(12)
        self.boutonSeConnecter.setFont(font2)
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

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.retour = QPushButton(self.frame_4)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(30, 30, 200, 40))
        self.retour.setMinimumSize(QSize(200, 40))
        self.retour.setMaximumSize(QSize(400, 1677215))
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

        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"R\u00e9cup\u00e9ration du Mot de Passe", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"  Mail", None))
        self.boutonSeConnecter.setText(QCoreApplication.translate("Form", u"Envoyer", None))
        self.retour.setText(QCoreApplication.translate("Form", u"Retour", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    page_login = QWidget()
    ui = Ui_Form()
    ui.setupUi(page_login)
    page_login.show()
    sys.exit(app.exec_())
