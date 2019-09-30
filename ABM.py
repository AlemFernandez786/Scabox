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
        self.identificador=identificador
        self.sql = 'DELETE FROM articulo WHERE art_id = ' + identificador +' AND tip_id=2'
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def alta_serializables(self, valores):
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
        self.conexion.commit()

    def consulta_serializables(self, valor):
        self.valor = valor
        self.sql = 'SELECT * FROM serializable WHERE ser_mac = "' + str(self.valor) + '"'
        self.cursor.execute(self.sql)
        ser_info = self.cursor.fetchall()
        return ser_info

    def consulta_ser_all(self):
        self.sql = 'SELECT * FROM serializable'
        self.cursor.execute(self.sql)
        ser_all = self.cursor.fetchall()
        return ser_all

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
        self.sql = 'DELETE from empleados where emp_legajo= ' + str(self.identificador)
        self.cursor.execute(self.sql)
        self.conexion.commit()

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
        self.cursor.execute(self.sql)
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

