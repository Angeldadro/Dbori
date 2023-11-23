FROM python:3.11-slim
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt .
RUN python -m pip install -r requirements.txt
# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app
# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Ejecuta Uvicorn para la aplicación FastAPI
CMD ["python", "run.py"]
