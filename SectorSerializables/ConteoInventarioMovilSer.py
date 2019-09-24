from PyQt5 import QtWidgets
from Pantallas.Serializables import conteoDeInventarioPorMovil


class ConteoInventarioMovilSerializables(QtWidgets.QWidget, conteoDeInventarioPorMovil.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.consultarStockSer)

    def consultarStockSer(self):
        self.value1 = self.se_input_1.text()
        self.value2 = self.se_input_2.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ConteoInventarioMovilSerializables()
    window.show()
    app.exec_()