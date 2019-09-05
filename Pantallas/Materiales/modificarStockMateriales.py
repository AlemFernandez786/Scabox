# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarStockMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 663)
        self.ma_input_buscar = QtWidgets.QLineEdit(Form)
        self.ma_input_buscar.setGeometry(QtCore.QRect(310, 80, 251, 31))
        self.ma_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_buscar.setText("")
        self.ma_input_buscar.setObjectName("ma_input_buscar")
        self.ma_btn_buscar = QtWidgets.QPushButton(Form)
        self.ma_btn_buscar.setGeometry(QtCore.QRect(570, 80, 131, 31))
        self.ma_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_buscar.setObjectName("ma_btn_buscar")
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
        self.ma_input_3 = QtWidgets.QLineEdit(Form)
        self.ma_input_3.setGeometry(QtCore.QRect(330, 420, 251, 31))
        self.ma_input_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_3.setText("")
        self.ma_input_3.setObjectName("ma_input_3")
        self.ma_input_2 = QtWidgets.QLineEdit(Form)
        self.ma_input_2.setGeometry(QtCore.QRect(330, 370, 251, 31))
        self.ma_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_2.setText("")
        self.ma_input_2.setObjectName("ma_input_2")
        self.ma_input_1 = QtWidgets.QLineEdit(Form)
        self.ma_input_1.setGeometry(QtCore.QRect(330, 320, 251, 31))
        self.ma_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_1.setText("")
        self.ma_input_1.setObjectName("ma_input_1")
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
        self.ma_btn_confirmar = QtWidgets.QPushButton(Form)
        self.ma_btn_confirmar.setGeometry(QtCore.QRect(270, 590, 131, 31))
        self.ma_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.ma_btn_confirmar.setObjectName("ma_btn_confirmar")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(430, 590, 131, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 470, 111, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_6.setObjectName("label_6")
        self.ma_input_4 = QtWidgets.QTextEdit(Form)
        self.ma_input_4.setGeometry(QtCore.QRect(330, 470, 251, 71))
        self.ma_input_4.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.ma_input_4.setObjectName("ma_input_4")
        self.ma_tabla = QtWidgets.QTreeWidget(Form)
        self.ma_tabla.setGeometry(QtCore.QRect(10, 130, 821, 171))
        self.ma_tabla.setObjectName("ma_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ma_tabla.headerItem().setFont(5, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ma_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ma_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.ma_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ma_btn_buscar.setText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Ingrese código del articulo"))
        self.label_2.setText(_translate("Form", "Modificacion de Stock (Materiales)"))
        self.label_3.setText(_translate("Form", "Cantidad actual"))
        self.label_5.setText(_translate("Form", "Cantidad minima"))
        self.label_4.setText(_translate("Form", "Cantidad maxima"))
        self.ma_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_6.setText(_translate("Form", "Descripcion"))
        self.ma_tabla.headerItem().setText(0, _translate("Form", "Codigo"))
        self.ma_tabla.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.ma_tabla.headerItem().setText(2, _translate("Form", "Cantidad de Stock disponible"))
        self.ma_tabla.headerItem().setText(3, _translate("Form", "Stock utilizado en los ultimos 30 dias"))
        self.ma_tabla.headerItem().setText(4, _translate("Form", "Stock Minimo permitido"))
        self.ma_tabla.headerItem().setText(5, _translate("Form", "Stock Maximo permitido"))
        __sortingEnabled = self.ma_tabla.isSortingEnabled()
        self.ma_tabla.setSortingEnabled(False)
        self.ma_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item  "))
        self.ma_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(0).setText(2, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(0).setText(3, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(0).setText(4, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(0).setText(5, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(1).setText(0, _translate("Form", "New Item"))
        self.ma_tabla.topLevelItem(1).setText(1, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(1).setText(2, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(1).setText(3, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(1).setText(4, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(1).setText(5, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(2).setText(0, _translate("Form", "New Item"))
        self.ma_tabla.topLevelItem(2).setText(1, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(2).setText(2, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(2).setText(3, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(2).setText(4, _translate("Form", "lorem"))
        self.ma_tabla.topLevelItem(2).setText(5, _translate("Form", "lorem"))
        self.ma_tabla.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

