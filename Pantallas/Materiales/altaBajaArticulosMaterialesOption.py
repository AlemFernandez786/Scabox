# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaBajaArticulosMaterialesOption.ui'
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
        self.ma_btn_alta = QtWidgets.QPushButton(Form)
        self.ma_btn_alta.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.ma_btn_alta.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_alta.setObjectName("ma_btn_alta")
        self.ma_btn_baja = QtWidgets.QPushButton(Form)
        self.ma_btn_baja.setGeometry(QtCore.QRect(190, 120, 151, 31))
        self.ma_btn_baja.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_baja.setObjectName("ma_btn_baja")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alta/Baja de artículos"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Alta/Baja de Artículos</span></p></body></html>"))
        self.ma_btn_alta.setText(_translate("Form", "ALTA"))
        self.ma_btn_baja.setText(_translate("Form", "BAJA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
