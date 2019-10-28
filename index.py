from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import sys

from Pantallas import inicio
import Serializables
import materiales
import CalidadWin
import Supervisor


class InicioSesion(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):    
        super(InicioSesion, self).__init__(*args, **kwargs)
        self.ui = inicio.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_inicio.clicked.connect(self.verificarSesion)

    def verificarSesion(self):
        self.password = self.ui.input_pass.text()
        self.usuario  = self.ui.input_legajo.text()
        try:
            int(self.usuario)
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero entero en el usuario!!\n")
            return
        if len(self.usuario) > 4:
            QMessageBox.about(self, "Error!!", "\nEl usuario no puede ser mayor a 4 cifras!!\n")
            return
        if int(self.usuario) < 0:
            QMessageBox.about(self, "Error!!", "\nIngrese un numero positivo en el usuario!!\n")
            return
        if self.password.isalnum():
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nLa contraseña esta vacia!!\n")
            return
        usu_existente = indiceconsultas.usuario_existente(self.usuario)
        try:
            int(usu_existente[0][0])
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nUsuario inexistente!!\n")
            return
        usuario_activo = indiceconsultas.obtener_estado(self.usuario)
        if int(usuario_activo[0][0]) == 1:
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nUsuario inactivo!!\n")
            return
        pass_correcta = indiceconsultas.pass_correcta(self.usuario)
        invertir_pass = pass_correcta[0][1]
        pass_invertida = ""
        for i in range((len(invertir_pass)-1), -1, -1):
            pass_invertida += invertir_pass[i]
        if str(pass_invertida) == str(self.password):
            pass
        else:
            QMessageBox.about(self, "Error!!", "\nContraseña incorrecta!!\n")
            return
        sector = indiceconsultas.obtener_sector(self.usuario)
        if sector[0][0] == 1:
            QMessageBox.about(self, "Error!!", "\nModulo aun no implementado!!\n")
        if sector[0][0] == 2:
            self.close()
            self.serializables = Serializables.VentanaSerializables()
            self.serializables.show()
        if sector[0][0] == 3:
            self.close()
            self.materiales = materiales.VentanaMateriales()
            self.materiales.show()
        if sector[0][0] == 4:
            self.close()
            self.supervisor = Supervisor.VentanaSupervisor()
            self.supervisor.show()
        if sector[0][0] == 5:
            self.close()
            self.calidad = CalidadWin.VentanaCalidad()
            self.calidad.show()
        if sector[0][0] == 6:
            QMessageBox.about(self, "Error!!", "\nUsted no tiene acceso al sistema!!\n")


class IndiceConsultas:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def usuario_existente(self, valor):
        self.valor = valor
        self.sql_usuario = 'SELECT u.usu_legajo ' \
                           'FROM usuarios u ' \
                           'WHERE u.usu_legajo = '+str(self.valor)
        self.cursor.execute(self.sql_usuario)
        usu_existente = self.cursor.fetchall()
        return usu_existente

    def pass_correcta(self, valor):
        self.valor = valor
        self.sql_pass_correcta = 'SELECT u.usu_legajo, u.usu_password ' \
                                 'FROM usuarios u ' \
                                 'WHERE u.usu_legajo = '+str(self.valor)
        self.cursor.execute(self.sql_pass_correcta)
        usuario_pass = self.cursor.fetchall()
        return usuario_pass

    def obtener_sector(self, valor):
        self.valor = valor
        self.sql_sector = 'SELECT emp_sector ' \
                          'FROM historial_sectores ' \
                          'WHERE emp_legajo = '+str(self.valor)+' ' \
                          'ORDER BY fecha_cambio_sector DESC ' \
                          'LIMIT 1'
        self.cursor.execute(self.sql_sector)
        sector = self.cursor.fetchall()
        return sector

    def obtener_estado(self, valor):
        self.valor = valor
        self.sql_estado = 'SELECT activo ' \
                          'FROM usuarios ' \
                          'WHERE usu_legajo = '+str(self.valor)
        self.cursor.execute(self.sql_estado)
        estado = self.cursor.fetchall()
        return estado


indiceconsultas = IndiceConsultas()
app = QtWidgets.QApplication([])
ventana_inicio = InicioSesion()
ventana_inicio.show()
sys.exit(app.exec_())