# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaDenuncias.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(953, 520)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 721, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 170, 931, 251))
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
        self.ca_input_buscar = QtWidgets.QLineEdit(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(130, 110, 551, 31))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_buscar.setText("")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(690, 110, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 90, 541, 16))
        self.label.setObjectName("label")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(400, 450, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Denuncias"))
        self.label_2.setText(_translate("Form", "Consulta de Denuncias"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Id de denuncia"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Nº de folio"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Nº de acta"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "Legajo"))
        self.ca_tabla.headerItem().setText(4, _translate("Form", "Comisaria"))
        self.ca_tabla.headerItem().setText(5, _translate("Form", "Móvil"))
        self.ca_tabla.headerItem().setText(6, _translate("Form", "Técnico 1"))
        self.ca_tabla.headerItem().setText(7, _translate("Form", "Técnico 2"))
        self.ca_tabla.headerItem().setText(8, _translate("Form", "Fecha del siniestro"))
        self.ca_tabla.headerItem().setText(9, _translate("Form", "fecha de denuncia"))
        self.ca_tabla.headerItem().setText(10, _translate("Form", "MAC extraviados"))
        self.ca_tabla.headerItem().setText(11, _translate("Form", "Articulos extravidos"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese legajo de técnico o MAC de equipo extraviado:"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
