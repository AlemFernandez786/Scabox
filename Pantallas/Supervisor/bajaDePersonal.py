# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaDePersonal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 245)
        self.su_btn_cancelar = QtWidgets.QPushButton(Form)
        self.su_btn_cancelar.setGeometry(QtCore.QRect(290, 200, 131, 31))
        self.su_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.su_btn_cancelar.setObjectName("su_btn_cancelar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 110, 191, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 400, 31))
        self.label_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                 "text-align:center;")
        self.label_3.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 231, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.su_input_1 = QtWidgets.QLineEdit(Form)
        self.su_input_1.setGeometry(QtCore.QRect(240, 110, 281, 31))
        self.su_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_1.setText("")
        self.su_input_1.setObjectName("su_input_1")
        self.su_btn_confirmar = QtWidgets.QPushButton(Form)
        self.su_btn_confirmar.setGeometry(QtCore.QRect(120, 200, 131, 31))
        self.su_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_confirmar.setObjectName("su_btn_confirmar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Baja de Personal"))
        self.su_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label.setText(_translate("Form", "Ingrese Nº de Legajo"))
        self.label_2.setText(_translate("Form", "Baja de Personal"))
        self.label_3.setText(_translate("Form", "Nota: Solo se podrán eliminar técnicos que no hayan realizado ningún trabajo"))
        self.su_btn_confirmar.setText(_translate("Form", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
