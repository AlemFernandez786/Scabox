# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionMaxMin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 400)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ma_label_descripcion = QtWidgets.QLabel(Form)
        self.ma_label_descripcion.setGeometry(QtCore.QRect(170, 20, 241, 31))
        self.ma_label_descripcion.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_descripcion.setObjectName("ma_label_1")
        self.ma_label_maximo = QtWidgets.QLabel(Form)
        self.ma_label_maximo.setGeometry(QtCore.QRect(170, 60, 251, 31))
        self.ma_label_maximo.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_maximo.setObjectName("ma_label_2")
        self.ma_label_minimo = QtWidgets.QLabel(Form)
        self.ma_label_minimo.setGeometry(QtCore.QRect(170, 100, 251, 31))
        self.ma_label_minimo.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_minimo.setObjectName("ma_label_3")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 230, 111, 31))
        self.label_10.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 180, 111, 31))
        self.label_11.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_11.setObjectName("label_11")
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(80, 330, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(240, 330, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.ma_input_maximo = QtWidgets.QSpinBox(Form)
        self.ma_input_maximo.setGeometry(QtCore.QRect(160, 230, 251, 31))
        self.ma_input_maximo.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_maximo.setMaximum(9999)
        self.ma_input_maximo.setObjectName("ma_input_maximo")
        self.ma_input_minimo = QtWidgets.QSpinBox(Form)
        self.ma_input_minimo.setGeometry(QtCore.QRect(160, 180, 251, 31))
        self.ma_input_minimo.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_minimo.setMaximum(9999)
        self.ma_input_minimo.setObjectName("ma_input_minimo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ma_input_minimo, self.ma_input_maximo)
        Form.setTabOrder(self.ma_input_maximo, self.ma_btn_confirmar)
        Form.setTabOrder(self.ma_btn_confirmar, self.ma_btn_cancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificación de stock máximo y mÍnimo"))
        self.label_4.setText(_translate("Form", "Material:"))
        self.label_5.setText(_translate("Form", "Cantidad minimo:"))
        self.label_6.setText(_translate("Form", "Cantidad maximo:"))
        self.ma_label_descripcion.setText(_translate("Form", ""))
        self.ma_label_maximo.setText(_translate("Form", ""))
        self.ma_label_minimo.setText(_translate("Form", ""))
        self.label_10.setText(_translate("Form", "Cantidad maximo"))
        self.label_11.setText(_translate("Form", "Cantidad minimo"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
