from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 663)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.se_btn_cancelar.setText(_translate("Form", "Volver"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "MAC"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Fecha ingreso"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Estado"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(True)
        self.se_tabla.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
