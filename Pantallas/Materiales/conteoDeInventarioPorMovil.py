# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conteoDeInventarioPorMovil.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 357)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-30, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ma_input_2 = QtWidgets.QLineEdit(Form)
        self.ma_input_2.setGeometry(QtCore.QRect(160, 150, 251, 31))
        self.ma_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_2.setText("")
        self.ma_input_2.setObjectName("ma_input_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 201, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 121, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.ma_input_1 = QtWidgets.QLineEdit(Form)
        self.ma_input_1.setGeometry(QtCore.QRect(160, 100, 251, 31))
        self.ma_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_1.setText("")
        self.ma_input_1.setObjectName("ma_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 51, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(240, 290, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(400, 290, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.ma_label_1 = QtWidgets.QLabel(Form)
        self.ma_label_1.setGeometry(QtCore.QRect(450, 110, 301, 131))
        self.ma_label_1.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"")
        self.ma_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ma_label_1.setObjectName("ma_label_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(560, 80, 101, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ma_input_3 = QtWidgets.QSpinBox(Form)
        self.ma_input_3.setGeometry(QtCore.QRect(240, 200, 171, 31))
        self.ma_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_3.setObjectName("ma_input_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Conteo de Inventario por Móvil"))
        self.label_5.setText(_translate("Form", "Cantidad de material contado"))
        self.label_4.setText(_translate("Form", "Codigó de Material"))
        self.label.setText(_translate("Form", "Móvil"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ma_label_1.setText(_translate("Form", "XX"))
        self.label_3.setText(_translate("Form", "Stock por Móvil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

