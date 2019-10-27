from PyQt5 import QtWidgets
from Pantallas.Serializables import modificacionDeStockSerializables


class ModificacionStockSerializables(QtWidgets.QWidget, modificacionDeStockSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_buscar.clicked.connect(self.buscarSerializables)
        self.se_btn_confirmar.clicked.connect(self.modificarStock)

    def buscarSerializables(self):
        self.value1 = self.se_input_buscar.text()

    def modificarStock(self):
        self.value1 = self.se_input_1.text()
        self.value2 = self.se_input_2.text()
        self.value3 = self.se_input_3.text()
        self.value4 = self.se_input_4.toPlainText()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ModificacionStockSerializables()
    window.show()
    app.exec_()