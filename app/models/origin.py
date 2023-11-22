from pydantic import BaseModel

class ModelosOrigin(BaseModel):
    Código: str
    Nombre_y_Apellido: str
    Nacionalidad: str
    N_de_identificación: str
    Fecha_de_ingreso: str
    Fecha_de_salida: str
    Modo_de_ingreso: str
    Empresa: str