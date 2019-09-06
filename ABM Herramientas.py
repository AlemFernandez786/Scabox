import mysql.connector

class ABM():
    def __init__(self):
        self.conexion = mysql.connector.connect(user = 'root',password = '',host = 'localhost',database = 'ScaBox')
        self.cursor = self.conexion.cursor()

    def baja_herramientas(self, identificador):
        self.columna=columna
        self.identificador=identificador
        self.sql = 'DELETE FROM articulo WHERE art_id ' = ' + identificador
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def alta_herramienta(self, valores):
        from datetime import date
        #Transforma fecha para meterla en bd
        today = date.today()
        today = str(today)
        today = ''.join(e for e in today if e.isalnum())
        self.valores = valores
        #Transforma la tupla en lista para meter los elementos fijos
        self.valores = list(self.valores)
        self.valores[1] = '"' + str(valores[1]) + '"'
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
        self.sql= 'SELECT * FROM herramientas WHERE den_id = ' + self.valor
        self.cursor.execute(self.sql)
        a=self.cursor.fetchall()
        print(a)

test=ABM()