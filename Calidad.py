import mysql.connector

class ABM():
    def __init__(self):
        self.conexion = mysql.connector.connect(user = 'root',password = '',host = 'localhost',database = 'ScaBox')
        self.cursor = self.conexion.cursor()

    def alta(self,tabla,valores):
        self.tabla = tabla
        self.valores = valores
        self.items = ''
        if(len(valores) > 0):
            for v in valores:
                self.items += ' %s,'
        self.sql = 'INSERT INTO ' + self.tabla + ' VALUES ' + '(' + self.items[:-1] + ')'
        self.cursor.execute(self.sql,self.valores)
        self.conexion.commit()

    def baja(self, tabla, columna, identificador):
        self.tabla=tabla
        self.columna=columna
        self.identificador=identificador
        self.sql = 'DELETE FROM '+tabla+' WHERE '+ columna + ' = ' + identificador
        self.cursor.execute (self.sql)
        self.conexion.commit()

    #def modificacion(self):

    def alta_denuncia(self, valores):
        self.valores=valores
        self.sql = 'INSERT INTO `denuncias` VALUES (' + ",".join(map(str,valores)) + ')'
        self.cursor.execute (self.sql)
        self.conexion.commit()

    def consulta_denuncia(self, valor):
        self.valor=valor
        self.sql= 'SELECT * FROM denuncias WHERE den_id = ' + self.valor
        self.cursor.execute(self.sql)
        a=self.cursor.fetchall()

a=ABM()
a.alta('empleados', (1236, 12366479, 'chicho','seri'))
#a.baja('empleados', 'emp_legajo', '1234')
a.alta_denuncia((1230,123,321,12,190518,1234,190520))