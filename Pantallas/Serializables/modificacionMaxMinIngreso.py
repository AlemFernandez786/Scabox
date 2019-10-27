# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionMaxMinIngreso.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 263)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-190, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.se_input_1 = QtWidgets.QLineEdit(Form)
        self.se_input_1.setGeometry(QtCore.QRect(160, 100, 251, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setText("")
        self.se_input_1.setObjectName("se_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 101, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(80, 190, 131, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")
        self.se_btn_cancelar = QtWidgets.QPushButton(Form)
        self.se_btn_cancelar.setGeometry(QtCore.QRect(240, 190, 131, 31))
        self.se_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.se_btn_cancelar.setObjectName("se_btn_cancelar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Máximo y Mínimo"))
        self.label_2.setText(_translate("Form", "Modificación Max/Min"))
        self.label.setText(_translate("Form", "MAC del serializable"))
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
