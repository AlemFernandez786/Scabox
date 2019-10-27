# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaDeArticulosMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(859, 381)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 781, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 171, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 161, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(250, 320, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(450, 320, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(440, 200, 121, 31))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_8.setObjectName("label_8")
        self.ma_input_ingreso = QtWidgets.QSpinBox(Form)
        self.ma_input_ingreso.setGeometry(QtCore.QRect(210, 110, 211, 31))
        self.ma_input_ingreso.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_ingreso.setMaximum(9999)
        self.ma_input_ingreso.setObjectName("ma_input_ingreso")
        self.ma_input_minima = QtWidgets.QSpinBox(Form)
        self.ma_input_minima.setGeometry(QtCore.QRect(210, 200, 211, 31))
        self.ma_input_minima.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_minima.setMaximum(9999)
        self.ma_input_minima.setObjectName("ma_input_minima")
        self.ma_input_maxima = QtWidgets.QSpinBox(Form)
        self.ma_input_maxima.setGeometry(QtCore.QRect(560, 200, 251, 31))
        self.ma_input_maxima.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_maxima.setMaximum(9999)
        self.ma_input_maxima.setObjectName("ma_input_maxima")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(440, 110, 121, 31))
        self.label_10.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_10.setObjectName("label_10")
        self.ma_input_descripcion = QtWidgets.QLineEdit(Form)
        self.ma_input_descripcion.setGeometry(QtCore.QRect(560, 110, 251, 31))
        self.ma_input_descripcion.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_descripcion.setObjectName("ma_input_descripcion")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ma_input_ingreso, self.ma_input_descripcion)
        Form.setTabOrder(self.ma_input_descripcion, self.ma_input_minima)
        Form.setTabOrder(self.ma_input_minima, self.ma_input_maxima)
        Form.setTabOrder(self.ma_input_maxima, self.ma_btn_confirmar)
        Form.setTabOrder(self.ma_btn_confirmar, self.ma_btn_cancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alta"))
        self.label_2.setText(_translate("Form", "Alta de Artículos"))
        self.label_4.setText(_translate("Form", "Cantidad que se ingresa"))
        self.label_5.setText(_translate("Form", "Cantidad minima"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_8.setText(_translate("Form", "Cantidad maxima"))
        self.label_10.setText(_translate("Form", "Descripción"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
