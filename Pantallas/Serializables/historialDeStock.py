from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 425)
        self.se_input_buscar = QtWidgets.QLineEdit(Form)
        self.se_input_buscar.setGeometry(QtCore.QRect(310, 80, 251, 31))
        self.se_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_buscar.setText("")
        self.se_input_buscar.setObjectName("se_input_buscar")
        self.se_btn_buscar = QtWidgets.QPushButton(Form)
        self.se_btn_buscar.setGeometry(QtCore.QRect(570, 80, 131, 31))
        self.se_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_buscar.setObjectName("se_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 80, 181, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(30, 140, 791, 161))
        self.se_tabla.setObjectName("se_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(0, font)
        self.se_tabla.setColumnWidth(0, 140)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(1, font)
        self.se_tabla.setColumnWidth(1, 130)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(2, font)
        self.se_tabla.setColumnWidth(2, 130)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(3, font)
        self.se_tabla.setColumnWidth(3, 235)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(4, font)
        self.se_volver = QtWidgets.QPushButton(Form)
        self.se_volver.setGeometry(QtCore.QRect(360, 350, 131, 31))
        self.se_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_volver.setObjectName("se_volver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Historial de equipos"))
        self.se_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese el número de MAC"))
        self.label_2.setText(_translate("Form", "Historial de Stock"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "MAC"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Fecha de ingreso"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Fecha de entrega"))
        self.se_tabla.headerItem().setText(3, _translate("Form", "Fecha de colocación o devolución"))
        self.se_tabla.headerItem().setText(4, _translate("Form", "Estado"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(False)
        self.se_tabla.setSortingEnabled(__sortingEnabled)
        self.se_volver.setText(_translate("Form", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())