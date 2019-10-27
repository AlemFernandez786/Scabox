# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionSectorDePersonal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 300)
        self.su_btn_cancelar = QtWidgets.QPushButton(Form)
        self.su_btn_cancelar.setGeometry(QtCore.QRect(290, 250, 131, 31))
        self.su_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.su_btn_cancelar.setObjectName("su_btn_cancelar")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 110, 100, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(50, 153, 150, 31))
        self.label_1.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 521, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.su_input_1 = QtWidgets.QLineEdit(Form)
        self.su_input_1.setGeometry(QtCore.QRect(200, 110, 300, 31))
        self.su_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.su_input_1.setMaxLength(10)
        self.su_input_1.setObjectName("su_input_1")

        self.su_input_2 = QtWidgets.QLineEdit(Form)
        self.su_input_2.setGeometry(QtCore.QRect(210, 155, 290, 31))
        self.su_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.su_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.su_input_2.setMaxLength(10)
        self.su_input_2.setObjectName("su_input_2")

        self.su_btn_confirmar = QtWidgets.QPushButton(Form)
        self.su_btn_confirmar.setGeometry(QtCore.QRect(130, 250, 131, 31))
        self.su_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_confirmar.setObjectName("su_btn_confirmar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificación de sector"))
        self.su_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label.setText(_translate("Form", "Contraseña"))
        self.label_1.setText(_translate("Form", "Confirmar Contraseña"))
        self.label_2.setText(_translate("Form", "Ingrese Contraseña"))
        self.su_btn_confirmar.setText(_translate("Form", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())