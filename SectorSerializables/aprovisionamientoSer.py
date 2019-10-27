from PyQt5 import QtWidgets
from Pantallas.Serializables import aprovisionamiento


class AprovisionamientoSerializables(QtWidgets.QWidget, aprovisionamiento.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.consultarStockSer)

    def consultarStockSer(self):
        self.value1 = self.se_input_1.text()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AprovisionamientoSerializables()
    window.show()
    app.exec_()