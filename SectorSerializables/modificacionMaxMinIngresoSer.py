from PyQt5 import QtWidgets
from Pantallas.Serializables import modificacionMaxMinIngreso
from Pantallas.Serializables import modificacionMaxMin

class ModificacionMaxMinIngresoSerializables(QtWidgets.QWidget, modificacionMaxMinIngreso.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.elegirCodigoSer)

    def elegirCodigoSer(self):
        self.value1 = self.se_input_1.text()
        self.window = ModificarMinMaxSerializables()
        self.window.show()

class ModificarMinMaxSerializables(QtWidgets.QWidget, modificacionMaxMin.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.modificarMinMaxSer)

    def modificarMinMaxSer(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ModificacionMaxMinIngresoSerializables()
    window.show()
    app.exec_()