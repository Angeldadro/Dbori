import datetime
from fastapi import APIRouter, HTTPException
from app.Db.dbadapter import dbadapter

from app.models.origin import ModelosOrigin

Router = APIRouter()

@Router.post("/leer")
async def subir():
    adapter = dbadapter()
    
    try:
        returned=adapter.leerUsuarios()
        return returned
    except Exception as e:
        raise HTTPException(status_code=400, detail="Problema al crear el usuario")

    return
