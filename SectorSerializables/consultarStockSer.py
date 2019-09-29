from PyQt5 import QtWidgets, QtGui, QtCore
from Pantallas.Serializables import consultarStockSerializables
from Abm import ABM_serializables
import random

class ConsultarStockSerializables(QtWidgets.QWidget,consultarStockSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_buscar.clicked.connect(self.buscarArticulo)
        _translate = QtCore.QCoreApplication.translate
        ser_all = AbmObj.consulta_ser_all()
        for cant_ser_bd in range(0,len(ser_all)):
            QtWidgets.QTreeWidgetItem(self.se_tabla)
        for posicion in range(0,6):
            for i in range(0, len(ser_all)):
                self.se_tabla.topLevelItem(i).setText(posicion, str(ser_all[i][posicion]))
                print(str(ser_all[i][posicion]))

    def buscarArticulo(self):
        self.valor1 = str(self.se_input_buscar.text())
        try:
            consulta = AbmObj.consulta_serializables(self.valor1)
            print(consulta[0][1])
        except:
            print("No se encontro el numero de MAC buscado")


AbmObj = ABM_serializables()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ConsultarStockSerializables()
    window.show()
    app.exec_()