# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registroMovilesTecnicos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 461)
        Form.setStyleSheet("background-color:white;")
        self.ca_btn_4 = QtWidgets.QPushButton(Form)
        self.ca_btn_4.setGeometry(QtCore.QRect(70, 280, 311, 41))
        self.ca_btn_4.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_4.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_4.setFlat(False)
        self.ca_btn_4.setObjectName("ca_btn_4")
        self.ca_btn_3 = QtWidgets.QPushButton(Form)
        self.ca_btn_3.setGeometry(QtCore.QRect(70, 220, 311, 41))
        self.ca_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_3.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_3.setFlat(False)
        self.ca_btn_3.setObjectName("ca_btn_3")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(270, 410, 111, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.ca_btn_1 = QtWidgets.QPushButton(Form)
        self.ca_btn_1.setGeometry(QtCore.QRect(70, 100, 311, 41))
        self.ca_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_1.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_1.setFlat(False)
        self.ca_btn_1.setObjectName("ca_btn_1")
        self.ca_btn_2 = QtWidgets.QPushButton(Form)
        self.ca_btn_2.setGeometry(QtCore.QRect(70, 160, 311, 41))
        self.ca_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_2.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_2.setFlat(False)
        self.ca_btn_2.setObjectName("ca_btn_2")
        self.ca_btn_5 = QtWidgets.QPushButton(Form)
        self.ca_btn_5.setGeometry(QtCore.QRect(70, 340, 311, 41))
        self.ca_btn_5.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_5.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_5.setFlat(False)
        self.ca_btn_5.setObjectName("ca_btn_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 251, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ca_btn_4.setText(_translate("Form", "Modificar dupla por movil"))
        self.ca_btn_3.setText(_translate("Form", "Modificar registro de moviles"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ca_btn_1.setText(_translate("Form", "Alta movil"))
        self.ca_btn_2.setText(_translate("Form", "Baja movil"))
        self.ca_btn_5.setText(_translate("Form", "Consultar registro de moviles y tecnicos"))
        self.label.setText(_translate("Form", "Registro móviles y técnicos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
