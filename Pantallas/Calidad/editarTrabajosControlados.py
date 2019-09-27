# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTrabajosControlados.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 615)
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(180, 80, 381, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
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
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 71, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(420, 320, 91, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.ca_input_7 = QtWidgets.QTextEdit(Form)
        self.ca_input_7.setGeometry(QtCore.QRect(530, 420, 271, 71))
        self.ca_input_7.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_7.setObjectName("ca_input_7")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 91, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.ca_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ca_btn_confirmar.setGeometry(QtCore.QRect(250, 530, 131, 31))
        self.ca_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_confirmar.setObjectName("ca_btn_confirmar")
        self.ca_input_3 = QtWidgets.QLineEdit(Form)
        self.ca_input_3.setGeometry(QtCore.QRect(110, 370, 301, 31))
        self.ca_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_3.setText("")
        self.ca_input_3.setObjectName("ca_input_3")
        self.ca_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ca_btn_cancelar.setGeometry(QtCore.QRect(450, 530, 131, 31))
        self.ca_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_cancelar.setObjectName("ca_btn_cancelar")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 420, 91, 31))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(420, 370, 91, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ca_input_4 = QtWidgets.QLineEdit(Form)
        self.ca_input_4.setGeometry(QtCore.QRect(140, 420, 271, 31))
        self.ca_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_4.setText("")
        self.ca_input_4.setObjectName("ca_input_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(420, 420, 101, 31))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_7.setObjectName("label_7")
        self.ca_input_2 = QtWidgets.QLineEdit(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(130, 320, 281, 31))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setText("")
        self.ca_input_2.setObjectName("ca_input_2")
        self.ca_input_5 = QtWidgets.QLineEdit(Form)
        self.ca_input_5.setGeometry(QtCore.QRect(530, 320, 271, 31))
        self.ca_input_5.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_5.setText("")
        self.ca_input_5.setObjectName("ca_input_5")
        self.ca_input_6 = QtWidgets.QLineEdit(Form)
        self.ca_input_6.setGeometry(QtCore.QRect(530, 370, 271, 31))
        self.ca_input_6.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_6.setText("")
        self.ca_input_6.setObjectName("ca_input_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" vertical-align:super;\">Ingrese cualquier dato: número de orden,domicilio,técnicos o móvil,etc</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Editar trabajos controlados"))
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
        self.label_4.setText(_translate("Form", "Domicilio"))
        self.label_5.setText(_translate("Form", "Tecnico Nº 1"))
        self.label_3.setText(_translate("Form", "Nº de Orden "))
        self.ca_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ca_btn_cancelar.setText(_translate("Form", "Eliminar"))
        self.label_8.setText(_translate("Form", "Móvil"))
        self.label_6.setText(_translate("Form", "Tecnico Nº 2"))
        self.label_7.setText(_translate("Form", "Observaciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
