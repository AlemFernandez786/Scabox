# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockPorMovilMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 498)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 231, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 320, 261, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ma_tabla_datos = QtWidgets.QTreeWidget(Form)
        self.ma_tabla_datos.setGeometry(QtCore.QRect(30, 80, 681, 131))
        self.ma_tabla_datos.setObjectName("ma_tabla_datos")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(2, font)
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(300, 410, 141, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 230, 81, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 260, 171, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.ma_label_descripcion = QtWidgets.QLabel(Form)
        self.ma_label_descripcion.setGeometry(QtCore.QRect(310, 230, 311, 31))
        self.ma_label_descripcion.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_descripcion.setText("")
        self.ma_label_descripcion.setObjectName("ma_label_descripcion")
        self.ma_label_stock = QtWidgets.QLabel(Form)
        self.ma_label_stock.setGeometry(QtCore.QRect(310, 260, 311, 31))
        self.ma_label_stock.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_stock.setText("")
        self.ma_label_stock.setObjectName("ma_label_stock")
        self.ma_input_cantidad = QtWidgets.QSpinBox(Form)
        self.ma_input_cantidad.setGeometry(QtCore.QRect(250, 360, 261, 31))
        self.ma_input_cantidad.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_cantidad.setMaximum(9999)
        self.ma_input_cantidad.setObjectName("ma_input_cantidad")
        self.ma_btn_salir = QtWidgets.QPushButton(Form)
        self.ma_btn_salir.setGeometry(QtCore.QRect(300, 450, 141, 31))
        self.ma_btn_salir.setStyleSheet("background-color: #ff4e4e;\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_salir.setObjectName("ma_btn_salir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock por Movil"))
        self.label_2.setText(_translate("Form", "Stock por Movil"))
        self.label_3.setText(_translate("Form", "Cantidad de materiales contados"))
        self.ma_tabla_datos.headerItem().setText(0, _translate("Form", "Código"))
        self.ma_tabla_datos.headerItem().setText(1, _translate("Form", "Descripción"))
        self.ma_tabla_datos.headerItem().setText(2, _translate("Form", "Cantidad de materiales"))
        self.ma_btn_confirmar.setText(_translate("Form", "Modificar"))
        self.label_4.setText(_translate("Form", "Descripción"))
        self.label_5.setText(_translate("Form", "Cantidad de materiales"))
        self.ma_btn_salir.setText(_translate("Form", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

