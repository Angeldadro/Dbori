from fastapi import HTTPException
import psycopg2
import os
class db:
    def __init__(self):
        self.conexión= psycopg2.connect(
                                        host= os.getenv("DB_HOST") or "dpg-clf5qlrl00ks73a6mdp0-a.oregon-postgres.render.com",
                                        database= os.getenv("DB_NAME") or "dborigin",
                                        user=  os.getenv("DB_USER") or "dborigin_user",
                                        password= os.getenv("DB_PASSWORD") or "64D6o2sE41x3onuFu7CEQb8SeAJRCtiR"
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
            raise HTTPException( status_code=400, detail="Problema con la petición a la base de datos")
