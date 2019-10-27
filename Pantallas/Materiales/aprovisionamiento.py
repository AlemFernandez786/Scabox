# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aprovisionamiento.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 449)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 691, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(430, 380, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.ma_btn_modificar = QtWidgets.QPushButton(Form)
        self.ma_btn_modificar.setGeometry(QtCore.QRect(350, 340, 131, 31))
        self.ma_btn_modificar.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_modificar.setObjectName("ma_btn_modificar")
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(260, 380, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_tabla_datos = QtWidgets.QTreeWidget(Form)
        self.ma_tabla_datos.setGeometry(QtCore.QRect(20, 90, 801, 141))
        self.ma_tabla_datos.setObjectName("ma_tabla_datos")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla_datos.headerItem().setFont(2, font)
        self.ma_label_descripcion = QtWidgets.QLabel(Form)
        self.ma_label_descripcion.setGeometry(QtCore.QRect(230, 250, 381, 31))
        self.ma_label_descripcion.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_descripcion.setText("")
        self.ma_label_descripcion.setObjectName("ma_label_descripcion")
        self.ma_input_cantidad = QtWidgets.QSpinBox(Form)
        self.ma_input_cantidad.setGeometry(QtCore.QRect(230, 290, 381, 31))
        self.ma_input_cantidad.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_cantidad.setMaximum(9999)
        self.ma_input_cantidad.setObjectName("ma_input_cantidad")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aprovisionamiento"))
        self.label_2.setText(_translate("Form", "Aprovisionamiento"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_tabla_datos.headerItem().setText(0, _translate("Form", "Código"))
        self.ma_tabla_datos.headerItem().setText(1, _translate("Form", "Descripción"))
        self.ma_tabla_datos.headerItem().setText(2, _translate("Form", "Cantidad de pedido automático"))
        self.ma_btn_modificar.setText(_translate("Form", "Modificar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
