# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from socket import *
from codecs import decode
from PyQt5 import QtCore, QtGui, QtWidgets

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"


#server.connect(ADDRESS)

class Ui_MainWindow(object):
    def __init__(self):
        self.connFlag = 0
        self.greetings = "Welcome to the Chatroom. You have been connected to the server"
        self.server = socket(AF_INET, SOCK_STREAM)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnConn = QtWidgets.QPushButton(self.centralwidget)
        self.btnConn.setObjectName("btnConn")
        self.horizontalLayout.addWidget(self.btnConn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setEnabled(False)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout.addWidget(self.btnSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)


        self.btnConn.clicked.connect(lambda: self.pressedConn())
        self.btnSend.clicked.connect(lambda: self.pressedSend())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi-user Chat Room"))
        self.lblTitle.setText(_translate("MainWindow", "Want To Connect?"))
        self.label.setText(_translate("MainWindow", "Message:"))
        self.btnConn.setText(_translate("MainWindow", "Connect"))
        self.btnSend.setText(_translate("MainWindow", "Send"))

    def pressedConn(self):
        if self.connFlag == 0:
            self.server.connect(ADDRESS)
            self.textBrowser.append(decode(self.server.recv(BUFSIZE), CODE))
            self.btnSend.setEnabled(True)
            self.label.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.btnConn.setText("Disconnect")
            self.connFlag = 1
        else:
            #self.textBrowser.append(decode(self.server.recv(BUFSIZE), CODE))
            self.server.close()
            self.server = socket(AF_INET, SOCK_STREAM)
            self.btnSend.setEnabled(False)
            self.label.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.btnConn.setText("Connect")
            self.textBrowser.append("You've disconnected to the chat room")
            self.connFlag = 0
        
    def pressedSend(self):
        #print("Message: %s" % self.lineEdit.text())
        #self.textBrowser.append("From: %s" % self.lineEdit.text())
        self.server.send(bytes(self.lineEdit.text(), CODE))
        self.textBrowser.append(decode(self.server.recv(BUFSIZE), CODE))
        self.lineEdit.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

