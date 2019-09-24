# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockPorMovil.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 532)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 231, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 90, 41, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.se_input_1 = QtWidgets.QLineEdit(Form)
        self.se_input_1.setGeometry(QtCore.QRect(80, 90, 281, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setText("")
        self.se_input_1.setObjectName("se_input_1")
        self.se_input_2 = QtWidgets.QLineEdit(Form)
        self.se_input_2.setGeometry(QtCore.QRect(450, 90, 261, 31))
        self.se_input_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_2.setText("")
        self.se_input_2.setObjectName("se_input_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 90, 61, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(30, 150, 681, 281))
        self.se_tabla.setObjectName("se_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.se_tabla.headerItem().setFont(1, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(1, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(1, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.se_tabla)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(1, font)
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(300, 470, 141, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.se_input_2, self.se_input_1)
        Form.setTabOrder(self.se_input_1, self.se_tabla)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Stock por Movil"))
        self.label.setText(_translate("Form", "Móvil"))
        self.label_3.setText(_translate("Form", "Material"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Móvil"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Material"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(False)
        self.se_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item lorem ipsum "))
        self.se_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(1).setText(0, _translate("Form", "New Item"))
        self.se_tabla.topLevelItem(1).setText(1, _translate("Form", "lorem"))
        self.se_tabla.topLevelItem(2).setText(0, _translate("Form", "New Item"))
        self.se_tabla.topLevelItem(2).setText(1, _translate("Form", "lorem"))
        self.se_tabla.setSortingEnabled(__sortingEnabled)
        self.se_btn_confirmar.setText(_translate("Form", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
