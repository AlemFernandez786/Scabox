# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaBajaArticulosHerramientasOption.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 209)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 51))
        self.label.setStyleSheet("font-size:20px;")
        self.label.setObjectName("label")
        self.he_btn_1 = QtWidgets.QPushButton(Form)
        self.he_btn_1.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.he_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_1.setObjectName("he_btn_1")
        self.he_btn_2 = QtWidgets.QPushButton(Form)
        self.he_btn_2.setGeometry(QtCore.QRect(190, 120, 151, 31))
        self.he_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_2.setObjectName("he_btn_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alta/Baja de Artículos"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Alta/Baja de Artículos</span></p></body></html>"))
        self.he_btn_1.setText(_translate("Form", "ALTA"))
        self.he_btn_2.setText(_translate("Form", "BAJA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
