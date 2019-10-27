# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sectorControlDeCalidad.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 570)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 231, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ca_btn_2 = QtWidgets.QPushButton(Form)
        self.ca_btn_2.setGeometry(QtCore.QRect(80, 90, 251, 41))
        self.ca_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_2.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_2.setFlat(False)
        self.ca_btn_2.setObjectName("ca_btn_2")
        self.ca_btn_3 = QtWidgets.QPushButton(Form)
        self.ca_btn_3.setGeometry(QtCore.QRect(80, 150, 251, 41))
        self.ca_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_3.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_3.setFlat(False)
        self.ca_btn_3.setObjectName("ca_btn_3")
        self.ca_btn_4 = QtWidgets.QPushButton(Form)
        self.ca_btn_4.setGeometry(QtCore.QRect(80, 210, 251, 41))
        self.ca_btn_4.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_4.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_4.setFlat(False)
        self.ca_btn_4.setObjectName("ca_btn_4")
        self.ca_btn_5 = QtWidgets.QPushButton(Form)
        self.ca_btn_5.setGeometry(QtCore.QRect(80, 270, 251, 41))
        self.ca_btn_5.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_5.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_5.setFlat(False)
        self.ca_btn_5.setObjectName("ca_btn_5")
        self.ca_btn_6 = QtWidgets.QPushButton(Form)
        self.ca_btn_6.setGeometry(QtCore.QRect(80, 330, 251, 41))
        self.ca_btn_6.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_6.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_6.setFlat(False)
        self.ca_btn_6.setObjectName("ca_btn_6")
        self.ca_btn_7 = QtWidgets.QPushButton(Form)
        self.ca_btn_7.setGeometry(QtCore.QRect(80, 390, 251, 41))
        self.ca_btn_7.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_7.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_7.setFlat(False)
        self.ca_btn_7.setObjectName("ca_btn_7")
        self.ca_btn_8 = QtWidgets.QPushButton(Form)
        self.ca_btn_8.setGeometry(QtCore.QRect(230, 510, 101, 31))
        self.ca_btn_8.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.ca_btn_8.setObjectName("ca_btn_8")
        self.ca_btn_9 = QtWidgets.QPushButton(Form)
        self.ca_btn_9.setGeometry(QtCore.QRect(80, 450, 251, 41))
        self.ca_btn_9.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ca_btn_9.setIconSize(QtCore.QSize(16, 20))
        self.ca_btn_9.setFlat(False)
        self.ca_btn_9.setObjectName("ca_btn_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ScaBox - Calidad"))
        self.label.setText(_translate("Form", "Sector Control de Calidad"))
        self.ca_btn_2.setText(_translate("Form", "Trabajos Realizados"))
        self.ca_btn_3.setText(_translate("Form", "Denuncias"))
        self.ca_btn_4.setText(_translate("Form", "Presentismo"))
        self.ca_btn_5.setText(_translate("Form", "Técnicos y moviles"))
        self.ca_btn_6.setText(_translate("Form", "Descontar por extravío"))
        self.ca_btn_7.setText(_translate("Form", "Trabajos controlados"))
        self.ca_btn_8.setText(_translate("Form", "Cancelar"))
        self.ca_btn_9.setText(_translate("Form", "Consulta de personal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
