

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_inicio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_inicio.setGeometry(QtCore.QRect(340, 310, 121, 41))
        self.btn_inicio.setObjectName("btn_inicio")
        self.btn_inicio.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.input_legajo = QtWidgets.QLineEdit(self.centralwidget)
        self.input_legajo.setGeometry(QtCore.QRect(330, 209, 191, 31))
        self.input_legajo.setObjectName("input_legajo")
        self.input_legajo.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.input_legajo.setText("")
        self.input_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pass.setGeometry(QtCore.QRect(330, 250, 191, 31))
        self.input_pass.setObjectName("input_pass")
        self.input_pass.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.input_pass.setText("")
        self.label_bienvenido = QtWidgets.QLabel(self.centralwidget)
        self.label_bienvenido.setGeometry(QtCore.QRect(260, 90, 321, 71))
        self.label_bienvenido.setObjectName("label_bienvenido")
        self.label_legajo = QtWidgets.QLabel(self.centralwidget)
        self.label_legajo.setGeometry(QtCore.QRect(190, 210, 111, 31))
        self.label_legajo.setObjectName("label_legajo")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(190, 250, 111, 31))
        self.label_pass.setObjectName("label_pass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScaBox"))
        self.btn_inicio.setText(_translate("MainWindow", "INICIAR"))
        self.label_bienvenido.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido</span></p></body></html>"))
        self.label_legajo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Legajo</span></p></body></html>"))
        self.label_pass.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Contraseña</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
