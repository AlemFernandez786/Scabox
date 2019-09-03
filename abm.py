import mysql.connector


class ABMC:
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="",
                                                database="ScaBox")
        self.cursor = self.conexion.cursor()

    def alta(self):
        pass

    def baja(self, tabla, identificador):
        bajar = "DELETE FROM " + tabla + "WHERE id =" + identificador

        self.cursor.execute(bajar)
        self.conexion.commit()
        self.cursor.close()
