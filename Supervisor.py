from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Supervisor import alerta_confirmacion
from Pantallas.Supervisor import alerta_error
from Pantallas.Supervisor import altaBajaPersonalOption
from Pantallas.Supervisor import altaDePersonal
from Pantallas.Supervisor import bajaDePersonal
from Pantallas.Supervisor import modificacionSectorDePersonal
from Pantallas.Supervisor import panelModificarSectorPersonal
from Pantallas.Supervisor import consultarStock
from Pantallas.Supervisor import supervisor
from Pantallas.Materiales import consultarStockMateriales
from ABM import ABM_materiales
import mysql.connector

import sys

class VentanaSupervisor(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaSupervisor, self).__init__(*args, **kwargs)
        self.ui = supervisor.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.clicked.connect(self.consultar_Stock)
        self.ui.su_btn_2.clicked.connect(self.altaBajaPersonal)
        self.ui.su_btn_3.clicked.connect(self.modificacionSector)
        self.ui.su_btn_cancelar.clicked.connect(self.cancelar)

    def consultar_Stock(self):
        seleccionsectorparaconsulta = Sectordeconsulta(self)
        seleccionsectorparaconsulta.exec_()

    def altaBajaPersonal(self):
        ventanaaltabajapersonal = AltaBajaPersonal(self)
        ventanaaltabajapersonal.exec_()

    def modificacionSector(self):
        ventanamodificacionsector = ModificacionSector(self)
        ventanamodificacionsector.exec_()

    def cancelar(self):
        self.close()

class Sectordeconsulta(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Sectordeconsulta, self).__init__(*args, **kwargs)
        self.ui = consultarStock.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.pressed.connect(self.materiales)
        self.ui.su_btn_2.pressed.connect(self.herramientas)
        self.ui.su_btn_3.clicked.connect(self.serializables)

    def materiales(self):
        ventanamateriales = StockMateriales(self)
        ventanamateriales.exec_()

    def herramientas(self):
        ventanaherramientas = StockHerramientas(self)
        ventanaherramientas.exec_()

    def serializables(self):
        ventanaserializables = StockSerializables(self)
        ventanaserializables.exec_()

class StockMateriales(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMateriales, self).__init__(*args, **kwargs)
        self.ui = consultarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            # resultado[i].insert(3, str(999))
            posicion = 0
            for a in range(0, len(resultado[i])):
                item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
                test = resultado[i][a]
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

        self.ui.ma_btn_buscar.clicked.connect(self.consulta)
        self.ui.ma_btn_volver.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def consulta(self):
        try:
            codigo = int(self.ui.ma_input_buscar.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))
        posicion = 0
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return
        _translate = QtCore.QCoreApplication.translate

        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(i)))
            posicion += 1

        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            # print(resultado[i])
            posicion = 0
            for a in range(0, len(resultado[i])):
                item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
                test = ''
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

class AltaBajaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AltaBajaPersonal, self).__init__(*args, **kwargs)
        self.ui = altaBajaPersonalOption.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.pressed.connect(self.alta)
        self.ui.su_btn_2.pressed.connect(self.baja)

    def alta(self):
        ventanaalta = AltaPersonal(self)
        ventanaalta.exec_()

    def baja(self):
        ventanabaja = BajaPersonal(self)
        ventanabaja.exec_()

class AltaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AltaPersonal, self).__init__(*args, **kwargs)
        self.ui = altaDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.alta)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
        # self.ui.su_input_1.clicked.connect(self.modificacionSector)

    def alta(self):
        ventanaalta = Alta(self)
        ventanaalta.exec_()

    def cancelar(self):
        self.close()

class BajaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(BajaPersonal, self).__init__(*args, **kwargs)
        self.ui = bajaDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.alta)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
        # self.ui.su_input_1.clicked.connect(self.modificacionSector)

    def alta(self):
        ventanaalta = Alta(self)
        ventanaalta.exec_()

    def cancelar(self):
        self.close()

class ModificacionSector(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificacionSector, self).__init__(*args, **kwargs)
        self.ui = modificacionSectorDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.Buscarlegajo)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
        #self.ui.su_input_1.clicked.connect(self.modificacionSector)

    def Buscarlegajo(self):
        ventanaBuscarlegajo = BuscarLegajo(self)
        ventanaBuscarlegajo.exec_()

    def cancelar(self):
        self.close()

class BuscarLegajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(BuscarLegajo, self).__init__(*args, **kwargs)
        self.ui = panelModificarSectorPersonal.Ui_Form()
        self.ui.setupUi(self)
        # self.ui.su_btn_confirmar.pressed.connect(self.alta)
        # self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
        #self.ui.su_input_1.clicked.connect(self.modificacionSector)

    def alta(self):
        ventanaalta = Alta(self)
        ventanaalta.exec_()

    def cancelar(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaSupervisor()
    application.show()
    sys.exit(app.exec_())
#TODO
#boton volver de stockmate
#stockHerr y seri
#
#alta/baja
#limitar el campolegajo
#armar todos los inputs
