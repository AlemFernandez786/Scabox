# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTrabajoVisitado.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 648)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 501, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ca_btn_modificar = QtWidgets.QPushButton(Form)
        self.ca_btn_modificar.setGeometry(QtCore.QRect(370, 590, 131, 31))
        self.ca_btn_modificar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_modificar.setObjectName("ca_btn_modificar")
        self.ca_btn_eliminar = QtWidgets.QPushButton(Form)
        self.ca_btn_eliminar.setGeometry(QtCore.QRect(370, 540, 131, 31))
        self.ca_btn_eliminar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ca_btn_eliminar.setObjectName("ca_btn_eliminar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 90, 541, 16))
        self.label.setObjectName("label")
        self.ca_input_buscar = QtWidgets.QLineEdit(Form)
        self.ca_input_buscar.setGeometry(QtCore.QRect(130, 110, 551, 31))
        self.ca_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_buscar.setObjectName("ca_input_buscar")
        self.ca_btn_buscar = QtWidgets.QPushButton(Form)
        self.ca_btn_buscar.setGeometry(QtCore.QRect(690, 110, 131, 31))
        self.ca_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ca_btn_buscar.setObjectName("ca_btn_buscar")
        self.ca_tabla = QtWidgets.QTreeWidget(Form)
        self.ca_tabla.setGeometry(QtCore.QRect(10, 160, 901, 101))
        self.ca_tabla.setStyleSheet("border:none;")
        self.ca_tabla.setObjectName("ca_tabla")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(6, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(7, font)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ca_tabla.headerItem().setFont(8, font)
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
        self.ca_input_9 = QtWidgets.QLineEdit(Form)
        self.ca_input_9.setGeometry(QtCore.QRect(660, 480, 231, 31))
        self.ca_input_9.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_9.setText("")
        self.ca_input_9.setObjectName("ca_input_9")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(530, 380, 151, 31))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 141, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(530, 330, 131, 31))
        self.label_9.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_9.setObjectName("label_9")
        self.ca_input_5 = QtWidgets.QLineEdit(Form)
        self.ca_input_5.setGeometry(QtCore.QRect(680, 280, 211, 31))
        self.ca_input_5.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_5.setText("")
        self.ca_input_5.setObjectName("ca_input_5")
        self.ca_input_1 = QtWidgets.QLineEdit(Form)
        self.ca_input_1.setGeometry(QtCore.QRect(170, 280, 291, 31))
        self.ca_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_1.setText("")
        self.ca_input_1.setObjectName("ca_input_1")
        self.ca_input_7 = QtWidgets.QLineEdit(Form)
        self.ca_input_7.setGeometry(QtCore.QRect(690, 380, 201, 31))
        self.ca_input_7.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_7.setText("")
        self.ca_input_7.setObjectName("ca_input_7")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 121, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 420, 341, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.ca_input_6 = QtWidgets.QLineEdit(Form)
        self.ca_input_6.setGeometry(QtCore.QRect(670, 330, 221, 31))
        self.ca_input_6.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_6.setText("")
        self.ca_input_6.setObjectName("ca_input_6")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(520, 430, 201, 31))
        self.label_10.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_10.setObjectName("label_10")
        self.ca_input_2 = QtWidgets.QLineEdit(Form)
        self.ca_input_2.setGeometry(QtCore.QRect(180, 330, 281, 31))
        self.ca_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_2.setText("")
        self.ca_input_2.setObjectName("ca_input_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 480, 111, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(540, 280, 121, 31))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 380, 61, 31))
        self.label_11.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(520, 480, 131, 31))
        self.label_12.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_12.setObjectName("label_12")
        self.ca_input_3 = QtWidgets.QLineEdit(Form)
        self.ca_input_3.setGeometry(QtCore.QRect(110, 380, 351, 31))
        self.ca_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_3.setText("")
        self.ca_input_3.setObjectName("ca_input_3")
        self.ca_input_8 = QtWidgets.QLineEdit(Form)
        self.ca_input_8.setGeometry(QtCore.QRect(730, 430, 161, 31))
        self.ca_input_8.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_8.setText("")
        self.ca_input_8.setObjectName("ca_input_8")
        self.ca_input_4 = QtWidgets.QTextEdit(Form)
        self.ca_input_4.setGeometry(QtCore.QRect(30, 450, 431, 61))
        self.ca_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ca_input_4.setObjectName("ca_input_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Editar Trabajo Visitado"))
        self.ca_btn_modificar.setText(_translate("Form", "Modificar"))
        self.ca_btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.label.setText(_translate("Form", "Ingrese cualquier dato de busqueda: nº de orden, domicilio,nombre o DNI del abonado,numero de cliente,etc"))
        self.ca_btn_buscar.setText(_translate("Form", "Buscar"))
        self.ca_tabla.headerItem().setText(0, _translate("Form", "Nº de orden"))
        self.ca_tabla.headerItem().setText(1, _translate("Form", "Domicilio"))
        self.ca_tabla.headerItem().setText(2, _translate("Form", "Nombre del abonado"))
        self.ca_tabla.headerItem().setText(3, _translate("Form", "DNI del abonado"))
        self.ca_tabla.headerItem().setText(4, _translate("Form", "Número de cliente"))
        self.ca_tabla.headerItem().setText(5, _translate("Form", "Códigos de finalizacion"))
        self.ca_tabla.headerItem().setText(6, _translate("Form", "Observaciones"))
        self.ca_tabla.headerItem().setText(7, _translate("Form", "MAC de los equipos instalados"))
        self.ca_tabla.headerItem().setText(8, _translate("Form", "Materiales utilizados"))
        __sortingEnabled = self.ca_tabla.isSortingEnabled()
        self.ca_tabla.setSortingEnabled(False)
        self.ca_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item  "))
        self.ca_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(0).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(0).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(0, _translate("Form", "New Item"))
        self.ca_tabla.topLevelItem(1).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(1).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(0, _translate("Form", "New Item"))
        self.ca_tabla.topLevelItem(2).setText(1, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(2, _translate("Form", "lorem"))
        self.ca_tabla.topLevelItem(2).setText(3, _translate("Form", "lorem"))
        self.ca_tabla.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("Form", "Codigos de finalizacion"))
        self.label_3.setText(_translate("Form", "Nombre del abonado"))
        self.label_9.setText(_translate("Form", "Numero del cliente"))
        self.label_4.setText(_translate("Form", "Número de Orden"))
        self.label_5.setText(_translate("Form", "Tareas realizadas u observaciones de la cancelacion"))
        self.label_10.setText(_translate("Form", "MAC de los equipos instalados"))
        self.label_7.setText(_translate("Form", "DNI del abonado"))
        self.label_11.setText(_translate("Form", "Domicilio"))
        self.label_12.setText(_translate("Form", "Materiales utilizados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
