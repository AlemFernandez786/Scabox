# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarStockMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 524)
        self.su_tabla = QtWidgets.QTreeWidget(Form)
        self.su_tabla.setGeometry(QtCore.QRect(10, 180, 911, 251))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.su_tabla.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.su_tabla.headerItem().setFont(5, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.su_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)
        item_0.setFont(4, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.su_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.su_tabla)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(4, font)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 171, 41))
        self.label_2.setStyleSheet("font-size:20px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(750, 60, 171, 41))
        self.label_3.setStyleSheet("font-size:20px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.su_btn_volver = QtWidgets.QPushButton(Form)
        self.su_btn_volver.setGeometry(QtCore.QRect(380, 460, 131, 31))
        self.su_btn_volver.setStyleSheet("background-color: rgb(99, 206, 104);\n"
"color:white;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_volver.setObjectName("su_btn_volver")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 120, 171, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.su_input_buscar = QtWidgets.QLineEdit(Form)
        self.su_input_buscar.setGeometry(QtCore.QRect(360, 120, 251, 31))
        self.su_input_buscar.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.su_input_buscar.setText("")
        self.su_input_buscar.setObjectName("su_input_buscar")
        self.su_btn_buscar = QtWidgets.QPushButton(Form)
        self.su_btn_buscar.setGeometry(QtCore.QRect(620, 120, 131, 31))
        self.su_btn_buscar.setStyleSheet("background-color: rgb(199, 199, 199);\n"
"color:black;\n"
"font-size:10pt;\n"
"border:none;")
        self.su_btn_buscar.setObjectName("su_btn_buscar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.su_tabla.headerItem().setText(0, _translate("Form", "Codigo"))
        self.su_tabla.headerItem().setText(1, _translate("Form", "Descripcion"))
        self.su_tabla.headerItem().setText(2, _translate("Form", "Cantidad de Stock disponible"))
        self.su_tabla.headerItem().setText(3, _translate("Form", "Stock utilizado en los ultimos 30 dias"))
        self.su_tabla.headerItem().setText(4, _translate("Form", "Stock Minimo permitido"))
        self.su_tabla.headerItem().setText(5, _translate("Form", "Stock Maximo permitido"))
        __sortingEnabled = self.su_tabla.isSortingEnabled()
        self.su_tabla.setSortingEnabled(False)
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        # posicion = 0
        # resultados = resultado[0]
        _translate = QtCore.QCoreApplication.translate
        len_resultado=(len(resultado))
        for i in range (0,len_resultado):
            #print(resultado[i])
            posicion = 0
            for a in range (0,len(resultado[i])):
                test=resultado[i][a]
                #print(test)
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion+=1
                #print(resultado[i][a])
        self.su_tabla.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Consulta Stock"))
        self.label_3.setText(_translate("Form", "Materiales"))
        self.su_btn_volver.setText(_translate("Form", "Volver"))
        self.label.setText(_translate("Form", "Ingrese código del articulo"))
        self.su_btn_buscar.setText(_translate("Form", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
