# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sectorMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 581)
        Form.setStyleSheet("background-color:white;")
        self.ma_btn_4 = QtWidgets.QPushButton(Form)
        self.ma_btn_4.setGeometry(QtCore.QRect(70, 280, 311, 41))
        self.ma_btn_4.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_4.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_4.setFlat(False)
        self.ma_btn_4.setObjectName("ma_btn_4")
        self.ma_btn_3 = QtWidgets.QPushButton(Form)
        self.ma_btn_3.setGeometry(QtCore.QRect(70, 220, 311, 41))
        self.ma_btn_3.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_3.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_3.setFlat(False)
        self.ma_btn_3.setObjectName("ma_btn_3")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(270, 530, 111, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.ma_btn_6 = QtWidgets.QPushButton(Form)
        self.ma_btn_6.setGeometry(QtCore.QRect(70, 400, 311, 41))
        self.ma_btn_6.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_6.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_6.setFlat(False)
        self.ma_btn_6.setObjectName("ma_btn_6")
        self.ma_btn_1 = QtWidgets.QPushButton(Form)
        self.ma_btn_1.setGeometry(QtCore.QRect(70, 100, 311, 41))
        self.ma_btn_1.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_1.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_1.setFlat(False)
        self.ma_btn_1.setObjectName("ma_btn_1")
        self.ma_btn_2 = QtWidgets.QPushButton(Form)
        self.ma_btn_2.setGeometry(QtCore.QRect(70, 160, 311, 41))
        self.ma_btn_2.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_2.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_2.setFlat(False)
        self.ma_btn_2.setObjectName("ma_btn_2")
        self.ma_btn_7 = QtWidgets.QPushButton(Form)
        self.ma_btn_7.setGeometry(QtCore.QRect(70, 460, 311, 41))
        self.ma_btn_7.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_7.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_7.setFlat(False)
        self.ma_btn_7.setObjectName("ma_btn_7")
        self.ma_btn_5 = QtWidgets.QPushButton(Form)
        self.ma_btn_5.setGeometry(QtCore.QRect(70, 340, 311, 41))
        self.ma_btn_5.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_5.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_5.setFlat(False)
        self.ma_btn_5.setObjectName("ma_btn_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 20, 231, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ma_btn_4.setText(_translate("Form", "Máxima/Mínima de Stock"))
        self.ma_btn_3.setText(_translate("Form", "Alta/Baja de Articulos"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ma_btn_6.setText(_translate("Form", "Inventario"))
        self.ma_btn_1.setText(_translate("Form", "Consulta de Stock"))
        self.ma_btn_2.setText(_translate("Form", "Modificacion de Stock"))
        self.ma_btn_7.setText(_translate("Form", "Aprovisionamiento"))
        self.ma_btn_5.setText(_translate("Form", "Stock por movil"))
        self.label.setText(_translate("Form", "Sector Materiales"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

