from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Calidad import agregarDenuncia
from Pantallas.Calidad import agregarTrabajoVisitado
from Pantallas.Calidad import alerta_confirmacion
from Pantallas.Calidad import alerta_error
from Pantallas.Calidad import altaMovil
from Pantallas.Calidad import bajaMovil
from Pantallas.Calidad import consultaDenuncias
from Pantallas.Calidad import consultaDeRegistroDeExtraviosPorFecha
from Pantallas.Calidad import consultaDeRegistroDeExtraviosPorMac
from Pantallas.Calidad import consultaDeRegistroDeExtraviosPorMovil
from Pantallas.Calidad import consultaDeRegistroDeExtraviosPorTecnico
from Pantallas.Calidad import consultaDeRegistroDeMoviles
from Pantallas.Calidad import consultaDeTrabajosVisitados
from Pantallas.Calidad import consultarPersonalCalidad
from Pantallas.Calidad import consultarTrabajoControlado
from Pantallas.Calidad import denuncias
from Pantallas.Calidad import descontarPorExtravio
from Pantallas.Calidad import editarTrabajosControlados
from Pantallas.Calidad import editarTrabajoVisitado
from Pantallas.Calidad import modificacionDeStock
from Pantallas.Calidad import modificacionRegistroMovil
from Pantallas.Calidad import modificarDuplaPorMovil
from Pantallas.Calidad import panelModificarStock
from Pantallas.Calidad import presentismo
from Pantallas.Calidad import registrarNuevoTrabajoControlado
from Pantallas.Calidad import registroDeAusencia
from Pantallas.Calidad import registroDeEntradaSalida
from Pantallas.Calidad import registroDeExtraviosOpcion
from Pantallas.Calidad import registroMovilesTecnicos
from Pantallas.Calidad import sectorControlDeCalidad
from Pantallas.Calidad import trabajosControlados
from Pantallas.Calidad import trabajosVisitados
from ABM import ABM_materiales
from ABM import ABM_supervisor
import mysql.connector
import sys


def __init__(self):
    self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
    self.cursor = self.conexion.cursor()

