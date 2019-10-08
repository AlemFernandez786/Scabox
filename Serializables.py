from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from datetime import date, timedelta
import smtplib
from Pantallas.Serializables import sectorSerializables

#from SectorSerializables import stockMovilSer
#from SectorSerializables import ConteoInventarioMovilSer
#from SectorSerializables import aprovisionamientoSer
from Pantallas.Serializables import consultarStockSerializables
from Pantallas.Serializables import modificacionDeStockSerializables
from Pantallas.Serializables import altaBajaArticulosOption
from Pantallas.Serializables import altaDeArticulosSerializables
from Pantallas.Serializables import bajaDeArticulosSerializables
from Pantallas.Serializables import modificacionMaxMinIngreso
from Pantallas.Serializables import modificacionMaxMin
from Pantallas.Serializables import stockPorMovil
from Pantallas.Serializables import tecnicosPorMovil
from Pantallas.Serializables import stockPorTipo
from Pantallas.Serializables import aprovisionamiento
from Pantallas.Serializables import estadoArticuloSerializables
from Pantallas.Serializables import alertEstadoArticuloSerializables
from ABM import ABM_serializables

import sys


class VentanaSerializables(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaSerializables, self).__init__(*args, **kwargs)
        self.ui = sectorSerializables.Ui_Form()
        self.ui.setupUi(self)
        self.ui.se_btn_1.clicked.connect(self.consulta_stock)
        self.ui.se_btn_2.clicked.connect(self.consulta_stock_tipo)
        self.ui.se_btn_3.clicked.connect(self.alta_baja_stock)
        self.ui.se_btn_4.clicked.connect(self.maxima_minima_stock)
        self.ui.se_btn_5.clicked.connect(self.stock_movil)
        self.ui.se_btn_6.clicked.connect(self.inventario_stock)
        self.ui.se_btn_7.clicked.connect(self.aprovisionamiento_stock)
        self.ui.se_btn_8.clicked.connect(self.historial)
        self.ui.se_btn_9.clicked.connect(self.estado)
        self.ui.se_btn_cancelar.clicked.connect(self.cancelar)

    def consulta_stock(self):
        self.window = ConsultarStockSerializables()
        self.window.show()

    def consulta_stock_tipo(self):
        self.window_Stock_Tipo = ConsultarStockTipoSerializables()
        self.window_Stock_Tipo.show()

    def alta_baja_stock(self):
        self.window = altaBaja()
        self.window.show()

    def maxima_minima_stock(self):
        self.windowminmax = ModificacionMaxMinIngresoSerializables()
        self.windowminmax.show()

    def stock_movil(self):
        self.window_stock_movil = TecnicosMovilSerializables()
        self.window_stock_movil.show()

    def inventario_stock(self):
        #self.window = ConteoInventarioMovilSer.ConteoInventarioMovilSerializables()
        #self.window.show()
        pass

    def aprovisionamiento_stock(self):
        self.window = Aprovisionamiento()
        self.window.show()
        pass

    def historial(self):
        print("historial")

    def estado(self):
        self.window_estado = EstadoSerializable()
        self.window_estado.show()

    def cancelar(self):
        self.close()


