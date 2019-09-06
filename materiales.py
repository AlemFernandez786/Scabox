from PyQt5 import QtWidgets
from Pantallas.Materiales import altaBajaArticulosMaterialesOption
from Pantallas.Materiales import sectorMateriales
from Pantallas.Materiales import modificacionMaxMinIngreso
from Pantallas.Materiales import aprovisionamiento
from Pantallas.Materiales import consultarStockMateriales
from Pantallas.Materiales import conteoDeInventarioPorMovil
from Pantallas.Materiales import modificarStockMateriales
from Pantallas.Materiales import stockPorMovilMateriales
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
        ventanaalta = AltaBaja(self)
        ventanaalta.exec_()

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


class AltaBaja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AltaBaja, self).__init__(*args, **kwargs)
        self.ui = altaBajaArticulosMaterialesOption.Ui_Form()
        self.ui.setupUi(self)


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


class InventarioMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(InventarioMovil, self).__init__(*args, **kwargs)
        self.ui = conteoDeInventarioPorMovil.Ui_Form()
        self.ui.setupUi(self)


class Aprovisionamiento(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Aprovisionamiento, self).__init__(*args, **kwargs)
        self.ui = aprovisionamiento.Ui_Form()
        self.ui.setupUi(self)


class StockMateriales(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMateriales, self).__init__(*args, **kwargs)
        self.ui = consultarStockMateriales.Ui_Form()
        self.ui.setupUi(self)


class MaximaMinima(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(MaximaMinima, self).__init__(*args, **kwargs)
        self.ui = modificacionMaxMinIngreso.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())
