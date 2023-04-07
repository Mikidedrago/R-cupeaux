import sys 

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())