class ConsultarStockSerializables(QtWidgets.QWidget, consultarStockSerializables.Ui_Form):
    ser_all = []

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_buscar.clicked.connect(self.buscarArticulo)
        self.se_btn_volver.clicked.connect(self.salir)
        _translate = QtCore.QCoreApplication.translate
        self.ser_all = AbmObj.consulta_ser_all()
        for cant_ser_bd in range(0, len(self.ser_all)):
            QtWidgets.QTreeWidgetItem(self.se_tabla)
        for posicion in range(0, 3):
            for i in range(0, len(self.ser_all)):
                self.se_tabla.topLevelItem(i).setText(posicion, str(self.ser_all[i][posicion]))

    def buscarArticulo(self):
        try:
            self.valor1 = str(self.se_input_buscar.text())
        except:
            QMessageBox.about(self, "Error!!", "\nIngrese el numero de MAC!!\n")
            self.se_tabla.clear()
            for cant_ser_bd in range(0, len(self.ser_all)):
                QtWidgets.QTreeWidgetItem(self.se_tabla)
            for i in range(0, len(self.ser_all)):
                for posicion in range(0, 3):
                    self.se_tabla.topLevelItem(i).setText(posicion, str(self.ser_all[i][posicion]))
            return

        consulta = AbmObj.consulta_serializables(self.valor1)
        try:
            consulta = consulta[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nMAC inexistente!!\n")
            self.se_tabla.clear()
            for cant_ser_bd in range(0, len(self.ser_all)):
                QtWidgets.QTreeWidgetItem(self.se_tabla)
            for i in range(0, len(self.ser_all)):
                for posicion in range(0, 3):
                    self.se_tabla.topLevelItem(i).setText(posicion, str(self.ser_all[i][posicion]))
            return

        self.se_tabla.clear()
        QtWidgets.QTreeWidgetItem(self.se_tabla)
        for i in range(0, len(consulta)):
            self.se_tabla.topLevelItem(0).setText(i, str(consulta[i]))
        '''
        for i in range(1, len(self.ser_all)):
            for posicion in range(0, 3):
                test = ""
                self.se_tabla.topLevelItem(i).setText(posicion, str(test))'''

    def salir(self):
        self.close()


class ConsultarStockTipoSerializables(QtWidgets.QWidget, modificacionDeStockSerializables.Ui_Form):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ser_tipo_all = AbmObj.consulta_ser_tipo()
        self.se_btn_cancelar.clicked.connect(self.salir)
        self.se_btn_buscar.clicked.connect(self.stockPorTipo)
        for cant_ser_bd in range(0, len(self.ser_tipo_all)):
                QtWidgets.QTreeWidgetItem(self.se_tabla)
        for posicion in range(0, 6):
            for i in range(0, len(self.ser_tipo_all)):
                none_a_cero = str(self.ser_tipo_all[i][posicion])
                if none_a_cero == "None":
                    none_a_cero = "0"
                self.se_tabla.topLevelItem(i).setText(posicion, str(none_a_cero))

    def stockPorTipo(self):
        self.value1 = self.se_input_buscar.text()
        try:
            int(self.value1)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero entero!!\n")
            return
        tipo = AbmObj.tipo_existente(self.value1)
        try:
            if str(tipo[0][0]) == self.value1:
                pass
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nTipo inexistente!!\n")
            return
        application.window_Stock_Tipo.close()
        self.window_Stock_Tipo2 = StockTotalPorTipo()
        self.window_Stock_Tipo2.show()

    def salir(self):
        self.close()


class StockTotalPorTipo(QtWidgets.QWidget ,stockPorTipo.Ui_Form):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_cancelar.clicked.connect(self.cancelar)
        self.label.setText("Código del tipo: "+str(application.window_Stock_Tipo.value1))

        estado_serializables = AbmObj.estado_ser_por_tipo(application.window_Stock_Tipo.value1)
        for i in range (0, len(estado_serializables)):
            estado = ""
            QtWidgets.QTreeWidgetItem(self.se_tabla)
            self.se_tabla.topLevelItem(i).setText(0, str(estado_serializables[i][0]))
            self.se_tabla.topLevelItem(i).setText(1, str(estado_serializables[i][1]))
            if estado_serializables[i][2] == 0:
                estado = "En stock"
            elif estado_serializables[i][2] == 1:
                estado = "En movil"
            else:
                estado = "Error: Multiples moviles"
            self.se_tabla.topLevelItem(i).setText(2, estado)

    def cancelar(self):
        self.close()
        application.window_Stock_Tipo = ConsultarStockTipoSerializables()
        application.window_Stock_Tipo.show()

        pass


class altaBaja(QtWidgets.QWidget, altaBajaArticulosOption.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_1.clicked.connect(self.altaSerializableOpc)
        self.se_btn_2.clicked.connect(self.bajaSerializableOpc)

    def altaSerializableOpc(self):
        self.close()
        self.window = altaArticulo()
        self.window.show()

    def bajaSerializableOpc(self):
        self.close()
        self.window = bajaArticulo()
        self.window.show()


class altaArticulo(QtWidgets.QWidget, altaDeArticulosSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.altaSer)
        self.se_btn_cancelar.clicked.connect(self.salir)
        tipos = AbmObj.listado_tipos_ser_CB()
        for i in range(0, len(tipos)):
            self.se_input_2.addItem(str(tipos[i][0]))


    def altaSer(self):
        self.value1 = self.se_input_1.text()
        self.value1 = self.value1.upper()
        print(self.value1)
        if self.value1.isalnum():
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero hexadecimal!!\n")
            return
        if len(self.value1) == 12:
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nLa longitud debe ser de 12 cifras!!\n")
            return
        try:
            int(self.value1, 16)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nEl dato ingresado no es hexadecimal!!\n")
            return
        mac = se_consultas.mac_existente(self.value1)
        try:
            if str(mac[0][0]).upper() == str(self.value1).upper():
                QMessageBox.about(self, "Error!!", "\nEse numero de MAC ya existe en la base de datos!!\n")
                return
        except:
            pass

        self.value2 = self.se_input_2.currentText()
        valores = [self.value1, self.value2]
        AbmObj.alta_serializables(valores)
        QMessageBox.about(self, "Exito!!", "\nAlta exitosa!!\n")

    def salir(self):
        self.close()


class bajaArticulo(QtWidgets.QWidget, bajaDeArticulosSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.bajaSer)
        self.se_btn_cancelar.clicked.connect(self.salir)

    def bajaSer(self):
        self.value1 = self.se_input_1.text()
        self.value1 = self.value1.upper()

        if self.value1.isalnum():
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero hexadecimal!!\n")
            return
        if len(self.value1) == 12:
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nLa longitud debe ser de 12 cifras!!\n")
            return
        try:
            int(self.value1, 16)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nEl dato ingresado no es hexadecimal!!\n")
            return
        mac = se_consultas.mac_existente(self.value1)
        try:
            if (str(mac[0][0])).upper() == self.value1:
                pass
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nMAC inexistente!!\n")
            return
        self.sql = 'SELECT ser_estado FROM historial_serializables WHERE ser_mac = "'+str(self.value1)+'"'
        se_conexion.cursor.execute(self.sql)
        ser_estado = se_conexion.cursor.fetchall()
        if ser_estado[0][0] == 1:
            AbmObj.baja_serializables(self.value1)
            QMessageBox.about(self, "Exito!!", "\nBorrado de forma exitosa!!\n")
        elif ser_estado[0][0] == 2:
            self.sql2 = 'select mov_id from serializable_movil WHERE ser_mac = "'+str(self.value1)+'"'
            se_conexion.cursor.execute(self.sql2)
            num_mov = se_conexion.cursor.fetchall()
            print(num_mov)
            QMessageBox.about(self, "Error!!", "\nSerializable asignado al movil "+str(num_mov[0][0])+"!!\n")
            return
        else:
            print(self.sql[0][0])
            QMessageBox.about(self, "Error!!", "\nNo se puede eliminar ese serializable!!\n")
            return

    def salir(self):
        self.close()


class ModificacionMaxMinIngresoSerializables(QtWidgets.QWidget, modificacionMaxMinIngreso.Ui_Form):
    value1 = ""

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.elegirCodigoSer)
        self.se_btn_cancelar.clicked.connect(self.salir)

    def elegirCodigoSer(self):
        self.value1 = self.se_input_1.text()
        if self.value1.isalnum():
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero hexadecimal!!\n")
            return
        if len(self.value1) == 12:
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nLa longitud debe ser de 12 cifras!!\n")
            return
        try:
            int(self.value1, 16)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nEl dato ingresado no es hexadecimal!!\n")
            return
        mac = se_consultas.mac_existente(self.value1)
        try:
            if str(mac[0][0]) == self.value1:
                pass
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nMAC inexistente!!\n")
            return
        self.close()
        self.window = ModificarMinMaxSerializables()
        self.window.show()

    def salir(self):
        self.close()


class ModificarMinMaxSerializables(QtWidgets.QWidget, modificacionMaxMin.Ui_Form):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.modificarMinMaxSer)
        self.se_btn_cancelar.clicked.connect(self.salir)
        self.minmax = AbmObj.consulta_min_max(application.windowminmax.value1)
        self.se_label_1.setText(str(self.minmax[0][1]))
        self.se_label_2.setText(str(self.minmax[0][3]))
        self.se_label_3.setText(str(self.minmax[0][4]))
        self.se_input_1.setValue(self.minmax[0][3])
        self.se_input_2.setValue(self.minmax[0][4])


    def modificarMinMaxSer(self):
        value_min = self.se_input_1.text()
        value_max = self.se_input_2.text()
        AbmObj.modificar_min_max_ser(value_min, value_max, self.minmax[0][0])
        print(self.minmax[0][0])
        QMessageBox.about(self, "Exito!!", "\nModificado de forma exitosa!!\n")
        self.close()
        application.windowminmax = ModificacionMaxMinIngresoSerializables()
        application.windowminmax.show()

    def salir(self):
        self.close()
        application.windowminmax = ModificacionMaxMinIngresoSerializables()
        application.windowminmax.show()


