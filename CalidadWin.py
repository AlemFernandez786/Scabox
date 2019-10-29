from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Pantallas.Calidad import agregarDenuncia
from Pantallas.Calidad import agregarTrabajoVisitado
from Pantallas.Calidad import altaMovil
from Pantallas.Calidad import consultaDenuncias
from Pantallas.Calidad import consultaDeRegistroDeMoviles
from Pantallas.Calidad import consultaDeTrabajosVisitados
from Pantallas.Calidad import consultarPersonalCalidad
from Pantallas.Calidad import consultarTrabajoControlado
from Pantallas.Calidad import denuncias
from Pantallas.Calidad import editarTrabajosControlados
from Pantallas.Calidad import editarTrabajoVisitado
from Pantallas.Calidad import descontarPorExtravio
from Pantallas.Calidad import modificacionRegistroMovil
from Pantallas.Calidad import presentismo
from Pantallas.Calidad import registrarNuevoTrabajoControlado
from Pantallas.Calidad import registroDeAusencia
from Pantallas.Calidad import registroDeEntradaSalida
from Pantallas.Calidad import registroMovilesTecnicos
from Pantallas.Calidad import sectorControlDeCalidad
from Pantallas.Calidad import trabajosControlados
from Pantallas.Calidad import trabajosVisitados
from Pantallas.Calidad import modificacionLugarTec
from Pantallas.Calidad import salidadiaria
from Pantallas.Calidad import modificacionsalida
from Pantallas.Calidad import consultaDescuentos
from Pantallas.Calidad import agergarDescontaPorExtravio
from ABM import ABM_materiales
from ABM import ABM_supervisor
from Calidad import Calidad
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
        self.ui.ca_btn_2.clicked.connect(self.trabajos_realizados)
        self.ui.ca_btn_3.clicked.connect(self.Denuncias)
        self.ui.ca_btn_4.clicked.connect(self.Presentismo)
        self.ui.ca_btn_5.clicked.connect(self.Registromyt)
        self.ui.ca_btn_6.clicked.connect(self.descontar)
        self.ui.ca_btn_7.clicked.connect(self.trabajoscon)
        self.ui.ca_btn_8.clicked.connect(self.cancelar)
        self.ui.ca_btn_9.clicked.connect(self.personal)

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

    def personal(self):
        ventanapersonal = consultarPersonal(self)
        ventanapersonal.exec_()

    def cancelar(self):
        self.close()


