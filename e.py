#import mysql.connector

class ABM():
    def __init__(self):
        self.conexion = mysql.connector.connect(user = 'root',password = '',host = 'localhost',database = 'capsi_srl')
        self.cursor = self.conexion.cursor()

    def alta(self,tabla,campos,valores):
        self.tabla = tabla
        self.valores = valores
        self.campos = ''
        self.items = ''

        if(len(campos) > 0):
            for c in campos:
                self.campos += c + ','
        if(len(valores) > 0):
            for v in valores:
                self.items += ' %s,'
        self.sql = 'INSERT INTO ' + self.tabla + '(' + self.campos[:-1] + ')' + 'VALUES' + '(' + self.items[:-1] + ')'

        self.cursor.execute(self.sql,self.valores)
        self.conexion.commit()

    #def consulta(self,tabla):

    #def modificacion(self):




#abm = ABM()
#v = ('codigo','fecha','descripcion')
#query = 'INSERT INTO articulos_herramientas(codigo,cantidad,cantidad_max,cantidad_min,fecha,descripcion) VALUES (%s, %s, %s, %s, %s, %s)'
#t = ('24452452','2010/09/05','Lorem ')
#abm.alta('articulos_herramientas',v,t)
