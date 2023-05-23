import time
from PyQt5.QtCore import QTimer, QObject, pyqtSignal

class Timer_date(QObject):
    date_heure_updated = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.heure)
        self.timer.start()

    def heure(self):
        self.date_heure = str(time.strftime('%d/%m/%y %H:%M:%S', time.localtime()))
        print(self.date_heure)
        self.date_heure_updated.emit(self.date_heure)



