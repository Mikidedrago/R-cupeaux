import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from accueil import Ui_MainWindow
from principal import Ui_Dialog

class Connexion(QMainWindow):
    def __init__(self):
        super(Connexion, self).__init__()
        self.page_une()

    def page_une(self):
        self.p1 = Ui_MainWindow()
        self.p1.setupUi(self)
        self.p1.pushButton.clicked.connect(self.page_deux)
        self.show()

    def page_deux(self):
        self.close()
        self.p2 = Ui_Dialog()
        self.p2.setupUi1(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Connexion()
    sys.exit(app.exec_())