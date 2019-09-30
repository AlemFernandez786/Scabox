from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Supervisor import altaBajaPersonalOption
from Pantallas.Supervisor import altaDePersonal
from Pantallas.Supervisor import bajaDePersonal
from Pantallas.Supervisor import modificacionSectorDePersonal
from Pantallas.Supervisor import panelModificarSectorPersonal
from Pantallas.Supervisor import consultarStock
from Pantallas.Supervisor import supervisor
from Pantallas.Supervisor import IngresoContraseña
from Pantallas.Supervisor import consultarPersonalSupervisor
from materiales import StockMateriales
from ABM import ABM_supervisor
import mysql.connector
import sys


def __init__(self):
    self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
    self.cursor = self.conexion.cursor()


class VentanaSupervisor(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(VentanaSupervisor, self).__init__(*args, **kwargs)
        self.ui = supervisor.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.clicked.connect(self.consultar_Stock)
        self.ui.su_btn_2.clicked.connect(self.altaBajaPersonal)
        self.ui.su_btn_3.clicked.connect(self.modificacionSector)
        self.ui.su_btn_4.clicked.connect(self.personal)
        self.ui.su_btn_cancelar.clicked.connect(self.cancelar)

    def consultar_Stock(self):
        seleccionsectorparaconsulta = Sectordeconsulta(self)
        seleccionsectorparaconsulta.exec_()

    def altaBajaPersonal(self):
        ventanaaltabajapersonal = AltaBajaPersonal(self)
        ventanaaltabajapersonal.exec_()

    def modificacionSector(self):
        ventanamodificacionsector = ModificacionSector(self)
        ventanamodificacionsector.exec_()

    def personal(self):
        ventanadepersonal = ConsultadePersonal(self)
        ventanadepersonal.exec_()

    def cancelar(self):
        self.close()

class Sectordeconsulta(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Sectordeconsulta, self).__init__(*args, **kwargs)
        self.ui = consultarStock.Ui_Form()
        self.ui.setupUi(self)
        self.ui.su_btn_1.pressed.connect(self.materiales)
        self.ui.su_btn_2.pressed.connect(self.herramientas)
        self.ui.su_btn_3.clicked.connect(self.serializables)

    def materiales(self):
        ventanamateriales = StockMateriales(self)
        ventanamateriales.exec_()

    def herramientas(self):
        ventanaherramientas = StockHerramientas(self)
        ventanaherramientas.exec_()

    def serializables(self):
        ventanaserializables = StockSerializables(self)
        ventanaserializables.exec_()


# class StockMateriales(QtWidgets.QDialog):
#     def __init__(self, *args, **kwargs):
#         super(StockMateriales, self).__init__(*args, **kwargs)
#         self.ui = consultarStockMateriales.Ui_Form()
#         self.ui.setupUi(self)
#         consultar = ABM_materiales()
#         resultado = consultar.consulta_materiales_gral()
#         _translate = QtCore.QCoreApplication.translate
#         len_resultado = (len(resultado))
#         for i in range(0, len_resultado):
#             # resultado[i].insert(3, str(999))
#             posicion = 0
#             for a in range(0, len(resultado[i])):
#                 item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
#                 test = resultado[i][a]
#                 self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
#                 posicion += 1
#
#         self.ui.ma_btn_buscar.clicked.connect(self.consulta)
#         self.ui.ma_btn_volver.clicked.connect(self.salir)
#
#     def salir(self):
#         self.close()
#
#     def consulta(self):
#         try:
#             codigo = int(self.ui.ma_input_buscar.text())
#         except ValueError:
#             QMessageBox.about(self, "Error!!", "\nIngrese un código!!\n")
#             return
#         consultar = ABM_materiales()
#         resultado = consultar.consulta_materiales(str(codigo))
#         posicion = 0
#         try:
#             resultados = resultado[0]
#         except IndexError:
#             QMessageBox.about(self, "Error!!", "\nArtículo inexistente!!\n")
#             return
#         _translate = QtCore.QCoreApplication.translate
#
#         for i in resultados:
#             if posicion == 3:
#                 posicion = posicion + 1
#             self.ui.ma_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(i)))
#             posicion += 1
#
#         consultar = ABM_materiales()
#         resultado = consultar.consulta_materiales_gral()
#         _translate = QtCore.QCoreApplication.translate
#         len_resultado = (len(resultado))
#         for i in range(1, len_resultado):
#             posicion = 0
#             for a in range(0, len(resultado[i])):
#                 item_0 = QtWidgets.QTreeWidgetItem(self.ui.ma_tabla)
#                 test = ''
#                 self.ui.ma_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
#                 posicion += 1

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
        if war == QMessageBox.Cancel:
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
                    QtWidgets.QTreeWidgetItem(self.ui.su_tabla)
                    for a in range(0, len(resultado[i])):
                        test = resultado[i][a]
                        self.ui.su_tabla.topLevelItem(0).setText(posicion, _translate("Form", str(test)))
                        posicion += 1

            def CambiaSector(self):
                sector = 0
                # Herramientas 1
                if self.ui.su_radiobutton_2.isChecked():
                    sector = 1
                # Serializables 2
                elif self.ui.su_radiobutton_3.isChecked():
                    sector = 2
                # Materiales 3
                elif self.ui.su_radiobutton_1.isChecked():
                    sector = 3
                # Supervisor 4
                elif self.ui.su_radiobutton_5.isChecked():
                    sector = 4
                # Control de calidad 5
                elif self.ui.su_radiobutton_4.isChecked():
                    sector = 5
                # Tecnicos 6
                elif self.ui.su_radiobutton_6.isChecked():
                    sector = 6

                class ActualizaContrasenas(QtWidgets.QDialog):
                    def __init__(self, *args, **kwargs):
                        super(ActualizaContrasenas, self).__init__(*args, **kwargs)
                        self.ui = IngresoContraseña.Ui_Form()
                        self.ui.setupUi(self)
                        self.ui.su_btn_confirmar.pressed.connect(self.CambiaSector)
                        self.ui.su_btn_cancelar.pressed.connect(self.cancelar)

                    def CambiaSector(self):
                        clave1 = str(self.ui.su_input_1.text())
                        clave2 = str(self.ui.su_input_2.text())
                        if len(clave1) < 5:
                            war = QMessageBox.warning(self, "Advertencia",
                                                      '''Contraseña demasiado corta''', QMessageBox.Cancel)
                            if war == QMessageBox.Cancel:
                                return
                        if clave1 == clave2:
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
    application = VentanaSupervisor()
    application.show()
    sys.exit(app.exec_())
