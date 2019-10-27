# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sectorMateriales.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 581)
        Form.setStyleSheet("")
        self.ma_btn_maxmin = QtWidgets.QPushButton(Form)
        self.ma_btn_maxmin.setGeometry(QtCore.QRect(70, 280, 311, 41))
        self.ma_btn_maxmin.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_maxmin.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_maxmin.setFlat(False)
        self.ma_btn_maxmin.setObjectName("ma_btn_maxmin")
        self.ma_btn_altabaja = QtWidgets.QPushButton(Form)
        self.ma_btn_altabaja.setGeometry(QtCore.QRect(70, 220, 311, 41))
        self.ma_btn_altabaja.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_altabaja.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_altabaja.setFlat(False)
        self.ma_btn_altabaja.setObjectName("ma_btn_altabaja")
        self.ma_btn_cancelar = QtWidgets.QPushButton(Form)
        self.ma_btn_cancelar.setGeometry(QtCore.QRect(270, 530, 111, 31))
        self.ma_btn_cancelar.setStyleSheet("color:white;\n"
"background-color:#ff4e4e;\n"
"border:none;")
        self.ma_btn_cancelar.setObjectName("ma_btn_cancelar")
        self.ma_btn_inventario = QtWidgets.QPushButton(Form)
        self.ma_btn_inventario.setGeometry(QtCore.QRect(70, 400, 311, 41))
        self.ma_btn_inventario.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_inventario.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_inventario.setFlat(False)
        self.ma_btn_inventario.setObjectName("ma_btn_inventario")
        self.ma_btn_consulta = QtWidgets.QPushButton(Form)
        self.ma_btn_consulta.setGeometry(QtCore.QRect(70, 100, 311, 41))
        self.ma_btn_consulta.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_consulta.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_consulta.setFlat(False)
        self.ma_btn_consulta.setObjectName("ma_btn_consulta")
        self.ma_btn_modificacion = QtWidgets.QPushButton(Form)
        self.ma_btn_modificacion.setGeometry(QtCore.QRect(70, 160, 311, 41))
        self.ma_btn_modificacion.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_modificacion.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_modificacion.setFlat(False)
        self.ma_btn_modificacion.setObjectName("ma_btn_modificacion")
        self.ma_btn_aprovisionamiento = QtWidgets.QPushButton(Form)
        self.ma_btn_aprovisionamiento.setGeometry(QtCore.QRect(70, 460, 311, 41))
        self.ma_btn_aprovisionamiento.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_aprovisionamiento.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_aprovisionamiento.setFlat(False)
        self.ma_btn_aprovisionamiento.setObjectName("ma_btn_aprovisionamiento")
        self.ma_btn_stockmovil = QtWidgets.QPushButton(Form)
        self.ma_btn_stockmovil.setGeometry(QtCore.QRect(70, 340, 311, 41))
        self.ma_btn_stockmovil.setStyleSheet("background-color:#5f5fff;\n"
"color:white;\n"
"border:none;\n"
"font-size:15px;")
        self.ma_btn_stockmovil.setIconSize(QtCore.QSize(16, 20))
        self.ma_btn_stockmovil.setFlat(False)
        self.ma_btn_stockmovil.setObjectName("ma_btn_stockmovil")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 20, 231, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ScaBox - Materiales"))
        self.ma_btn_maxmin.setText(_translate("Form", "Máxima/Mínima de Stock"))
        self.ma_btn_altabaja.setText(_translate("Form", "Alta/Baja de Articulos"))
        self.ma_btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.ma_btn_inventario.setText(_translate("Form", "Inventario"))
        self.ma_btn_consulta.setText(_translate("Form", "Consulta de Stock"))
        self.ma_btn_modificacion.setText(_translate("Form", "Modificacion de Stock"))
        self.ma_btn_aprovisionamiento.setText(_translate("Form", "Aprovisionamiento"))
        self.ma_btn_stockmovil.setText(_translate("Form", "Stock por movil"))
        self.label.setText(_translate("Form", "Sector Materiales"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
