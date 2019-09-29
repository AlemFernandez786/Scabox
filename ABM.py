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
        self.valor=valor
        self.sql= 'SELECT * FROM articulo WHERE art_id = ' + self.valor +' AND tip_id = 2'
        self.cursor.execute(self.sql)
        art_info=self.cursor.fetchall()
        print(art_info)

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
        self.sql = 'DELETE FROM articulo WHERE art_id = ' + identificador +' AND tip_id=3'
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
        self.valores.insert(3, str('3'))
        self.valores = tuple(self.valores)
        # Creamos la query
        self.sql = 'INSERT INTO articulo VALUES (' + ",".join(map(str, self.valores)) + ')'
        # Ejecutamos la query
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def consulta_materiales(self, valor):
        self.valor=valor
        self.sql= 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE art_id = ' + self.valor +' AND tip_id = 3'
        self.cursor.execute(self.sql)
        art_info=self.cursor.fetchall()
        return art_info

    def consulta_materiales_gral(self):
        self.sql = 'SELECT art_id, art_nombre, art_cantidad, art_cant_min, art_cant_max FROM articulo WHERE tip_id = 3'
        self.cursor.execute(self.sql)
        art_info = self.cursor.fetchall()
        lista = []
        for i in range(0, len(art_info)):

            lista.append(list(art_info[i]))
        for i in range(0, len(art_info)):
            fecha1 = str(date.today() + timedelta(days=-30))
            fecha2 = str(date.today())
            sql1 = 'SELECT sum(hm.his_mat_cantidad) FROM historial_materiales hm WHERE hm.art_id = '+str(lista[i][0])+' AND hm.his_mat_fecha BETWEEN DATE("'+fecha1+'") AND DATE("'+fecha2+'")'
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

class ABM_supervisor:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host='localhost', database='ScaBox')
        self.cursor = self.conexion.cursor()

    def baja_personal(self, identificador):
        self.identificador=identificador
        self.sql = 'DELETE FROM empleados WHERE emp_legajo = ' + identificador
        self.cursor.execute (self.sql)
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
        art_info = self.cursor.fetchall()
        art_info = ''.join(e for e in str(art_info[0]) if e.isalnum())
        if art_info == 'None':
            art_info = 1
        else:
            art_info = int(art_info)
            art_info += 1
        # Transforma la tupla en lista para meter los elementos fijos
        self.valores = []
        self.valores.insert(0, str(art_info))
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
        sector.insert(1, art_info)
        sector.insert(2,'5')
        sector.insert(3, '"' + 'Alta' + '"')
        # Creamos la query
        self.sql = 'INSERT INTO historial_sectores VALUES (' + ",".join(map(str, sector)) + ')'
        # Ejecutamos la query
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


# mat=ABM_materiales()
# her=ABM_herramientas()
# test.baja_serializables('8585')
# test.alta_serializables(('HD', '40'))
# her.alta_herramientas(('Destorplano','50', '5','15'))
# test.consulta_herramientas('2')
# test.modificacion_herramientas(('85','50'))
# test.consulta_herramientas('85')
# test.baja_herramientas('4')
# test.modificacion_serializables(('8585','145'))
# test.consulta_serializables('8585')
# mat.alta_materiales(('Divisorx3', '100','50','200'))
# test.baja_materiales('4')
# test.consulta_materiales('4')
# test.modificacion_materiales(('4','50'))
# asd=ABM()
# asd.consulta_materiales("123")
#sup=ABM_supervisor()
# sup.alta_personal(('57152336','ale','logi'))
#sup.modificacion_sector(('126','1'))
