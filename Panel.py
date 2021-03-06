from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def window():
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Text")

    label = QLabel(win)
    image = QPixmap('images/imagenTeste1.png')
    label.setPixmap(image)

    win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window()
    sys.exit(app.exec_())
