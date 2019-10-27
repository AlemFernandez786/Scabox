from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 663)
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
        self.label.setGeometry(QtCore.QRect(120, 80, 171, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.se_btn_cancelar = QtWidgets.QPushButton(Form)
        self.se_btn_cancelar.setGeometry(QtCore.QRect(330, 570, 131, 31))
        self.se_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.se_btn_cancelar.setObjectName("se_btn_cancelar")
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(10, 120, 821, 381))
        self.se_tabla.setObjectName("se_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(5, font)


####        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock por tipo"))
        self.se_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Código del serializable: "))
        self.se_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Codigo"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Cantidad de Stock disponible"))
        self.se_tabla.headerItem().setText(3, _translate("Form", "Stock Minimo permitido"))
        self.se_tabla.headerItem().setText(4, _translate("Form", "Stock Maximo permitido"))
        self.se_tabla.headerItem().setText(5, _translate("Form", "Stock utilizado en los ultimos 30 dias"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(False)
        self.se_tabla.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
