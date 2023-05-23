python -m PyQt5.uic.pyuic -x responsive_app_login.ui -o responsive_app_login2.py 

pyrcc5 ressource.qrc -o ressource_rc.py  

Login
page_login


self.info_fausseFrame.hide()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page_login = QtWidgets.QWidget()
    ui = Login()
    ui.page_Login(page_login)
    page_login.show()
    sys.exit(app.exec_())
python -m PyQt5.uic.pyuic -x responsive_app_login_v2.ui -o responsive_app_login_v2.py 
