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
        print(a)

    def cambio_sector(self,legajo,sector_nuevo,motivo):
        self.legajo=legajo
        self.sql= 'SELECT * FROM `empleados` WHERE `emp_legajo`= ' + self.legajo
        self.cursor.execute(self.sql)
        a = self.cursor.fetchall()
        print(a)
        if a ==[]:
            print('puto')
        self.sector_nuevo=sector_nuevo
        self.motivo=motivo
        from datetime import date
        today = date.today()
        #self.sql= 'INSERT INTO historial_cambios_sector VALUES ('+ today + ',' +self.legajo+','
        self.sql='UPDATE empleados SET emp_sector = '+ sector_nuevo + ' WHERE emp_legajo = '+legajo
        self.cursor.execute(self.sql)
        self.conexion.commit()
        # fecha cambio datatime
        # legajo int
        # serctor inicial int
        # sector fnal int
        # motivo varchar




a=ABM()
a.cambio_sector('1234','1','reverervre')