# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockPorMovilIngreso.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 498)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 231, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ma_tabla_datos = QtWidgets.QTreeWidget(Form)
        self.ma_tabla_datos.setGeometry(QtCore.QRect(30, 80, 681, 271))
        self.ma_tabla_datos.setObjectName("ma_tabla_datos")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla_datos.headerItem().setFont(1, font)
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(300, 440, 141, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 360, 41, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(230, 390, 71, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.ma_label_movil = QtWidgets.QLabel(Form)
        self.ma_label_movil.setGeometry(QtCore.QRect(310, 360, 311, 31))
        self.ma_label_movil.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_movil.setText("")
        self.ma_label_movil.setObjectName("ma_label_movil")
        self.ma_label_tecnicos = QtWidgets.QLabel(Form)
        self.ma_label_tecnicos.setGeometry(QtCore.QRect(310, 390, 311, 31))
        self.ma_label_tecnicos.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.ma_label_tecnicos.setText("")
        self.ma_label_tecnicos.setObjectName("ma_label_tecnicos")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock por Movil"))
        self.label_2.setText(_translate("Form", "Stock por Movil"))
        self.ma_tabla_datos.headerItem().setText(0, _translate("Form", "Móvil"))
        self.ma_tabla_datos.headerItem().setText(1, _translate("Form", "Técnicos"))
        self.ma_btn_confirmar.setText(_translate("Form", "confirmar"))
        self.label_4.setText(_translate("Form", "Móvil"))
        self.label_5.setText(_translate("Form", "Técnicos"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
