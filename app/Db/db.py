import psycopg2
import os
class db:
    def __init__(self):
        self.conexión= psycopg2.connect(
                                        host="dpg-clf5qlrl00ks73a6mdp0-a.oregon-postgres.render.com",
                                        database="dborigin",
                                        user="dborigin_user",
                                        password="64D6o2sE41x3onuFu7CEQb8SeAJRCtiR"
                                       )
    def ejecutarSentencia(self, sentencia, valores=None):
        try:
            cursor = self.conexión.cursor()
            if valores:
                cursor.execute(sentencia, valores)
            else:
                cursor.execute(sentencia)
            self.conexión.commit()
            return cursor
        except Exception as e:
            raise e
