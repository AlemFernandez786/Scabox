# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarStockMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 663)
        self.ma_input_buscar = QtWidgets.QLineEdit(Form)
        self.ma_input_buscar.setGeometry(QtCore.QRect(310, 80, 251, 31))
        self.ma_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_buscar.setText("")
        self.ma_input_buscar.setObjectName("ma_input_buscar")
        self.ma_btn_buscar = QtWidgets.QPushButton(Form)
        self.ma_btn_buscar.setGeometry(QtCore.QRect(570, 80, 131, 31))
        self.ma_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_buscar.setObjectName("ma_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 80, 171, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ma_input_minimo = QtWidgets.QLineEdit(Form)
        self.ma_input_minimo.setEnabled(False)
        self.ma_input_minimo.setGeometry(QtCore.QRect(330, 420, 251, 31))
        self.ma_input_minimo.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.ma_input_minimo.setText("")
        self.ma_input_minimo.setObjectName("ma_input_minimo")
        self.ma_input_maximo = QtWidgets.QLineEdit(Form)
        self.ma_input_maximo.setEnabled(False)
        self.ma_input_maximo.setGeometry(QtCore.QRect(330, 370, 251, 31))
        self.ma_input_maximo.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.ma_input_maximo.setText("")
        self.ma_input_maximo.setObjectName("ma_input_maximo")
        self.ma_input_actual = QtWidgets.QLineEdit(Form)
        self.ma_input_actual.setEnabled(False)
        self.ma_input_actual.setGeometry(QtCore.QRect(330, 320, 251, 31))
        self.ma_input_actual.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.ma_input_actual.setText("")
        self.ma_input_actual.setObjectName("ma_input_actual")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 320, 111, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 420, 111, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 370, 121, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(270, 590, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(430, 590, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 470, 111, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ma_input_descripcion = QtWidgets.QTextEdit(Form)
        self.ma_input_descripcion.setEnabled(False)
        self.ma_input_descripcion.setGeometry(QtCore.QRect(330, 470, 251, 31))
        self.ma_input_descripcion.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.ma_input_descripcion.setObjectName("ma_input_descripcion")
        self.ma_tabla_datos = QtWidgets.QTreeWidget(Form)
        self.ma_tabla_datos.setGeometry(QtCore.QRect(10, 130, 821, 171))
        self.ma_tabla_datos.setObjectName("ma_tabla_datos")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla_datos.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla_datos.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla_datos.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla_datos.headerItem().setFont(5, font)
        self.ma_input_cantidad = QtWidgets.QLineEdit(Form)
        self.ma_input_cantidad.setEnabled(True)
        self.ma_input_cantidad.setGeometry(QtCore.QRect(330, 520, 251, 31))
        self.ma_input_cantidad.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_cantidad.setText("")
        self.ma_input_cantidad.setObjectName("ma_input_cantidad")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(200, 520, 111, 31))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_7.setObjectName("label_7")
        self.label.setBuddy(self.ma_input_buscar)
        self.label_3.setBuddy(self.ma_input_actual)
        self.label_5.setBuddy(self.ma_input_minimo)
        self.label_4.setBuddy(self.ma_input_maximo)
        self.label_6.setBuddy(self.ma_input_descripcion)
        self.label_7.setBuddy(self.ma_input_cantidad)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ma_input_buscar, self.ma_btn_buscar)
        Form.setTabOrder(self.ma_btn_buscar, self.ma_tabla_datos)
        Form.setTabOrder(self.ma_tabla_datos, self.ma_input_actual)
        Form.setTabOrder(self.ma_input_actual, self.ma_input_maximo)
        Form.setTabOrder(self.ma_input_maximo, self.ma_input_minimo)
        Form.setTabOrder(self.ma_input_minimo, self.ma_input_descripcion)
        Form.setTabOrder(self.ma_input_descripcion, self.ma_input_cantidad)
        Form.setTabOrder(self.ma_input_cantidad, self.ma_btn_confirmar)
        Form.setTabOrder(self.ma_btn_confirmar, self.ma_btn_cancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificación de stock"))
        self.ma_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese código del articulo"))
        self.label_2.setText(_translate("Form", "Modificacion de Stock (Materiales)"))
        self.label_3.setText(_translate("Form", "Cantidad actual"))
        self.label_5.setText(_translate("Form", "Cantidad mínima"))
        self.label_4.setText(_translate("Form", "Cantidad máxima"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_6.setText(_translate("Form", "Descripción"))
        self.ma_tabla_datos.headerItem().setText(0, _translate("Form", "Codigo"))
        self.ma_tabla_datos.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.ma_tabla_datos.headerItem().setText(2, _translate("Form", "Cantidad de Stock disponible"))
        self.ma_tabla_datos.headerItem().setText(3, _translate("Form", "Stock utilizado en los ultimos 30 dias"))
        self.ma_tabla_datos.headerItem().setText(4, _translate("Form", "Stock Minimo permitido"))
        self.ma_tabla_datos.headerItem().setText(5, _translate("Form", "Stock Maximo permitido"))
        self.label_7.setText(_translate("Form", "Ingreso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

