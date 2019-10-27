from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 400)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.se_label_1 = QtWidgets.QLabel(Form)
        self.se_label_1.setGeometry(QtCore.QRect(170, 20, 241, 31))
        self.se_label_1.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.se_label_1.setObjectName("se_label_1")
        self.se_label_2 = QtWidgets.QLabel(Form)
        self.se_label_2.setGeometry(QtCore.QRect(170, 60, 251, 31))
        self.se_label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.se_label_2.setObjectName("se_label_2")
        self.se_label_3 = QtWidgets.QLabel(Form)
        self.se_label_3.setGeometry(QtCore.QRect(170, 100, 241, 31))
        self.se_label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.se_label_3.setObjectName("se_label_3")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 230, 111, 31))
        self.label_10.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 180, 111, 31))
        self.label_11.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_11.setObjectName("label_11")
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(80, 330, 131, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")
        self.se_btn_cancelar = QtWidgets.QPushButton(Form)
        self.se_btn_cancelar.setGeometry(QtCore.QRect(240, 330, 131, 31))
        self.se_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.se_btn_cancelar.setObjectName("se_btn_cancelar")
        self.se_input_2 = QtWidgets.QSpinBox(Form)
        self.se_input_2.setGeometry(QtCore.QRect(160, 230, 251, 31))
        self.se_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_2.setObjectName("se_input_2")
        self.se_input_2.setMaximum(9999999)
        self.se_input_1 = QtWidgets.QSpinBox(Form)
        self.se_input_1.setGeometry(QtCore.QRect(160, 180, 251, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setObjectName("se_input_1")
        self.se_input_1.setMaximum(9999999)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Máximo y Mínimo"))
        self.label_4.setText(_translate("Form", "Serializable:"))
        self.label_5.setText(_translate("Form", "Cantidad Mínima:"))
        self.label_6.setText(_translate("Form", "Cantidad Máxima:"))
        self.label_10.setText(_translate("Form", "Cantidad Máxima"))
        self.label_11.setText(_translate("Form", "Cantidad Mínima"))
        self.se_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.se_btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
