# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sectorHerramientas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 581)
        Form.setStyleSheet("")
        self.he_btn_3 = QtWidgets.QPushButton(Form)
        self.he_btn_3.setGeometry(QtCore.QRect(80, 210, 251, 41))
        self.he_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_3.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_3.setFlat(False)
        self.he_btn_3.setObjectName("he_btn_3")
        self.he_btn_2 = QtWidgets.QPushButton(Form)
        self.he_btn_2.setGeometry(QtCore.QRect(80, 150, 251, 41))
        self.he_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_2.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_2.setFlat(False)
        self.he_btn_2.setObjectName("he_btn_2")
        self.he_btn_5 = QtWidgets.QPushButton(Form)
        self.he_btn_5.setGeometry(QtCore.QRect(80, 330, 251, 41))
        self.he_btn_5.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_5.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_5.setFlat(False)
        self.he_btn_5.setObjectName("he_btn_5")
        self.he_btn_7 = QtWidgets.QPushButton(Form)
        self.he_btn_7.setGeometry(QtCore.QRect(80, 450, 251, 41))
        self.he_btn_7.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_7.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_7.setFlat(False)
        self.he_btn_7.setObjectName("he_btn_7")
        self.he_btn_6 = QtWidgets.QPushButton(Form)
        self.he_btn_6.setGeometry(QtCore.QRect(80, 390, 251, 41))
        self.he_btn_6.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_6.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_6.setFlat(False)
        self.he_btn_6.setObjectName("he_btn_6")
        self.he_btn_1 = QtWidgets.QPushButton(Form)
        self.he_btn_1.setGeometry(QtCore.QRect(80, 90, 251, 41))
        self.he_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_1.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_1.setFlat(False)
        self.he_btn_1.setObjectName("he_btn_1")
        self.he_btn_cancelar = QtWidgets.QPushButton(Form)
        self.he_btn_cancelar.setGeometry(QtCore.QRect(230, 520, 101, 31))
        self.he_btn_cancelar.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.he_btn_cancelar.setObjectName("he_btn_cancelar")
        self.he_btn_4 = QtWidgets.QPushButton(Form)
        self.he_btn_4.setGeometry(QtCore.QRect(80, 270, 251, 41))
        self.he_btn_4.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.he_btn_4.setIconSize(QtCore.QSize(16, 20))
        self.he_btn_4.setFlat(False)
        self.he_btn_4.setObjectName("he_btn_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sector Herramientas"))
        self.he_btn_3.setText(_translate("Form", "Alta/Baja de Articulos"))
        self.he_btn_2.setText(_translate("Form", "Modificacion de Stock"))
        self.he_btn_5.setText(_translate("Form", "Stock por movil"))
        self.he_btn_7.setText(_translate("Form", "Estado del articulo"))
        self.he_btn_6.setText(_translate("Form", "Stock por tecnico"))
        self.he_btn_1.setText(_translate("Form", "Consulta de Stock"))
        self.he_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.he_btn_4.setText(_translate("Form", "Máxima/Mínima de Stock"))
        self.label.setText(_translate("Form", "Sector Herramientas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
