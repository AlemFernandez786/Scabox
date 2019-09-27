# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarTrabajoControlado.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 393)
        self.ca_input_buscar = QtWidgets.QLineEdit(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(180, 80, 381, 31))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_buscar.setText("")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(570, 80, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 60, 301, 16))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_volver = QtWidgets.QPushButton(Form)
        self.ca_btn_volver.setGeometry(QtCore.QRect(350, 340, 131, 31))
        self.ca_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_volver.setObjectName("ca_btn_volver")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 120, 821, 181))
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ca_tabla.headerItem().setFont(4, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ca_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ca_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ca_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" vertical-align:super;\">Ingrese cualquier dato: número de orden,domicilio,técnicos o móvil,etc</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Registros de trabajos controlados"))
        self.ca_btn_volver.setText(_translate("Form", "Volver"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Número de orden"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Domicilio"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Técnicos"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "Móvil"))
        self.ca_tabla.headerItem().setText(4, _translate("Form", "Observaciones"))
        __sortingEnabled = self.ca_tabla.isSortingEnabled()
        self.ca_tabla.setSortingEnabled(False)
        self.ca_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item  "))
        self.ca_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(0).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(0).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(0).setText(4, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(0, _translate("Form", "New Item"))
        self.ca_tabla.topLevelItem(1).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(4, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(0, _translate("Form", "New Item"))
        self.ca_tabla.topLevelItem(2).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(4, _translate("Form", "lorem"))
        self.ca_tabla.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
