import mysql.connector

class Calidad:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def consulta_articulos(self, valor):
        self.valor=valor
        if self.valor == 0:
            self.sql = 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo'
            self.cursor.execute(self.sql)
            art_info = self.cursor.fetchall()
        else:
            self.sql = 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE art_id = ' + str(self.valor)
            self.cursor.execute(self.sql)
            art_info = self.cursor.fetchall()
        return art_info

    def consulta_materiales_gral(self):
        self.sql = 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE tip_id = 3'
        self.cursor.execute(self.sql)
        art_info = self.cursor.fetchall()
        lista = []
        for i in range(0, len(art_info)):
            lista.append(list(art_info[i]))
        for i in range(0, len(art_info)):
            lista[i].insert(3, 'NULL')
        art_info = tuple(lista)
        return art_info

    def modificacion_materiales(self, valor):
        self.valor=valor
        # Obtenemos la cantidad actual y creamos la variable modificada
        self.sql = 'SELECT art_cantidad FROM articulo WHERE art_id = ' + self.valor[0] + ' AND tip_id = 3'
        self.cursor.execute(self.sql)
        cant_actual = self.cursor.fetchall()
        cant_actual = ''.join(e for e in str(cant_actual[0]) if e.isalnum())
        cant_actual = int(cant_actual)
        cant_ingresada = int(self.valor[1])
        cantidad=cant_actual+cant_ingresada
        # Obtenemos fecha actual de ingreso
        from datetime import date
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        # Ejecutamos las querys de modificacion en DB
        self.sql = 'UPDATE articulo SET art_fecha_ultimo_ingreso ' \
                   '= ' + today + ' WHERE art_id = ' + self.valor[0]+' AND tip_id=3'
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE articulo SET art_cantidad ' \
                   '= ' + str(cantidad) + ' WHERE art_id = ' + self.valor[0] + ' AND tip_id=3'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def agregar_trabajo_realizado(self, valor):
        self.valor=valor
        self.sql = 'INSERT INTO `trabajos_realizados` (`nro_orden`, `domicilio`, `mov_id`, ' \
                   '`observaciones`, `fecha_trabajo`) VALUES ' \
                    '('+str(self.valor[0])+',"'+self.valor[1]+'",'+str(self.valor[2])+',"'+self.valor[3]+'",'+str(self.valor[4])+')'

        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_movil(self, valor):
        self.valor = valor
        self.sql = 'SELECT * FROM movil WHERE mov_id = ' + self.valor
        self.cursor.execute(self.sql)
        consul_movil = self.cursor.fetchall()
        return consul_movil

    def consulta_ot(self, valor):
        self.valor = valor
        self.sql = 'SELECT * FROM trabajos_realizados WHERE nro_orden = ' + str(self.valor)
        self.cursor.execute(self.sql)
        consul_ot = self.cursor.fetchall()
        return consul_ot

    def registra_trab(self,valor, valor2):
        registrabajo = []
        registrabajo.insert(0, str(valor[0]))
        registrabajo.insert(1, '"' + str(valor[2]) + '"')
        registrabajo.insert(2, str(valor[7]))
        registrabajo.insert(3, '"' + str(valor[3]) + '"')
        registrabajo.insert(4, str(valor[8]))
        registrabajo.insert(5, '"' + str(valor[1]) + '"')
        if valor[4]=='':
            registrabajo.insert(6, str(0))
        else:
            registrabajo.insert(6,str(valor[4]))
        if valor[5]=='':
            registrabajo.insert(7, str(0))
        else:
            registrabajo.insert(7,str(valor[5]))
        self.sql = 'INSERT INTO trabajos_realizados VALUES (' + ",".join(map(str, registrabajo)) + ')'
        self.cursor.execute(self.sql)
        codi=''
        for i in range(0, len(valor2)):
            codi=codi+str(valor2[0])+', '
        codi=codi[0:-2]
        self.sql = 'INSERT INTO finalizacion_trabajo VALUES ("'+str(codi)+'", '+str(valor[0])+')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_trabajos(self):
        self.sql = 'SELECT t.nro_orden, t.domicilio, t.mov_id, t.fecha_trabajo, t.nom_cliente, ' \
                   't.dni_cliente, t.nro_cliente, c.cod_finalizacion, t.observaciones FROM trabajos_realizados t JOIN finalizacion_trabajo c using(nro_orden)'
        self.cursor.execute(self.sql)
        trabajos = self.cursor.fetchall()
        test2 = []
        for i in range(0, len(trabajos)):
            test = []
            tecnicos=[]
            for a in range(0, 3):
                test.append(trabajos[i][a])
            self.sql='SELECT s.emp_legajo as Leg, (SELECT e.emp_apellido FROM empleados e WHERE e.emp_legajo=Leg) as Apellido, ' \
                     '(SELECT e.emp_nombre FROM empleados e WHERE e.emp_legajo=Leg) as Nombre ' \
                     'FROM salidas_diarias s JOIN trabajos_realizados t ON t.mov_id=s.estado_tecnico ' \
                     'WHERE t.nro_orden='+str(trabajos[i][0])+' AND t.fecha_trabajo=s.fecha GROUP by s.emp_legajo'
            self.cursor.execute(self.sql)
            tecnicos = self.cursor.fetchall()
            tecs=''
            if len(tecnicos)==2:
                for a in range(0, len(tecnicos)):
                    tecs=str(tecnicos[a][0])+', '+str(tecnicos[a][1])+' '+str(tecnicos[a][2])
                    test.append (tecs)
            elif len(tecnicos)==1:
                tecs = str(tecnicos[0][0]) + ', ' + str(tecnicos[0][1]) + ' ' + str(tecnicos[0][2])
                test.append(tecs)
                test.append('')
            for u in range(3, 9):
                test.append(trabajos[i][u])

            self.sql = 'SELECT ser_mac from trabajo_serializable where nro_orden=' + str(trabajos[i][0])
            self.cursor.execute(self.sql)
            macs = self.cursor.fetchall()
            mac = ''
            for a in range(0, len(macs)):
                maca = str(macs[a])
                maca = ''.join(e for e in str(maca) if e.isalnum())
                mac = str(mac) + ' ' + maca
            test.append(mac)
            self.sql = 'SELECT art_id, ot_art_cantidad from trabajo_materiales where nro_orden=' + str(trabajos[i][0])
            self.cursor.execute(self.sql)
            mats = self.cursor.fetchall()
            mat = ''
            for a in range(0, len(mats)):
                mat = mat + 'Art: ' + str(mats[a][0]) + ', Cant: ' + str(mats[a][1]) + '. '
            test.append(mat)
            test2.append(test)
        return test2

    def separar_cantidad_ot(self, valor, ot, movil):
        numOt = ot
        # dividimos al label obtenido por espacios
        labelDividido = (valor.split())
        codCant = []
        # creamos la variable control para que ingrese a codCant cada codigo con su cantidad
        control = 0
        # creamos una tupla para agregar cada codigo con su cantidad
        codCantIndividual = []
        for i in range(0, len(labelDividido)):
            if labelDividido[i] != 'Art:' or labelDividido[i] != 'Cant:':
                var1 = labelDividido[i]
                var1 = ''.join(e for e in str(var1) if e.isalnum())
                # se verifica si el objeto obtenido es numero
                if var1.isnumeric():
                    control += 1
                    codCantIndividual.append(var1)
                    # se verifica si ya estan los pares de datos para mandar
                    # a la tupla pincipal
                    if control == 2:
                        codCant2 = []
                        numOt = ''.join(e for e in str(numOt) if e.isalnum())
                        codCant2.append(numOt)
                        codCant2.append(codCantIndividual[0])
                        codCant2.append(codCantIndividual[1])
                        codCant.append(codCant2)
                        control = 0
                        codCantIndividual = []
        for i in range(0, len(codCant)):
            self.sql = 'INSERT INTO trabajo_materiales VALUES (' + ",".join(map(str, codCant[i])) + ')'
            self.cursor.execute(self.sql)
            self.sql= 'SELECT art_mov_cantidad from articulo_movil where art_id='+str(codCant[i][1])+' AND mov_id='+str(movil)
            print(self.sql)
            self.cursor.execute(self.sql)
            cantidad=self.cursor.fetchall()
            cantidad = ''.join(e for e in str(cantidad) if e.isalnum())
            cantidadactual= int(cantidad)-int(codCant[i][2])
            print(cantidadactual)
            self.sql = 'UPDATE articulo_movil SET art_mov_cantidad='+str(cantidadactual)+' WHERE art_id='+str(codCant[i][1])+' AND mov_id='+str(movil)
            print(self.sql)
            self.cursor.execute(self.sql)
        self.conexion.commit()

    def agregar_ot_mac(self, ot, mac):
        numOt = ot
        labelDividido = (mac.split())
        for i in range(0, len(labelDividido)):
            var1 = labelDividido[i]
            var1 = ''.join(e for e in str(var1) if e.isalnum())
            self.sql = 'SELECT * from serializable WHERE ser_mac="' + var1 + '"'
            self.cursor.execute(self.sql)
            verificadormac = self.cursor.fetchall()
            if verificadormac:
                mac1=[]
                numOt = ''.join(e for e in str(numOt) if e.isalnum())
                mac1.append(numOt)
                var1='"'+var1+'"'
                mac1.append(var1)
                self.sql = 'INSERT INTO trabajo_serializable VALUES (' + ",".join(map(str, mac1)) + ')'
                self.cursor.execute(self.sql)
                import datetime
                hoy = datetime.date.today()
                hoy = ('{:%Y%m%d}'.format(hoy))
                self.sql = 'INSERT INTO historial_serializables (ser_mac, ser_estado, ser_fecha_ultimo_estado)' \
                           'VALUES (' + var1 + ', 3, ' + hoy + ')'
                self.cursor.execute(self.sql)
                self.conexion.commit()
        self.conexion.commit()

    def buscar_domicilio_ot(self,valor):
        self.sql = 'SELECT domicilio FROM trabajos_realizados WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        domicilio = self.cursor.fetchall()
        return domicilio

    def buscar_ot_existe(self,valor):
        self.sql = 'SELECT * FROM trabajos_realizados WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        domicilio = self.cursor.fetchall()
        return domicilio

    def eliminar_ot(self,valor):
        self.sql = 'DELETE FROM trabajo_serializable WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM trabajo_materiales WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM finalizacion_trabajo WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM trabajos_realizados WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_existe_mac_ot(self, valor):
        verificador = True
        labelDividido = (valor.split())
        if valor=='':
            verificador = False
        for i in range(0, len(labelDividido)):
            var1 = labelDividido[i]
            var1 = ''.join(e for e in str(var1) if e.isalnum())
            self.sql = 'SELECT * from trabajo_serializable WHERE ser_mac="' + var1 + '"'
            self.cursor.execute(self.sql)
            mac = self.cursor.fetchall()
            if not mac:
                verificador = False
                return verificador
        return verificador

    def buscar_ot(self,valor):
        self.sql = 'SELECT t.nro_orden, t.domicilio, t.mov_id, t.fecha_trabajo, t.nom_cliente, ' \
                   't.dni_cliente, t.nro_cliente, c.cod_finalizacion, t.observaciones ' \
                   'FROM trabajos_realizados t JOIN finalizacion_trabajo c using(nro_orden) WHERE nro_orden='+str(valor)
        self.cursor.execute(self.sql)
        trabajos = self.cursor.fetchall()
        test2 = []
        for i in range(0, 1):
            test = []
            tecnicos = []
            for a in range(0, 3):
                test.append(trabajos[i][a])
            fecha = (''.join(e for e in str(trabajos[i][3]) if e.isalnum()))
            self.sql = 'SELECT s.emp_legajo as Leg, (SELECT e.emp_apellido FROM empleados e WHERE e.emp_legajo=Leg) as Apellido, ' \
                       '(SELECT e.emp_nombre FROM empleados e WHERE e.emp_legajo=Leg) as Nombre ' \
                       'FROM salidas_diarias s JOIN trabajos_realizados t ON t.mov_id=s.estado_tecnico ' \
                       'WHERE t.nro_orden=' + str(trabajos[i][0]) + ' AND t.fecha_trabajo=s.fecha GROUP by s.emp_legajo'
            self.cursor.execute(self.sql)
            tecnicos = self.cursor.fetchall()
            tecs = ''
            if len(tecnicos) == 2:
                for i in range(0, len(tecnicos)):
                    tecs = str(tecnicos[i][0]) + ', ' + str(tecnicos[i][1]) + ' ' + str(tecnicos[i][2])
                    test.append(tecs)
            elif len(tecnicos) == 1:
                tecs = str(tecnicos[0][0]) + ', ' + str(tecnicos[0][1]) + ' ' + str(tecnicos[0][2])
                test.append(tecs)
                test.append('')
            for u in range(3, 8):
                test.append(trabajos[0][u])
            test2.append(test)
        return (test2)

    def consulta_patente(self, valor):
        self.valor = valor
        self.sql = 'SELECT * FROM movil WHERE mov_patente = "' + str(self.valor)+'"'
        self.cursor.execute(self.sql)
        consulta_patente = self.cursor.fetchall()
        return consulta_patente

    def consulta_apellido_en_movil(self, valor):
        self.valor = valor
        self.sql = 'SELECT mov_id FROM dupla_movil WHERE emp_legajo=' \
                   '(SELECT e.emp_legajo from empleados e WHERE e.emp_apellido="' + str(self.valor)+'")'
        self.cursor.execute(self.sql)
        consulta_apellido = self.cursor.fetchall()
        return consulta_apellido

    def consulta_apellido(self, valor):
        self.valor = valor
        self.sql = 'SELECT * from empleados WHERE emp_apellido = "' + str(self.valor)+'"'
        self.cursor.execute(self.sql)
        consulta_apellido_s = self.cursor.fetchall()
        return consulta_apellido_s

    def consulta_legajos(self,valor):
        self.valor = valor
        self.sql = 'SELECT emp_legajo from empleados WHERE emp_apellido = "' + str(self.valor) + '"'
        self.cursor.execute(self.sql)
        consulta_legajos = self.cursor.fetchall()
        return consulta_legajos

    def consulta_existen_legajos(self,valor):
        self.valor = valor
        self.sql = 'SELECT * from empleados WHERE emp_legajo = ' + str(self.valor)
        self.cursor.execute(self.sql)
        consulta_e_legajos = self.cursor.fetchall()
        return consulta_e_legajos

    def consulta_apellido_legajo(self,valor):
        if valor=='':
            #si se esta haciendo busqueda por apellido, se anula la funcion
            return
        self.valor = valor
        self.sql = 'SELECT emp_apellido from empleados WHERE emp_legajo = ' + str(self.valor)
        self.cursor.execute(self.sql)
        consulta_a_legajos = self.cursor.fetchall()
        if consulta_a_legajos ==[]:
            return consulta_a_legajos
        else:
            consulta_a_legajos = ''.join(e for e in str(consulta_a_legajos[0]) if e.isalnum())
            return consulta_a_legajos

    def alta_movil(self,valor):
        self.valor=valor
        from datetime import date
        import datetime
        # Creamos el id
        self.sql = 'SELECT MAX(mov_id) from movil'
        self.cursor.execute(self.sql)
        mov_info = self.cursor.fetchall()
        mov_info = ''.join(e for e in str(mov_info[0]) if e.isalnum())
        if mov_info == 'None':
            mov_info = 1
        else:
            mov_info = int(mov_info)
            mov_info += 1
        #se limpia la fecha de vtv y licencia
        #vtv
        vtv=self.valor[2]
        b=len(vtv)
        #para windows
        ano=(vtv[b-4]+vtv[b-3]+vtv[b-2]+vtv[b-1])
        vtv=vtv[0:b-5]
        c=len(vtv)
        mes=''
        dia=''
        if c==3:
            mes='0'+vtv[2]
            dia='0'+vtv[0]
        if c==5:
            mes = vtv[3]+ vtv[4]
            dia = vtv[0]+ vtv[1]
        if c==4:
            if vtv[1]=='/':
                mes = vtv[2] + vtv[3]
                dia='0'+vtv[0]
            elif vtv[2]=='/':
                mes = '0'+ vtv[3]
                dia=vtv[0] + vtv[1]
        vtvok=(ano+mes+dia)
        # licencia
        lic = self.valor[4]
        b = len(lic)
        # for Linux
        # ano = (lic[b - 2] + lic[b - 1])
        # lic = lic[0:b - 3]
        # for Windows
        ano = (lic[b - 4] + lic[b - 3] +lic[b - 2] +lic[b - 1])
        lic = lic[0:b - 5]
        c = len(lic)
        mes = ''
        dia = ''
        if c == 3:
            mes = '0' + lic[2]
            dia = '0' + lic[0]
        if c == 5:
            mes = lic[3] + lic[4]
            dia = lic[0] + lic[1]
        if c == 4:
            if lic[1] == '/':
                mes = lic[2] + lic[3]
                dia = '0' + lic[0]
            elif lic[2] == '/':
                mes = '0' + lic[3]
                dia = lic[0] + lic[1]
        licok = (ano + mes + dia)
        # Transforma la tupla en lista para meter los elementos fijos
        self.valores = []
        self.valores.insert(0, str(mov_info))
        self.valores.insert(1, '"' + str(self.valor[0]) + '"')
        self.valores.insert(2, str(self.valor[1]))
        self.valores.insert(3, '"' + str(vtvok) + '"')
        self.valores.insert(4, str(self.valor[3]))
        self.valores.insert(5, '"' + str(licok) + '"')
        self.valores.insert(6, str(self.valor[5]))
        self.valores = tuple(self.valores)
        # Creamos la query
        self.sql = 'INSERT INTO movil VALUES (' + ",".join(map(str, self.valores)) + ')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        # inertamos el movil en la tabla articulos por movil
        self.sql='SELECT art_id FROM articulo'
        self.cursor.execute(self.sql)
        ids=self.cursor.fetchall()
        if ids:
            for i in range (0, len(ids)):
                idsql=''.join(e for e in str(ids[i]) if e.isalnum())
                self.sql='INSERT INTO articulo_movil VALUES ('+str(mov_info)+', '+idsql+', 0)'
                self.cursor.execute(self.sql)
        self.conexion.commit()

    def modificacion_movil(self):
        self.sql='SELECT * FROM movil'
        self.cursor.execute(self.sql)
        a=self.cursor.fetchall()
        print(a)
        return a

    def movil_por_patente(self,valor):
        self.sql = 'SELECT * from movil WHERE mov_patente= "' + valor +'"'
        self.cursor.execute(self.sql)
        movil = self.cursor.fetchall()
        return movil

    def movil_por_id(self,valor):
        self.sql = 'SELECT * from movil WHERE mov_id= "' + valor +'"'
        self.cursor.execute(self.sql)
        movil = self.cursor.fetchall()
        return movil

    def registra_poliza(self, patente, poliza):
        self.sql = 'UPDATE movil SET mov_seguro= '+poliza+' WHERE mov_patente= "' + patente + '"'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def registra_VTV(self, patente, vtv):
        vtv = ''.join(e for e in str(vtv) if e.isalnum())
        self.sql = 'UPDATE movil SET mov_vtv= ' + vtv + ' WHERE mov_patente= "' + patente + '"'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def registra_verde(self, patente, verde):
        self.sql = 'UPDATE movil SET mov_tarjeta_verde= ' + verde + ' WHERE mov_patente= "' + patente + '"'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def registra_lic(self, patente, lic):
        lic = ''.join(e for e in str(lic) if e.isalnum())
        self.sql = 'UPDATE movil SET mov_licencia= ' + lic + ' WHERE mov_patente= "' + patente + '"'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def registra_legajo(self, patente, legajo):
        self.sql = 'UPDATE movil SET emp_legajo= ' + legajo + ' WHERE mov_patente= "' + patente + '"'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_de_codigos (self):
        self.sql = 'SELECT cod_finalizacion from codigo_finalizacion'
        self.cursor.execute(self.sql)
        codigos_f = self.cursor.fetchall()
        cod_f=[]
        for i in range (0, len(codigos_f)):
            cod_f.append(''.join(e for e in str(codigos_f[i]) if e.isalnum()))
        return cod_f

    def consulta_de_moviles (self):
        self.sql = 'SELECT mov_id from movil'
        self.cursor.execute(self.sql)
        moviles = self.cursor.fetchall()
        consul_moviles=[]
        for i in range (0, len(moviles)):
            consul_moviles.append(''.join(e for e in str(moviles[i]) if e.isalnum()))
        return consul_moviles

    def consulta_de_legajos (self):
        self.sql = 'SELECT emp_legajo from empleados'
        self.cursor.execute(self.sql)
        legajos = self.cursor.fetchall()
        consul_legajos = []
        for i in range(0, len(legajos)):
            consul_legajos.append(''.join(e for e in str(legajos[i]) if e.isalnum()))
        return consul_legajos

    def consulta_diaria (self):
        #buscamos la fecha de la ultima salida registrada
        self.sql = 'SELECT MAX(Fecha) from salidas_diarias'
        self.cursor.execute(self.sql)
        ultimo_dia = self.cursor.fetchall()
        ultimo_dia=ultimo_dia[0][0]
        ultimo_dia=(''.join(e for e in str(ultimo_dia) if e.isalnum()))
        #buscamos los datos con la fecha obtenida
        self.sql = 'SELECT e.emp_apellido, s.emp_legajo, s.estado_tecnico, s.Fecha from salidas_diarias s ' \
                   'JOIN empleados e using(emp_legajo) WHERE Fecha= ' + str(ultimo_dia)+' GROUP BY emp_legajo ORDER BY estado_tecnico '
        self.cursor.execute(self.sql)
        salidas = self.cursor.fetchall()
        return salidas

    def busqueda_salida_diaria (self,valor):
        dia=valor
        self.sql = 'SELECT e.emp_apellido, s.emp_legajo, s.estado_tecnico, s.Fecha from salidas_diarias s ' \
                   'JOIN empleados e using(emp_legajo) WHERE Fecha= ' + str(dia)+' GROUP BY emp_legajo ORDER BY estado_tecnico '
        self.cursor.execute(self.sql)
        salidas = self.cursor.fetchall()
        return salidas

    def consulta_diaria_tec (self,valor):
        import datetime
        hoy= datetime.date.today()
        ya = ('{:%Y%m%d}'.format(hoy))
        #buscamos la fecha de la ultima salida registrada
        self.sql = 'SELECT * from salidas_diarias where emp_legajo= '+str(valor)+' and fecha='+ya
        self.cursor.execute(self.sql)
        tecnico_en_salida = self.cursor.fetchall()
        return(tecnico_en_salida)

    def regritra_cambio_salida(self,valor):
        self.valor = valor
        fecha=(''.join(e for e in str(self.valor[0]) if e.isalnum()))
        self.valor[0]=fecha
        registracambio = []
        registracambio.append(str(self.valor[0]))
        registracambio.append(str(self.valor[1]))
        registracambio.append('"'+str(self.valor[2])+'"')
        self.sql = 'INSERT INTO salidas_diarias (Fecha, emp_legajo, estado_tecnico) VALUES (' + ",".join(map(str, registracambio)) + ')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def regritra_cambio_salida_registrada(self,valor):
        self.valor = valor
        fecha=(''.join(e for e in str(self.valor[0]) if e.isalnum()))
        registracambio = []
        registracambio.append(str(self.valor[1]))
        registracambio.append('"'+str(self.valor[2])+'"')
        self.sql = 'UPDATE salidas_diarias SET estado_tecnico = ' + str(registracambio[1]) +' WHERE Fecha='+fecha+' AND emp_Legajo ='  + str(registracambio[0])
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def actualizacion_duplas(self):
        self.sql='SELECT MAX(fecha) from salidas_diarias'
        self.cursor.execute(self.sql)
        fechamax = self.cursor.fetchall()
        fechamax=(fechamax[0])
        fecha = (''.join(e for e in str(fechamax) if e.isalnum()))
        fecha = fecha[12:20]
        self.sql='SELECT emp_legajo, estado_tecnico from salidas_diarias WHERE fecha='+fecha
        self.cursor.execute(self.sql)
        datosduplas = self.cursor.fetchall()
        self.sql='DELETE FROM dupla_movil'
        self.cursor.execute(self.sql)
        for i in range(0, len(datosduplas)):
            if len(datosduplas[i][1])<5:
                self.sql = 'INSERT INTO dupla_movil VALUES (' + ",".join(map(str, datosduplas[i])) + ')'
                self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_tecnico_en_movil(self,valor):
        # buscamos la fecha de la ultima salida registrada
        self.sql = 'SELECT MAX(Fecha) from salidas_diarias'
        self.cursor.execute(self.sql)
        ultimo_dia = self.cursor.fetchall()
        if str(ultimo_dia)=='[(None,)]':
            return
        ultimo_dia = (''.join(e for e in str(ultimo_dia) if e.isalnum()))
        ultimo_dia = ultimo_dia[12:20]
        # buscamos los datos con la fecha obtenida
        self.sql = 'SELECT COUNT(estado_tecnico) from salidas_diarias WHERE estado_tecnico= "' + valor[2]+'" AND Fecha=' + str(ultimo_dia)
        self.cursor.execute(self.sql)
        count_movil = self.cursor.fetchall()
        count_movil = (''.join(e for e in str(count_movil) if e.isalnum()))
        valorretorno=0
        if count_movil=='2' and int(valor[2])<5:
            valorretorno=1
            self.sql = 'SELECT emp_legajo from salidas_diarias WHERE fecha ='+ str(ultimo_dia)+ ' and estado_tecnico = "' + valor[2]+'"'
            self.cursor.execute(self.sql)
            tec_in_movil = self.cursor.fetchall()
            tec_in_movil2=[]
            for i in range(0, len(tec_in_movil)):
                tec_in_movil2.append(''.join(e for e in str(tec_in_movil[i]) if e.isalnum()))
            for i in range (0, len(tec_in_movil)):
                if tec_in_movil2[i]==valor[1]:
                    valorretorno=2
        return valorretorno

    def registra_salida_modificada(self):
        import datetime
        hoy = datetime.date.today()
        ya = ('{:%Y%m%d}'.format(hoy))
        self.sql = 'SELECT emp_legajo from salidas_diarias where fecha= ' + ya
        self.cursor.execute(self.sql)
        tecnico_en_salida = self.cursor.fetchall()
        tec_in_movil2 = []
        for i in range(0, len(tecnico_en_salida)):
            tec_in_movil2.append(''.join(e for e in str(tecnico_en_salida[i]) if e.isalnum()))
        test=''
        for i in range (0, len(tec_in_movil2)):
            test=test+' AND emp_legajo = '+tec_in_movil2[i]
        self.sql = 'SELECT emp_legajo, estado_tecnico from salidas_diarias WHERE Fecha ='+ya+test
        self.cursor.execute(self.sql)
        tecnico_en_salida2 = self.cursor.fetchall()
        # obtener el dia anterior al ultimo agegado
        self.sql = 'SELECT DISTINCT fecha from salidas_diarias ORDER BY fecha DESC LIMIT 1,1'
        self.cursor.execute(self.sql)
        fecha_anterior = self.cursor.fetchall()
        fecha_anterior = (''.join(e for e in str(fecha_anterior) if e.isalnum()))
        fecha_anterior = fecha_anterior[12:20]
        test2 = ''
        for i in range(0, len(tec_in_movil2)):
            test2 = test2 + ' AND emp_legajo = ' + tec_in_movil2[i]
        self.sql = 'SELECT emp_legajo, estado_tecnico from salidas_diarias WHERE Fecha ' \
                   '= ' + fecha_anterior +' AND emp_legajo NOT IN (SELECT emp_legajo from ' \
                                          'salidas_diarias WHERE Fecha = ' + fecha_anterior + test2+')'
        self.cursor.execute(self.sql)
        tecnico_en_salida22 = self.cursor.fetchall()
        for i in range (0, len(tecnico_en_salida22)):
            self.sql = 'INSERT INTO salidas_diarias (fecha, emp_legajo, estado_tecnico) VALUES ' \
                       '(' + ya+', '+str(tecnico_en_salida22[i][0]) +', "'+str(tecnico_en_salida22[i][1])+ '")'
            self.cursor.execute(self.sql)
            self.conexion.commit()
        self.actualizacion_duplas()
        self.registrar_ausentes()

    def verifica_modificacion(self):
        import datetime
        hoy=datetime.date.today()
        ya=('{:%Y%m%d}'.format(hoy))
        self.sql='SELECT * from salidas_diarias WHERE fecha='+ya
        self.cursor.execute(self.sql)
        valorretorna=self.cursor.fetchall()
        return  valorretorna

    def verificar_modificacion_cargada(self):
        import datetime
        hoy=datetime.date.today()
        ya=('{:%y%m%d}'.format(hoy))
        self.sql='SELECT COUNT(emp_legajo) FROM salidas_diarias WHERE fecha='+ya
        self.cursor.execute(self.sql)
        cantidadHoy=self.cursor.fetchall()
        print(cantidadHoy)
        self.sql='SELECT COUNT(emp_legajo) FROM empleados'
        self.cursor.execute(self.sql)
        cantidadEmpleados= self.cursor.fetchall()
        print(cantidadEmpleados)
        verificador=False
        cantidadHoy = ''.join(e for e in str(cantidadHoy) if e.isalnum())
        cantidadEmpleados = ''.join(e for e in str(cantidadEmpleados) if e.isalnum())
        if str(cantidadHoy)==str(cantidadEmpleados):
            verificador=True
        return verificador

    def registra_salida_igual_anterior(self):
        self.sql = 'SELECT DISTINCT MAX(fecha) from salidas_diarias'
        self.cursor.execute(self.sql)
        fecha_anterior = self.cursor.fetchall()
        fecha_anterior = (''.join(e for e in str(fecha_anterior) if e.isalnum()))
        fecha_anterior = fecha_anterior[12:20]
        self.sql = 'SELECT s.emp_legajo, s.estado_tecnico from salidas_diarias s WHERE Fecha='+ fecha_anterior
        self.cursor.execute(self.sql)
        tecnico_en_salida = self.cursor.fetchall()
        import datetime
        hoy = datetime.date.today()
        hoy = ('{:%Y%m%d}'.format(hoy))
        for i in range(0, len(tecnico_en_salida)):
            self.sql = 'INSERT INTO salidas_diarias (fecha, emp_legajo, estado_tecnico) VALUES ' \
                       '(' + hoy + ', ' + str(tecnico_en_salida[i][0]) + ', "' + str(tecnico_en_salida[i][1]) + '")'
            self.cursor.execute(self.sql)
            self.conexion.commit()
        self.actualizacion_duplas()
        self.registrar_ausentes()

    def registrar_denuncia(self,valor):
        self.sql='INSERT INTO denuncias (den_numero_folio, den_numero_acta, den_numero_legajo, den_comisaria, ' \
                 'den_fecha_siniestro, den_fecha_ingreso, mov_id) VALUES  (' + ",".join(map(str, valor)) + ')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_art(self):
        self.sql='SELECT art_id from articulo GROUP BY art_id'
        self.cursor.execute(self.sql)
        art=self.cursor.fetchall()
        consul_art = []
        for i in range(0, len(art)):
            consul_art.append(''.join(e for e in str(art[i]) if e.isalnum()))
        return consul_art

    def separar_cantidad(self,valor,acta):
        self.sql='SELECT MAX(den_id) from denuncias WHERE den_numero_acta='+acta
        self.cursor.execute(self.sql)
        idDenuncia=self.cursor.fetchall()
        #dividimos al label obtenido por espacios
        labelDividido=(valor.split( ))
        codCant=[]
        #creamos la variable control para que ingrese a codCant cada codigo con su cantidad
        control=0
        #creamos una tupla para agregar cada codigo con su cantidad
        codCantIndividual=[]
        for i in range(0,len(labelDividido)):
            if labelDividido[i]!='Art:' or labelDividido[i]!='Cant:':
                var1=labelDividido[i]
                var1 = ''.join(e for e in str(var1) if e.isalnum())
                #se verifica si el objeto obtenido es numero
                if var1.isnumeric():
                    control += 1
                    codCantIndividual.append(var1)
                    #se verifica si ya estan los pares de datos para mandar
                    #a la tupla pincipal
                    if control==2:
                        codCant2=[]
                        idDenuncia = ''.join(e for e in str(idDenuncia) if e.isalnum())
                        codCant2.append(idDenuncia)
                        codCant2.append(codCantIndividual[0])
                        codCant2.append(codCantIndividual[1])
                        codCant.append(codCant2)
                        control=0
                        codCantIndividual=[]
        for i in range (0, len(codCant)):
            self.sql='INSERT INTO detalle_denuncia_materiales VALUES ('+ ",".join(map(str, codCant[i])) + ')'
            self.cursor.execute(self.sql)
        self.conexion.commit()

    def agergar_denuncia_emp(self, valor, tec1, tec2):
        self.sql = 'SELECT MAX(den_id) from denuncias WHERE den_numero_acta=' + valor
        self.cursor.execute(self.sql)
        idDenuncia = self.cursor.fetchall()
        emp1=[]
        idDenuncia = ''.join(e for e in str(idDenuncia) if e.isalnum())
        emp1.append(idDenuncia)
        emp1.append(tec1)
        self.sql = 'INSERT INTO detalle_denuncia_empleados VALUES (' + ",".join(map(str, emp1)) + ')'
        self.cursor.execute(self.sql)
        if tec2 != '':
            emp2 = []
            emp2.append(idDenuncia)
            emp2.append(tec2)
            self.sql = 'INSERT INTO detalle_denuncia_empleados VALUES (' + ",".join(map(str, emp2)) + ')'
            self.cursor.execute(self.sql)
            self.conexion.commit()
        self.conexion.commit()

    def agregar_denuncia_mac(self, valor, mac):
        self.sql = 'SELECT MAX(den_id) from denuncias WHERE den_numero_acta=' + valor
        self.cursor.execute(self.sql)
        idDenuncia = self.cursor.fetchall()
        labelDividido = (mac.split())
        for i in range(0, len(labelDividido)):
            var1 = labelDividido[i]
            var1 = ''.join(e for e in str(var1) if e.isalnum())
            self.sql = 'SELECT * from serializable WHERE ser_mac="' + var1 + '"'
            self.cursor.execute(self.sql)
            verificadormac = self.cursor.fetchall()
            if verificadormac:
                mac1=[]
                idDenuncia = ''.join(e for e in str(idDenuncia) if e.isalnum())
                mac1.append(idDenuncia)
                mac1.append(var1)
                self.sql = 'INSERT INTO detalle_denuncia_serializables VALUES (' + ",".join(map(str, mac1)) + ')'
                self.cursor.execute(self.sql)
                import datetime
                hoy = datetime.date.today()
                hoy = ('{:%Y%m%d}'.format(hoy))
                var1 = '"' + var1 + '"'
                self.sql = 'INSERT INTO historial_serializables (ser_mac, ser_estado, ser_fecha_ultimo_estado)' \
                           'VALUES ('+var1+', 5, '+hoy+')'
                self.cursor.execute(self.sql)
            self.conexion.commit()

    def consulta_mac(self, valor):
        verificador=True
        labelDividido = (valor.split())
        for i in range(0, len(labelDividido)):
            var1 = labelDividido[i]
            var1 = ''.join(e for e in str(var1) if e.isalnum())
            self.sql = 'SELECT * from serializable WHERE ser_mac="' + var1 + '"'
            self.cursor.execute(self.sql)
            mac = self.cursor.fetchall()
            if not mac:
                verificador=False
                return verificador
        return verificador

    def borrar(self):
        self.sql='DELETE FROM `detalle_denuncia_empleados` WHERE den_id = 10'
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM `detalle_denuncia_materiales` WHERE den_id = 10'
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM `detalle_denuncia_serializables` WHERE den_id= 10'
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM `denuncias` WHERE `denuncias`.`den_id` = 10'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_denuncia(self):
        self.sql='SELECT  d.den_id, d.den_numero_folio, d.den_numero_acta, d.den_numero_legajo, d.den_comisaria, d.mov_id, d.den_fecha_siniestro, d.den_fecha_ingreso FROM denuncias d'
        self.cursor.execute(self.sql)
        denuncias=self.cursor.fetchall()
        denuncias2=[]
        for i in range(0, len(denuncias)):
            agregar=[]
            agregar.append(denuncias[i])
            self.sql = 'SELECT emp_legajo from detalle_denuncia_empleados where den_id='+str(denuncias[i][0])
            self.cursor.execute(self.sql)
            empleados = self.cursor.fetchall()
            emp1 = empleados[0]
            emp1 = ''.join(e for e in str(emp1) if e.isalnum())
            agregar.append(emp1)
            if len(empleados)==1:
                agregar.append('')
            else:
                emp2 = empleados[1]
                emp2 = ''.join(e for e in str(emp2) if e.isalnum())
                agregar.append(emp2)
            self.sql = 'SELECT ser_mac from detalle_denuncia_serializables where den_id='+str(denuncias[i][0])
            self.cursor.execute(self.sql)
            macs = self.cursor.fetchall()
            mac=''
            for a in range(0, len(macs)):
                maca=str(macs[a])
                maca = ''.join(e for e in str(maca) if e.isalnum())
                mac=str(mac)+' '+maca
            agregar.append(mac)
            self.sql = 'SELECT art_id, det_den_mat_cantidad from detalle_denuncia_materiales where den_id='+str(denuncias[i][0])
            self.cursor.execute(self.sql)
            mats = self.cursor.fetchall()
            mat = ''
            for a in range(0, len(mats)):
                mat=mat+'Art: '+str(mats[a][0])+', Cant: '+str(mats[a][1])+'. '
            agregar.append(mat)
            denuncias2.append(agregar)
        denuncias3=[]
        for i in range(0, len(denuncias2)):
            agregar2=[]
            agregar2.append(denuncias2[i][0][0])
            agregar2.append(denuncias2[i][0][1])
            agregar2.append(denuncias2[i][0][2])
            agregar2.append(denuncias2[i][0][3])
            agregar2.append(denuncias2[i][0][4])
            agregar2.append(denuncias2[i][0][5])
            agregar2.append(denuncias2[i][1])
            agregar2.append(denuncias2[i][2])
            agregar2.append(denuncias2[i][0][6])
            agregar2.append(denuncias2[i][0][7])
            agregar2.append(denuncias2[i][3])
            agregar2.append(denuncias2[i][4])
            denuncias3.append(agregar2)
        return denuncias3

    def busqueda_denuncia(self, valor):
        if len(str(valor))<5:
            self.sql='SELECT den_id from detalle_denuncia_empleados where emp_legajo='+str(valor)
            self.cursor.execute(self.sql)
            idd=self.cursor.fetchall()
            idd = ''.join(e for e in str(idd) if e.isalnum())
            self.sql = 'SELECT  d.den_id, d.den_numero_folio, d.den_numero_acta, d.den_numero_legajo, ' \
                       'd.den_comisaria, d.mov_id, d.den_fecha_siniestro, d.den_fecha_ingreso FROM denuncias d where d.den_id='+str(idd)
            self.cursor.execute(self.sql)
            denuncias = self.cursor.fetchall()
            denuncias2 = []
            for i in range(0, len(denuncias)):
                agregar = []
                agregar.append(denuncias[i])
                self.sql = 'SELECT emp_legajo from detalle_denuncia_empleados where den_id=' + str(denuncias[i][0])
                self.cursor.execute(self.sql)
                empleados = self.cursor.fetchall()
                emp1 = empleados[0]
                emp1 = ''.join(e for e in str(emp1) if e.isalnum())
                agregar.append(emp1)
                if len(empleados) == 1:
                    agregar.append('')
                else:
                    emp2 = empleados[1]
                    emp2 = ''.join(e for e in str(emp2) if e.isalnum())
                    agregar.append(emp2)
                self.sql = 'SELECT ser_mac from detalle_denuncia_serializables where den_id=' + str(denuncias[i][0])
                self.cursor.execute(self.sql)
                macs = self.cursor.fetchall()
                mac = ''
                for a in range(0, len(macs)):
                    maca = str(macs[a])
                    maca = ''.join(e for e in str(maca) if e.isalnum())
                    mac = str(mac) + ' ' + maca
                agregar.append(mac)
                self.sql = 'SELECT art_id, det_den_mat_cantidad from detalle_denuncia_materiales where den_id=' + str(
                    denuncias[i][0])
                self.cursor.execute(self.sql)
                mats = self.cursor.fetchall()
                mat = ''
                for a in range(0, len(mats)):
                    mat = mat + 'Art: ' + str(mats[a][0]) + ', Cant: ' + str(mats[a][1]) + '. '
                agregar.append(mat)
                denuncias2.append(agregar)
            denuncias3 = []
            for i in range(0, len(denuncias2)):
                agregar2 = []
                agregar2.append(denuncias2[i][0][0])
                agregar2.append(denuncias2[i][0][1])
                agregar2.append(denuncias2[i][0][2])
                agregar2.append(denuncias2[i][0][3])
                agregar2.append(denuncias2[i][0][4])
                agregar2.append(denuncias2[i][0][5])
                agregar2.append(denuncias2[i][1])
                agregar2.append(denuncias2[i][2])
                agregar2.append(denuncias2[i][0][6])
                agregar2.append(denuncias2[i][0][7])
                agregar2.append(denuncias2[i][3])
                agregar2.append(denuncias2[i][4])
                denuncias3.append(agregar2)
            return denuncias3
        else:
            self.sql = 'SELECT den_id from detalle_denuncia_serializables where ser_mac=' + str(valor)
            self.cursor.execute(self.sql)
            idd = self.cursor.fetchall()
            idd = ''.join(e for e in str(idd) if e.isalnum())
            self.sql = 'SELECT  d.den_id, d.den_numero_folio, d.den_numero_acta, d.den_numero_legajo, ' \
                       'd.den_comisaria, d.mov_id, d.den_fecha_siniestro, d.den_fecha_ingreso FROM denuncias d where d.den_id=' + str(idd)
            self.cursor.execute(self.sql)
            denuncias = self.cursor.fetchall()
            denuncias2 = []
            for i in range(0, len(denuncias)):
                agregar = []
                agregar.append(denuncias[i])
                self.sql = 'SELECT emp_legajo from detalle_denuncia_empleados where den_id=' + str(denuncias[i][0])
                self.cursor.execute(self.sql)
                empleados = self.cursor.fetchall()
                emp1 = empleados[0]
                emp1 = ''.join(e for e in str(emp1) if e.isalnum())
                agregar.append(emp1)
                if len(empleados) == 1:
                    agregar.append('')
                else:
                    emp2 = empleados[1]
                    emp2 = ''.join(e for e in str(emp2) if e.isalnum())
                    agregar.append(emp2)
                self.sql = 'SELECT ser_mac from detalle_denuncia_serializables where den_id=' + str(denuncias[i][0])
                self.cursor.execute(self.sql)
                macs = self.cursor.fetchall()
                mac = ''
                for a in range(0, len(macs)):
                    maca = str(macs[a])
                    maca = ''.join(e for e in str(maca) if e.isalnum())
                    mac = str(mac) + ' ' + maca
                agregar.append(mac)
                self.sql = 'SELECT art_id, det_den_mat_cantidad from detalle_denuncia_materiales where den_id=' + str(
                    denuncias[i][0])
                self.cursor.execute(self.sql)
                mats = self.cursor.fetchall()
                mat = ''
                for a in range(0, len(mats)):
                    mat = mat + 'Art: ' + str(mats[a][0]) + ', Cant: ' + str(mats[a][1]) + '. '
                agregar.append(mat)
                denuncias2.append(agregar)
            denuncias3 = []
            for i in range(0, len(denuncias2)):
                agregar2 = []
                agregar2.append(denuncias2[i][0][0])
                agregar2.append(denuncias2[i][0][1])
                agregar2.append(denuncias2[i][0][2])
                agregar2.append(denuncias2[i][0][3])
                agregar2.append(denuncias2[i][0][4])
                agregar2.append(denuncias2[i][0][5])
                agregar2.append(denuncias2[i][1])
                agregar2.append(denuncias2[i][2])
                agregar2.append(denuncias2[i][0][6])
                agregar2.append(denuncias2[i][0][7])
                agregar2.append(denuncias2[i][3])
                agregar2.append(denuncias2[i][4])
                denuncias3.append(agregar2)
            return denuncias3

    def consulta_existe_mac(self, valor):
        self.sql='SELECT * from detalle_denuncia_serializables where ser_mac="'+str(valor)+'"'
        self.cursor.execute(self.sql)
        mac=self.cursor.fetchall()
        return mac

    def consulta_ausentes(self):
        self.sql = 'SELECT * from ausentes'
        self.cursor.execute(self.sql)
        ausen = self.cursor.fetchall()
        return ausen

    def consulta_ausentes_legajo(self, valor):
        self.sql = 'SELECT * from ausentes where emp_legajo='+str(valor)
        self.cursor.execute(self.sql)
        ausen = self.cursor.fetchall()
        return ausen

    def registrar_justificacion(self, valor, legajo):
        if valor=='SI':
            self.sql='UPDATE ausentes SET aus_justificacion="SI" where emp_legajo=' + str(legajo)
            self.cursor.execute(self.sql)
            # self.conexion.commit()
        if valor=='NO':
            self.sql = 'UPDATE ausentes SET aus_justificacion="NO" where emp_legajo=' + str(legajo)
            self.cursor.execute(self.sql)
        self.conexion.commit()

    def registrar_ausentes(self):
        self.sql = 'SELECT MAX(fecha) from salidas_diarias'
        self.cursor.execute(self.sql)
        fechamax = self.cursor.fetchall()
        fechamax = (fechamax[0])
        fecha = (''.join(e for e in str(fechamax) if e.isalnum()))
        fecha = fecha[12:20]
        self.sql = 'SELECT emp_legajo, estado_tecnico from salidas_diarias WHERE fecha=' + fecha
        self.cursor.execute(self.sql)
        ausentes = self.cursor.fetchall()
        salidas = []
        for i in range(0, len(ausentes)):
            if (len(ausentes[i][1]) > 4):
                if (ausentes[i][1] != 'Supervisor') and (ausentes[i][1] != 'Materiales') and (ausentes[i][1] != 'Herramientas') and (ausentes[i][1] != 'Calidad') and (ausentes[i][1] != 'Serializable') and (ausentes[i][1] != 'En Base'):
                    salidas.append(ausentes[i])
        for i in range (0, len(salidas)):
            self.sql = 'INSERT INTO ausentes (emp_legajo, aus_fecha) VALUES (' + str(salidas[i][0])+', '+ str(fecha)+ ')'
            self.cursor.execute(self.sql)
        self.conexion.commit()

    def agregar_descuento(self,valor):
        self.sql='INSERT INTO descuentos (emp_legajo, des_importe, des_fecha) VALUES(' + ",".join(map(str, valor)) + ')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_descuentos(self):
        self.sql = 'SELECT emp_legajo, des_importe, des_fecha FROM descuentos'
        self.cursor.execute(self.sql)
        desc=self.cursor.fetchall()
        return desc

    def busqueda_descuentos(self, valor):
        self.sql = 'SELECT emp_legajo, des_importe, des_fecha FROM descuentos where emp_legajo='+str(valor)
        self.cursor.execute(self.sql)
        desc = self.cursor.fetchall()
        return desc

    def consulta_ot2(self):
        self.sql='SELECT nro_orden from trabajos_realizados'
        self.cursor.execute(self.sql)
        ot=self.cursor.fetchall()
        ots=[]
        for i in range (0, len(ot)):
            ot_actual = ''.join(e for e in str(ot[i]) if e.isalnum())
            ots.append(ot_actual)
        return ots

    def busqueda_ot_control(self,valor):
        self.sql='SELECT * from trabajos_controlados where nro_orden='+str(valor)
        self.cursor.execute(self.sql)
        ot=self.cursor.fetchall()
        return ot

    def agergar_controlado(self, valor):
        self.sql = 'INSERT INTO trabajos_controlados VALUES (' + ",".join(map(str, valor)) + ')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_control(self):
        self.sql = 'SELECT * from trabajos_controlados'
        self.cursor.execute(self.sql)
        ot = self.cursor.fetchall()
        return ot

    def consulta_ot_controlado(self):
        self.sql='SELECT nro_orden from trabajos_controlados'
        self.cursor.execute(self.sql)
        ot=self.cursor.fetchall()
        ots=[]
        for i in range (0, len(ot)):
            ot_actual = ''.join(e for e in str(ot[i]) if e.isalnum())
            ots.append(ot_actual)
        return ots

    def consulta_existe_controlado(self,valor):
        self.sql='SELECT * from trabajos_controlados where nro_orden='+str(valor)
        self.cursor.execute(self.sql)
        ots=self.cursor.fetchall()
        return ots

    def borrar_ot_contol(self,valor):
        self.sql = 'DELETE FROM trabajos_controlados WHERE nro_orden=' + str(valor)
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def registrar_horario(self,valor):
        self.sql = 'INSERT INTO entradas_salidas (emp_legajo, eys_fecha, eys_entrada, eys_salida) VALUES(' + ",".join(map(str, valor)) + ')'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def modificar_horario(self,valor):
        self.sql = 'UPDATE entradas_salidas SET eys_entrada='+str(valor[2])+' where emp_legajo='+str(valor[0])+' AND eys_fecha='+str(valor[1])
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE entradas_salidas SET eys_salida='+str(valor[3])+' where emp_legajo='+str(valor[0]) +' AND eys_fecha='+str(valor[1])
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_horarios(self):
        self.sql ='SELECT emp_legajo, eys_fecha, eys_entrada, eys_salida from entradas_salidas order by eys_fecha DESC'
        self.cursor.execute(self.sql)
        hora=self.cursor.fetchall()
        return hora

    def consulta_horarios_empleado(self,legajo):
        self.sql = 'SELECT emp_legajo, eys_fecha, eys_entrada, eys_salida from entradas_salidas where emp_legajo='+str(legajo)
        self.cursor.execute(self.sql)
        hora = self.cursor.fetchall()
        return hora

    def consulta_horarios_empleado_existente(self,legajo, fecha):
        self.sql = 'SELECT * from entradas_salidas where emp_legajo='+str(legajo)+' and eys_fecha='+str(fecha)
        self.cursor.execute(self.sql)
        hora = self.cursor.fetchall()
        return hora

