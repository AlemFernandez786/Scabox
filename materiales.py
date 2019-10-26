from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Materiales import altaBajaArticulosMaterialesOption
from Pantallas.Materiales import sectorMateriales
from Pantallas.Materiales import modificacionMaxMinIngreso
from Pantallas.Materiales import aprovisionamiento
from Pantallas.Materiales import consultarStockMateriales
from Pantallas.Materiales import conteoDeInventarioPorMovil
from Pantallas.Materiales import modificarStockMateriales
from Pantallas.Materiales import stockPorMovilMateriales
from Pantallas.Materiales import altaDeArticulosMateriales
from Pantallas.Materiales import bajaDeArticulosMateriales
from Pantallas.Materiales import modificacionMaxMin
from Pantallas.Materiales import stockPorMovilIngreso
import mysql.connector
from ABM import ABM_materiales
import smtplib  # Librería de servidor SMTP
from datetime import date, timedelta
import sys


class VentanaMateriales(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaMateriales, self).__init__(*args, **kwargs)
        self.ui = sectorMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_consulta.clicked.connect(self.consulta_stock)
        self.ui.ma_btn_modificacion.clicked.connect(self.modificacion_stock)
        self.ui.ma_btn_altabaja.clicked.connect(self.alta_baja_stock)
        self.ui.ma_btn_maxmin.clicked.connect(self.maxima_minima_stock)
        self.ui.ma_btn_stockmovil.clicked.connect(self.stock_movil)
        self.ui.ma_btn_inventario.clicked.connect(self.inventario_movil)
        self.ui.ma_btn_aprovisionamiento.clicked.connect(self.aprovisionamiento_stock)
        self.ui.ma_btn_cancelar.clicked.connect(self.cancelar)

    def consulta_stock(self):
        ventanaconsulta = StockMateriales(self)
        ventanaconsulta.exec_()

    def modificacion_stock(self):
        ventanamodificacionstock = ModificarStock(self)
        ventanamodificacionstock.exec_()

    def alta_baja_stock(self):
        ventanaaltabaja = VentanaAltaBaja(self)
        ventanaaltabaja.exec_()

    def maxima_minima_stock(self):
        ventanamaxmin = MaximaMinima(self)
        ventanamaxmin.exec_()

    def stock_movil(self):
        ventanastockmovilingreso = StockMovilIngreso(self)
        ventanastockmovilingreso.exec_()

    def inventario_movil(self):
        ventanainventario = InventarioMovil(self)
        ventanainventario.exec_()

    def aprovisionamiento_stock(self):
        # Compara si el dia es viernes .weekday() retorna los dias como un entero 0 para lunes hasta 6 para domingo
        if date.today().weekday() == 4:
            ventanaaprovisionamiento = Aprovisionamiento(self)
            ventanaaprovisionamiento.exec_()
        else:
            QMessageBox.about(self, "Alerta!!", "\nLos pedidos se realizan los dias viernes!!\n")

    def cancelar(self):
        self.close()


class VentanaAltaBaja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(VentanaAltaBaja, self).__init__(*args, **kwargs)
        self.ui = altaBajaArticulosMaterialesOption.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_alta.pressed.connect(self.alta)
        self.ui.ma_btn_baja.pressed.connect(self.baja)

    def alta(self):
        ventanaalta = Alta(self)
        ventanaalta.exec_()

    def baja(self):
        ventanabaja = Baja(self)
        ventanabaja.exec_()


class Alta(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Alta, self).__init__(*args, **kwargs)
        self.ui = altaDeArticulosMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_input_ingreso.clear()
        self.ui.ma_input_maxima.clear()
        self.ui.ma_input_minima.clear()

    def salir(self):
        self.close()

    def confirmar(self):
        if self.ui.ma_input_descripcion.text() == "":
            QMessageBox.about(self, "Error", "\nIngrese descripción\n del artículo!!\n")
            return
        if self.ui.ma_input_maxima.value() == 0 or self.ui.ma_input_minima.value() == 0 \
                or self.ui.ma_input_ingreso == 0:
            QMessageBox.about(self, "Error", "\nIngrese un valor!!\n")
            return
        if self.ui.ma_input_minima.value() >= self.ui.ma_input_maxima.value():
            QMessageBox.about(self, "Error", "\nLa cantidad mínima no puede \n ser igual o superior a la máxima!!\n")
            return
        lcl_valores = [
            str(self.ui.ma_input_descripcion.text()), str(self.ui.ma_input_ingreso.text()),
            str(self.ui.ma_input_minima.text()), str(self.ui.ma_input_maxima.text())]
        try:
            lcl_agregar = ABM_materiales()
            lcl_agregar.alta_materiales(lcl_valores)
        except mysql.connector.Error:
            QMessageBox.about(self, "Error", "Ingrese un valor!!")
            return
        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")
        self.close()


