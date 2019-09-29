# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarPersonalSupervisor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(930, 524)
        self.su_tabla = QtWidgets.QTreeWidget(Form)
        self.su_tabla.setGeometry(QtCore.QRect(10, 190, 911, 251))
        self.su_tabla.setObjectName("su_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.su_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(3, font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 50, 171, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.su_btn_volver = QtWidgets.QPushButton(Form)
        self.su_btn_volver.setGeometry(QtCore.QRect(380, 460, 131, 31))
        self.su_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_volver.setObjectName("su_btn_volver")
        self.su_input_buscar = QtWidgets.QLineEdit(Form)
        self.su_input_buscar.setGeometry(QtCore.QRect(350, 120, 251, 31))
        self.su_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_buscar.setText("")
        self.su_input_buscar.setObjectName("su_input_buscar")
        self.su_btn_buscar = QtWidgets.QPushButton(Form)
        self.su_btn_buscar.setGeometry(QtCore.QRect(610, 120, 131, 31))
        self.su_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_buscar.setObjectName("su_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 120, 101, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lista de Personal"))
        self.su_tabla.headerItem().setText(0, _translate("Form", "Legajo"))
        self.su_tabla.headerItem().setText(1, _translate("Form", "Nombre"))
        self.su_tabla.headerItem().setText(2, _translate("Form", "Apellido"))
        self.su_tabla.headerItem().setText(3, _translate("Form", "Sector"))
        self.label_2.setText(_translate("Form", "Personal"))
        self.su_btn_volver.setText(_translate("Form", "Volver"))
        self.su_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese Apellido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
