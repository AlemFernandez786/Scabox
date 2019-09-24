from PyQt5 import QtWidgets

from Pantallas.Serializables import sectorSerializables
from SectorSerializables import consultarStockSer
from SectorSerializables import modificacionStockSer
from SectorSerializables import altaBajaArticulosSer
from SectorSerializables import stockMovilSer
from SectorSerializables import modificacionMaxMinIngresoSer
from SectorSerializables import ConteoInventarioMovilSer
from SectorSerializables import aprovisionamientoSer

import sys


class VentanaSerializables(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaSerializables, self).__init__(*args, **kwargs)
        self.ui = sectorSerializables.Ui_Form()
        self.ui.setupUi(self)
        self.ui.se_btn_1.clicked.connect(self.consulta_stock)
        self.ui.se_btn_2.clicked.connect(self.modificacion_stock)
        self.ui.se_btn_3.clicked.connect(self.alta_baja_stock)
        self.ui.se_btn_4.clicked.connect(self.maxima_minima_stock)
        self.ui.se_btn_5.clicked.connect(self.stock_movil)
        self.ui.se_btn_6.clicked.connect(self.inventario_stock)
        self.ui.se_btn_7.clicked.connect(self.aprovisionamiento_stock)
        self.ui.se_btn_8.clicked.connect(self.historial)
        self.ui.se_btn_cancelar.clicked.connect(self.cancelar)

    def consulta_stock(self):
        self.window = consultarStockSer.ConsultarStockSerializables()
        self.window.show()

    def modificacion_stock(self):
        self.window = modificacionStockSer.ModificacionStockSerializables()
        self.window.show()

    def alta_baja_stock(self):
        self.window = altaBajaArticulosSer.altaBaja()
        self.window.show()

    def maxima_minima_stock(self):
        self.window = modificacionMaxMinIngresoSer.ModificacionMaxMinIngresoSerializables()
        self.window.show()

    def stock_movil(self):
        self.window = stockMovilSer.StockMovilSerializables()
        self.window.show()

    def inventario_stock(self):
        self.window = ConteoInventarioMovilSer.ConteoInventarioMovilSerializables()
        self.window.show()

    def aprovisionamiento_stock(self):
        self.window = aprovisionamientoSer.AprovisionamientoSerializables()
        self.window.show()

    def historial(self):
        print("historial")

    def cancelar(self):
        self.close()


#class MaximaMinima(QtWidgets.QDialog):
 #   def __init__(self, *args, **kwargs):
  #      super(MaximaMinima, self).__init__(*args, **kwargs)
   #     self.ui = modificacionMaxMinIngreso.Ui_Form()
    #    self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaSerializables()
    application.show()
    sys.exit(app.exec_())
