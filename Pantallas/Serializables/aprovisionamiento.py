# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aprovisionamiento.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 449)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 691, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.se_btn_cancelar = QtWidgets.QPushButton(Form)
        self.se_btn_cancelar.setGeometry(QtCore.QRect(430, 380, 131, 31))
        self.se_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.se_btn_cancelar.setObjectName("se_btn_cancelar")
        self.se_btn_confirmar = QtWidgets.QPushButton(Form)
        self.se_btn_confirmar.setGeometry(QtCore.QRect(260, 380, 131, 31))
        self.se_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.se_btn_confirmar.setObjectName("se_btn_confirmar")
        self.se_tabla = QtWidgets.QTreeWidget(Form)
        self.se_tabla.setGeometry(QtCore.QRect(20, 90, 801, 141))
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
        self.se_tabla.setColumnWidth(1, 140)
        self.se_input_1 = QtWidgets.QSpinBox(Form)
        self.se_input_1.setGeometry(QtCore.QRect(230, 290, 381, 31))
        self.se_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.se_input_1.setMaximum(1000)
        self.se_input_1.setObjectName("se_input_1")
        self.se_label_1 = QtWidgets.QLabel(Form)
        self.se_label_1.setGeometry(QtCore.QRect(230, 250, 381, 31))
        self.se_label_1.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.se_label_1.setObjectName("se_label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aprovisionamiento"))
        self.label_2.setText(_translate("Form", "Aprovisionamiento"))
        self.se_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.se_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.se_tabla.headerItem().setText(0, _translate("Form", "Código"))
        self.se_tabla.headerItem().setText(1, _translate("Form", "Serializable"))
        self.se_tabla.headerItem().setText(2, _translate("Form", "Cantidad de pedido automatico"))
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
