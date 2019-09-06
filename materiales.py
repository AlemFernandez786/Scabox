from PyQt5 import QtWidgets

from Pantallas.Materiales import sectorMateriales
from Pantallas.Materiales import modificacionMaxMinIngreso
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
        self.ui.ma_btn_6.clicked.connect(self.inventario_stock)
        self.ui.ma_btn_7.clicked.connect(self.aprovisionamiento_stock)
        self.ui.ma_btn_cancelar.clicked.connect(self.cancelar)

    def consulta_stock(self):
        print("Consulta")

    def modificacion_stock(self):
        print("modificacion")

    def alta_baja_stock(self):
        print("alta/baja")

    def maxima_minima_stock(self):
        ventanamaxmin = MaximaMinima(self)
        ventanamaxmin.exec_()

    def stock_movil(self):
        print("stock x movil")

    def inventario_stock(self):
        print("inventario")

    def aprovisionamiento_stock(self):
        print("aprovisionamiento")

    def cancelar(self):
        self.close()


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
