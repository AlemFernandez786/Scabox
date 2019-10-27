# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarStock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 209)
        Form.setStyleSheet("background-color:white;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 171, 51))
        self.label.setStyleSheet("font-size:20px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 171, 51))
        self.label_2.setStyleSheet("font-size:20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.su_btn_1 = QtWidgets.QPushButton(Form)
        self.su_btn_1.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.su_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_1.setObjectName("su_btn_1")
        self.su_btn_2 = QtWidgets.QPushButton(Form)
        self.su_btn_2.setGeometry(QtCore.QRect(190, 120, 151, 31))
        self.su_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_2.setObjectName("su_btn_2")
        self.su_btn_3 = QtWidgets.QPushButton(Form)
        self.su_btn_3.setGeometry(QtCore.QRect(380, 120, 151, 31))
        self.su_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_3.setObjectName("su_btn_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Consultar Stock"))
        self.label_2.setText(_translate("Form", "Supervisor"))
        self.su_btn_1.setText(_translate("Form", "Materiales"))
        self.su_btn_2.setText(_translate("Form", "Herramientas"))
        self.su_btn_3.setText(_translate("Form", "Serializables"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
