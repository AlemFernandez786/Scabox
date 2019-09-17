from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Materiales import altaBajaArticulosMaterialesOption
from Pantallas.Materiales import sectorMateriales
from Pantallas.Materiales import modificacionMaxMinIngreso
from Pantallas.Materiales import aprovisionamiento
from Pantallas.Materiales import consultarStockMateriales
from Pantallas.Materiales import conteoDeInventarioPorMovil
from Pantallas.Materiales import modificarStockMateriales
from Pantallas.Materiales import stockPorMovilMateriales
from Pantallas.Materiales import altaDeArticulosMateriales
from Pantallas.Materiales import bajaDeArticulosMateriales
from ABM import ABM_materiales

import sys


class VentanaMateriales(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaMateriales, self).__init__(*args, **kwargs)
        self.ui = sectorMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_1.clicked.connect(self.consulta_stock)
        self.ui.ma_btn_2.clicked.connect(self.modificacion_stock)
        self.ui.ma_btn_3.clicked.connect(self.alta_baja_stock)
        self.ui.ma_btn_4.clicked.connect(self.maxima_minima_stock)
        self.ui.ma_btn_5.clicked.connect(self.stock_movil)
        self.ui.ma_btn_6.clicked.connect(self.inventario_movil)
        self.ui.ma_btn_7.clicked.connect(self.aprovisionamiento_stock)
        self.ui.ma_btn_cancelar.clicked.connect(self.cancelar)

    def consulta_stock(self):
        ventanaconsulta = StockMateriales(self)
        ventanaconsulta.exec_()

    def modificacion_stock(self):
        ventanamodificacionstock = ModificarStock(self)
        ventanamodificacionstock.exec_()

    def alta_baja_stock(self):
        ventanaaltabaja = VentanaAltaBaja(self)
        ventanaaltabaja.exec_()

    def maxima_minima_stock(self):
        ventanamaxmin = MaximaMinima(self)
        ventanamaxmin.exec_()

    def stock_movil(self):
        ventanastockmovil = StockPorMovil(self)
        ventanastockmovil.exec_()

    def inventario_movil(self):
        ventanainventario = InventarioMovil(self)
        ventanainventario.exec_()

    def aprovisionamiento_stock(self):
        ventanaaprovisionamiento = Aprovisionamiento(self)
        ventanaaprovisionamiento.exec_()

    def cancelar(self):
        self.close()


class VentanaAltaBaja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(VentanaAltaBaja, self).__init__(*args, **kwargs)
        self.ui = altaBajaArticulosMaterialesOption.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_1.pressed.connect(self.alta)
        self.ui.ma_btn_2.pressed.connect(self.baja)

    def alta(self):
        ventanaalta = Alta(self)
        ventanaalta.exec_()

    def baja(self):
        ventanabaja = Baja(self)
        ventanabaja.exec_()


class Alta(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Alta, self).__init__(*args, **kwargs)
        self.ui = altaDeArticulosMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

    def salir(self):
        self.close()

    def confirmar(self):
        valores=(str(self.ui.ma_input_6.toPlainText()),str(self.ui.ma_input_2.text()),str(self.ui.ma_input_3.text()),str(self.ui.ma_input_4.text()))
        agregar=ABM_materiales()
        agregar.alta_materiales(valores)

class Baja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Baja, self).__init__(*args, **kwargs)
        self.ui = bajaDeArticulosMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()


class StockPorMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockPorMovil, self).__init__(*args, **kwargs)
        self.ui = stockPorMovilMateriales.Ui_Form()
        self.ui.setupUi(self)


class ModificarStock(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificarStock, self).__init__(*args, **kwargs)
        self.ui = modificarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_buscar.clicked.connect(self.busqueda)
        self.ui.ma_btn_confirmar.clicked.connect(self.modificacion)

    def salir(self):
        self.close()

    def busqueda(self):
        try:
            codigo = int(self.ui.ma_input_buscar.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))

        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return
        # self.ui.ma_input_1.setDisabled(True)
        self.ui.ma_input_1.setText(str(resultados[2]))
        self.ui.ma_input_2.setDisabled(True)
        self.ui.ma_input_2.setText(str(resultados[4]))
        self.ui.ma_input_3.setDisabled(True)
        self.ui.ma_input_3.setText(str(resultados[3]))
        self.ui.ma_input_4.setDisabled(True)
        self.ui.ma_input_4.setText(str(resultados[1]))

    def modificacion(self):
        valor = ["",""]
        valor[0] = str(self.ui.ma_input_buscar.text())
        try:
            cantidad = int(self.ui.ma_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        valor[1]=str(cantidad)
        modificar = ABM_materiales()
        modificar.modificacion_materiales(valor)
        codigo=(int(valor[0]))
        self.busqueda()



class InventarioMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(InventarioMovil, self).__init__(*args, **kwargs)
        self.ui = conteoDeInventarioPorMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()


class Aprovisionamiento(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Aprovisionamiento, self).__init__(*args, **kwargs)
        self.ui = aprovisionamiento.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()


class StockMateriales(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMateriales, self).__init__(*args, **kwargs)
        self.ui = consultarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
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
        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla.topLevelItem(0).setText(posicion, str(i))
            posicion += 1


class MaximaMinima(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(MaximaMinima, self).__init__(*args, **kwargs)
        self.ui = modificacionMaxMinIngreso.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())