class Baja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Baja, self).__init__(*args, **kwargs)
        self.ui = bajaDeArticulosMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

    def salir(self):
        self.close()

    def confirmar(self):
        lcl_codigo = (str(self.ui.ma_input_codigo.text()))
        try:
            instanciaabm = ABM_materiales()
            busqueda = instanciaabm.consulta_materiales(lcl_codigo)
        except mysql.connector.Error:
            QMessageBox.about(self, "Error!!", "\nIngrese un número!!\n")
            self.ui.ma_input_codigo.clear()
            return
        if not busqueda:
            QMessageBox.about(self, "Error", "\nArtículo inexistente!!\n")
            return
        try:
            instanciaabm.baja_materiales(lcl_codigo)
        except mysql.connector.Error:
            return
        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")
        self.ui.ma_input_codigo.clear()


class StockMovilIngreso(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMovilIngreso, self).__init__(*args, **kwargs)
        self.ui = stockPorMovilIngreso.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        # Inserción de datos en tabla
        self.sql = 'SELECT dm.mov_id, e.emp_nombre, e.emp_apellido FROM empleados e JOIN dupla_movil dm ON' \
                   ' e.emp_legajo=dm.emp_legajo ORDER BY dm.mov_id ASC'
        self.cursor.execute(self.sql)
        lcl_resultado = self.cursor.fetchall()
        lcl_lista = []
        lcl_duplas = []
        for i in range(0, len(lcl_resultado)):
            lcl_lista.append(list(lcl_resultado[i]))
        lcl_resultado = lcl_lista

        for i in range(0, len(lcl_resultado)):
            if i+1 >= len(lcl_resultado):
                break
            if lcl_resultado[i][0] == lcl_resultado[i+1][0]:
                lcl_dupla = []
                lcl_numero = str(lcl_resultado[i][0])
                lcl_dupla.append(lcl_numero)
                lcl_tecnicos = (str(lcl_resultado[i][1]) + " " + str(lcl_resultado[i][2]) + ", "
                                + str(lcl_resultado[i+1][1]) + " " + str(lcl_resultado[i+1][2]))

                lcl_dupla.append(lcl_tecnicos)
                lcl_duplas.append(lcl_dupla)
        lcl_len_resultado = (len(lcl_duplas))
        for i in range(0, lcl_len_resultado):
            lcl_posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(lcl_duplas[i])):
                lcl_filas = lcl_duplas[i][a]

                self.ui.ma_tabla_datos.topLevelItem(i).setText(lcl_posicion, str(lcl_filas))
                lcl_posicion += 1
        # -------------------------------------

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_tabla_datos.doubleClicked.connect(self.confirmar)

    def info(self):
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
            self.ui.ma_label_movil.setText(lcl_datos.text(0))
            self.ui.ma_label_tecnicos.setText(lcl_datos.text(1))

    # --------------------------------------

    def confirmar(self):
        lcl_datos = 0
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
        ventanastockmovil = StockPorMovil()
        try:
            lcl_datos.text(0)
        except AttributeError:
            QMessageBox.about(self, "Error!!", "Seleccione un móvil")
            return
        ventanastockmovil.tabla(lcl_datos.text(0))
        ventanastockmovil.exec_()


class StockPorMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockPorMovil, self).__init__(*args, **kwargs)
        self.ui = stockPorMovilMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_btn_salir.clicked.connect(self.salir)
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_input_cantidad.clear()
        self.lcl_codigo = 0

        # Inserción de datos en tabla
    def tabla(self, cod):
        self.lcl_codigo = cod
        sql = 'SELECT am.art_id, a.art_nombre, am.art_mov_cantidad FROM articulo_movil am JOIN articulo a ON ' \
              'am.art_id = a.art_id WHERE mov_id='+str(self.lcl_codigo)+' AND a.tip_id = 2'
        self.cursor.execute(sql)
        lcl_resultado = self.cursor.fetchall()
        lcl_lista = []
        for i in range(0, len(lcl_resultado)):
            lcl_lista.append(list(lcl_resultado[i]))
        lcl_resultado = tuple(lcl_lista)
        lcl_len_resultado = (len(lcl_resultado))
        for i in range(0, lcl_len_resultado):
            self.ui.ma_tabla_datos.takeTopLevelItem(i)
            lcl_posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(lcl_resultado[i])):
                lcl_filas = lcl_resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(lcl_posicion, str(lcl_filas))
                lcl_posicion += 1
        # -------------------------------------

        # Muestra datos seleccionados
    def info(self):
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
            self.ui.ma_label_descripcion.setText(lcl_datos.text(0))
            self.ui.ma_label_stock.setText(lcl_datos.text(1))

    # --------------------------------------

    def confirmar(self):
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        try:
            lcl_datos = lcl_seleccion[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nSelecciones un artículo!!\n")
            return
        try:
            lcl_cantidad = int(self.ui.ma_input_cantidad.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un número!!\n")
            return

        if lcl_cantidad == 0:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        instancia = ABM_materiales()
        actual = instancia.consulta_materiales(lcl_datos.text(0))
        if lcl_cantidad > int(actual[0][2]):
            QMessageBox.about(self, "Error!!", "\nCantidad no disponible!!\n")
            return
        lcl_warning = QMessageBox.warning(self, "Advertencia",
                                          "El artículo ha sido modificado.\nQuieres guardar los cambios?",
                                          QMessageBox.Ok, QMessageBox.Cancel)
        if lcl_warning == QMessageBox.Ok:
            try:
                lcl_cantidad = int(self.ui.ma_input_cantidad.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            lcl_total = lcl_cantidad + int(lcl_datos.text(2))
            sql = 'UPDATE articulo_movil SET art_mov_cantidad = ' + str(lcl_total) + ' WHERE art_id = ' + \
                  str(lcl_datos.text(0)) + ' AND mov_id = ' + str(self.lcl_codigo)
            self.cursor.execute(sql)
            lcl_valor = [str(lcl_datos.text(0)), str(-1*lcl_cantidad)]
            instancia.modificacion_materiales(lcl_valor)

            self.conexion.commit()
        else:
            return
        self.tabla(self.lcl_codigo)
        self.ui.ma_input_cantidad.clear()
        self.ui.ma_label_stock.clear()
        self.ui.ma_label_descripcion.clear()

    def salir(self):
        self.close()


class ModificarStock(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificarStock, self).__init__(*args, **kwargs)
        self.ui = modificarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_buscar.clicked.connect(self.busqueda)
        self.ui.ma_btn_confirmar.clicked.connect(self.modificacion)
        self.tabla()
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_tabla_datos.doubleClicked.connect(self.busqueda)

    def tabla(self):
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales_gral()
        lcl_len_resultado = (len(lcl_resultado))
        for i in range(0, lcl_len_resultado):
            self.ui.ma_tabla_datos.takeTopLevelItem(i)
            lcl_posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(lcl_resultado[i])):
                lcl_filas = lcl_resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(lcl_posicion, str(lcl_filas))
                lcl_posicion += 1

        # Muestra datos seleccionados

    def info(self):
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
            self.ui.ma_input_buscar.setText(lcl_datos.text(0))

    # --------------------------------------

    def salir(self):
        self.close()

    def busqueda(self):
        try:
            lcl_codigo = int(self.ui.ma_input_buscar.text())
        except ValueError:
            self.tabla()
            self.ui.ma_input_actual.clear()
            self.ui.ma_input_maximo.clear()
            self.ui.ma_input_minimo.clear()
            self.ui.ma_input_cantidad.clear()
            self.ui.ma_input_descripcion.clear()
            QMessageBox.about(self, "Error!!", "\nIngrese solo números!!\n")
            self.ui.ma_input_buscar.clear()
            return
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales(str(lcl_codigo))
        try:
            lcl_resultados = lcl_resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            self.ui.ma_input_buscar.clear()
            return
        lcl_posicion = 0
        for i in lcl_resultados:
            if lcl_posicion == 3:
                lcl_posicion = lcl_posicion + 1
            self.ui.ma_tabla_datos.topLevelItem(0).setText(lcl_posicion, str(i))
            lcl_posicion += 1
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales_gral()
        lcl_len_resultado = (len(lcl_resultado))
        for i in range(1, lcl_len_resultado):
            lcl_posicion = 0
            for a in range(0, len(lcl_resultado[i])):
                self.ui.ma_tabla_datos.takeTopLevelItem(i)
                lcl_posicion += 1
        self.ui.ma_input_actual.setText(str(lcl_resultados[2]))
        self.ui.ma_input_maximo.setText(str(lcl_resultados[4]))
        self.ui.ma_input_minimo.setText(str(lcl_resultados[3]))
        self.ui.ma_input_descripcion.setText(str(lcl_resultados[1]))

    def modificacion(self):
        self.ui.ma_input_cantidad.returnPressed.connect(self.ui.ma_btn_confirmar.setFocus)
        try:
            lcl_cantidad = int(self.ui.ma_input_cantidad.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            self.ui.ma_input_cantidad.clear()
            return

        if (lcl_cantidad < 0) | (lcl_cantidad > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            self.ui.ma_input_cantidad.clear()
            return
        lcl_warning = QMessageBox.warning(self, "Advertencia",
                                          "El artículo ha sido modificado.\nQuieres guardar los cambios?",
                                          QMessageBox.Ok, QMessageBox.Cancel)
        if lcl_warning == QMessageBox.Ok:
            lcl_valor = ["", ""]
            lcl_valor[0] = str(self.ui.ma_input_buscar.text())
            try:
                lcl_cantidad = int(self.ui.ma_input_cantidad.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            lcl_valor[1] = str(lcl_cantidad)
            modificar = ABM_materiales()
            try:
                modificar.modificacion_materiales(lcl_valor)
            except mysql.connector.Error:
                return
            self.busqueda()
        else:
            return


class InventarioMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(InventarioMovil, self).__init__(*args, **kwargs)
        self.ui = conteoDeInventarioPorMovil.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_input_cantidad.clear()
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_input_movil.returnPressed.connect(self.verificar)
        self.ui.ma_input_codigo.returnPressed.connect(self.busqueda)

    def verificar(self):
        lcl_id_movil = self.ui.ma_input_movil.text()
        sql = 'SELECT mov_vtv FROM movil WHERE mov_id = ' + lcl_id_movil
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            QMessageBox.about(self, "Error!!", "\nIngrese un número de móvil!!\n")
            return

        lcl_movil = self.cursor.fetchall()
        if not lcl_movil:
            QMessageBox.about(self, "Error!!", "Móvil inexistente")
            self.ui.ma_input_movil.clear()
            return
        self.ui.ma_input_codigo.setFocus()

    def busqueda(self):
        lcl_codigo = self.ui.ma_input_codigo.text()
        lcl_movil = self.ui.ma_input_movil.text()
        sql = 'SELECT am.art_mov_cantidad FROM articulo_movil am JOIN articulo a ON am.art_id = a.art_id ' \
              'WHERE am.art_id = ' + lcl_codigo + ' AND am.mov_id = ' + lcl_movil + ' AND a.tip_id = 2'
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            QMessageBox.about(self, "Error!!", "\nIngrese un número!!\n")
            return
        lcl_datos = self.cursor.fetchall()
        if not lcl_datos:
            QMessageBox.about(self, "Error!!", "Artículo inexistente")
            self.ui.ma_input_codigo.clear()
            return
        self.ui.ma_label_stock.setText(str(lcl_datos[0][0]))
        self.ui.ma_input_cantidad.setFocus()

    def salir(self):
        self.close()

    def confirmar(self):
        lcl_cantidad = self.ui.ma_input_cantidad.text()
        lcl_movil = self.ui.ma_input_movil.text()
        lcl_codigo = self.ui.ma_input_codigo.text()
        sql = 'UPDATE articulo_movil SET art_mov_cantidad = ' + lcl_cantidad + ' WHERE ' \
              'mov_id = ' + lcl_movil + ' AND art_id = ' + lcl_codigo
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            QMessageBox.about(self, "Error!!", "\nIngrese un número!!\n")
            return
        self.conexion.commit()
        self.ui.ma_input_codigo.clear()
        self.ui.ma_input_movil.clear()
        self.ui.ma_input_cantidad.clear()
        self.ui.ma_label_stock.clear()
        self.ui.ma_input_movil.setFocus()


class Aprovisionamiento(QtWidgets.QDialog):
    lcl_articulos = ""

    def __init__(self, *args, **kwargs):
        super(Aprovisionamiento, self).__init__(*args, **kwargs)
        self.ui = aprovisionamiento.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.lcl_index = ""
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_btn_modificar.clicked.connect(self.modificar)
        self.pedido()

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)

    def info(self):
        self.lcl_index = self.ui.ma_tabla_datos.indexOfTopLevelItem(self.ui.ma_tabla_datos.currentItem())
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
            self.ui.ma_label_descripcion.setText(lcl_datos.text(1))
            lcl_dato = lcl_datos.text(2)
            if lcl_dato == '':
                lcl_dato = 0
            self.ui.ma_input_cantidad.setValue(int(lcl_dato))
    # --------------------------------------

    def modificar(self):
        try:
            self.ui.ma_tabla_datos.topLevelItem(self.lcl_index).setText(2, str(self.ui.ma_input_cantidad.value()))
        except TypeError:
            QMessageBox.about(self, "Error", "Seleccione un artículo!!")

    def confirmar(self):
        # (sudo) "python -m smtpd -c DebuggingServer -n localhost:1025" para ejecutar un servidor SMTP local
        if self.lcl_articulos == "":
            QMessageBox.about(self, "Error!!", "\nNo se encuentran artículos!!\n")
            return
        lcl_smtp_server = "localhost"
        lcl_port = 1025
        lcl_remitente = "aprovisionamiento@capsisrl.com.ar"
        lcl_destinatario = "aprovisionamiento@cablevision.com.ar"
        lcl_mensaje = "Subject: Aprovisionamiento\n\nSe solicita aprovisionamiento de los siguientes materiales:\n\n" \
                      "Codigo               Descripcion               Cantidad\n-----------" \
                      "--------------------------------------------\n" + self.lcl_articulos
        try:
            with smtplib.SMTP(lcl_smtp_server, lcl_port) as server:
                server.sendmail(lcl_remitente, lcl_destinatario, lcl_mensaje)
        except ConnectionError:
            QMessageBox.about(self, "Error!!", "\nNo hay conexión \ncon el servidor!!\n")
            return
        QMessageBox.about(self, "Éxito!!", "\nCorreo enviado correctamente!!\n")
        self.close()

    def pedido(self):
        lcl_fecha1 = str(date.today() + timedelta(days=-7))
        lcl_fecha2 = str(date.today())
        sql = 'SELECT a.art_id, a.art_nombre, sum(hm.his_mat_cant) FROM articulo a JOIN historial_materiales' \
              ' hm ON a.art_id=hm.art_id WHERE a.tip_id = 2 AND a.art_cantidad < a.art_cant_min AND ' \
              'hm.his_mat_fecha BETWEEN DATE("' + lcl_fecha1 + '") AND DATE("' + lcl_fecha2 + '") GROUP BY art_id'
        self.cursor.execute(sql)
        lcl_art_info = self.cursor.fetchall()
        lcl_lista = []
        for i in range(0, len(lcl_art_info)):
            lcl_lista.append(list(lcl_art_info[i]))
        lcl_art_info = tuple(lcl_lista)
        lcl_len_resultado = len(lcl_art_info)
        for i in range(0, lcl_len_resultado):
            lcl_posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(lcl_art_info[i])):
                lcl_filas = lcl_art_info[i][a]
                self.lcl_articulos += str(lcl_filas) + "                 "
                self.ui.ma_tabla_datos.topLevelItem(i).setText(lcl_posicion, str(lcl_filas))
                lcl_posicion += 1
            self.lcl_articulos += "\n"

    def salir(self):
        self.close()


class StockMateriales(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMateriales, self).__init__(*args, **kwargs)
        self.ui = consultarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_buscar.clicked.connect(self.consulta)
        self.ui.ma_btn_volver.clicked.connect(self.salir)
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_tabla_datos.doubleClicked.connect(self.consulta)
        self.tabla()

    def tabla(self):
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales_gral()
        lcl_len_resultado = (len(lcl_resultado))
        for i in range(0, lcl_len_resultado):
            self.ui.ma_tabla_datos.takeTopLevelItem(i)
            lcl_posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(lcl_resultado[i])):
                lcl_filas = lcl_resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(lcl_posicion, str(lcl_filas))
                lcl_posicion += 1

        # Muestra datos seleccionados
    def info(self):
        lcl_seleccion = self.ui.ma_tabla_datos.selectedItems()
        if lcl_seleccion:
            lcl_datos = lcl_seleccion[0]
            self.ui.ma_input_buscar.setText(lcl_datos.text(0))
    # --------------------------------------

    def salir(self):
        self.close()

    def consulta(self):
        try:
            lcl_codigo = int(self.ui.ma_input_buscar.text())
        except ValueError:
            self.tabla()
            QMessageBox.about(self, "Error!!", "\nIngrese solo números!!\n")
            self.ui.ma_input_buscar.clear()
            return
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales(str(lcl_codigo))
        try:
            lcl_resultados = lcl_resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            self.ui.ma_input_buscar.clear()
            return
        lcl_posicion = 0
        for i in lcl_resultados:
            if lcl_posicion == 3:
                lcl_posicion = lcl_posicion + 1
            self.ui.ma_tabla_datos.topLevelItem(0).setText(lcl_posicion, str(i))
            lcl_posicion += 1
        consultar = ABM_materiales()
        lcl_resultado = consultar.consulta_materiales_gral()
        lcl_len_resultado = (len(lcl_resultado))
        for i in range(1, lcl_len_resultado):
            lcl_posicion = 0
            for a in range(0, len(lcl_resultado[i])):
                self.ui.ma_tabla_datos.takeTopLevelItem(i)
                lcl_posicion += 1
        self.ui.ma_input_buscar.clear()


class MaximaMinima(QtWidgets.QDialog):
    lcl_datos = []
    lcl_valor = []

    def __init__(self, *args, **kwargs):
        super(MaximaMinima, self).__init__(*args, **kwargs)
        self.ui = modificacionMaxMinIngreso.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

    def salir(self):
        self.close()

    def confirmar(self):
        try:
            lcl_codigo = int(self.ui.ma_input_codigo.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        if (lcl_codigo < 0) | (lcl_codigo > 99999999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        con = ABM_materiales()
        lcl_valor = con.consulta_materiales(str(lcl_codigo))
        if not lcl_valor:
            QMessageBox.about(self, "Error", "Ingrese un código válido")
            return
        else:
            ventanamodificacionmaxmin = ModificacionMaximaMinima(self)
            ventanamodificacionmaxmin.capturarvalor(lcl_valor[0][0], lcl_valor[0][1], lcl_valor[0][3], lcl_valor[0][4])
            ventanamodificacionmaxmin.exec_()


class ModificacionMaximaMinima(QtWidgets.QDialog):
    lcl_codigo = ""

    def __init__(self, *args):
        super(ModificacionMaximaMinima, self).__init__(*args)
        self.ui = modificacionMaxMin.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

    def confirmar(self):
        lcl_minima = str(self.ui.ma_input_minimo.text())
        lcl_maxima = str(self.ui.ma_input_maximo.text())
        if int(lcl_minima) <= 0:
            QMessageBox.about(self, "Error!!", "\nEl valor mínimo no puede ser menor o igual 0.\n")
            return
        if int(lcl_maxima) <= int(lcl_minima):
            QMessageBox.about(self, "Error!!", "\nEl valor máximo no puede ser menor o igual que el valor mínimo.\n")
            return
        lcl_warning = QMessageBox.warning(self, "Advertencia",
                                                '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if lcl_warning == QMessageBox.Ok:
            sql = 'UPDATE articulo SET art_cant_min ' \
                       '= ' + lcl_minima + ' WHERE art_id = ' + self.lcl_codigo + ' AND tip_id=3'
            self.cursor.execute(sql)
            sql = 'UPDATE articulo SET art_cant_max ' \
                  '= ' + lcl_maxima + ' WHERE art_id = ' + self.lcl_codigo + ' AND tip_id=3'
            self.cursor.execute(sql)
            self.conexion.commit()
            self.ui.ma_label_minimo.setText(lcl_minima)
            self.ui.ma_label_maximo.setText(lcl_maxima)
            self.ui.ma_input_minimo.clear()
            self.ui.ma_input_maximo.clear()
        else:
            return

    def salir(self):
        self.close()

    def capturarvalor(self, cod, nom, mini, maxi):
        self.lcl_codigo = str(cod)
        self.ui.ma_label_descripcion.setText(str(nom))
        self.ui.ma_label_minimo.setText(str(mini))
        self.ui.ma_label_maximo.setText(str(maxi))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())
