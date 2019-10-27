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
        self.se_label_2 = QtWidgets.QLabel(Form)
        self.se_label_2.setGeometry(QtCore.QRect(250, 20, 231, 41))
        self.se_label_2.setStyleSheet("font-size:20px;\n"
"")
        self.se_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.se_label_2.setObjectName("se_label_2")
        self.se_label = QtWidgets.QLabel(Form)
        self.se_label.setGeometry(QtCore.QRect(30, 90, 65, 31))
        self.se_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.se_label.setObjectName("se_label")
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
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(300, 470, 141, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock por Móvil"))
        self.se_label_2.setText(_translate("Form", "Stock por Móvil"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Móvil"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Tecnicos"))
        __sortingEnabled = self.se_tabla.isSortingEnabled()
        self.se_tabla.setSortingEnabled(False)
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
