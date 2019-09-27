# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registroDeAusencia.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 460)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 531, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_input_2 = QtWidgets.QLineEdit(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(100, 150, 441, 31))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setText("")
        self.ca_input_2.setObjectName("ca_input_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 131, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 181, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(150, 100, 391, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 101, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(130, 390, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(290, 390, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.ca_input_3 = QtWidgets.QTextEdit(Form)
        self.ca_input_3.setGeometry(QtCore.QRect(150, 230, 391, 71))
        self.ca_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_3.setObjectName("ca_input_3")
        self.ca_radiobutton_1 = QtWidgets.QRadioButton(Form)
        self.ca_radiobutton_1.setGeometry(QtCore.QRect(220, 200, 82, 17))
        self.ca_radiobutton_1.setObjectName("ca_radiobutton_1")
        self.ca_radiobutton_2 = QtWidgets.QRadioButton(Form)
        self.ca_radiobutton_2.setGeometry(QtCore.QRect(280, 200, 82, 17))
        self.ca_radiobutton_2.setObjectName("ca_radiobutton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Registro de Ausencia"))
        self.label_5.setText(_translate("Form", "Motivo de ausencia"))
        self.label_6.setText(_translate("Form", "Certificado correspondiente"))
        self.label_4.setText(_translate("Form", "Legajo"))
        self.label.setText(_translate("Form", "Tecnico"))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ca_radiobutton_1.setText(_translate("Form", "Si"))
        self.ca_radiobutton_2.setText(_translate("Form", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
