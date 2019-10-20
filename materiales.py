from PyQt5 import QtWidgets, QtCore
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
        if date.today().weekday() == 6:
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
    def salir(self):
        self.close()

    def confirmar(self):
        if self.ui.ma_input_descripcion == "":
            QMessageBox.about(self, "Error", "\nIngrese descripción\n del artículo!!\n")
            return
        if self.ui.ma_input_maxima.value() == 0 or self.ui.ma_input_minima.value() == 0 \
                or self.ui.ma_input_ingreso == 0:
            QMessageBox.about(self, "Error", "\nIngrese un valor!!\n")
            return
        if self.ui.ma_input_minima.value() > self.ui.ma_input_maxima.value():
            QMessageBox.about(self, "Error", "\nLa cantidad mínima no puede \n superar a la máxima!!\n")
            return
        valores = [
            str(self.ui.ma_input_descripcion.toPlainText()), str(self.ui.ma_input_ingreso.text()),
            str(self.ui.ma_input_minima.text()), str(self.ui.ma_input_maxima.text())]
        agregar = ABM_materiales()
        agregar.alta_materiales(valores)

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
        codigo = (str(self.ui.ma_input_codigo.text()))

        instanciaabm = ABM_materiales()
        busqueda = instanciaabm.consulta_materiales(codigo)
        if not busqueda:
            QMessageBox.about(self, "Error", "\nArtículo inexistente!!\n")
            return
        try:
            instanciaabm.baja_materiales(codigo)
        except mysql.connector.Error:
            return
        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")


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
        resultado = self.cursor.fetchall()
        lista = []
        duplas = []
        for i in range(0, len(resultado)):
            lista.append(list(resultado[i]))
        resultado = lista

        for i in range(0, len(resultado)):
            if i+1 >= len(resultado):
                break
            if resultado[i][0] == resultado[i+1][0]:
                dupla = []
                numero = str(resultado[i][0])
                dupla.append(numero)
                wachos = (str(resultado[i][1]) + " " + str(resultado[i][2]) + ", " + str(resultado[i+1][1]) + " " +
                          str(resultado[i+1][2]))

                dupla.append(wachos)
                duplas.append(dupla)
        len_resultado = (len(duplas))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(duplas[i])):
                test = duplas[i][a]

                self.ui.ma_tabla_datos.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        # -------------------------------------

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_tabla_datos.doubleClicked.connect(self.confirmar)

    def info(self):
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_label_movil.setText(datos.text(0))
            self.ui.ma_label_tecnicos.setText(datos.text(1))

    # --------------------------------------

    def confirmar(self):
        datos = 0
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
        ventanastockmovil = StockPorMovil()
        try:
            datos.text(0)
        except AttributeError:
            return
        ventanastockmovil.tabla(datos.text(0))
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
        self.codigo = 0

        # Inserción de datos en tabla
    def tabla(self, cod):
        self.codigo = cod
        sql = 'SELECT am.art_id, a.art_nombre, am.art_mov_cantidad FROM articulo_movil am JOIN articulo a ON ' \
              'am.art_id = a.art_id WHERE mov_id='+str(self.codigo)+' AND a.tip_id = 2'
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        lista = []
        for i in range(0, len(resultado)):
            lista.append(list(resultado[i]))
        resultado = tuple(lista)
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        # -------------------------------------

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_label_descripcion.setText(datos.text(0))
            self.ui.ma_label_stock.setText(datos.text(1))

    # --------------------------------------

    def confirmar(self):
        valor = []
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        try:
            datos = seleccion[0]
        except IndexError:
            return
        try:
            cantidad = int(self.ui.ma_input_cantidad.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        if (cantidad < 0) | (cantidad > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            try:
                cantidad = int(self.ui.ma_input_cantidad.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            sql = str('UPDATE articulo_movil SET art_mov_cantidad ' 
                      '= ' + str(cantidad) + ' WHERE art_id = ' + str(datos.text(0)))
            self.cursor.execute(sql)
            cantidad = cantidad*(-1)
            valor.append(datos.text(0))
            valor.append(cantidad)
            instancia = ABM_materiales()
            instancia.modificacion_materiales(valor)
            self.conexion.commit()
            #TODO ver esto
        else:
            return
        self.tabla(self.codigo)

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

    def tabla(self):
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            self.ui.ma_tabla_datos.takeTopLevelItem(i)
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)
        self.ui.ma_tabla_datos.doubleClicked.connect(self.busqueda)

    def info(self):
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_input_buscar.setText(datos.text(0))

    # --------------------------------------

    def salir(self):
        self.close()

    def busqueda(self):
        try:
            codigo = int(self.ui.ma_input_buscar.text())
        except (ValueError, TypeError):
            self.tabla()
            self.ui.ma_input_actual.clear()
            self.ui.ma_input_maximo.clear()
            self.ui.ma_input_minimo.clear()
            self.ui.ma_input_descripcion.clear()
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return

        posicion = 0
        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla_datos.topLevelItem(0).setText(posicion, str(i))
            posicion += 1
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            posicion = 0

            for a in range(0, len(resultado[i])):
                self.ui.ma_tabla_datos.takeTopLevelItem(i)

                posicion += 1

        self.ui.ma_input_actual.setText(str(resultados[2]))
        self.ui.ma_input_maximo.setText(str(resultados[4]))
        self.ui.ma_input_minimo.setText(str(resultados[3]))
        self.ui.ma_input_descripcion.setText(str(resultados[1]))

    def modificacion(self):
        try:
            cantidad = int(self.ui.ma_input_cantidad.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        if (cantidad < 0) | (cantidad > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            valor = ["", ""]
            valor[0] = str(self.ui.ma_input_buscar.text())
            try:
                cantidad = int(self.ui.ma_input_cantidad.text())
            except (ValueError):
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            valor[1] = str(cantidad)
            modificar = ABM_materiales()
            try:
                modificar.modificacion_materiales(valor)
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
        id_movil = self.ui.ma_input_movil.text()
        sql = 'SELECT mov_vtv FROM movil WHERE mov_id = ' + id_movil
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            return

        movil = self.cursor.fetchall()
        if not movil:
            QMessageBox.about(self, "Error!!", "Móvil inexistente")
            self.ui.ma_input_movil.clear()
            return
        self.ui.ma_input_codigo.setFocus()

    def busqueda(self):
        codigo = self.ui.ma_input_codigo.text()
        sql = 'SELECT am.art_mov_cantidad FROM articulo_movil am JOIN articulo a ON am.art_id = a.art_id ' \
              'WHERE am.art_id = ' + codigo + ' AND am.mov_id = 1 AND a.tip_id = 2'
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            return
        datos = self.cursor.fetchall()
        if not datos:
            QMessageBox.about(self, "Error!!", "Artículo inexistente")
            self.ui.ma_input_codigo.clear()
            return
        self.ui.ma_label_stock.setText(str(datos[0][0]))
        self.ui.ma_input_cantidad.setFocus()

    def salir(self):
        self.close()

    def confirmar(self):
        cantidad = self.ui.ma_input_cantidad.text()
        movil = self.ui.ma_input_movil.text()
        codigo = self.ui.ma_input_codigo.text()
        sql = 'UPDATE articulo_movil SET art_mov_cantidad = ' + cantidad + ' WHERE ' \
              'mov_id = ' + movil + ' AND art_id = ' + codigo
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error:
            return
        self.conexion.commit()
        self.ui.ma_input_codigo.clear()
        self.ui.ma_input_movil.clear()
        self.ui.ma_input_cantidad.clear()
        self.ui.ma_label_stock.clear()
        self.ui.ma_input_movil.setFocus()


class Aprovisionamiento(QtWidgets.QDialog):
    articulos = ""

    def __init__(self, *args, **kwargs):
        super(Aprovisionamiento, self).__init__(*args, **kwargs)
        self.ui = aprovisionamiento.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_btn_modificar.clicked.connect(self.modificar)



        self.pedido()

        # Muestra datos seleccionados
        self.ui.ma_tabla_datos.itemSelectionChanged.connect(self.info)

    def info(self):
        self.index = self.ui.ma_tabla_datos.indexOfTopLevelItem(self.ui.ma_tabla_datos.currentItem())
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_label_descripcion.setText(datos.text(1))
            dato = datos.text(2)
            if dato == '':
                dato = 0
            self.ui.ma_input_cantidad.setValue(int(dato))
    # --------------------------------------

    def modificar(self):
        self.ui.ma_tabla_datos.topLevelItem(self.index).setText(2, str(self.ui.ma_input_cantidad.value()))

    def confirmar(self):
        # (sudo) "python -m smtpd -c DebuggingServer -n localhost:1025" para ejecutar un servidor SMTP local
        if self.articulos == "":
            QMessageBox.about(self, "Error!!", "\nNo se encuentran artículos!!\n")
            return
        smtp_server = "localhost"
        port = 1025
        remitente = "aprovisionamiento@capsisrl.com.ar"
        destinatario = "aprovisionamiento@cablevision.com.ar"
        mensaje = "Subject: Aprovisionamiento\n\nSe solicita aprovisionamiento de los siguientes materiales:\n\n" \
                  "Codigo               Descripcion               Cantidad\n-----------" \
                  "--------------------------------------------\n" + self.articulos
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.sendmail(remitente, destinatario, mensaje)
        except ConnectionError:
            QMessageBox.about(self, "Error!!", "\nNo hay conexión!!\n")
            return
        QMessageBox.about(self, "Éxito!!", "\nCorreo enviado correctamente!!\n")
        self.close()

    def pedido(self):
        fecha1 = str(date.today() + timedelta(days=-130))
        fecha2 = str(date.today())
        sql = 'SELECT a.art_id, a.art_nombre, sum(hm.his_mat_cant) FROM articulo a JOIN historial_materiales' \
              ' hm ON a.art_id=hm.art_id WHERE a.tip_id = 2 AND a.art_cantidad < a.art_cant_min AND ' \
              'hm.his_mat_fecha BETWEEN DATE("' + fecha1 + '") AND DATE("' + fecha2 + '") GROUP BY art_id'
        self.cursor.execute(sql)
        art_info = self.cursor.fetchall()


        lista = []

        for i in range(0, len(art_info)):
            lista.append(list(art_info[i]))
        art_info = tuple(lista)
        len_resultado = len(art_info)
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(art_info[i])):
                test = art_info[i][a]
                self.articulos += str(test) + "                 "
                self.ui.ma_tabla_datos.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
            self.articulos += "\n"

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
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            self.ui.ma_tabla_datos.takeTopLevelItem(i)
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla_datos)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla_datos.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

        # Muestra datos seleccionados
    def info(self):
        seleccion = self.ui.ma_tabla_datos.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_input_buscar.setText(datos.text(0))
    # --------------------------------------

    def salir(self):
        self.close()

    def consulta(self):
        try:
            codigo = int(self.ui.ma_input_buscar.text())
        except (ValueError, TypeError):
            self.tabla()
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return

        posicion = 0
        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla_datos.topLevelItem(0).setText(posicion, str(i))
            posicion += 1
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            posicion = 0

            for a in range(0, len(resultado[i])):

                self.ui.ma_tabla_datos.takeTopLevelItem(i)

                posicion += 1


class MaximaMinima(QtWidgets.QDialog):
    datos = []
    valor = []

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
            codigo = int(self.ui.ma_input_codigo.text())
        except ValueError:
            return

        if (codigo < 0) | (codigo > 99999999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        con = ABM_materiales()
        valor = con.consulta_materiales(str(codigo))
        if not valor:
            QMessageBox.about(self, "Error", "Ingrese un código válido")
            return
        else:
            ventanamodificacionmaxmin = ModificacionMaximaMinima(self)
            ventanamodificacionmaxmin.capturarvalor(valor[0][0], valor[0][1], valor[0][3], valor[0][4])
            ventanamodificacionmaxmin.exec_()


class ModificacionMaximaMinima(QtWidgets.QDialog):
    codigo = ""

    def __init__(self, *args):
        super(ModificacionMaximaMinima, self).__init__(*args)
        self.ui = modificacionMaxMin.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

    def confirmar(self):
        minima = str(self.ui.ma_input_minimo.text())
        maxima = str(self.ui.ma_input_maximo.text())
        if int(minima) <= 0:
            QMessageBox.about(self, "Error!!", "\nEl valor mínimo no puede ser menor o igual 0.\n")
            return
        if int(maxima) <= int(minima):
            QMessageBox.about(self, "Error!!", "\nEl valor máximo no puede ser menor o igual que el valor mínimo.\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            sql = 'UPDATE articulo SET art_cant_min ' \
                       '= ' + minima + ' WHERE art_id = ' + self.codigo + ' AND tip_id=3'
            self.cursor.execute(sql)
            sql = 'UPDATE articulo SET art_cant_max ' \
                  '= ' + maxima + ' WHERE art_id = ' + self.codigo + ' AND tip_id=3'
            self.cursor.execute(sql)
            self.conexion.commit()
            self.ui.ma_label_minimo.setText(minima)
            self.ui.ma_label_maximo.setText(maxima)
            self.ui.ma_input_minimo.clear()
            self.ui.ma_input_maximo.clear()
        else:
            return

    def salir(self):
        self.close()

    def capturarvalor(self, cod, nom, mini, maxi):
        self.codigo = str(cod)
        self.ui.ma_label_descripcion.setText(str(nom))
        self.ui.ma_label_minimo.setText(str(mini))
        self.ui.ma_label_maximo.setText(str(maxi))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())
