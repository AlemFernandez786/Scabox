# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaMovil.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 301)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 341, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(160, 60, 321, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 60, 71, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 110, 51, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(100, 230, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(300, 230, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.ca_input_2 = QtWidgets.QTextEdit(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(160, 110, 321, 71))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setObjectName("ca_input_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Baja Movil"))
        self.label.setText(_translate("Form", "Movil"))
        self.label_4.setText(_translate("Form", "Motivo"))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
