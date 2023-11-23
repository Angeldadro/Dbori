# db adapter
from fastapi import HTTPException
from app.Db.db import db


class dbadapter:
    def __init__(self):
        self.db = db()

    def crearUsuario(self, codigo, nombre, nacionalidad, identificacion, fecha_ingreso, fecha_salida, modo_ingreso, empresa):
        try:
            sentencia_sql = 'INSERT INTO public."Origin" ("Código", "Nombre_y_Apellido", "Nacionalidad", "identificación", "Fecha_de_ingreso", "Fecha_de_salida", "Modo_de_ingreso", "Empresa") VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'

            valores = (codigo, nombre, nacionalidad, identificacion,
                       fecha_ingreso, fecha_salida, modo_ingreso, empresa)

            self.db.ejecutarSentencia(sentencia_sql, valores)

            print("Se inserto el usuario con info: " + str(codigo) + " " + str(nombre) + " " + str(nacionalidad) + " " +
                  str(identificacion) + " " + str(fecha_ingreso) + " " + str(fecha_salida) + " " + str(modo_ingreso) + " " + str(empresa))
        except Exception as e:
            raise HTTPException(
                status_code=400, detail="Problema al ejecutar el SQL")

    def leerUsuarios(self):
        try:
            sentencia_sql = 'SELECT ("Código", "Nombre_y_Apellido", "Nacionalidad", "identificación", "Fecha_de_ingreso", "Fecha_de_salida", "Modo_de_ingreso", "Empresa") FROM public."Origin";'
            cursor = self.db.ejecutarSentencia(sentencia_sql).fetchall()
            values = [
                "codigo",
                "nombre",
                "nacionalidad",
                "identificación",
                "fecha_ingreso",
                "fecha_salida",
                "modo_ingreso",
                "empresa"
            ]
            # [
            #    [
            #       "(loco,locoloco,god,god,2023-11-22,2023-11-23,god,god)"
            #  ],
            # [
            #    "(loco2,locoloco,god,god,2023-11-22,2023-11-23,god,god)"
            # ]
            # ]
            result = []
            for item in cursor:
                # Elimina los paréntesis y divide la cadena en valores
                values = item[0].strip("()").split(",")
                # Asigna los valores a variables
                codigo, nombre, nacionalidad, identificacion, fecha_ingreso, fecha_salida, modo_ingreso, empresa = values
                # Crea un diccionario con las claves apropiadas
                diccionario = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "nacionalidad": nacionalidad,
                    "identificación": identificacion,
                    "fecha_ingreso": fecha_ingreso,
                    "fecha_salida": fecha_salida,
                    "modo_ingreso": modo_ingreso,
                    "empresa": empresa
                }
                result.append(diccionario)
            return result
        except Exception as e:
            raise HTTPException(
                status_code=400, detail="Problema al ejecutar el SQL")
