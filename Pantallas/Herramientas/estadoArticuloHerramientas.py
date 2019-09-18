# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadoArticuloHerramientas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 417)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-30, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.he_input_buscar = QtWidgets.QLineEdit(Form)
        self.he_input_buscar.setGeometry(QtCore.QRect(220, 80, 251, 31))
        self.he_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_input_buscar.setText("")
        self.he_input_buscar.setObjectName("he_input_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 80, 121, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.he_btn_confirmar = QtWidgets.QPushButton(Form)
        self.he_btn_confirmar.setGeometry(QtCore.QRect(240, 350, 131, 31))
        self.he_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_confirmar.setObjectName("he_btn_confirmar")
        self.he_btn_cancelar = QtWidgets.QPushButton(Form)
        self.he_btn_cancelar.setGeometry(QtCore.QRect(400, 350, 131, 31))
        self.he_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.he_btn_cancelar.setObjectName("he_btn_cancelar")
        self.he_btn_buscar = QtWidgets.QPushButton(Form)
        self.he_btn_buscar.setGeometry(QtCore.QRect(480, 80, 131, 31))
        self.he_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_buscar.setObjectName("he_btn_buscar")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 130, 121, 31))
        self.label_3.setStyleSheet("font:10pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(580, 130, 121, 31))
        self.label_4.setStyleSheet("font:10pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.he_label_1 = QtWidgets.QLabel(Form)
        self.he_label_1.setGeometry(QtCore.QRect(40, 160, 351, 41))
        self.he_label_1.setStyleSheet("font-size:20px;\n"
"")
        self.he_label_1.setText("")
        self.he_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.he_label_1.setObjectName("he_label_1")
        self.he_label_2 = QtWidgets.QLabel(Form)
        self.he_label_2.setGeometry(QtCore.QRect(440, 160, 341, 41))
        self.he_label_2.setStyleSheet("font-size:20px;\n"
"")
        self.he_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.he_label_2.setObjectName("he_label_2")
        self.he_btn_estado = QtWidgets.QPushButton(Form)
        self.he_btn_estado.setGeometry(QtCore.QRect(500, 250, 131, 31))
        self.he_btn_estado.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_estado.setObjectName("he_btn_estado")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 250, 121, 31))
        self.label_7.setStyleSheet("font:10pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_7.setObjectName("label_7")
        self.he_select = QtWidgets.QComboBox(Form)
        self.he_select.setGeometry(QtCore.QRect(220, 250, 271, 31))
        self.he_select.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_select.setObjectName("he_select")
        self.he_select.addItem("")
        self.he_select.addItem("")
        self.he_select.addItem("")
        self.he_select.addItem("")
        self.he_select.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stado de artículo"))
        self.label_2.setText(_translate("Form", "Estado Artículo: Sector Herramientas"))
        self.label.setText(_translate("Form", "Código Artículo"))
        self.he_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.he_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.he_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label_3.setText(_translate("Form", " Artículo"))
        self.label_4.setText(_translate("Form", "Estado"))
        self.he_label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:15pt;\">En Uso</span></p></body></html>"))
        self.he_btn_estado.setText(_translate("Form", "Cambiar Estado"))
        self.label_7.setText(_translate("Form", "Estado"))
        self.he_select.setItemText(0, _translate("Form", "En uso"))
        self.he_select.setItemText(1, _translate("Form", "Listas para entregar"))
        self.he_select.setItemText(2, _translate("Form", "Pendiente de arreglo"))
        self.he_select.setItemText(3, _translate("Form", "Rota/Extraviada"))
        self.he_select.setItemText(4, _translate("Form", "Pendiente de pedido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
