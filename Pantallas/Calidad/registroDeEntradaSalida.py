# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registroDeEntradaSalida.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 394)
        Form.setStyleSheet("background-color: rgb(243, 243, 243);\n")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-20, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 220, 151, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 121, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 220, 51, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(240, 340, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(400, 340, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 110, 771, 81))
        self.ca_tabla.setStyleSheet("border:none;")
        self.ca_tabla.setObjectName("ca_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ca_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(3, font)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(390, 270, 131, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ca_input_2 = QtWidgets.QDateEdit(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(120, 270, 211, 31))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setCalendarPopup(True)
        self.ca_input_2.setObjectName("ca_input_2")
        import datetime
        hoy = datetime.datetime.today()
        self.ca_input_2.setDate(QtCore.QDate(hoy))
        self.ca_input_3 = QtWidgets.QTimeEdit(Form)
        self.ca_input_3.setGeometry(QtCore.QRect(560, 220, 161, 31))
        self.ca_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_3.setObjectName("ca_input_3")
        self.ca_input_4 = QtWidgets.QTimeEdit(Form)
        self.ca_input_4.setGeometry(QtCore.QRect(560, 270, 161, 31))
        self.ca_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_4.setObjectName("ca_input_4")
        self.ca_input_1 = QtWidgets.QComboBox(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(125, 220, 201, 25))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setObjectName("ca_input_1")
        self.ca_input_1.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 60, 61, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(490, 60, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.ca_input_buscar = QtWidgets.QComboBox(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(260, 60, 201, 25))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_input_buscar.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Presentismo"))
        self.label_2.setText(_translate("Form", "Registro de entrada/salida"))
        self.label_5.setText(_translate("Form", "Horario de entrada"))
        self.label_4.setText(_translate("Form", "Fecha"))
        self.label.setText(_translate("Form", "Legajo"))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Tecnico"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Fecha"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Horario de entrada"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "Horario de salida"))
        self.label_6.setText(_translate("Form", "Horario de salida"))
        self.ca_input_1.setItemText(0, _translate("Form", "Seleccione Técnico"))
        self.label_3.setText(_translate("Form", "Legajo"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.ca_input_buscar.setItemText(0, _translate("Form", "Seleccione Técnico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
