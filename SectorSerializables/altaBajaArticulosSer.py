from PyQt5 import QtWidgets
from Pantallas.Serializables import altaBajaArticulosOption
from Pantallas.Serializables import altaDeArticulosSerializables
from Pantallas.Serializables import bajaDeArticulosSerializables


class altaBaja(QtWidgets.QWidget, altaBajaArticulosOption.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_1.clicked.connect(self.altaSerializableOpc)
        self.se_btn_2.clicked.connect(self.bajaSerializableOpc)

    def altaSerializableOpc(self):
        self.window = altaArticulo()
        self.window.show()

    def bajaSerializableOpc(self):
        self.window = bajaArticulo()
        self.window.show()

class altaArticulo(QtWidgets.QWidget, altaDeArticulosSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.altaSer)

    def altaSer(self):
        self.value1 = self.se_input_1.text()
        self.value2 = self.se_input_2.text()
        self.value3 = self.se_input_3.text()
        self.value4 = self.se_input_4.text()


class bajaArticulo(QtWidgets.QWidget, bajaDeArticulosSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.bajaSer)

    def bajaSer(self):
        self.value1 = self.se_input_1.text()
        self.value2 = self.se_input_2.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = altaBaja()
    window.show()
    app.exec_()
