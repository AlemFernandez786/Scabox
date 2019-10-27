# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panelModificarSectorPersonal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(955, 578)
        self.su_tabla = QtWidgets.QTreeWidget(Form)
        self.su_tabla.setGeometry(QtCore.QRect(10, 90, 935, 161))
        self.su_tabla.setObjectName("su_tabla")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.su_tabla.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(3, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.su_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 501, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 270, 121, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.su_radiobutton_1 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_1.setGeometry(QtCore.QRect(260, 280, 82, 17))
        self.su_radiobutton_1.setObjectName("su_radiobutton_1")
        self.su_radiobutton_2 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_2.setGeometry(QtCore.QRect(370, 280, 82, 17))
        self.su_radiobutton_2.setObjectName("su_radiobutton_2")
        self.su_radiobutton_3 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_3.setGeometry(QtCore.QRect(490, 280, 82, 17))
        self.su_radiobutton_3.setObjectName("su_radiobutton_3")
        self.su_radiobutton_4 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_4.setGeometry(QtCore.QRect(600, 280, 121, 17))
        self.su_radiobutton_4.setObjectName("su_radiobutton_4")
        self.su_radiobutton_5 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_5.setGeometry(QtCore.QRect(750, 280, 121, 17))
        self.su_radiobutton_5.setObjectName("su_radiobutton_5")
        self.su_radiobutton_6 = QtWidgets.QRadioButton(Form)
        self.su_radiobutton_6.setGeometry(QtCore.QRect(850, 280, 121, 17))
        self.su_radiobutton_6.setObjectName("su_radiobutton_6")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 390, 61, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label_3.setObjectName("label_3")
        self.su_input_1 = QtWidgets.QTextEdit(Form)
        self.su_input_1.setGeometry(QtCore.QRect(190, 390, 600, 91))
        self.su_input_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_1.setObjectName("su_input_1")
        self.su_btn_confirmar = QtWidgets.QPushButton(Form)
        self.su_btn_confirmar.setGeometry(QtCore.QRect(330, 510, 131, 31))
        self.su_btn_confirmar.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_confirmar.setObjectName("su_btn_confirmar")
        self.su_btn_cancelar = QtWidgets.QPushButton(Form)
        self.su_btn_cancelar.setGeometry(QtCore.QRect(530, 510, 131, 31))
        self.su_btn_cancelar.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"border:none;\n"
"background-color:#ff4e4e;")
        self.su_btn_cancelar.setObjectName("su_btn_cancelar")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.su_tabla.headerItem().setText(0, _translate("Form", "Legajo"))
        self.su_tabla.headerItem().setText(1, _translate("Form", "Nombre"))
        self.su_tabla.headerItem().setText(2, _translate("Form", "Apellido"))
        self.su_tabla.headerItem().setText(3, _translate("Form", "Sector"))
        __sortingEnabled = self.su_tabla.isSortingEnabled()
        self.su_tabla.setSortingEnabled(False)
        self.su_tabla.topLevelItem(0).setText(0, _translate("Form", "New Item  "))
        self.su_tabla.topLevelItem(0).setText(1, _translate("Form", "lorem"))
        self.su_tabla.topLevelItem(0).setText(2, _translate("Form", "lorem"))
        self.su_tabla.topLevelItem(0).setText(3, _translate("Form", "lorem"))
        self.su_tabla.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Modificar de Sector de Personal"))
        self.label.setText(_translate("Form", "Sector a transferir"))
        self.su_radiobutton_1.setText(_translate("Form", "Materiales"))
        self.su_radiobutton_2.setText(_translate("Form", "Herramientas"))
        self.su_radiobutton_3.setText(_translate("Form", "Serializables"))
        self.su_radiobutton_4.setText(_translate("Form", "Control de Calidad"))
        self.su_radiobutton_5.setText(_translate("Form", "Supervisor"))
        self.su_radiobutton_6.setText(_translate("Form", "Tecnico"))
        self.label_3.setText(_translate("Form", "Motivo"))
        self.su_input_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.su_btn_confirmar.setText(_translate("Form", "Confirmar"))
        self.su_btn_cancelar.setText(_translate("Form", "Cancelar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
