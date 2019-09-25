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
from Pantallas.Materiales import stockPorMovilMaterialesIngreso
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
        self.ui.ma_btn_1.clicked.connect(self.consulta_stock)
        self.ui.ma_btn_2.clicked.connect(self.modificacion_stock)
        self.ui.ma_btn_3.clicked.connect(self.alta_baja_stock)
        self.ui.ma_btn_4.clicked.connect(self.maxima_minima_stock)
        self.ui.ma_btn_5.clicked.connect(self.stock_movil)
        self.ui.ma_btn_6.clicked.connect(self.inventario_movil)
        self.ui.ma_btn_7.clicked.connect(self.aprovisionamiento_stock)
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
        ventanastockmovilingreso = StockPorMovilIngreso(self)
        ventanastockmovilingreso.exec_()

    def inventario_movil(self):
        ventanainventario = InventarioMovil(self)
        ventanainventario.exec_()

    def aprovisionamiento_stock(self):
        ventanaaprovisionamiento = Aprovisionamiento(self)
        ventanaaprovisionamiento.exec_()

    def cancelar(self):
        self.close()


class VentanaAltaBaja(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(VentanaAltaBaja, self).__init__(*args, **kwargs)
        self.ui = altaBajaArticulosMaterialesOption.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_1.pressed.connect(self.alta)
        self.ui.ma_btn_2.pressed.connect(self.baja)

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
        valores = [
            str(self.ui.ma_input_6.toPlainText()), str(self.ui.ma_input_2.text()), str(self.ui.ma_input_3.text()),
            str(self.ui.ma_input_4.text())]
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
        codigo = (str(self.ui.ma_input_1.text()))
        borrar = ABM_materiales()
        borrar.baja_materiales(codigo)
        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")


class StockPorMovilIngreso(QtWidgets.QDialog):
    datos = []
    valor = []

    def __init__(self, *args, **kwargs):
        super(StockPorMovilIngreso, self).__init__(*args, **kwargs)
        self.ui = stockPorMovilMaterialesIngreso.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def salir(self):
        self.close()

    def confirmar(self):
        codigo = int(self.ui.ma_input_1.text())
        if (codigo < 0) | (codigo > 99999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        sql = 'SELECT am.art_id, a.art_nombre, am.art_mov_cantidad FROM articulo_movil am JOIN articulo a ON ' \
              'am.art_id = a.art_id WHERE mov_id='+str(codigo)+' AND a.tip_id = 3'
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        lista = []
        for i in range(0, len(resultado)):
            lista.append(list(resultado[i]))
        resultado = tuple(lista)
        print(resultado)
        ventanastockmovil = StockPorMovil()
        ventanastockmovil.capturarvalor(resultado)
        ventanastockmovil.exec_()
        # valor = con.consulta_materiales(str(codigo))
        # if not valor:
        #     QMessageBox.about(self, "Error", "Ingrese un código válido")
        #     return
        # else:
        #     ventanamodificacionmaxmin = ModificacionMaximaMinima(self)
        #     ventanamodificacionmaxmin.capturarvalor(valor[0][0], valor[0][1], valor[0][3], valor[0][4])
        #     ventanamodificacionmaxmin.exec_()


class StockPorMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockPorMovil, self).__init__(*args, **kwargs)
        self.ui = stockPorMovilMateriales.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)
        self.ui.ma_btn_salir.clicked.connect(self.salir)

        # Inserción de datos en tabla
    def capturarvalor(self, datos):

        resultado = datos
        lista = []
        for i in range(0, len(resultado)):
            lista.append(list(resultado[i]))
        resultado = tuple(lista)
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        # -------------------------------------

        # Muestra datos seleccionados
        self.ui.ma_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ma_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_label_1.setText(datos.text(1))
            self.ui.ma_label_2.setText(datos.text(2))

    # --------------------------------------

    def confirmar(self):
        seleccion = self.ui.ma_tabla.selectedItems()
        datos = seleccion[0]
        try:
            self.cantidad = int(self.ui.ma_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        if (self.cantidad < 0) | (self.cantidad > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            try:
                self.cantidad = int(self.ui.ma_input_1.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            self.sql = 'UPDATE articulo_movil SET art_mov_cantidad ' \
                   '= ' + str(self.cantidad) + ' WHERE art_id = ' + str(datos.text(0))
            #TODO query no funca aca
            self.cursor.execute(self.sql)
            print(datos.text(0))
            print(self.cantidad)
        else:
            return

    def salir(self):
        self.close()
        # TODO reveer ventana stock por movil


class ModificarStock(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificarStock, self).__init__(*args, **kwargs)
        self.ui = modificarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            posicion = 0
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_buscar.clicked.connect(self.busqueda)
        self.ui.ma_btn_confirmar.clicked.connect(self.modificacion)

        # Muestra datos seleccionados
        self.ui.ma_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ma_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_input_buscar.setText(datos.text(0))

    # --------------------------------------

    def salir(self):
        self.close()

    def busqueda(self):
        try:
            codigo = int(self.ui.ma_input_buscar.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))

        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return
        QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
        posicion = 0
        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla.topLevelItem(0).setText(posicion, str(i))
            posicion += 1
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            # print(resultado[i])
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            for a in range(0, len(resultado[i])):
                self.ui.ma_tabla.topLevelItem(i).setHidden(True)
                posicion += 1

        self.ui.ma_input_1.setText(str(resultados[2]))
        self.ui.ma_input_2.setDisabled(True)
        self.ui.ma_input_2.setText(str(resultados[4]))
        self.ui.ma_input_3.setDisabled(True)
        self.ui.ma_input_3.setText(str(resultados[3]))
        self.ui.ma_input_4.setDisabled(True)
        self.ui.ma_input_4.setText(str(resultados[1]))

    def modificacion(self):
        try:
            self.cantidad = int(self.ui.ma_input_5.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        if (self.cantidad < 0) | (self.cantidad > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            valor = ["", ""]
            valor[0] = str(self.ui.ma_input_buscar.text())
            try:
                cantidad = int(self.ui.ma_input_5.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
            valor[1] = str(cantidad)
            modificar = ABM_materiales()
            modificar.modificacion_materiales(valor)
            self.busqueda()
        else:
            return


class InventarioMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(InventarioMovil, self).__init__(*args, **kwargs)
        self.ui = conteoDeInventarioPorMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ma_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()


class Aprovisionamiento(QtWidgets.QDialog):
    articulos = ""

    def __init__(self, *args, **kwargs):
        super(Aprovisionamiento, self).__init__(*args, **kwargs)
        self.ui = aprovisionamiento.Ui_Form()
        self.ui.setupUi(self)

        self.ui.ma_btn_cancelar.clicked.connect(self.salir)
        self.ui.ma_btn_confirmar.clicked.connect(self.confirmar)

        art_info = self.pedido(marca)
        lista = []

        for i in range(0, len(art_info)):
            lista.append(list(art_info[i]))
        art_info = tuple(lista)

        len_resultado = len(art_info)
        for i in range(0, len_resultado):

            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            for a in range(0, len(art_info[i])):
                test = art_info[i][a]
                self.articulos += str(test) + "                 "
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
            self.articulos += "\n"
        # Muestra datos seleccionados
        self.ui.ma_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ma_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ma_label.setText(datos.text(1))
            dato = datos.text(2)
            if dato == '':
                dato = 0
            self.ui.ma_input_1.setValue(int(dato))

    # --------------------------------------

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

    def pedido(self, marca1):
        conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        cursor = conexion.cursor()
        fecha1 = str(date.today() + timedelta(days=-60))
        fecha2 = str(date.today())
        sql = 'SELECT a.art_id, a.art_nombre, sum(hm.his_mat_cantidad) FROM articulo a JOIN historial_materiales' \
              ' hm ON a.art_id=hm.art_id WHERE a.tip_id = 3 AND a.art_cantidad < a.art_cant_min AND ' \
              'hm.his_mat_fecha BETWEEN DATE("' + fecha1 + '") AND DATE("' + fecha2 + '") GROUP BY art_id'
        cursor.execute(sql)
        query = cursor.fetchall()
        if marca1 == 1:
            return query
        else:
            query = ""
            return query

    def salir(self):
        self.close()


class StockMateriales(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMateriales, self).__init__(*args, **kwargs)
        self.ui = consultarStockMateriales.Ui_Form()
        self.ui.setupUi(self)
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            # resultado[i].insert(3, str(999))
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

        self.ui.ma_btn_buscar.clicked.connect(self.consulta)
        self.ui.ma_btn_volver.clicked.connect(self.salir)
    # Muestra datos seleccionados
        self.ui.ma_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ma_tabla.selectedItems()
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
            QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
            return
        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales(str(codigo))
        posicion = 0
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
            return
        _translate = QtCore.QCoreApplication.translate

        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.ma_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(i)))
            posicion += 1

        consultar = ABM_materiales()
        resultado = consultar.consulta_materiales_gral()
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            # print(resultado[i])
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
            for a in range(0, len(resultado[i])):
                self.ui.ma_tabla.topLevelItem(i).setHidden(True)
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
        codigo = int(self.ui.ma_input_1.text())
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
        minima = str(self.ui.ma_input_1.text())
        maxima = str(self.ui.ma_input_2.text())
        if int(minima) <= 0:
            QMessageBox.about(self, "Error!!", "\nEl valor mínimo no puede ser menor a 0.\n")
            return
        if int(maxima) <= int(minima):
            QMessageBox.about(self, "Error!!", "\nEl valor máximo no puede ser menor o igual que el valor mínimo.\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El artículo ha sido modificado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            self.sql = 'UPDATE articulo SET art_cant_min ' \
                       '= ' + minima + ' WHERE art_id = ' + self.codigo + ' AND tip_id=3'
            self.cursor.execute(self.sql)
            self.sql = 'UPDATE articulo SET art_cant_max ' \
                       '= ' + maxima + ' WHERE art_id = ' + self.codigo + ' AND tip_id=3'
            self.cursor.execute(self.sql)
            self.conexion.commit()
            self.ui.ma_label_2.setText(minima)
            self.ui.ma_label_3.setText(maxima)
            self.ui.ma_input_1.clear()
            self.ui.ma_input_2.clear()
        else:
            return

    def salir(self):
        self.close()

    def capturarvalor(self, id, nom, min, max):
        self.codigo = str(id)
        self.ui.ma_label_1.setText(str(nom))
        self.ui.ma_label_2.setText(str(min))
        self.ui.ma_label_3.setText(str(max))


# Compara si el dia es viernes .weekday() retorna los dias como un entero 0 para lunes hasta 6 para domingo
marca = 0
if date.today().weekday() == 2:
    marca = 1
    app = QtWidgets.QApplication([])
    aprov_automatico = Aprovisionamiento()
    aprov_automatico.pedido(marca)
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaMateriales()
    application.show()
    sys.exit(app.exec_())
