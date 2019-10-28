import mysql.connector
from datetime import date, timedelta

class ABM_herramientas:
    def __init__(self):
        self.conexion = mysql.connector.connect(user = 'root',password = '',host = 'localhost',database = 'ScaBox')
        self.cursor = self.conexion.cursor()

    def baja_herramientas(self, identificador):
        self.identificador=identificador
        self.sql = 'DELETE FROM articulo WHERE art_id = ' + identificador +' AND tip_id=1'
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def alta_herramientas(self, valores):
        from datetime import date
        #Transforma fecha para meterla en bd
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        self.valores = valores
        # Creamos el id
        self.sql = 'SELECT MAX(art_id) from articulo'
        self.cursor.execute(self.sql)
        art_info = self.cursor.fetchall()
        art_info = ''.join(e for e in str(art_info[0]) if e.isalnum())
        if art_info == 'None':
            art_info = 1
        else:
            art_info = int(art_info)
            art_info += 1
        #Transforma la tupla en lista para meter los elementos fijos
        self.valores = list(self.valores)
        self.valores.insert(0,str(art_info))
        self.valores[1] = '"' + str(valores[0]) + '"'
        self.valores.insert(2, today)
        self.valores.insert(3, str('1'))
        self.valores = tuple(self.valores)
        #Creamos la query
        self.sql = 'INSERT INTO articulo VALUES (' + ",".join(map(str, self.valores)) + ')'
        #Ejecutamos la query
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def consulta_herramientas(self, valor):
        self.valor=valor
        self.sql= 'SELECT * FROM articulo WHERE art_id = ' + self.valor +' AND tip_id = 1'
        self.cursor.execute(self.sql)
        a=self.cursor.fetchall()
        print(a)

    def modificacion_herramientas(self, valor):
        self.valor=valor
        #Obtenemos la cantidad actual y creamos la variable modificada
        self.sql = 'SELECT art_cantidad FROM articulo WHERE art_id = ' + self.valor[0] + ' AND tip_id = 1'
        self.cursor.execute(self.sql)
        cant_actual = self.cursor.fetchall()
        cant_actual = ''.join(e for e in str(cant_actual[0]) if e.isalnum())
        cant_actual = int(cant_actual)
        cant_ingresada = int(self.valor[1])
        cantidad=cant_actual+cant_ingresada
        #Obtenemos fecha actual de ingreso
        from datetime import date
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        #Ejecutamos las querys de modificacion en DB
        self.sql = 'UPDATE articulo SET art_fecha_ultimo_ingreso ' \
                   '= ' + today + ' WHERE art_id = ' + self.valor[0]+' AND tip_id=1'
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE articulo SET art_cantidad ' \
                   '= ' + str(cantidad) + ' WHERE art_id = ' + self.valor[0] + ' AND tip_id=1'
        self.cursor.execute(self.sql)
        self.conexion.commit()