class TecnicosMovilSerializables(QtWidgets.QWidget, tecnicosPorMovil.Ui_Form):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.materialesPorMovil)
        self.se_btn_cancelar.clicked.connect(self.cancelar)
        self.se_movil_tecnico = AbmObj.consulta_movil_tecnico()
        print(self.se_movil_tecnico)
        for cant_ser_bd in range(0, len(self.se_movil_tecnico)):
            QtWidgets.QTreeWidgetItem(self.se_tabla)
        for posicion in range(0, 2):
            for i in range(0, len(self.se_movil_tecnico)):
                self.se_tabla.topLevelItem(i).setText(posicion, str(self.se_movil_tecnico[i][posicion]))

    def materialesPorMovil(self):
        self.value1 = self.se_input_1.text()
        try:
            int(self.value1)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero entero!!\n")
            return
        movil = AbmObj.movil_existente(self.value1)
        try:
            if str(movil[0][0]) == self.value1:
                pass
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nMovil inexistente!!\n")
            return
        application.window_stock_movil.hide()
        self.windowStockMovil = StockMovilSerializables()
        self.windowStockMovil.show()

    def cancelar(self):
        self.close()


class StockMovilSerializables(QtWidgets.QWidget, stockPorMovil.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_mov_id = application.window_stock_movil.value1
        se_label_movil = "Móvil "+str(self.se_mov_id)
        self.se_label.setText(se_label_movil)
        consulta_ser_por_movil = AbmObj.consulta_ser_por_movil(self.se_mov_id)
        for i in range(0,len(consulta_ser_por_movil)):
            QtWidgets.QTreeWidgetItem(self.se_tabla)
            self.se_tabla.topLevelItem(i).setText(0, consulta_ser_por_movil[i][0])
            self.se_tabla.topLevelItem(i).setText(1, consulta_ser_por_movil[i][1])
        self.se_btn_confirmar.clicked.connect(self.confirmar)

    def confirmar(self):
        self.close()
        application.window_stock_movil.show()


class Aprovisionamiento(QtWidgets.QWidget, aprovisionamiento.Ui_Form):
    index = 0

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        if date.today().weekday() == 4:
            self.sql = 'SELECT ts.tipo_serializable, ts.desc_serializable, sum(cs.ser_cant), ts.cant_serializable, ts.cant_min_ser, ts.cant_max_ser FROM ' \
                       'tipo_serializable ts LEFT JOIN consumo_serializable cs ON ts.tipo_serializable = cs.ser_id ' \
                       'WHERE ((cs.ser_fecha_consumo BETWEEN DATE_SUB(NOW(), INTERVAL 7 DAY) AND NOW()) ' \
                       'OR cs.ser_fecha_consumo IS NULL) GROUP BY ts.tipo_serializable'
            se_conexion.cursor.execute(self.sql)
            self.consumo = se_conexion.cursor.fetchall()

            #El pedido debe:
            #1: Incluir el consumo de los ultimos 7 dias
            #2: En caso de estar por debajo de la cantidad minima, alcanzar la misma
            #3: En caso de superar la cantidad maxima, no realizar ningun pedido.

            for i in range(0, len(self.consumo)):
                QtWidgets.QTreeWidgetItem(self.se_tabla)
                self.se_tabla.topLevelItem(i).setText(0, str(self.consumo[i][0]))
                self.se_tabla.topLevelItem(i).setText(1, str(self.consumo[i][1]))

                if str(self.consumo[i][2]) == "None":
                    total_a_pedir = 0
                else:
                    total_a_pedir = int(self.consumo[i][2])
                if (int(self.consumo[i][3])+int(total_a_pedir))<int(self.consumo[i][4]):
                    total_a_pedir += (int(self.consumo[i][4])-(int(self.consumo[i][3])+int(total_a_pedir)))
                else:
                    pass
                if (int(self.consumo[i][3])+int(total_a_pedir))>int(self.consumo[i][5]):
                    total_a_pedir -= ((int(self.consumo[i][3])+int(total_a_pedir)) - int(self.consumo[i][5]))
                if int(total_a_pedir) < 0:
                    total_a_pedir = 0
                self.se_tabla.topLevelItem(i).setText(2, str(total_a_pedir))
            self.se_tabla.itemSelectionChanged.connect(self.info)
            self.se_input_1.valueChanged.connect(self.cambio_valor)
            self.se_btn_confirmar.clicked.connect(self.confirmar)
        else:
            self.se_btn_confirmar.clicked.connect(self.cancelar)
            QMessageBox.about(self, "Alerta!!", "\nLos pedidos se realizan los dias viernes!!\n")
        self.se_btn_cancelar.clicked.connect(self.cancelar)
        self.se_label_1.setText("Serializable")

    def cancelar(self):
        self.close()

    def cambio_valor(self):
        self.se_tabla.topLevelItem(self.index).setText(2, str(self.se_input_1.value()))

    def info(self):
        self.index = self.se_tabla.indexOfTopLevelItem(self.se_tabla.currentItem())
        seleccion = self.se_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.se_label_1.setText(datos.text(1))
            dato = datos.text(2)
            self.se_input_1.setValue(int(dato))

    def confirmar(self):
        advertencia = QMessageBox.warning(self, "Advertencia",
                                  '''Se realizara el envio del pedido.\n
                            Esta seguro que desea proceder?''', QMessageBox.Ok, QMessageBox.Cancel)
        if advertencia == QMessageBox.Ok:
            self.pedido = ""
            for i in range(0, 3):
                self.pedido += str(self.se_tabla.topLevelItem(i).text(0))+"                 "
                self.pedido += str(self.se_tabla.topLevelItem(i).text(1))+"                 "
                self.pedido += str(self.se_tabla.topLevelItem(i).text(2))+"\n"
            #print(str(self.pedido))
        else:
            return
        smtp_server = "localhost"
        port = 1025
        remitente = "aprovisionamiento@capsisrl.com.ar"
        destinatario = "aprovisionamiento@cablevision.com.ar"
        mensaje = "Subject: Aprovisionamiento\n\nSe solicita aprovisionamiento de los siguientes materiales:\n\n" \
                  "Codigo               Descripcion               Cantidad\n-----------" \
                  "--------------------------------------------\n" + self.pedido
        print(mensaje)
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.sendmail(remitente, destinatario, mensaje)
        except ConnectionError:
            QMessageBox.about(self, "Error!!", "\nNo hay conexión!!\n")
            return
        QMessageBox.about(self, "Éxito!!", "\nCorreo enviado correctamente!!\n")
        self.close()

        pass


class EstadoSerializable(QtWidgets.QWidget, estadoArticuloSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_buscar.clicked.connect(self.buscar_estado)
        self.se_btn_cancelar.clicked.connect(self.cancelar)
        self.se_btn_estado.clicked.connect(self.cambiar_estado)
        self.se_btn_estado.hide()
        self.se_cbx_1.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_7.hide()
        self.se_btn_estado.hide()
        self.se_label_1.hide()
        self.se_label_2.hide()

    def buscar_estado(self):
        self.valueEstado = str(self.se_input_buscar.text())
        self.valueEstado = self.valueEstado.upper()
        if self.valueEstado.isalnum():
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero hexadecimal!!\n")
            return
        if len(self.valueEstado) == 12:
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nLa longitud debe ser de 12 cifras!!\n")
            return
        try:
            int(self.valueEstado, 16)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nEl dato ingresado no es hexadecimal!!\n")
            return
        mac = se_consultas.mac_existente(self.valueEstado)
        try:
            if str(mac[0][0]) == str(self.valueEstado):
                pass
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nNo existe el numero de MAC!!\n")
            return
        self.se_btn_estado.show()
        self.se_cbx_1.show()
        self.label_3.show()
        self.label_4.show()
        self.label_7.show()
        self.se_btn_estado.show()
        self.se_label_1.setText(str(self.valueEstado))
        self.se_label_1.show()
        self.se_label_2.setText(str(se_consultas.obtener_estado_mac(self.valueEstado)[0][0]))
        self.se_label_2.show()


    def cambiar_estado(self):
        self.valuecbx = self.se_input_buscar.text()
        if self.valuecbx == "Listo para entregar":
            if str(se_consultas.obtener_estado_mac(self.valueEstado)[0][0]) == "Listo para entregar"
                print("Ya se encuentra listo")
            else
            pass
        elif self.valuecbx == "Devolucion":

            pass
        else:

            pass
        pass

    def cancelar(self):
        self.close()


class EleccionMovil(QtWidgets.QWidget, alertEstadoArticuloSerializables.Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.se_btn_confirmar.clicked.connect(self.confirmar)

    def confirmar(self):
        self.value_movil = self.se_input_1.text()
        self.value_movil = self.value_movil.upper()
        try:
            int(self.value_movil)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero decimal entero!!\n")
        self.movil = se_consultas.movil_existente(self.value_movil)
        try:
            self.movil[0][0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nNo existe ese movil!!\n")

class ConexionBD:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()


class ConsultasGenerales:

    def mac_existente(self, valor):
        self.sql = 'SELECT ser_mac FROM serializable WHERE ser_mac = "'+str(valor)+'"'
        se_conexion.cursor.execute(self.sql)
        mac = se_conexion.cursor.fetchall()
        return mac

    def movil_existente(self, valor):
        self.valor = valor
        self.sql = 'SELECT mov_id FROM movil WHERE mov_id = '+str(self.valor)
        se_conexion.cursor.execute(self.sql)
        movil = se_conexion.cursor.fetchall()
        return movil

    def obtener_estado_mac(self, valor):
        self.valor = valor
        self.sql = 'SELECT es.des_estado FROM historial_serializables hs ' \
                   'JOIN estados_serializables es ON es.id_estado_ser = hs.ser_estado ' \
                   'WHERE hs.ser_mac = "'+str(self.valor)+'"'
        se_conexion.cursor.execute(self.sql)
        estado = se_conexion.cursor.fetchall()
        return estado

se_conexion = ConexionBD()
se_consultas = ConsultasGenerales()
AbmObj = ABM_serializables()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaSerializables()
    application.show()
    sys.exit(app.exec_())