class VentanaCalidad(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(VentanaCalidad, self).__init__(*args, **kwargs)
        self.ui = sectorControlDeCalidad.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.clicked.connect(self.modificacion_Stock)
        self.ui.ca_btn_2.clicked.connect(self.trabajos_realizados)
        self.ui.ca_btn_3.clicked.connect(self.Denuncias)
        self.ui.ca_btn_4.clicked.connect(self.Presentismo)
        self.ui.ca_btn_5.clicked.connect(self.Registromyt)
        self.ui.ca_btn_6.clicked.connect(self.descontar)
        self.ui.ca_btn_7.clicked.connect(self.trabajoscon)
        self.ui.ca_btn_8.clicked.connect(self.cancelar)

    def modificacion_Stock(self):
        ventanamodificacionstock = ModificacionStockCali(self)
        ventanamodificacionstock.exec_()

    def trabajos_realizados(self):
        ventanatrabajos_realizados = Trabajos_realizados(self)
        ventanatrabajos_realizados.exec_()

    def Denuncias(self):
        ventanaDenuncias = paneldenuncias(self)
        ventanaDenuncias.exec_()

    def Presentismo(self):
        ventanaPresentismo = presentismoCali(self)
        ventanaPresentismo.exec_()

    def Registromyt(self):
        ventanaRegistromyt = registroMovTec(self)
        ventanaRegistromyt.exec_()

    def descontar(self):
        ventanadescontar = descontarExtravios(self)
        ventanadescontar.exec_()

    def trabajoscon(self):
        ventanatrabajoscon = trabajosControl(self)
        ventanatrabajoscon.exec_()

    def cancelar(self):
        self.close()

class ModificacionStockCali(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificacionStockCali, self).__init__(*args, **kwargs)
        self.ui = modificacionDeStock.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def buscar(self):
        ventanapanelstock = StockMaterialesCali(self)
        ventanapanelstock.exec_()

    def cancelar(self):
        self.close()

class StockMaterialesCali(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(StockMaterialesCali, self).__init__(*args, **kwargs)
        self.ui = panelModificarStock.Ui_Form()
        self.ui.setupUi(self)
        # consultar = ABM_materiales()
        # resultado = consultar.consulta_materiales_gral()
        # _translate = QtCore.QCoreApplication.translate
        # len_resultado = (len(resultado))
        # for i in range(0, len_resultado):
        #     # resultado[i].insert(3, str(999))
        #     posicion = 0
        #     for a in range(0, len(resultado[i])):
        #         item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
        #         test = resultado[i][a]
        #         self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
        #         posicion += 1

        self.ui.ca_btn_buscar.clicked.connect(self.consulta)
        self.ui.ca_btn_confirmar.clicked.connect(self.salir)
        self.ui.ca_btn_cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def consulta(self):
        # try:
        #     codigo = int(self.ui.ma_input_buscar.text())
        # except ValueError:
        #     QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
        #     return
        # consultar = ABM_materiales()
        # resultado = consultar.consulta_materiales(str(codigo))
        # posicion = 0
        # try:
        #     resultados = resultado[0]
        # except IndexError:
        #     QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
        #     return
        # _translate = QtCore.QCoreApplication.translate
        #
        # for i in resultados:
        #     if posicion == 3:
        #         posicion = posicion + 1
        #     self.ui.ma_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(i)))
        #     posicion += 1
        #
        # consultar = ABM_materiales()
        # resultado = consultar.consulta_materiales_gral()
        # _translate = QtCore.QCoreApplication.translate
        # len_resultado = (len(resultado))
        # for i in range(1, len_resultado):
        #     posicion = 0
        #     for a in range(0, len(resultado[i])):
        #         item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
        #         test = ''
        #         self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
        #         posicion += 1
        print('holi')

class Trabajos_realizados(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Trabajos_realizados, self).__init__(*args, **kwargs)
        self.ui = trabajosControlados.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.registrartrabajo)
        self.ui.ca_btn_2.pressed.connect(self.consultartrabajo)
        self.ui.ca_btn_3.pressed.connect(self.editartrabajo)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def registrartrabajo(self):
        ventanaregistrar_trabajo = registrar_trabajo (self)
        ventanaregistrar_trabajo.exec_()

    def consultartrabajo(self):
        ventanaconsultartrabajo = consultar_trabajo (self)
        ventanaconsultartrabajo.exec_()

    def editartrabajo(self):
        ventanaeditartrabajo = editar_trabajo (self)
        ventanaeditartrabajo.exec_()

    def cancelar(self):
        self.close()

class registrar_trabajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registrar_trabajo, self).__init__(*args, **kwargs)
        self.ui = registrarNuevoTrabajoControlado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class consultar_trabajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultar_trabajo, self).__init__(*args, **kwargs)
        self.ui = consultarTrabajoControlado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class editar_trabajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(editar_trabajo, self).__init__(*args, **kwargs)
        self.ui = editarTrabajosControlados.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class paneldenuncias(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(paneldenuncias, self).__init__(*args, **kwargs)
        self.ui = denuncias.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.Agregardenuncia)
        self.ui.ca_btn_2.pressed.connect(self.Consultardenuncia)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def Agregardenuncia(self):
        ventanaagregar = agregardenuncia(self)
        ventanaagregar.exec_()

    def Consultardenuncia(self):
        ventanaconsultardenuncia = consultardenuncia(self)
        ventanaconsultardenuncia.exec_()

    def cancelar(self):
        self.close()