class ABM_serializables:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def baja_serializables(self, identificador):
        self.identificador = identificador
        print(self.identificador)
        # Obtiene el id del tipo de serializable
        self.sql2 = 'SELECT s.tip_id FROM serializable s WHERE s.ser_mac = ' \
                    '"' + str(identificador) + '"'
        self.cursor.execute(self.sql2)
        tipo = self.cursor.fetchall()
        print(tipo)
        self.sql4 = 'DELETE FROM historial_serializables WHERE ser_mac = "' + str(identificador)+'"'
        self.cursor.execute(self.sql4)
        self.conexion.commit()
        self.sql = 'DELETE FROM serializable WHERE ser_mac = "' + str(identificador)+'"'
        self.cursor.execute(self.sql)
        self.conexion.commit()
        self.sql3 = 'UPDATE tipo_serializable SET cant_serializable = (cant_serializable - 1) ' \
                   'WHERE tipo_serializable = "' + str(tipo[0][0]) + '"'
        self.cursor.execute(self.sql3)
        self.conexion.commit()

    def alta_serializables(self, valores):
        from datetime import date
        # Transforma fecha para meterla en bd
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        self.valores = valores
        print(self.valores)
        # Obtiene el id del tipo de serializable
        self.sql2 = 'SELECT ts.tipo_serializable FROM tipo_serializable ts WHERE ts.desc_serializable = "'+str(valores[1])+'"'
        self.cursor.execute(self.sql2)
        tipo = self.cursor.fetchall()
        # Creamos la query
        self.sql = 'INSERT INTO serializable VALUES ("'+str(self.valores[0])+'","'+str(today)+'", '+str(tipo[0][0])+')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        self.conexion.commit()
        self.sql3 = 'UPDATE tipo_serializable SET cant_serializable = (cant_serializable + 1) ' \
                   'WHERE tipo_serializable = "' + str(tipo[0][0]) + '"'
        self.cursor.execute(self.sql3)
        self.conexion.commit()
        self.sql4 = 'INSERT INTO historial_serializables(ser_mac, ser_estado, ser_fecha_ultimo_estado) ' \
                    'VALUES ("'+str(self.valores[0])+'", 1, now())'
        self.cursor.execute(self.sql4)
        self.conexion.commit()

    def alta_tipo_serializables(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
        # Creamos el id
        self.sql_id = 'SELECT MAX(tipo_serializable) ' \
                      'FROM tipo_serializable'
        self.cursor.execute(self.sql_id)
        tipo_id = self.cursor.fetchall()
        tipo_id = ''.join(e for e in str(tipo_id[0]) if e.isalnum())
        if tipo_id == 'None':
            tipo_id = 1
        else:
            tipo_id = int(tipo_id)
            tipo_id += 1
        # Creamos la query
        self.sql = 'INSERT INTO tipo_serializable ' \
                   'VALUES ('+str(tipo_id)+',"'+str(self.valor1)+'", 0, '+str(self.valor2)+', '+str(self.valor3)+')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def modificar_min_max_ser(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
        self.sql = 'UPDATE tipo_serializable SET cant_min_ser = '+str(self.valor1)+', ' \
                    'cant_max_ser = '+str(self.valor2)+' WHERE tipo_serializable = '+str(self.valor3)
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def modificacion_serializables(self, valor):
        self.valor=valor
        # Obtenemos la cantidad actual y creamos la variable modificada
        self.sql = 'SELECT art_cantidad FROM articulo WHERE art_id = ' + self.valor[0] + ' AND tip_id = 2'
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
                   '= ' + today + ' WHERE art_id = ' + self.valor[0]+' AND tip_id=2'
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE articulo SET art_cantidad ' \
                   '= ' + str(cantidad) + ' WHERE art_id = ' + self.valor[0] + ' AND tip_id=2'
        self.cursor.execute(self.sql)
        self.conexion.commit()

class ABM_materiales:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def baja_materiales(self, identificador):
        self.identificador=identificador
        self.sql = 'DELETE FROM articulo_tecnico WHERE art_id = ' + str(identificador)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM articulo_movil WHERE art_id = ' + str(identificador)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE FROM articulo WHERE art_id = ' + identificador +' AND tip_id = 2'
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def alta_materiales(self, valores):
        from datetime import date
        # Transforma fecha para meterla en bd
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        self.valores = valores
        # Creamos el id
        self.sql = 'SELECT MAX(art_id) from articulo'
        self.cursor.execute(self.sql)
        art_info = self.cursor.fetchall()
        art_info = ''.join(e for e in str(art_info[0]) if e.isalnum())
        if art_info == 'None':
            art_info = 1
        else:
            art_info = int(art_info)
            art_info += 1
        # Transforma la tupla en lista para meter los elementos fijos
        self.valores = list(self.valores)
        self.valores.insert(0, str(art_info))
        self.valores[1] = '"' + str(valores[0]) + '"'
        self.valores.insert(2, today)
        self.valores.insert(3, str('2'))
        self.valores = tuple(self.valores)
        # Creamos la query
        self.sql = 'INSERT INTO articulo VALUES (' + ",".join(map(str, self.valores)) + ')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        #insertamos los articulos en tecnicos y moviles
        self.sql = 'SELECT emp_legajo FROM empleados'
        self.cursor.execute(self.sql)
        legs = self.cursor.fetchall()
        if legs:
            for i in range(0, len(legs)):
                legssql = ''.join(e for e in str(legs[i]) if e.isalnum())
                self.sql = 'INSERT INTO articulo_tecnico VALUES (' + legssql + ', ' + str(art_info) + ', 0)'
                self.cursor.execute(self.sql)
        self.sql = 'SELECT mov_id FROM movil'
        self.cursor.execute(self.sql)
        mov = self.cursor.fetchall()
        if mov:
            for i in range(0, len(mov)):
                movql = ''.join(e for e in str(mov[i]) if e.isalnum())
                self.sql = 'INSERT INTO articulo_movil VALUES (' +movql + ', ' + str(art_info) + ', 0)'
                self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_materiales(self, valor):
        self.valor=valor
        self.sql= 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE art_id = ' + self.valor +' AND tip_id = 2'
        self.cursor.execute(self.sql)
        art_info=self.cursor.fetchall()
        return art_info

    def consulta_materiales_gral(self):
        self.sql = 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE tip_id = 2'
        self.cursor.execute(self.sql)
        art_info = self.cursor.fetchall()
        lista = []
        for i in range(0, len(art_info)):

            lista.append(list(art_info[i]))
        for i in range(0, len(art_info)):
            fecha1 = str(date.today() + timedelta(days=-30))
            fecha2 = str(date.today())
            sql1 = 'SELECT sum(hm.his_mat_cant) FROM historial_materiales hm WHERE hm.art_id = '+str(lista[i][0])\
                   + ' AND hm.his_mat_fecha BETWEEN DATE("'+fecha1+'") AND DATE("'+fecha2+'")'
            self.cursor.execute(sql1)
            datos = self.cursor.fetchall()
            consumo = []
            for filas in datos:
                for filas1 in filas:
                    if filas1 == None:
                        filas1 = 0
                        consumo.append(filas1)
                    else:
                        consumo.append(int(filas1))
                lista[i].insert(3, str(consumo[0]))
        art_info = tuple(lista)
        return art_info

    def modificacion_materiales(self, valor):
        self.valor=valor
        # Obtenemos la cantidad actual y creamos la variable modificada
        self.sql = 'SELECT art_cantidad FROM articulo WHERE art_id = ' + self.valor[0] + ' AND tip_id = 2'
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
                   '= ' + today + ' WHERE art_id = ' + self.valor[0]+' AND tip_id = 2'
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE articulo SET art_cantidad ' \
                   '= ' + str(cantidad) + ' WHERE art_id = ' + self.valor[0] + ' AND tip_id = 2'
        self.cursor.execute(self.sql)
        self.conexion.commit()

class ABM_supervisor:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def consulta_empleado(self, valor):
        self.valor=valor
        self.sql= 'SELECT * FROM empleados WHERE emp_legajo = ' + self.valor
        self.cursor.execute(self.sql)
        consul_legajo=self.cursor.fetchall()
        return consul_legajo

    def baja_personal(self, identificador):
        self.identificador=identificador
        self.sql = 'DELETE from historial_sectores where emp_legajo= '+ str(self.identificador)
        self.cursor.execute (self.sql)
        self.sql = 'DELETE from usuarios where usu_legajo= ' + str(self.identificador)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE from articulo_tecnico where emp_legajo= ' + str(self.identificador)
        self.cursor.execute(self.sql)
        self.sql = 'DELETE from empleados where emp_legajo= ' + str(self.identificador)
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_empleado_en_ot(self, valor):
        verificador=True
        self.sql='SELECT * FROM movil WHERE emp_legajo='+str(valor)
        self.cursor.execute(self.sql)
        movil=self.cursor.fetchall()
        if movil:
            verificador=False
        self.sql = 'SELECT * FROM dupla_movil WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        dupla_movil = self.cursor.fetchall()
        if dupla_movil:
            verificador=True
        self.sql = 'SELECT * FROM entradas_salidas WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        entradas_salidas = self.cursor.fetchall()
        if entradas_salidas:
            verificador=False
        self.sql = 'SELECT * FROM ausentes WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        ausentes = self.cursor.fetchall()
        if ausentes:
            verificador=False
        self.sql = 'SELECT * FROM salidas_diarias WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        salidas_diarias = self.cursor.fetchall()
        if salidas_diarias:
            verificador=False
        self.sql = 'SELECT * FROM descuentos WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        descuentos = self.cursor.fetchall()
        if descuentos:
            verificador=False
        self.sql = 'SELECT * FROM detalle_denuncia_empleados WHERE emp_legajo=' + str(valor)
        self.cursor.execute(self.sql)
        detalle_denuncia_empleados = self.cursor.fetchall()
        if detalle_denuncia_empleados:
            verificador=False
        return verificador

    def alta_personal(self, valores):
        from datetime import date
        import time
        import datetime
        # Transforma fecha para meterla en bd
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        #self.valores = valores
        # Creamos el id
        self.sql = 'SELECT MAX(emp_legajo) from empleados'
        self.cursor.execute(self.sql)
        emp_info = self.cursor.fetchall()
        emp_info = ''.join(e for e in str(emp_info[0]) if e.isalnum())
        if emp_info == 'None':
            emp_info = 1
        else:
            emp_info = int(emp_info)
            emp_info += 1
        # Transforma la tupla en lista para meter los elementos fijos
        self.valores = []
        self.valores.insert(0, str(emp_info))
        self.valores.insert(1, str(valores[0]))
        self.valores.insert(2,'"' + str(valores[1]) + '"')
        self.valores.insert(3,'"' + str(valores[2]) + '"')
        self.valores.insert(4, today)
        self.valores = tuple(self.valores)
        # Creamos la query
        self.sql = 'INSERT INTO empleados VALUES (' + ",".join(map(str, self.valores)) + ')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        # inertamos el movil en la tabla articulos por movil
        self.sql = 'SELECT art_id FROM articulo'
        self.cursor.execute(self.sql)
        ids = self.cursor.fetchall()
        if ids:
            for i in range(0, len(ids)):
                idsql=''.join(e for e in str(ids[i]) if e.isalnum())
                self.sql ='INSERT INTO articulo_tecnico VALUES ('+ str(emp_info)+', '+ idsql+', 0)'
                self.cursor.execute(self.sql)

        self.conexion.commit()

        # modoficamos sector
        hoy = datetime.datetime.today()
        ya = ('{:%Y%m%d%H%M%S}'.format(hoy))
        sector=[]
        sector.insert(0, ya)
        sector.insert(1, emp_info)
        sector.insert(2,'6')
        sector.insert(3, '"' + 'Alta' + '"')
        # Creamos la query
        self.sql = 'INSERT INTO historial_sectores VALUES (' + ",".join(map(str, sector)) + ')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def emp_legajo(self):
        self.sql = 'SELECT MAX(emp_legajo) from empleados'
        self.cursor.execute(self.sql)
        emp_info = self.cursor.fetchall()
        emp_info = ''.join(e for e in str(emp_info[0]) if e.isalnum())
        if emp_info == 'None':
            emp_info = 1
        else:
            emp_info = int(emp_info)
            emp_info += 1
        return (emp_info)
        self.conexion.commit()

    def modificacion_sector(self, valor):
        import datetime
        hoy = datetime.datetime.today()
        ya = ('{:%Y%m%d%H%M%S}'.format(hoy))
        modificacion=[]
        modificacion.insert(0,ya)
        modificacion.insert(1,str(valor[1]))
        modificacion.insert(2,'"' + 'Cambio' + '"')
        self.sql = 'UPDATE historial_sectores SET fecha_cambio_sector ' \
                   '= ' + modificacion[0] + ' WHERE emp_legajo = ' + valor[0]
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE historial_sectores SET emp_sector ' \
                   '= ' + modificacion[1] + ' WHERE emp_legajo = ' + valor[0]
        self.cursor.execute(self.sql)
        self.sql = 'UPDATE historial_sectores SET motivo_cambio ' \
                   '= ' + modificacion[2] + ' WHERE emp_legajo = ' + valor[0]
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_dni(self,valor):
        self.valor = valor
        self.sql = 'SELECT * FROM empleados WHERE emp_documento = ' + self.valor
        self.cursor.execute(self.sql)
        consul_legajo = self.cursor.fetchall()
        return consul_legajo

    def consulta_empleado_sector(self,valor):
        self.valor = valor
        self.sql = 'SELECT a.emp_legajo, a.emp_nombre, a.emp_apellido' \
                   ', (SELECT desc_sector FROM sectores WHERE ' \
                   'emp_sector=b.emp_sector) FROM empleados a JOIN ' \
                   'historial_sectores b ON a.emp_legajo=b.emp_legajo WHERE a.emp_legajo=' + str(self.valor)
        self.cursor.execute(self.sql)
        consul_legajo = self.cursor.fetchall()
        return consul_legajo

    def actualizacion_de_claves(self,valor):
        self.sql = 'SELECT * from usuarios WHERE usu_legajo ='+valor[0][0]
        self.cursor.execute(self.sql)
        emp_info = self.cursor.fetchall()
        legajo_clave=valor[0][0]
        clave=valor[0][1]
        le = len(clave) - 1
        pass2 = ''
        for i in range(0, len(clave)):
            la = le - i
            pass2 += clave[la]
        if emp_info==[]:
            self.sql = 'INSERT INTO `usuarios` (`usu_legajo`, `usu_password`, `activo`) VALUES (' + legajo_clave+', "' +pass2+ '", 1 )'
            self.cursor.execute(self.sql)
            self.conexion.commit()
        else:
            pass3='"'+pass2+'"'
            self.sql = 'UPDATE usuarios SET usu_password = ' + pass3 +' WHERE usu_legajo='+legajo_clave
            self.cursor.execute(self.sql)
            self.conexion.commit()

    def validacion_sector(self,valor):
        self.sql = 'SELECT emp_sector FROM historial_sectores WHERE emp_legajo = ' + str(valor[0])
        self.cursor.execute(self.sql)
        sector = self.cursor.fetchall()
        sector = ''.join(e for e in str(sector[0]) if e.isalnum())
        sector = int(sector)
        confir = False
        if (sector == valor[1]):
            confir=True
        return confir

    def consulta_personal_gral(self):
        self.sql = 'SELECT a.emp_legajo, a.emp_nombre, a.emp_apellido, '\
                   '(SELECT a.desc_sector from sectores a JOIN historial_sectores b using (emp_sector) '\
                   'WHERE b.emp_legajo=a.emp_legajo) FROM empleados a'
        self.cursor.execute(self.sql)
        personal = self.cursor.fetchall()
        return personal

    def consulta_personal(self,valor):
        self.sql = 'SELECT a.emp_legajo, a.emp_nombre, a.emp_apellido, '\
                   '(SELECT a.desc_sector from sectores a JOIN historial_sectores b using (emp_sector) '\
                   'WHERE b.emp_legajo=a.emp_legajo) FROM empleados a WHERE a.emp_apellido= "' + str(valor)+'"'
        self.cursor.execute(self.sql)
        consul_personal = self.cursor.fetchall()
        return consul_personal

# a=ABM_supervisor()
# b=a.consulta_empleado_en_ot(str(100))