# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instalar glpk-utils
RUN apt-get update && apt-get install -y glpk-utils

# Crear las carpetas in y out dentro del contenedor
RUN mkdir -p /app/in /app/out

# Comando predeterminado para ejecutar el programa
CMD ["python", "main.py", "/app/in/tasks.csv", "/app/in/blocks.csv"]