class agregardenuncia(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(agregardenuncia, self).__init__(*args, **kwargs)
        self.ui = agregarDenuncia.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaconfirmar = confirmadenuncia(self)
        # ventanaconfirmar.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class consultardenuncia(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultardenuncia, self).__init__(*args, **kwargs)
        self.ui = consultaDenuncias.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class presentismoCali(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(presentismoCali, self).__init__(*args, **kwargs)
        self.ui = presentismo.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.Registrausentes)
        self.ui.ca_btn_2.pressed.connect(self.Registrarhorarios)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def Registrausentes(self):
        ventanaRegistrausentes = registrarAusentes(self)
        ventanaRegistrausentes.exec_()

    def Registrarhorarios(self):
        ventanaRegistrarhorarios = registrarHorarios(self)
        ventanaRegistrarhorarios.exec_()

    def cancelar(self):
        self.close()

class registrarAusentes(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registrarAusentes, self).__init__(*args, **kwargs)
        self.ui = registroDeAusencia.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class registrarHorarios(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registrarHorarios, self).__init__(*args, **kwargs)
        self.ui = registroDeEntradaSalida.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class registroMovTec(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registroMovTec, self).__init__(*args, **kwargs)
        self.ui = registroMovilesTecnicos.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.altamo)
        self.ui.ca_btn_2.pressed.connect(self.bajamo)
        self.ui.ca_btn_3.pressed.connect(self.modificarmo)
        self.ui.ca_btn_4.pressed.connect(self.modificardupla)
        self.ui.ca_btn_5.pressed.connect(self.consultarmo)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def altamo(self):
        ventanaaltamo = altaMovilCal(self)
        ventanaaltamo.exec_()

    def bajamo(self):
        ventanabajamo = bajaMovilCal(self)
        ventanabajamo.exec_()

    def modificarmo(self):
        ventanamodificarmo = modificarMovil(self)
        ventanamodificarmo.exec_()

    def modificardupla(self):
        ventanamodificardupla = modificarDupla(self)
        ventanamodificardupla.exec_()

    def consultarmo(self):
        ventanaconsultarmo = consultaMoviles(self)
        ventanaconsultarmo.exec_()

    def cancelar(self):
        self.close()

class altaMovilCal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(altaMovilCal, self).__init__(*args, **kwargs)
        self.ui = altaMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis)')

    def cancelar(self):
        self.close()

