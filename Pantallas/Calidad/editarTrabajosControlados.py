# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTrabajosControlados.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(534, 277)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 501, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_volver = QtWidgets.QPushButton(Form)
        self.ca_btn_volver.setGeometry(QtCore.QRect(290, 200, 131, 31))
        self.ca_btn_volver.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_volver.setObjectName("ca_btn_volver")
        self.ca_btn_eliminar = QtWidgets.QPushButton(Form)
        self.ca_btn_eliminar.setGeometry(QtCore.QRect(130, 200, 131, 31))
        self.ca_btn_eliminar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_eliminar.setObjectName("ca_btn_eliminar")
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(220, 120, 251, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 151, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Trabajos controlados"))
        self.label_2.setText(_translate("Form", "Eliminar Trabajo Controlado"))
        self.ca_btn_volver.setText(_translate("Form", "Volver"))
        self.ca_btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.label_4.setText(_translate("Form", "Número de Orden"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
