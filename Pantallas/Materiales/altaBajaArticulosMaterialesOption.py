# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaBajaArticulosMaterialesOption.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 209)
        Form.setStyleSheet("background-color:white;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 51))
        self.label.setStyleSheet("font-size:20px;")
        self.label.setObjectName("label")
        self.ma_btn_1 = QtWidgets.QPushButton(Form)
        self.ma_btn_1.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.ma_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_1.setObjectName("ma_btn_1")
        self.ma_btn_2 = QtWidgets.QPushButton(Form)
        self.ma_btn_2.setGeometry(QtCore.QRect(190, 120, 151, 31))
        self.ma_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_2.setObjectName("ma_btn_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Alta/Baja de Articulos</span></p></body></html>"))
        self.ma_btn_1.setText(_translate("Form", "ALTA"))
        self.ma_btn_2.setText(_translate("Form", "BAJA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

