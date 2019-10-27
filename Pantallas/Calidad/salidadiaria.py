# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salidadiaria.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 538)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-20, 40, 721, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(430, 110, 111, 21))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 110, 131, 21))
        self.label.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(30, 170, 621, 271))
        self.ca_tabla.setStyleSheet("border:none;")
        self.ca_tabla.setObjectName("ca_tabla")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ca_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ca_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ca_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ca_tabla.headerItem().setFont(3, font)
        self.ca_btn_volver = QtWidgets.QPushButton(Form)
        self.ca_btn_volver.setGeometry(QtCore.QRect(480, 460, 131, 31))
        self.ca_btn_volver.setStyleSheet("background-color: #ff4e4e;\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_volver.setObjectName("ca_btn_volver")
        self.ca_input_1 = QtWidgets.QDateEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(300, 110, 110, 26))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setCalendarPopup(True)
        self.ca_input_1.setObjectName("ca_input_1")
        import datetime
        hoy = datetime.datetime.today()
        self.ca_input_1.setDate(QtCore.QDate(hoy))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Móviles y Técnicos"))
        self.label_2.setText(_translate("Form", "Planilla de salida diaria"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Buscar por fecha:"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Sector / Movil"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Tecnico"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Legajo"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "Fecha"))
        self.ca_btn_volver.setText(_translate("Form", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())