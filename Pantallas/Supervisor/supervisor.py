# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supervisor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 405)
        Form.setStyleSheet("background-color:white;")
        self.su_btn_cancelar = QtWidgets.QPushButton(Form)
        self.su_btn_cancelar.setGeometry(QtCore.QRect(270, 350, 111, 31))
        self.su_btn_cancelar.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.su_btn_cancelar.setObjectName("su_btn_cancelar")
        self.su_btn_2 = QtWidgets.QPushButton(Form)
        self.su_btn_2.setGeometry(QtCore.QRect(70, 150, 311, 41))
        self.su_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_2.setIconSize(QtCore.QSize(16, 20))
        self.su_btn_2.setFlat(False)
        self.su_btn_2.setObjectName("su_btn_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 231, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.su_btn_1 = QtWidgets.QPushButton(Form)
        self.su_btn_1.setGeometry(QtCore.QRect(70, 90, 311, 41))
        self.su_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_1.setIconSize(QtCore.QSize(16, 20))
        self.su_btn_1.setFlat(False)
        self.su_btn_1.setObjectName("su_btn_1")
        self.su_btn_3 = QtWidgets.QPushButton(Form)
        self.su_btn_3.setGeometry(QtCore.QRect(70, 210, 311, 41))
        self.su_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_3.setIconSize(QtCore.QSize(16, 20))
        self.su_btn_3.setFlat(False)
        self.su_btn_3.setObjectName("su_btn_3")
        self.su_btn_4 = QtWidgets.QPushButton(Form)
        self.su_btn_4.setGeometry(QtCore.QRect(70, 270, 311, 41))
        self.su_btn_4.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.su_btn_4.setIconSize(QtCore.QSize(16, 20))
        self.su_btn_4.setFlat(False)
        self.su_btn_4.setObjectName("su_btn_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.su_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.su_btn_2.setText(_translate("Form", "Alta/Baja de Personal"))
        self.label.setText(_translate("Form", "Supervisor"))
        self.su_btn_1.setText(_translate("Form", "Consulta de Stock"))
        self.su_btn_3.setText(_translate("Form", "Modificación de sector de personal"))
        self.su_btn_4.setText(_translate("Form", "Personal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
#supervisor ven