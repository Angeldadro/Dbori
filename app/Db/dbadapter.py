# db adapter
import os
from fastapi import HTTPException
import requests
from app.Db.db import db
import uuid

class dbadapter:
    def __init__(self):
        self.db = db()

    def crearUsuario(self, codigo, nombre, nacionalidad, identificacion, fecha_ingreso, fecha_salida, modo_ingreso, empresa):
        try:
            sentencia_sql = 'INSERT INTO public."Origin" ("Id", "Código", "Nombre_y_Apellido", "Nacionalidad", "identificación", "Fecha_de_ingreso", "Fecha_de_salida", "Modo_de_ingreso", "Empresa") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
            aidi=uuid.uuid4()
            #convertir el uuid a texto
            aidi=str(aidi)
            valores = ( aidi,codigo, nombre, nacionalidad, identificacion,
                       fecha_ingreso, fecha_salida, modo_ingreso, empresa)

            self.db.ejecutarSentencia(sentencia_sql, valores)
            url = os.getenv("APPS_URL") or 'https://script.google.com/macros/s/AKfycbwWdZSk6ivN_WM_yNvpnCAbRtOap_OC5NsQCD7lkoAhkTQOlnUVK4Yrw1oj_g5CZhEO/exec'
            try:
                requests.get(url, timeout=2)
                return { "msg": "Ok" }
            except Exception as e:
                return { "msg": "Error" }
            
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
                "Id",
                "codigo",
                "nombre",
                "nacionalidad",
                "identificación",
                "fecha_ingreso",
                "fecha_salida",
                "modo_ingreso",
                "empresa"
            ]
            result = []
            for item in cursor:
                # Elimina los paréntesis y divide la cadena en valores
                values = item[0].strip("()").split(",")
                # Asigna los valores a variables
                Id, codigo, nombre, nacionalidad, identificacion, fecha_ingreso, fecha_salida, modo_ingreso, empresa = values
                # Crea un diccionario con las claves apropiadas
                diccionario = {
                    "Id": Id,
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
