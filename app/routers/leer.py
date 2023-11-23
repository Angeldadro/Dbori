import datetime
from fastapi import APIRouter, HTTPException
from app.Db.dbadapter import dbadapter

from app.models.origin import ModelosOrigin

Router = APIRouter()

@Router.get("/leer")
async def subir():
    adapter = dbadapter()
    
    try:
        returned=adapter.leerUsuarios()
        print(returned)
        return returned
    except Exception as e:
        raise HTTPException(status_code=400, detail="Problema al crear el usuario")

    return