class Trabajos_realizados(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Trabajos_realizados, self).__init__(*args, **kwargs)
        self.ui = trabajosVisitados.Ui_Form()
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
        self.ui = agregarTrabajoVisitado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_agregar.pressed.connect(self.agregar)
        self.ui.ca_btn_agregar_2.pressed.connect(self.agregarart)
        cali=Calidad()
        cods = cali.consulta_de_codigos()
        for i in range(0, len(cods)):
            self.ui.ca_input_10.addItem(str(cods[i]))
        art = cali.consulta_art()
        for i in range(0, len(art)):
            self.ui.ca_input_13.addItem(str(art[i]))

        mov = Calidad()
        movi = mov.consulta_de_moviles()
        for i in range(0, len(movi)):
            self.ui.ca_input_11.addItem(str(movi[i]))

    def agregarart(self):
        contenidolabel=self.ui.label_11.text()
        validaarticulo=self.ui.ca_input_13.currentText()
        if validaarticulo=='Art.':
            QMessageBox.about(self, "Error!!", "\nIngresar articulo\n")
            return
        try:
            validacantidad = int(self.ui.ca_input_14.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngresar cantidad\n")
            return
        validacantidad = self.ui.ca_input_14.text()
        if validacantidad == '':
            QMessageBox.about(self, "Error!!", "\nIngresar cantidad\n")
            return
        contenidonuevo='Art: '
        contenidonuevo=contenidonuevo+self.ui.ca_input_13.currentText()
        contenidonuevo=contenidonuevo+', Cant: '
        contenidonuevo=contenidonuevo+self.ui.ca_input_14.text()
        contenidonuevo=contenidonuevo+'. '
        contenidolabel=contenidolabel+contenidonuevo
        self.ui.label_11.setText(str(contenidolabel))
        self.ui.ca_input_13.setItemText(0, "Art.")
        self.ui.ca_input_13.setCurrentText("Art.")
        self.ui.ca_input_14.setText('')

    def agregar(self):
        lo2=[]
        lo2.append(self.ui.label_12.text())
        lo2.append(self.ui.ca_input_10.currentText())
        lo3=[]
        for i in range (0, len(lo2)):
            cod1 = ''.join(e for e in str(lo2[i]) if e.isalnum())
            lo3.append(cod1)
        lo4=lo3[0]+' '
        lo5=lo3[1]
        lo6=(str(lo4)+' '+str(lo5))
        lo6=''.join(e for e in str(lo6) if e.isalnum())
        lo7=([lo6[i:i+3] for i in range (0,len(lo6),3)])
        lo8=''
        for i in range (0,len(lo7)):
            lo8=lo8+', '+lo7[i]
        lo8=lo8.lstrip(', ' )
        self.ui.label_12.setText(str(lo8))

    def confirmar(self):
        #Se validan los ingresos
        #solo son de caracter obligatorio los mas relevantes para la empresa
        #ot, domicilio, movil, fecha y codigos
        try:
            codigo = int(self.ui.ca_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nVerificar num OT\n")
            return
        if (codigo < 1) | (codigo > 9999999999):
            QMessageBox.about(self, "Error!!", "\nValor OT incorrecta!!\n")
            return

        con = Calidad()
        macs = (self.ui.ca_input_8.text())
        verificador = con.consulta_mac(macs)
        if verificador == False:
            QMessageBox.about(self, "Error", "Campo Macs incorrecto")
            return

        verificador2 = con.consulta_existe_mac_ot(macs)
        if verificador2 == True:
            QMessageBox.about(self, "Error", "Mac ya consumida")
            return

        valorot = con.consulta_ot(str(codigo))
        if valorot:
            QMessageBox.about(self, "Error", "Ot Existente")
            return

        valordom = (self.ui.ca_input_3.text())
        if not valordom:
            QMessageBox.about(self, "Error", "El domicilio no puede estar vacío")
            return

        valormov=(self.ui.ca_input_11.currentText())
        if valormov=='Seleccione un movil':
            QMessageBox.about(self, "Error", "El movil no puede estar vacío")
            return

        valorcod=(self.ui.ca_input_10.currentText())
        if valorcod == 'Seleccione un codigo':
            QMessageBox.about(self, "Error", "Debe ingresar al menos un codigo\nde finalización")
            return

        #se obtiene la fecha corriente y valida q no sea mayor q la ingresada
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_12.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha = (valorfecha.toString('yyMMdd'))
        valores = [
            str(self.ui.ca_input_1.text()),
            str(self.ui.ca_input_2.text()), str(self.ui.ca_input_3.text()),str(self.ui.ca_input_4.toPlainText()),
            str(self.ui.ca_input_5.text()), str(self.ui.ca_input_6.text()), str(self.ui.ca_input_8.text()),
            str(self.ui.ca_input_11.currentText()),valorfecha]
        #se obtienen los codigos confirmados
        lo2 = []
        lo2.append(self.ui.label_12.text())
        #se envian los datos a la funciion
        con.registra_trab(valores, lo2)

        contenidolabel = self.ui.label_11.text()
        ot = self.ui.ca_input_1.text()
        macs = self.ui.ca_input_8.text()
        movil= str(self.ui.ca_input_11.currentText())

        con.separar_cantidad_ot(contenidolabel, ot, movil)
        con.agregar_ot_mac(ot, macs)

        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")
        self.close()

    def cancelar(self):
        self.close()

class consultar_trabajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultar_trabajo, self).__init__(*args, **kwargs)
        self.ui = consultaDeTrabajosVisitados.Ui_Form()
        self.ui.setupUi(self)
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)
        cal=Calidad()
        trabajos=cal.consulta_trabajos()
        len_resultado = (len(trabajos))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(trabajos[i])):
                test = trabajos[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1


    def buscar(self):
        try:
            codigo = int(self.ui.ca_input_buscar.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nVerificar num OT\n")
            return
        cal=Calidad()
        verificador=cal.buscar_ot_existe(str(self.ui.ca_input_buscar.text()))
        if not verificador:
            QMessageBox.about(self, "Error!!", "\nOT no existe\n")
            return
        ot=self.ui.ca_input_buscar.text()
        trabajos=cal.buscar_ot(ot)
        # trabajos = cal.consulta_trabajos()
        len_resultado = (len(trabajos))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(trabajos[i])):
                test = trabajos[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1


    def cancelar(self):
        self.close()

class editar_trabajo(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(editar_trabajo, self).__init__(*args, **kwargs)
        self.ui = editarTrabajoVisitado.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_eliminar.pressed.connect(self.confirmar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def confirmar(self):
        try:
            codigo = int(self.ui.ca_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nVerificar num OT\n")
            return
        cal=Calidad()
        ot=str(self.ui.ca_input_1.text())
        otv=cal.buscar_ot_existe(ot)
        if not otv:
            QMessageBox.about(self, "Error", "Ot Inexistente")
            return
        domicilio=cal.buscar_domicilio_ot(self.ui.ca_input_1.text())
        if domicilio=='None':
            QMessageBox.about(self, "Error", "Ot Inexistente")
            return
        else:
            domicilio = (domicilio[0][0])
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se eliminará la ot: '''+str(self.ui.ca_input_1.text())+
                                      '''\nde domicilio: '''+str(domicilio)+'''.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.eliminar_ot(self.ui.ca_input_1.text())
                self.close()
            else:
                return

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
        self.ui.ca_btn_agregar.pressed.connect(self.agregar)
        cali = Calidad()
        movi = cali.consulta_de_moviles()
        for i in range(0, len(movi)):
            self.ui.ca_input_6.addItem(str(movi[i]))
        legs = cali.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_9.addItem(str(legs[i]))
        for i in range(0, len(legs)):
            self.ui.ca_input_10.addItem(str(legs[i]))
        art = cali.consulta_art()
        for i in range(0, len(art)):
            self.ui.ca_input_11.addItem(str(art[i]))

    def agregar(self):
        contenidolabel=self.ui.label.text()
        validaarticulo=self.ui.ca_input_11.currentText()
        if validaarticulo=='Art.':
            QMessageBox.about(self, "Error!!", "\nIngresar articulo\n")
            return
        try:
            validacantidad = int(self.ui.ca_input_12.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngresar cantidad\n")
            return
        validacantidad = self.ui.ca_input_12.text()
        if validacantidad == '':
            QMessageBox.about(self, "Error!!", "\nIngresar cantidad\n")
            return
        contenidonuevo='Art: '
        contenidonuevo=contenidonuevo+self.ui.ca_input_11.currentText()
        contenidonuevo=contenidonuevo+', Cant: '
        contenidonuevo=contenidonuevo+self.ui.ca_input_12.text()
        contenidonuevo=contenidonuevo+'. '
        contenidolabel=contenidolabel+contenidonuevo
        self.ui.label.setText(str(contenidolabel))
        self.ui.ca_input_11.setItemText(0, "Art.")
        self.ui.ca_input_11.setCurrentText("Art.")
        self.ui.ca_input_12.setText('')

    def confirmar(self):
        cali = Calidad()
        acta = self.ui.ca_input_2.text()
        macs = (self.ui.ca_input_5.text())
        verificador = cali.consulta_mac(macs)
        if verificador == False:
            QMessageBox.about(self, "Error", "Campo Macs incorrecto")
            return
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_4.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha = (valorfecha.toString('yyMMdd'))
        #
        valorfecha2 = (self.ui.ca_input_8.date())
        if valorfecha2 > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha2= (valorfecha2.toString('yyMMdd'))
        denuncia=[]
        if (self.ui.ca_input_6.currentText())=='Seleccione un movil':
            QMessageBox.about(self, "Error", "Seleccione un movil")
            return
        if (self.ui.ca_input_9.currentText())=='Seleccione un Técnico':
            QMessageBox.about(self, "Error", "Seleccione un Técnico")
            return
        if (self.ui.ca_input_1.text())=='':
            QMessageBox.about(self, "Error", "Campo folio no puede estar vacio")
            return
        if (self.ui.ca_input_2.text())=='':
            QMessageBox.about(self, "Error", "Campo acta no puede estar vacio")
            return
        if (self.ui.ca_input_3.text())=='':
            QMessageBox.about(self, "Error", "Campo comisaria no puede estar vacio")
            return
        if (self.ui.ca_input_7.text())=='':
            QMessageBox.about(self, "Error", "Campo legajo denuncia no puede estar vacio")
            return
        denuncia.append(self.ui.ca_input_1.text())
        denuncia.append(self.ui.ca_input_2.text())
        denuncia.append(self.ui.ca_input_7.text())
        denuncia.append(self.ui.ca_input_3.text())
        denuncia.append(str(valorfecha))
        denuncia.append(str(valorfecha2))
        denuncia.append(self.ui.ca_input_6.currentText())

        cali.registrar_denuncia(denuncia)
        contenidolabel = self.ui.label.text()
        acta=self.ui.ca_input_2.text()
        macs=self.ui.ca_input_5.text()
        tec1=self.ui.ca_input_9.currentText()
        if (self.ui.ca_input_10.currentText()) == 'Seleccione un Técnico':
            tec2=''
        else:
            tec2=self.ui.ca_input_10.currentText()
        cali.separar_cantidad(contenidolabel, acta)
        cali.agregar_denuncia_mac(acta, macs)
        cali.agergar_denuncia_emp(acta, tec1, tec2)
        QMessageBox.about(self, "Confirmado!!", "\nDenuncia cargada correctamente\n")
        self.close()

    def cancelar(self):
        self.close()

class consultardenuncia(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultardenuncia, self).__init__(*args, **kwargs)
        self.ui = consultaDenuncias.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        cal = Calidad()
        denuncias = cal.consulta_denuncia()
        len_resultado = (len(denuncias))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(denuncias[i])):
                test = denuncias[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

    def buscar(self):
        cal = Calidad()
        if len(self.ui.ca_input_buscar.text())<5:
            try:
                codigo = int(self.ui.ca_input_buscar.text())
            except ValueError:
                QMessageBox.about(self, "Error!!", "\nVerificar numero de legajo\n")
                return
            consulta=cal.consulta_existen_legajos(self.ui.ca_input_buscar.text())
            if not consulta:
                QMessageBox.about(self, "Error!!", "\nLegajo inexsitente\n")
                return
        if len(self.ui.ca_input_buscar.text())>4 and len(self.ui.ca_input_buscar.text())<12:
            QMessageBox.about(self, "Error!!", "\nVerificar numero de busqueda\n")
            return
        if len(self.ui.ca_input_buscar.text())>11:
            consulta2 = cal.consulta_existe_mac(self.ui.ca_input_buscar.text())
            if not consulta2:
                QMessageBox.about(self, "Error!!", "\nMac no se encuentra en denuncias\n")
                return
        denuncias=cal.busqueda_denuncia(self.ui.ca_input_buscar.text())
        len_resultado = (len(denuncias))
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(denuncias[i])):
                test = denuncias[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

    def cancelar(self):
        self.close()

class presentismoCali(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(presentismoCali, self).__init__(*args, **kwargs)
        self.ui = presentismo.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_1.pressed.connect(self.Registrausentes)
        self.ui.ca_btn_2.pressed.connect(self.Registrarhorarios)
        self.ui.ca_btn_3.pressed.connect(self.saliadia)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def Registrausentes(self):
        ventanaRegistrausentes = registrarAusentes(self)
        ventanaRegistrausentes.exec_()

    def Registrarhorarios(self):
        ventanaRegistrarhorarios = registrarHorarios(self)
        ventanaRegistrarhorarios.exec_()

    def saliadia(self):
        ventanasaliadia = panelSalidasDiarias(self)
        ventanasaliadia.exec_()

    def cancelar(self):
        self.close()

class registrarAusentes(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registrarAusentes, self).__init__(*args, **kwargs)
        self.ui = registroDeAusencia.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        cal = Calidad()
        ausentes = cal.consulta_ausentes()
        len_resultado = (len(ausentes))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(ausentes[i])):
                test = ausentes[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        legs = cal.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_buscar.addItem(str(legs[i]))
        self.ui.ca_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ca_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ca_input_1.setText(datos.text(1))

    def buscar(self):
        legajo=self.ui.ca_input_buscar.currentText()
        if legajo =='Seleccione Técnico':
            QMessageBox.about(self, "Error!!", "\nIngrese Legajo\n")
            return
        cali = Calidad()
        resultado = cali.consulta_ausentes_legajo(legajo)
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

    def confirmar(self):
        legajo=self.ui.ca_input_1.text()
        cal=Calidad()
        if self.ui.ca_input_1.text()=='':
            QMessageBox.about(self, "Error!!", "\nSeleccione el legajo de la tabla\nque desea actualizar")
            return
        if self.ui.ca_input_2.isChecked() == True:
            validador='SI'
            cal.registrar_justificacion(validador, legajo)
        if self.ui.ca_input_3.isChecked() == True:
            validador = 'NO'
            cal.registrar_justificacion(validador, legajo)
        self.close()

    def cancelar(self):
        self.close()

class registrarHorarios(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registrarHorarios, self).__init__(*args, **kwargs)
        self.ui = registroDeEntradaSalida.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        cal=Calidad()
        legs = cal.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_buscar.addItem(str(legs[i]))
        for i in range(0, len(legs)):
            self.ui.ca_input_1.addItem(str(legs[i]))
        hora = cal.consulta_horarios()
        len_resultado = (len(hora))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(hora[i])):
                test = hora[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

    def confirmar(self):
        cal=Calidad()
        legajo = self.ui.ca_input_1.currentText()
        if legajo == 'Seleccione Técnico':
            QMessageBox.about(self, "Error!!", "\nIngrese Legajo\n")
            return
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_2.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha=(valorfecha.toString('yyMMdd'))
        horas=[]
        horas.append(legajo)
        horas.append(valorfecha)
        ida=''.join(e for e in str(self.ui.ca_input_3.text()) if e.isalnum())
        vuelta = ''.join(e for e in str(self.ui.ca_input_4.text()) if e.isalnum())
        ida=ida+'00'
        horas.append(ida)
        vuelta=vuelta+'00'
        horas.append(vuelta)
        verificafecha = cal.consulta_horarios_empleado_existente(legajo, valorfecha)
        if verificafecha:
            war = QMessageBox.warning(self, "Advertencia",
                                      '''El registro de ese usuario en esa fecha \nya se ingresó.\n
                                Desea modificarlo?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.modificar_horario(horas)
                hora = cal.consulta_horarios()
                len_resultado = (len(hora))
                QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
                self.ui.ca_tabla.clear()
                for i in range(0, len_resultado):
                    posicion = 0
                    QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
                    for a in range(0, len(hora[i])):
                        test = hora[i][a]
                        self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                        posicion += 1
            else:
                return
        else:
            cal.registrar_horario(horas)
            hora = cal.consulta_horarios()
            len_resultado = (len(hora))
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            self.ui.ca_tabla.clear()
            for i in range(0, len_resultado):
                posicion = 0
                QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
                for a in range(0, len(hora[i])):
                    test = hora[i][a]
                    self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                    posicion += 1


    def buscar(self):
        legajo = self.ui.ca_input_buscar.currentText()
        if legajo == 'Seleccione Técnico':
            QMessageBox.about(self, "Error!!", "\nIngrese Legajo\n")
            return
        cali = Calidad()
        resultado = cali.consulta_horarios_empleado(legajo)
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

    def cancelar(self):
        self.close()

class registroMovTec(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registroMovTec, self).__init__(*args, **kwargs)
        self.ui = registroMovilesTecnicos.Ui_Form()
        self.ui.setupUi(self)

        self.ui.ca_btn_1.pressed.connect(self.altamo)
        self.ui.ca_btn_3.pressed.connect(self.modificarmo)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)

    def altamo(self):
        ventanaaltamo = altaMovilCal(self)
        ventanaaltamo.exec_()

    def modificarmo(self):
        ventanamodificarmo = modificarMovil(self)
        ventanamodificarmo.exec_()

    def cancelar(self):
        self.close()

class altaMovilCal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(altaMovilCal, self).__init__(*args, **kwargs)
        self.ui = altaMovil.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        cali=Calidad()
        legs = cali.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_6.addItem(str(legs[i]))

    def confirmar(self):
        codigo = (self.ui.ca_input_1.text())
        if not codigo:
            QMessageBox.about(self, "Error", "La patente no puede estar vacía")
            return
        con = Calidad()
        valor = con.consulta_patente(str(codigo))
        if valor:
            QMessageBox.about(self, "Error", "Patente existente")
            return
        codigo1 = (self.ui.ca_input_2.text())
        if not codigo1:
            QMessageBox.about(self, "Error", "La poliza no puede estar vacía")
            return
        codigo3 = (self.ui.ca_input_4.text())
        if not codigo3:
            QMessageBox.about(self, "Error", "El campo de Tarjeta verde no puede estar vacío")
            return
        codigo4 = (str(self.ui.ca_input_6.currentText()))
        if codigo4=="Seleccione un Técnico":
            QMessageBox.about(self, "Error", "Debe elegir técnico titular del vehiculo")
            return
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_3.date())
        if valorfecha < hoy:
            QMessageBox.about(self, "Error", "No puede ingresar datos vencidos")
            return
        valorfecha2 = (self.ui.ca_input_5.date())
        if valorfecha2 < hoy:
            QMessageBox.about(self, "Error", "No puede ingresar datos vencidos")
            return
        #se arma la tupla
        valores = [
            str(self.ui.ca_input_1.text()),
            str(self.ui.ca_input_2.text()), str(self.ui.ca_input_3.text()), str(self.ui.ca_input_4.text()),
            str(self.ui.ca_input_5.text()),str(self.ui.ca_input_6.currentText())]
        con.alta_movil(valores)
        QMessageBox.about(self, "Confirmación", "\nConfirmado!!\n")
        self.close()

    def cancelar(self):
        self.close()

class modificarMovil(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(modificarMovil, self).__init__(*args, **kwargs)
        self.ui = modificacionRegistroMovil.Ui_Form()
        self.ui.setupUi(self)

        consultar = Calidad()
        resultado = consultar.modificacion_movil()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1
        mov = consultar.consulta_de_moviles()
        for i in range(0, len(mov)):
            self.ui.ca_input_buscar.addItem(str(mov[i]))

        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)

        self.ui.ca_tabla.itemSelectionChanged.connect(self.info)

    def info(self):
        seleccion = self.ui.ca_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            self.ui.ca_input_1.setText(datos.text(0))
            self.ui.ca_input_2.setText(datos.text(1))
            self.ui.ca_input_3.setText(datos.text(2))
            from datetime import datetime
            VTV=datetime.strptime(str(datos.text(3)),'%Y-%m-%d').date()
            self.ui.ca_input_4.setDate(VTV)
            self.ui.ca_input_5.setText(datos.text(4))
            lic = datetime.strptime(str(datos.text(5)), '%Y-%m-%d').date()
            self.ui.ca_input_6.setDate(lic)
            self.ui.ca_input_7.addItem("")
            self.ui.ca_input_7.setItemText(0, datos.text(6))
            cali = Calidad()
            legs = cali.consulta_de_legajos()
            for i in range(0, len(legs)):
                self.ui.ca_input_7.addItem(str(legs[i]))


    def confirmar(self):
        import datetime
        hoy = datetime.datetime.today()
        valorfechavtv = (self.ui.ca_input_4.date())
        if valorfechavtv < hoy:
            QMessageBox.about(self, "Error", "No puede ingresar datos vencidos")
            return
        valorfechalic = (self.ui.ca_input_6.date())
        if valorfechalic < hoy:
            QMessageBox.about(self, "Error", "No puede ingresar datos vencidos")
            return
        seleccion = self.ui.ca_tabla.selectedItems()
        if seleccion:
            datos = seleccion[0]
            patente=datos.text(1)
            poliza = self.ui.ca_input_3.text()
            vtv = self.ui.ca_input_4.date()
            verde=self.ui.ca_input_5.text()
            lic=self.ui.ca_input_6.date()
            legajo=self.ui.ca_input_7.currentText()
        cal=Calidad()
        try:
            movil = cal.movil_por_patente(patente)
        except UnboundLocalError:
            QMessageBox.warning(self, "Advertencia",
                                '''No hay cambios''', QMessageBox.Ok)
            self.info()
            return
        vtv = (vtv.toString('yyyy-MM-dd'))
        lic = (lic.toString('yyyy-MM-dd'))
        sinca=True
        if str(movil[0][2])!=poliza:
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se modificará el numero \nde la poliza de segura.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:

                cal.registra_poliza(patente, poliza)
                sinca=False
            else:
                return

        if str(movil[0][3])!=str(vtv):
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se modificará la fecha de vencimiento\nde la verificacion tecnica.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.registra_VTV(patente,vtv)
                sinca = False
            else:
                return
        if str(movil[0][4])!= verde:
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se modificará el numero \nde la Tarjeta verde.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.registra_verde(patente,verde)
            else:
                return
        if str(movil[0][5])!= str(lic):
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se modificará la fecha de vencimiento \nde la licencia.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.registra_lic(patente, lic)
                sinca = False
            else:
                return
        if str(movil[0][6])!= legajo:
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se modificará el numero \nde legajo.\n
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.registra_legajo(patente,legajo)
                sinca = False
            else:
                return
        if sinca==True:
            QMessageBox.warning(self, "Advertencia",
                                      '''No hay cambios''', QMessageBox.Ok)
            return
        self.close()

    def buscar(self):
        movil=self.ui.ca_input_buscar.currentText()
        cali = Calidad()
        resultado = cali.movil_por_id(movil)
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

    def cancelar(self):
        self.close()

class panelSalidasDiarias(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(panelSalidasDiarias, self).__init__(*args, **kwargs)
        self.ui = modificacionsalida.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_cancelar.pressed.connect(self.volver)
        self.ui.ca_btn_1.pressed.connect(self.modificar)
        self.ui.ca_btn_2.pressed.connect(self.registrarigual)
        self.ui.ca_btn_3.pressed.connect(self.consulta)

    def volver(self):
        self.close()

    def buscar(self):
        self.close()

    def consulta(self):
        ventanaconsulta = consultarSalidasDIarias(self)
        ventanaconsulta.exec_()

    def modificar(self):
        ventanamodificar = modificar_tecnico_lugar(self)
        ventanamodificar.exec_()

    def registrarigual(self):
        ventanaregistrarigual = registarSalidaIgualaAnterior(self)
        # ventanaregistrarigual.exec_()

class consultarSalidasDIarias(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultarSalidasDIarias, self).__init__(*args, **kwargs)
        self.ui = salidadiaria.Ui_Form()
        self.ui.setupUi(self)
        consultar = Calidad()
        # resultado = consultar.consulta_diaria()
        try:
            resultado = consultar.consulta_diaria()
        except mysql.connector.Error:
            return
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.volver)

    def volver(self):
        self.close()

    def buscar(self):
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_1.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha=(valorfecha.toString('yyMMdd'))
        consultar = Calidad()
        # resultado = consultar.busqueda_salida_diaria(valorfecha)
        try:
            resultado = consultar.busqueda_salida_diaria(valorfecha)
        except mysql.connector.Error:
            return
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

class modificar_tecnico_lugar(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(modificar_tecnico_lugar, self).__init__(*args, **kwargs)
        self.ui = modificacionLugarTec.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.confirmar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        self.ui.ca_btn_registrar.pressed.connect(self.registrar)
        cali = Calidad()
        legs = cali.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_1.addItem(str(legs[i]))
        lugar = cali.consulta_de_moviles()
        lugar.append('Ausente')
        lugar.append('Supervisor')
        lugar.append('Materiales')
        lugar.append('Herramientas')
        lugar.append('Calidad')
        lugar.append('Serializable')
        lugar.append('En Base')
        lugar.append('Enfermedad')
        lugar.append('Vacaciones')
        lugar.append('Estudio')
        lugar.append('Mudanza')
        lugar.append('Otros')
        for i in range(0, len(lugar)):
            self.ui.ca_input_2.addItem(str(lugar[i]))

    def confirmar(self):
        if self.ui.ca_input_1.currentText() == "Seleccione un Técnico":
            QMessageBox.about(self, "Error!!",
                              "\nSeleccione Técnico")
            return
        if self.ui.ca_input_2.currentText() == "Seleccione un movil o estado":
            QMessageBox.about(self, "Error!!",
                              "\nSeleccione movil o estado")
            return
        war = QMessageBox.warning(self, "Advertencia",
                                  '''Se modificará el lugar del técnico.\n
                            Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            legajo=(self.ui.ca_input_1.currentText())
            movil=(self.ui.ca_input_2.currentText())
            from datetime import date
            hoy = date.today()
            formato = "%y-%m-%d"
            hoy = hoy.strftime(formato)
            cambio=[]
            cambio.append(hoy)
            cambio.append(legajo)
            cambio.append(movil)
            cal= Calidad()
            consultarcambio = cal.consulta_tecnico_en_movil(cambio)
            if consultarcambio or consultarcambio==0:
                if consultarcambio==2:
                    QMessageBox.about(self, "Error!!",
                                      "\nEl técnico ya se encuentra en ese movil")
                    return
                else:
                    consultaTecEnSalida = cal.consulta_diaria_tec(cambio[1])
                    if consultaTecEnSalida:
                        QMessageBox.about(self, "Error!!",
                                          "\nEl técnico ya se encuentra en la \n planilla del dia de la fecha")
                        return
                    else:
                        cal.regritra_cambio_salida(cambio)
                        cal.actualizacion_duplas()
            else:
                cal.regritra_cambio_salida(cambio)
                cal.actualizacion_duplas()
        else:
            return

    def cancelar(self):
        self.close()

    def registrar(self):
        cal = Calidad()
        validaModificacion = cal.verifica_modificacion()
        if not validaModificacion:
            QMessageBox.about(self, "Error!!",
                                  "\nNo se registraron cambios")
            return
        else:
            verificador=cal.verificar_modificacion_cargada()
            if verificador == True:
                QMessageBox.about(self, "Error!!",
                                  "\nYa se cargó la planilla del día")
                return
            else:
                war = QMessageBox.warning(self, "Advertencia",
                                          '''Se registrarán los tecnicos restantes.\nde la misma manera en la que estaban\nen la salida anterior
                                    Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
                if war == QMessageBox.Ok:
                    cal.registra_salida_modificada()
                    QMessageBox.about(self, "Exito",
                                      "\nPlanilla del día cargada correctamente")
                    return
        self.close()

class registarSalidaIgualaAnterior(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(registarSalidaIgualaAnterior, self).__init__(*args, **kwargs)
        cal = Calidad()
        verificador = cal.verificar_modificacion_cargada()
        if verificador == True:
            QMessageBox.about(self, "Error!!",
                              "\nYa se cargó la planilla del día")
            return
        else:
            war = QMessageBox.warning(self, "Advertencia",
                                      '''Se registrarán los tecnicos de la misma manera \nen la que estaban en la salida anterior
                                Desea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
            if war == QMessageBox.Ok:
                cal.registra_salida_igual_anterior()
                QMessageBox.about(self, "Exito",
                                  "\nPlanilla del día cargada correctamente")
                return
            if war == QMessageBox.Cancel:
                return

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
        self.ui.ca_btn_1.pressed.connect(self.agregarDescuento)
        self.ui.ca_btn_2.pressed.connect(self.consultaDescuento)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)


    def agregarDescuento(self):
        ventanaagregarDescuento = agregar_descuento(self)
        ventanaagregarDescuento.exec_()

    def consultaDescuento (self):
        ventanaconsultaDescuento = consulta_descuento(self)
        ventanaconsultaDescuento.exec_()

    def cancelar(self):
        self.close()

class agregar_descuento(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(agregar_descuento, self).__init__(*args, **kwargs)
        self.ui = agergarDescontaPorExtravio.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_confirmar.pressed.connect(self.agregar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        cali=Calidad()
        legs = cali.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_1.addItem(str(legs[i]))

    def agregar(self):
        try:
            codigo = int(self.ui.ca_input_2.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nIngersar solo números enteros\n")
            return
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_3.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha=(valorfecha.toString('yyMMdd'))
        if self.ui.ca_input_1.currentText()=='Seleccione Técnico':
            QMessageBox.about(self, "Error", "Seleccione técnico")
            return
        descuento=[]
        descuento.append(self.ui.ca_input_1.currentText())
        descuento.append(self.ui.ca_input_2.text())
        descuento.append(valorfecha)
        cali=Calidad()
        cali.agregar_descuento(descuento)
        QMessageBox.about(self, "Confirmado!!", "\nDescuento cargado correctamente\n")
        self.close()
    def cancelar(self):
        self.close()

class consulta_descuento(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consulta_descuento, self).__init__(*args, **kwargs)
        self.ui = consultaDescuentos.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_cancelar.pressed.connect(self.cancelar)
        cal = Calidad()
        denuncias = cal.consulta_descuentos()
        len_resultado = (len(denuncias))
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(denuncias[i])):
                test = denuncias[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        legs = cal.consulta_de_legajos()
        for i in range(0, len(legs)):
            self.ui.ca_input_buscar.addItem(str(legs[i]))

    def buscar(self):
        if self.ui.ca_input_buscar.currentText()=='Seleccione técnico':
            QMessageBox.about(self, "Error", "Seleccione técnico")
            return
        cal=Calidad()
        descuentos = cal.busqueda_descuentos(self.ui.ca_input_buscar.currentText())
        len_resultado = (len(descuentos))
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(descuentos[i])):
                test = descuentos[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

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
        cal=Calidad()
        legs = cal.consulta_ot2()
        for i in range(0, len(legs)):
            self.ui.ca_input_1.addItem(str(legs[i]))

    def confirmar(self):
        cal = Calidad()
        if self.ui.ca_input_1.currentText()=='Seleccione OT':
            QMessageBox.about(self, "Error", "Seleccionar trabajo")
            return
        verificador=cal.consulta_existe_controlado(self.ui.ca_input_1.currentText())
        if verificador:
            QMessageBox.about(self, "Error", "El trabajo ya se controló")
            return
        import datetime
        hoy = datetime.datetime.today()
        valorfecha = (self.ui.ca_input_2.date())
        if valorfecha > hoy:
            QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
            return
        valorfecha=(valorfecha.toString('yyMMdd'))
        otcontrol=[]
        otcontrol.append(self.ui.ca_input_1.currentText())
        otcontrol.append(valorfecha)
        otcontrol.append('"'+self.ui.ca_input_3.toPlainText()+'"')
        cal=Calidad()
        cal.agergar_controlado(otcontrol)
        QMessageBox.about(self, "Confirmado!!", "\nTrabajo controlado cargado correctamente\n")
        self.close()

    def cancelar(self):
        self.close()

class consultarTrabControlado(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultarTrabControlado, self).__init__(*args, **kwargs)
        self.ui = consultarTrabajoControlado.Ui_Form()
        self.ui.setupUi(self)
        print('sdcsavd')
        self.ui.ca_btn_buscar.pressed.connect(self.buscar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)
        cal = Calidad()
        control = cal.consulta_control()
        len_resultado = (len(control))
        print(control)
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(control[i])):
                test = control[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1
        legs = cal.consulta_ot_controlado()
        for i in range(0, len(legs)):
            self.ui.ca_input_buscar.addItem(str(legs[i]))

    def buscar(self):
        if self.ui.ca_input_buscar.currentText() == 'Seleccione OT':
            QMessageBox.about(self, "Error", "Seleccione numero de orden")
            return
        cal = Calidad()
        control = cal.busqueda_ot_control(self.ui.ca_input_buscar.currentText())
        len_resultado = (len(control))
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(control[i])):
                test = control[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, str(test))
                posicion += 1

    def cancelar(self):
        self.close()

class editarTrabajoControlado(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(editarTrabajoControlado, self).__init__(*args, **kwargs)
        self.ui = editarTrabajosControlados.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_eliminar.pressed.connect(self.confirmar)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)

    def confirmar(self):
        try:
            codigo = int(self.ui.ca_input_1.text())
        except ValueError:
            QMessageBox.about(self, "Error!!", "\nVerificar num OT\n")
            return
        cal = Calidad()
        verificador = cal.consulta_existe_controlado(self.ui.ca_input_1.text())
        if not verificador:
            QMessageBox.about(self, "Error", "No existe trabajo controlado")
            return

        war = QMessageBox.warning(self, "Advertencia",
                                  '''Se eliminará la ot: ''' + str(self.ui.ca_input_1.text()) +
                                  '''\nDesea seguir?''', QMessageBox.Ok, QMessageBox.Cancel)
        if war == QMessageBox.Ok:
            cal.borrar_ot_contol(self.ui.ca_input_1.text())
            QMessageBox.about(self, "Confirmado!!", "\nTrabajo controlado eliminado\n")
            self.close()
        else:
            return

    def cancelar(self):
        self.close()

class consultarPersonal(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(consultarPersonal, self).__init__(*args, **kwargs)
        self.ui = consultarPersonalCalidad.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ca_btn_buscar.pressed.connect(self.consulta)
        self.ui.ca_btn_volver.pressed.connect(self.cancelar)
        consultar = ABM_supervisor()
        resultado = consultar.consulta_personal_gral()
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        for i in range(0, len_resultado):
            posicion = 0
            item_0 = QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

    def consulta(self):
        codigo = str(self.ui.ca_input_buscar.text())
        consultar = ABM_supervisor()
        resultado = consultar.consulta_personal(str(codigo))
        posicion = 0
        try:
            resultados = resultado[0]
        except IndexError:
            QMessageBox.about(self, "Error!!", "\nPersonal inexistente!!\n")
            return
        _translate = QtCore.QCoreApplication.translate
        len_resultado = (len(resultado))
        QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
        self.ui.ca_tabla.clear()
        for i in range(0, len_resultado):
            posicion = 0
            QtWidgets.QTreeWidgetItem(self.ui.ca_tabla)
            for a in range(0, len(resultado[i])):
                test = resultado[i][a]
                self.ui.ca_tabla.topLevelItem(i).setText(posicion, _translate("Form", str(test)))
                posicion += 1

    def cancelar(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = VentanaCalidad()
    application.show()
    sys.exit(app.exec_())
