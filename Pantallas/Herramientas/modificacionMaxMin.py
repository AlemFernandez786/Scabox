# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionMaxMin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 419)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-190, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.he_input_2 = QtWidgets.QLineEdit(Form)
        self.he_input_2.setGeometry(QtCore.QRect(110, 150, 301, 31))
        self.he_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.he_input_2.setText("")
        self.he_input_2.setObjectName("he_input_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.he_input_4 = QtWidgets.QLineEdit(Form)
        self.he_input_4.setGeometry(QtCore.QRect(160, 250, 251, 31))
        self.he_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_input_4.setText("")
        self.he_input_4.setObjectName("he_input_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 111, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.he_input_1 = QtWidgets.QLineEdit(Form)
        self.he_input_1.setGeometry(QtCore.QRect(160, 100, 251, 31))
        self.he_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_input_1.setText("")
        self.he_input_1.setObjectName("he_input_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 101, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.he_input_3 = QtWidgets.QLineEdit(Form)
        self.he_input_3.setGeometry(QtCore.QRect(160, 200, 251, 31))
        self.he_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_input_3.setText("")
        self.he_input_3.setObjectName("he_input_3")
        self.he_btn_confirmar = QtWidgets.QPushButton(Form)
        self.he_btn_confirmar.setGeometry(QtCore.QRect(90, 330, 131, 31))
        self.he_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_confirmar.setObjectName("he_btn_confirmar")
        self.he_btn_cancelar = QtWidgets.QPushButton(Form)
        self.he_btn_cancelar.setGeometry(QtCore.QRect(250, 330, 131, 31))
        self.he_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.he_btn_cancelar.setObjectName("he_btn_cancelar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificación de Máximo y Mínimo"))
        self.label_2.setText(_translate("Form", "Modificacion Max/Min"))
        self.label_5.setText(_translate("Form", "Cantidad Minima"))
        self.label_6.setText(_translate("Form", "Cantidad Maxima"))
        self.label_4.setText(_translate("Form", "Material"))
        self.label.setText(_translate("Form", "Codigo material"))
        self.he_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.he_btn_cancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
