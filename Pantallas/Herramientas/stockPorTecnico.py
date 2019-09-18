# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockPorTecnico.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 530)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 231, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.he_tabla = QtWidgets.QTreeWidget(Form)
        self.he_tabla.setGeometry(QtCore.QRect(30, 80, 681, 141))
        self.he_tabla.setObjectName("he_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.he_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.he_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.he_tabla.headerItem().setFont(2, font)
        self.he_btn_confirmar = QtWidgets.QPushButton(Form)
        self.he_btn_confirmar.setGeometry(QtCore.QRect(290, 470, 141, 31))
        self.he_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.he_btn_confirmar.setObjectName("he_btn_confirmar")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(180, 270, 121, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.he_label_1 = QtWidgets.QLabel(Form)
        self.he_label_1.setGeometry(QtCore.QRect(310, 240, 311, 31))
        self.he_label_1.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.he_label_1.setText("")
        self.he_label_1.setObjectName("he_label_1")
        self.he_label_2 = QtWidgets.QLabel(Form)
        self.he_label_2.setGeometry(QtCore.QRect(310, 270, 311, 31))
        self.he_label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.he_label_2.setText("")
        self.he_label_2.setObjectName("he_label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 240, 51, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.he_label_3 = QtWidgets.QLabel(Form)
        self.he_label_3.setGeometry(QtCore.QRect(310, 300, 311, 31))
        self.he_label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.he_label_3.setText("")
        self.he_label_3.setObjectName("he_label_3")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(130, 300, 171, 31))
        self.label_9.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(200, 360, 171, 31))
        self.label_10.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_10.setObjectName("label_10")
        self.he_input_1 = QtWidgets.QSpinBox(Form)
        self.he_input_1.setGeometry(QtCore.QRect(200, 400, 281, 31))
        self.he_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.he_input_1.setObjectName("he_input_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock por técnico"))
        self.label_2.setText(_translate("Form", "Stock por Tecnico"))
        self.he_tabla.headerItem().setText(0, _translate("Form", "Técnico"))
        self.he_tabla.headerItem().setText(1, _translate("Form", "Fecha de entrega"))
        self.he_tabla.headerItem().setText(2, _translate("Form", "Cantidad de herramientas"))
        self.he_btn_confirmar.setText(_translate("Form", "confirmar"))
        self.label_5.setText(_translate("Form", "Fecha de entrega"))
        self.label_4.setText(_translate("Form", "Técnico"))
        self.label_9.setText(_translate("Form", "Cantidad de herramientas"))
        self.label_10.setText(_translate("Form", "Cantidad de herramientas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
