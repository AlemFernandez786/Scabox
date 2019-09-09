import mysql.connector

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
        # print(art_info)
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


mat=ABM_materiales()
her=ABM_herramientas()
#test.baja_serializables('8585')
#test.alta_serializables(('HD', '40'))
#her.alta_herramientas(('Destorplano','50', '5','15'))
#test.consulta_herramientas('2')
#test.modificacion_herramientas(('85','50'))
#test.consulta_herramientas('85')
#test.baja_herramientas('4')
#test.modificacion_serializables(('8585','145'))
#test.consulta_serializables('8585')
#mat.alta_materiales(('Divisorx3', '100','50','200'))
#test.baja_materiales('4')
#test.consulta_materiales('4')
#test.modificacion_materiales(('4','50'))
#asd=ABM()
#asd.consulta_materiales("123")