class bajaMovilCal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(bajaMovilCal, self).__init__(*args, **kwargs)
        self.ui = bajaMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class modificarMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(modificarMovil, self).__init__(*args, **kwargs)
        self.ui = modificacionRegistroMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class modificarDupla(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(modificarDupla, self).__init__(*args, **kwargs)
        self.ui = modificarDuplaPorMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class consultaMoviles(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultaMoviles, self).__init__(*args, **kwargs)
        self.ui = consultaDeRegistroDeMoviles.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class descontarExtravios(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(descontarExtravios, self).__init__(*args, **kwargs)
        self.ui = descontarPorExtravio.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class trabajosControl(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(trabajosControl, self).__init__(*args, **kwargs)
        self.ui = trabajosControlados.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.registratrab)
        self.ui.ca_btn_2.pressed.connect(self.consultartrab)
        self.ui.ca_btn_3.pressed.connect(self.editartrab)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def registratrab (self):
        ventanaregistratrab = regustrarTrabajoControlado(self)
        ventanaregistratrab.exec_()

    def consultartrab(self):
        ventanaconsultartrab = consultarTrabControlado(self)
        ventanaconsultartrab.exec_()

    def editartrab (self):
        ventanaeditartrab = editarTrabajoControlado(self)
        ventanaeditartrab.exec_()

    def cancelar(self):
        self.close()

class regustrarTrabajoControlado(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(regustrarTrabajoControlado, self).__init__(*args, **kwargs)
        self.ui = registrarNuevoTrabajoControlado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class consultarTrabControlado(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultarTrabControlado, self).__init__(*args, **kwargs)
        self.ui = consultarTrabajoControlado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class editarTrabajoControlado(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(editarTrabajoControlado, self).__init__(*args, **kwargs)
        self.ui = editarTrabajosControlados.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def confirmar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()

class ccc(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ccc, self).__init__(*args, **kwargs)
        self.ui = ccc.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def buscar(self):
        # ventanaxx = xx(self)
        # ventanaxx.exec_()
        print('holis')

    def cancelar(self):
        self.close()




class AltaBajaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AltaBajaPersonal, self).__init__(*args, **kwargs)
        self.ui = altaBajaPersonalOption.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.pressed.connect(self.alta)
        self.ui.su_btn_2.pressed.connect(self.baja)

    def alta(self):
        ventanaalta = AltaPersonal(self)
        ventanaalta.exec_()

    def baja(self):
        ventanabaja = BajaPersonal(self)
        ventanabaja.exec_()

class AltaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AltaPersonal, self).__init__(*args, **kwargs)
        self.ui = altaDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.alta)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
        # self.ui.su_input_1.clicked.connect(self.modificacionSector)

    def alta(self):
        try:
            self.legajo = int(self.ui.su_input_4.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        codigo = int(self.ui.su_input_4.text())
        if (codigo < 0) | (codigo > 99999999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        con = ABM_supervisor()
        valor = con.consulta_dni(str(codigo))
        if valor:
            QMessageBox.about(self, "Error", "DNI Existente")
            return
        valores = [
            str(self.ui.su_input_4.text()),
            str(self.ui.su_input_2.text()), str(self.ui.su_input_3.text())]
        agregar = ABM_supervisor()
        agregar.alta_personal(valores)

        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")
        self.close()

    def cancelar(self):
        self.close()

class BajaPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(BajaPersonal, self).__init__(*args, **kwargs)
        self.ui = bajaDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.baja)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)

    def baja(self):
        try:
            self.legajo = int(self.ui.su_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return

        codigo = int(self.ui.su_input_1.text())
        if (codigo < 0) | (codigo > 99999999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        con = ABM_supervisor()
        valor = con.consulta_empleado(str(codigo))
        if not valor:
            QMessageBox.about(self, "Error", "Ingrese un legajo válido")
            return


        if (self.legajo < 0) | (self.legajo > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''El empleado será eliminado.\n
                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            legajo = ["", ""]
            legajo[0] = int(self.ui.su_input_1.text())
            try:
                legajo = int(self.ui.su_input_1.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
                return
        if war== QMessageBox.Cancel:
            return
        bajar=ABM_supervisor()
        bajar.baja_personal(legajo)
        self.close()

    def cancelar(self):
        self.close()

class ModificacionSector(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ModificacionSector, self).__init__(*args, **kwargs)
        self.ui = modificacionSectorDePersonal.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_confirmar.pressed.connect(self.Buscarlegajo)
        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)

    def Buscarlegajo(self):
        try:
            self.legajo = int(self.ui.su_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        num_legajo = int(self.ui.su_input_1.text())
        if (num_legajo < 0) | (num_legajo > 99999999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        con = ABM_supervisor()
        valor = con.consulta_empleado(str(num_legajo))
        if not valor:
            QMessageBox.about(self, "Error", "Ingrese un legajo válido")
            return
        if (self.legajo < 0) | (self.legajo > 9999):
            QMessageBox.about(self, "Error!!", "\nValor incorrecto!!\n")
            return
        self.close()

        class MostrarLegajoConsulta(QtWidgets.QDialog):
            def __init__(self, *args, **kwargs):
                super(MostrarLegajoConsulta, self).__init__(*args, **kwargs)
                self.ui = panelModificarSectorPersonal.Ui_Form()
                self.ui.setupUi(self)
                self.ui.su_btn_confirmar.pressed.connect(self.CambiaSector)
                self.ui.su_btn_cancelar.pressed.connect(self.cancelar)
                consultar = ABM_supervisor()
                resultado = consultar.consulta_empleado_sector(num_legajo)
                _translate = QtCore.QCoreApplication.translate
                len_resultado = (len(resultado))
                for i in range(0, len_resultado):
                    posicion = 0
                    for a in range(0, len(resultado[i])):
                        item_0 = QtWidgets.QTreeWidgetItem(self.ui.su_tabla)
                        test = resultado[i][a]
                        self.ui.su_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(test)))
                        posicion += 1

            def CambiaSector(self):
                sector=0
                #Herramientas 1
                if self.ui.su_radiobutton_2.isChecked()==True:
                    sector=1
                #Serializables 2
                elif self.ui.su_radiobutton_3.isChecked()==True:
                    sector=2
                #Materiales 3
                elif self.ui.su_radiobutton_1.isChecked()==True:
                    sector=3
                #Supervisor 4
                elif self.ui.su_radiobutton_5.isChecked()==True:
                    sector=4
                #Control de calidad 5
                elif self.ui.su_radiobutton_4.isChecked()==True:
                    sector = 5
                #Tecnicos 6
                elif self.ui.su_radiobutton_6.isChecked()==True:
                  sector = 6

                class ActualizaContraseñas(QtWidgets.QDialog):
                    def __init__(self, *args, **kwargs):
                        super(ActualizaContraseñas, self).__init__(*args, **kwargs)
                        self.ui = IngresoContraseña.Ui_Form()
                        self.ui.setupUi(self)
                        self.ui.su_btn_confirmar.pressed.connect(self.CambiaSector)
                        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)

                    def CambiaSector(self):
                        clave1= str(self.ui.su_input_1.text())
                        clave2= str(self.ui.su_input_2.text())
                        if len(clave1)<5:
                            war = QMessageBox.warning(self, "Advertencia",
                                                      '''Contraseña demasiado corta''', QMessageBox.Cancel)
                            if war == QMessageBox.Cancel:
                                return
                        if clave1==clave2:
                            passw = str(self.ui.su_input_1.text())
                            pasend = []
                            pasend.append((str(num_legajo), passw))
                            sup = ABM_supervisor()
                            sup.actualizacion_de_claves(pasend)
                            self.close()
                        else:
                            war = QMessageBox.warning(self, "Advertencia",
                                                      '''Las contraseñas no coinciden''', QMessageBox.Cancel)
                            if war == QMessageBox.Cancel:
                                return
                        war = QMessageBox.warning(self, "Advertencia",
                                                  '''El empleado será cambiado de sector.\n
                                            Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
                        if war == QMessageBox.Ok:
                            sup = ABM_supervisor()
                            sup.modificacion_sector((str(num_legajo), str(sector)))
                            self.close()
                        if war == QMessageBox.Cancel:
                            return
                    def cancelar(self):
                        self.close()
                        return
                val=[]
                val.append(num_legajo)
                val.append(sector)
                sup = ABM_supervisor()
                vali=sup.validacion_sector(val)
                if vali==True:
                    war = QMessageBox.warning(self, "Advertencia",
                                              '''El empleado ya es parte de ese sector''', QMessageBox.Cancel)
                    if war == QMessageBox.Cancel:
                        return
                if (sector != 6) and (sector != 0):
                    ventanapass=ActualizaContraseñas(self)
                    ventanapass.exec_()
                elif sector != 0:
                    war = QMessageBox.warning(self, "Advertencia",
                                              '''El empleado será cambiado de sector.\n
                                        Quieres guardar los cambios?''', QMessageBox.Ok, QMessageBox.Cancel)
                    if war == QMessageBox.Ok:
                        sup = ABM_supervisor()
                        sup.modificacion_sector((str(num_legajo), str(sector)))
                        self.close()
                    if war == QMessageBox.Cancel:
                        return
                elif sector==0:
                    war = QMessageBox.warning(self, "Advertencia",
                                              '''Seleccionar sector''', QMessageBox.Cancel)
                    if war == QMessageBox.Cancel:
                        return
                self.close()

            def cancelar(self):
                self.close()

        ventanaBuscarlegajo = MostrarLegajoConsulta(self)
        ventanaBuscarlegajo.exec_()

    def cancelar(self):
        self.close()

class ConsultadePersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(ConsultadePersonal, self).__init__(*args, **kwargs)
        self.ui = consultarPersonalSupervisor.Ui_Form()
        self.ui.setupUi(self)
        consultar = ABM_supervisor()
        resultado = consultar.consulta_personal_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            item_0 = QtWidgets.QTreeWidgetItem(self.ui.su_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.su_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

        self.ui.su_btn_buscar.clicked.connect(self.consulta)
        self.ui.su_btn_volver.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def consulta(self):
        codigo = str(self.ui.su_input_buscar.text())
        consultar = ABM_supervisor()
        resultado = consultar.consulta_personal(str(codigo))
        posicion = 0
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nPersonal inexistente!!\n")
            return
        _translate = QtCore.QCoreApplication.translate
        for i in resultados:
            if posicion == 3:
                posicion = posicion + 1
            self.ui.su_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(i)))
            posicion += 1
        consultar = ABM_supervisor()
        resultado = consultar.consulta_personal_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(1, len_resultado):
            posicion = 0
            for a in range(0, len(resultado[i])):
                test = ''
                self.ui.su_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaCalidad()
    application.show()
    sys.exit(app.exec_())
