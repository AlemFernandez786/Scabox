# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionRegistroMovil.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 659)
        self.ca_input_buscar = QtWidgets.QComboBox(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(280, 60, 251, 31))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        # self.ca_input_buscar.setText("")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_input_buscar.addItem("")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(540, 60, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 60, 61, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(270, 600, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(430, 600, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 100, 821, 181))
        self.ca_tabla.setObjectName("ca_tabla")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(5, font)
        self.ca_input_2 = QtWidgets.QLineEdit(Form)
        self.ca_input_2.setEnabled(False)
        self.ca_input_2.setGeometry(QtCore.QRect(320, 340, 291, 31))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setText("")
        self.ca_input_2.setObjectName("ca_input_2")
        self.ca_input_3 = QtWidgets.QLineEdit(Form)
        self.ca_input_3.setGeometry(QtCore.QRect(460, 380, 151, 31))
        self.ca_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_3.setText("")
        self.ca_input_3.setObjectName("ca_input_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 350, 71, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ca_input_5 = QtWidgets.QLineEdit(Form)
        self.ca_input_5.setGeometry(QtCore.QRect(370, 460, 241, 31))
        self.ca_input_5.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_5.setText("")
        self.ca_input_5.setObjectName("ca_input_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(210, 500, 241, 31))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 390, 191, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 420, 181, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(210, 460, 131, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ca_input_4 = QtWidgets.QDateEdit(Form)
        self.ca_input_4.setGeometry(QtCore.QRect(500, 420, 110, 26))
        self.ca_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_4.setCalendarPopup(True)
        self.ca_input_4.setObjectName("ca_input_4")
        import datetime
        hoy = datetime.datetime.today()
        self.ca_input_4.setDate(QtCore.QDate(hoy))
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setEnabled(False)
        self.ca_input_1.setGeometry(QtCore.QRect(320, 300, 291, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(210, 310, 71, 31))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(210, 540, 131, 31))
        self.label_9.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_9.setObjectName("label_9")
        self.ca_input_7 = QtWidgets.QComboBox(Form)
        self.ca_input_7.setGeometry(QtCore.QRect(510, 540, 101, 25))
        self.ca_input_7.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_7.setObjectName("ca_input_7")
        self.ca_input_6 = QtWidgets.QDateEdit(Form)
        self.ca_input_6.setGeometry(QtCore.QRect(500, 500, 110, 26))
        self.ca_input_6.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_6.setCalendarPopup(True)
        self.ca_input_6.setObjectName("ca_input_6")
        self.ca_input_6.setDate(QtCore.QDate(hoy))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Móviles y Técnico"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Nº Móvil"))
        self.label_2.setText(_translate("Form", "Modificacion de registro de móvil "))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ca_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Nro Movil"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Patente"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Nº Poliza"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "VTV Vencimiento"))
        self.ca_tabla.headerItem().setText(4, _translate("Form", "Tarjeta verde"))
        self.ca_tabla.headerItem().setText(5, _translate("Form", "Licencia Fecha vencimiento"))
        self.ca_tabla.headerItem().setText(6, _translate("Form", "Legajo titular"))
        self.label_3.setText(_translate("Form", "Patente"))
        self.label_7.setText(_translate("Form", "Fecha de vencimiento de \n"
"Licencia de conducir del titular"))
        self.label_4.setText(_translate("Form", "Nº Poliza de seguro"))
        self.label_5.setText(_translate("Form", "Fecha vencimiento VTV"))
        self.label_6.setText(_translate("Form", "Tarjeta verde"))
        self.label_8.setText(_translate("Form", "Nro Movil"))
        self.label_9.setText(_translate("Form", "Legajo de titular"))
        self.ca_input_buscar.setItemText(0, _translate("Form", "Seleccione un movil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
