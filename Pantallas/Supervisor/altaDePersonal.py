# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaDePersonal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 418)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 341, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 211, 21))
        self.label_3.setStyleSheet("font-size:13px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.su_input_1 = QtWidgets.QLineEdit(Form)
        self.su_input_1.setGeometry(QtCore.QRect(120, 110, 301, 31))
        self.su_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_1.setText("")
        self.su_input_1.setObjectName("su_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 110, 71, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.su_input_2 = QtWidgets.QLineEdit(Form)
        self.su_input_2.setGeometry(QtCore.QRect(120, 160, 301, 31))
        self.su_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_2.setText("")
        self.su_input_2.setObjectName("su_input_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 71, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.su_input_3 = QtWidgets.QLineEdit(Form)
        self.su_input_3.setGeometry(QtCore.QRect(120, 210, 301, 31))
        self.su_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_3.setText("")
        self.su_input_3.setObjectName("su_input_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 260, 71, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.su_input_4 = QtWidgets.QLineEdit(Form)
        self.su_input_4.setGeometry(QtCore.QRect(120, 260, 301, 31))
        self.su_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_4.setText("")
        self.su_input_4.setObjectName("su_input_4")
        self.su_btn_confirmar = QtWidgets.QPushButton(Form)
        self.su_btn_confirmar.setGeometry(QtCore.QRect(70, 360, 131, 31))
        self.su_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_confirmar.setObjectName("su_btn_confirmar")
        self.su_btn_cancelar = QtWidgets.QPushButton(Form)
        self.su_btn_cancelar.setGeometry(QtCore.QRect(270, 360, 131, 31))
        self.su_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.su_btn_cancelar.setObjectName("su_btn_cancelar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Alta de Personal"))
        self.label_3.setText(_translate("Form", "Ingrese datos del individuo"))
        self.label.setText(_translate("Form", "Legajo"))
        self.label_4.setText(_translate("Form", "Nombre"))
        self.label_5.setText(_translate("Form", "Apellido"))
        self.label_6.setText(_translate("Form", "DNI"))
        self.su_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.su_btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
