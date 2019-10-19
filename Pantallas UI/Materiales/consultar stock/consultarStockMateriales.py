# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarStockMaterialesPrueba.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 518)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(750, 60, 171, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ma_input_buscar = QtWidgets.QLineEdit(Form)
        self.ma_input_buscar.setGeometry(QtCore.QRect(360, 120, 251, 31))
        self.ma_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_buscar.setObjectName("ma_input_buscar")
        self.ma_btn_buscar = QtWidgets.QPushButton(Form)
        self.ma_btn_buscar.setGeometry(QtCore.QRect(620, 119, 131, 31))
        self.ma_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_buscar.setObjectName("ma_btn_buscar")
        self.ma_tabla_datos = QtWidgets.QTreeWidget(Form)
        self.ma_tabla_datos.setGeometry(QtCore.QRect(10, 180, 911, 251))
        self.ma_tabla_datos.setObjectName("ma_tabla_datos")
        self.ma_btn_volver = QtWidgets.QPushButton(Form)
        self.ma_btn_volver.setGeometry(QtCore.QRect(380, 460, 131, 31))
        self.ma_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_volver.setObjectName("ma_btn_volver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Consulta de Stock"))
        self.label.setText(_translate("Form", "Consulta Stock"))
        self.label_2.setText(_translate("Form", "Materiales"))
        self.label_3.setText(_translate("Form", "Ingrese código de artículo"))
        self.ma_btn_buscar.setText(_translate("Form", "Buscar"))
        self.ma_tabla_datos.headerItem().setText(0, _translate("Form", "Código"))
        self.ma_tabla_datos.headerItem().setText(1, _translate("Form", "Descripción"))
        self.ma_tabla_datos.headerItem().setText(2, _translate("Form", "Stock"))
        self.ma_tabla_datos.headerItem().setText(3, _translate("Form", "Cantidad de Stock últimos 30 días"))
        self.ma_tabla_datos.headerItem().setText(4, _translate("Form", "Stock mínimo"))
        self.ma_tabla_datos.headerItem().setText(5, _translate("Form", "Stock máximo"))
        self.ma_btn_volver.setText(_translate("Form", "volver"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
