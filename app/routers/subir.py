import datetime
from fastapi import APIRouter, HTTPException
from app.Db.dbadapter import dbadapter

from app.models.origin import ModelosOrigin

Router = APIRouter()

@Router.post("/subir")
async def subir(subida: ModelosOrigin):
    adapter = dbadapter()
    
    try:
        adapter.crearUsuario(
            subida.Código,
            subida.Nombre_y_Apellido,
            subida.Nacionalidad,
            subida.N_de_identificación,
            datetime.datetime.strptime(subida.Fecha_de_ingreso, "%Y-%m-%d").date(),
            datetime.datetime.strptime(subida.Fecha_de_salida, "%Y-%m-%d").date(),
            subida.Modo_de_ingreso,
            subida.Empresa)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Problema al crear el usuario")

    return
