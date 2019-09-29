# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacionDeStockSerializables.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 831, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.se_input_3 = QtWidgets.QLineEdit(Form)
        self.se_input_3.setGeometry(QtCore.QRect(330, 420, 251, 31))
        self.se_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_3.setText("")
        self.se_input_3.setObjectName("se_input_3")
        self.se_input_2 = QtWidgets.QLineEdit(Form)
        self.se_input_2.setGeometry(QtCore.QRect(330, 370, 251, 31))
        self.se_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_2.setText("")
        self.se_input_2.setObjectName("se_input_2")
        self.se_input_1 = QtWidgets.QLineEdit(Form)
        self.se_input_1.setGeometry(QtCore.QRect(330, 320, 251, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setText("")
        self.se_input_1.setObjectName("se_input_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 320, 111, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 420, 111, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 370, 121, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(270, 590, 131, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")
        self.se_btn_cancelar = QtWidgets.QPushButton(Form)
        self.se_btn_cancelar.setGeometry(QtCore.QRect(430, 590, 131, 31))
        self.se_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.se_btn_cancelar.setObjectName("se_btn_cancelar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 470, 111, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.se_input_4 = QtWidgets.QTextEdit(Form)
        self.se_input_4.setGeometry(QtCore.QRect(330, 470, 251, 71))
        self.se_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_4.setObjectName("se_input_4")
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(10, 120, 821, 181))
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.se_tabla.headerItem().setFont(6, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(5, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(5, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(5, font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.se_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese código del articulo"))
        self.label_2.setText(_translate("Form", "Modificacion de Stock (Serializables)"))
        self.label_3.setText(_translate("Form", "Cantidad actual"))
        self.label_5.setText(_translate("Form", "Cantidad minima"))
        self.label_4.setText(_translate("Form", "Cantidad maxima"))
        self.se_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.se_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_6.setText(_translate("Form", "Descripcion"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Codigo MAC"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Cantidad de Stock disponible"))
        self.se_tabla.headerItem().setText(3, _translate("Form", "Lote"))
        self.se_tabla.headerItem().setText(4, _translate("Form", "Stock utilizado en los ultimos 30 dias"))
        self.se_tabla.headerItem().setText(5, _translate("Form", "Stock Minimo permitido"))
        self.se_tabla.headerItem().setText(6, _translate("Form", "Stock Maximo permitido"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(False)
        self.se_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item  "))
        self.se_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(0).setText(2, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(0).setText(3, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(0).setText(4, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(0).setText(5, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(0).setText(6, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(0, _translate("Form", "New Item"))
        self.se_tabla.topLevelItem(1).setText(1, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(2, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(3, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(4, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(5, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(6, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(0, _translate("Form", "New Item"))
        self.se_tabla.topLevelItem(2).setText(1, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(2, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(3, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(4, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(5, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(6, _translate("Form", "lorem"))
        self.se_tabla.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
