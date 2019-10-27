# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaDeTrabajosVisitados.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(741, 516)
        Form.setStyleSheet("background-color: rgb(243, 243, 243);\n")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(590, 110, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 90, 541, 16))
        self.label.setObjectName("label")
        self.ca_input_buscar = QtWidgets.QLineEdit(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(30, 110, 551, 31))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 170, 721, 271))
        self.ca_tabla.setStyleSheet("border:none;")
        self.ca_tabla.setObjectName("ca_tabla")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(6, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(7, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(8, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(9, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(10, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(11, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(12, font)
        self.ca_btn_volver = QtWidgets.QPushButton(Form)
        self.ca_btn_volver.setGeometry(QtCore.QRect(300, 470, 131, 31))
        self.ca_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_volver.setObjectName("ca_btn_volver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Trabajos realizados"))
        self.label_2.setText(_translate("Form", "Consulta de trabajos realizados"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese  nº de orden:"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Nº de orden"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Domicilio"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Movil"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "Tecnico 1"))
        self.ca_tabla.headerItem().setText(4, _translate("Form", "Tecnico 2"))
        self.ca_tabla.headerItem().setText(5, _translate("Form", "Fecha"))
        self.ca_tabla.headerItem().setText(6, _translate("Form", "Nombre del abonado"))
        self.ca_tabla.headerItem().setText(7, _translate("Form", "DNI del abonado"))
        self.ca_tabla.headerItem().setText(8, _translate("Form", "Número de cliente"))
        self.ca_tabla.headerItem().setText(9, _translate("Form", "Códigos de finalizacion"))
        self.ca_tabla.headerItem().setText(10, _translate("Form", "Observaciones"))
        self.ca_tabla.headerItem().setText(11, _translate("Form", "MAC de los equipos instalados"))
        self.ca_tabla.headerItem().setText(12, _translate("Form", "Materiales utilizados"))
        self.ca_btn_volver.setText(_translate("Form", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
