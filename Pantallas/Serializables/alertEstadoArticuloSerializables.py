# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alertEstadoArticuloSerializables.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 229)
        self.se_input_1 = QtWidgets.QLineEdit(Form)
        self.se_input_1.setGeometry(QtCore.QRect(90, 40, 291, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setText("")
        self.se_input_1.setObjectName("se_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(130, 160, 131, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Movil"))
        self.se_btn_confirmar.setText(_translate("Form", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
