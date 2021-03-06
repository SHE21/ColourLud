import sys
import cv2
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Capture'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('color.png')
        #label.setPixmap(pixmap)
        label.resize(400, 400)
        #label.move(120, 50)
        label.setStyleSheet("text-align: center;vertical-align: middle;")

        camera_port = 0
        camera = cv2.VideoCapture(0)

        while True:
            img = camera.read()[1]
            img2 = ImageTk.PhotoImage(Image.fromarray(img))
            label.setPixmap(img2)

        self.show()


    def other(self):
        label = QLabel(self)
        label.setText("Label")
        label.move(40, 40)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())
