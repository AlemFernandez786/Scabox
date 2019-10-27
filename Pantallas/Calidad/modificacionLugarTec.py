# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionLugarTec.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 284)
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(300, 170, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 191, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 421, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(80, 170, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_input_1 = QtWidgets.QComboBox(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(280, 80, 171, 25))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setObjectName("ca_input_1")
        self.ca_input_1.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 191, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ca_input_2 = QtWidgets.QComboBox(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(280, 120, 171, 25))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setObjectName("ca_input_2")
        self.ca_input_2.addItem("")
        self.ca_btn_registrar = QtWidgets.QPushButton(Form)
        self.ca_btn_registrar.setGeometry(QtCore.QRect(120, 220, 291, 41))
        self.ca_btn_registrar.setStyleSheet("background-color: #5f5fff;\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_registrar.setObjectName("ca_btn_registrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Moviles y Técnicos"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label.setText(_translate("Form", "Elija Nº de Legajo"))
        self.label_2.setText(_translate("Form", "Modificación de lugar del técnico"))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar cambio"))
        self.label_3.setText(_translate("Form", "Elija lugar o estado"))
        self.ca_btn_registrar.setText(_translate("Form", "Terminar y registrar Salida"))
        self.ca_input_1.setCurrentText(_translate("Form", "Seleccione un Técnico"))
        self.ca_input_1.setItemText(0, _translate("Form", "Seleccione un Técnico"))
        self.ca_input_2.setCurrentText(_translate("Form", "Seleccione un movil"))
        self.ca_input_2.setItemText(0, _translate("Form", "Seleccione un movil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