a=Calidad()
# b=a.alta_movil((['1111111', '3212', '27/10/2021', '12323', '27/10/2022', '124']))

#Buscar trbajos realizados # -----------------------------------------------------------------
#modiicar alta movil para q ingerse legajos existentes #--------------------------------------
#modificar tabla movil, con legajo titular #--------------------------------------------------
#editar trabajos visitados #------------------------------------------------------------------
#validar fechas modificacion movil #----------------------------------------------------------
#constinuar denuncia #------------------------------------------------------------------------
#crear tabla detalle_denuncia_legajos #-------------------------------------------------------
#actualizar datos necesarios en denuncias #---------------------------------------------------
# denuncias: agergar campo movil #------------------------------------------------------------
#agregar el id de denuncia a codCant, asi queda listo para agergar #--------------------------
#ageregar id denuncia auto_increemtnt #-------------------------------------------------------
#mostrar consulta de denuncias #--------------------------------------------------------------
# consumo de serializables (verificar tabla) #------------------------------------------------
# consumo de materiales - agregar campo en tabla o buscar forma #-----------------------------
# registro de ausencia: quitar tecnico, agegar fecha, quitar motivo #-------------------------
# que hacer con los registros de ausencia? #--------------------------------------------------
# tabla nueva legajo, fecha, justificado o no? #----------------------------------------------
# modificar registro de moviles #-------------------------------------------------------------
# descuento por extravio: quitar tecnico, agergar fecha de extravio, quitar motivo #----------
# tabla de descuento por extravios? legajo, fecha, importe #----------------------------------
# trabajos controlaos #-----------------------------------------------------------------------
# entrada y salida #--------------------------------------------------------------------------
# modificacio de stack
# agregar las querys para eliminar trabajo visitado #-----------------------------------------
# agregar boton consulta personal #-----------------------------------------------------------

# ausencias verificar existen #---------------------------------------------------------------
# virificar horario#--------------------------------------------------------------------------

#buscartrabajo------------

#pasar boton salidas diarias a presentismo

# supervisor:
# mostrar stock
# materuales no funciona (el unico q andaba)

#-------------set fecha en ventana
# import datetime
# hoy = datetime.datetime.today()
# self.ca_input_1.setDate(QtCore.QDate(hoy))

# -------------validar fecha futura update
# import datetime
#         hoy = datetime.datetime.today()
#         valorfecha = (self.ui.ca_input_1.date())
#         if valorfecha > hoy:
#             QMessageBox.about(self, "Error", "No puede ingresar fechas futuras")
#             return
#         valorfecha=(valorfecha.toString('yyMMdd'))
#
# ------------limpiar objeto
# cant_actual = ''.join(e for e in str(cant_actual[0]) if e.isalnum())
#
# -------------ingresar tupla en query
# self.sql = 'INSERT INTO trabajos_realizados VALUES (' + ",".join(map(str, registrabajo)) + ')'

# --------------ayer
# from datetime import timedelta
# import datetime
# ayer = datetime.date.today() - timedelta(1)
# ayer = ('{:%Y%m%d}'.format(ayer))
a=a.consulta_diaria()