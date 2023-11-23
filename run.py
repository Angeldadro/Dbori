import os
from uvicorn import run

if __name__ == "__main__":
    app_module = "app.main:app"  # Indica el módulo y la instancia de la aplicación FastAPI
    port = int(os.getenv("PORT") or 8000)  # Lee el puerto desde la variable de entorno, o usa 8000 como valor predeterminado
    run(app_module, host="0.0.0.0", port=port)
