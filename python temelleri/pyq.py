import sys
from PyQt5 import QtWidgets
from PyQt5.OtWidgets import QApplication,QMainWindow

def window():
    app=QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    sys.exit(app.exec_())
window()
