# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDir.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 267)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("BOLADO ESTOU")
        self.Browser = QtWidgets.QPushButton(self.centralwidget)
        self.Browser.setGeometry(QtCore.QRect(490, 30, 80, 31))
        self.Browser.setObjectName("Browser")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 100, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.getText)
        self.pushButton.setGeometry(QtCore.QRect(490, 100, 80, 31))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 200, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 200, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Software Colonometry"))
        self.label.setText(_translate("MainWindow", "Images Directory:"))
        self.Browser.setText(_translate("MainWindow", "Browser"))
        self.pushButton.setText(_translate("MainWindow", "Browser"))
        self.label_2.setText(_translate("MainWindow", "Directory to save CSV Files:"))
        self.pushButton_2.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_3.setText(_translate("MainWindow", "CANCEL"))

    def getText(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'D:\CURSOS', "Folder (*.dir)")
        self.textEdit.setText(fname[0])


if __name__ == "__main__":
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
