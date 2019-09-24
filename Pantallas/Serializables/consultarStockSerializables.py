
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 525)
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(10, 200, 911, 251))
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

        ''' item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
            font = QtGui.QFont()
            font.setPointSize(8)
            item_0.setFont(0, font)
            font = QtGui.QFont()
            font.setPointSize(8)
            item_0.setFont(5, font)
            '''
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 171, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(750, 60, 171, 41))
        self.label_3.setStyleSheet("font-size:20px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.se_btn_volver = QtWidgets.QPushButton(Form)
        self.se_btn_volver.setGeometry(QtCore.QRect(380, 470, 131, 31))
        self.se_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_volver.setObjectName("se_btn_volver")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 140, 171, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.se_btn_buscar = QtWidgets.QPushButton(Form)
        self.se_btn_buscar.setGeometry(QtCore.QRect(610, 140, 131, 31))
        self.se_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_buscar.setObjectName("se_btn_buscar")
        self.se_input_buscar = QtWidgets.QLineEdit(Form)
        self.se_input_buscar.setGeometry(QtCore.QRect(350, 140, 251, 31))
        self.se_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_buscar.setText("")
        self.se_input_buscar.setObjectName("se_input_buscar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Codigo MAC"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Fecha ingreso"))
        self.se_tabla.headerItem().setText(3, _translate("Form", "Tipo"))
        self.se_tabla.headerItem().setText(4, _translate("Form", "Stock Minimo permitido"))
        self.se_tabla.headerItem().setText(5, _translate("Form", "Stock Maximo permitido"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(True)
        self.label_2.setText(_translate("Form", "Consulta Stock"))
        self.label_3.setText(_translate("Form", "Serializables"))
        self.se_btn_volver.setText(_translate("Form", "Volver"))
        self.label.setText(_translate("Form", "Ingrese código del articulo"))
        self.se_btn_buscar.setText(_translate("Form", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
