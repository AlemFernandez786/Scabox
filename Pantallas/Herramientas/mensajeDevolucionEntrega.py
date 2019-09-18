# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mensajeDevolucionEntrega.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(359, 191)
        Form.setWindowTitle("")
        self.he_radiobutton_1 = QtWidgets.QRadioButton(Form)
        self.he_radiobutton_1.setGeometry(QtCore.QRect(50, 50, 141, 41))
        self.he_radiobutton_1.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.he_radiobutton_1.setObjectName("he_radiobutton_1")
        self.he_radiobutton_2 = QtWidgets.QRadioButton(Form)
        self.he_radiobutton_2.setGeometry(QtCore.QRect(210, 50, 141, 41))
        self.he_radiobutton_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.he_radiobutton_2.setObjectName("he_radiobutton_2")
        self.he_btn_confirmar = QtWidgets.QPushButton(Form)
        self.he_btn_confirmar.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.he_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_confirmar.setObjectName("he_btn_confirmar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.he_radiobutton_1.setText(_translate("Form", "Devo&lucion"))
        self.he_radiobutton_2.setText(_translate("Form", "Ent&rega"))
        self.he_btn_confirmar.setText(_translate("Form", "confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
