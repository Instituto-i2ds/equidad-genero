# Usa una imagen base de Python con soporte para Debian
FROM python:3.12-slim-bullseye

# Establece el directorio de trabajo en raíz del contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Crea un entorno virtual en /app y instala las dependencias
RUN python -m venv venv \
  && venv/bin/pip install --upgrade pip \
  && venv/bin/pip install --no-cache-dir -r requirements.txt


# Copia el resto del código de la aplicación
COPY . .

# Establece la variable de entorno para usar el entorno virtual
ENV PATH="/app/venv/bin:$PATH"

# Expone el puerto en el que correrá la aplicación
# EXPOSE 8000

# Comando para ejecutar la aplicación
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Establece el punto de entrada para ejecutar un shell
# ENTRYPOINT ["/bin/bash"]



# ------------------- comando para crear uan imagen de Docker ---------------

# docker build -t my_image .     # . : es la ruta donde se encuentra el archivo Dockerfile

# docker run --name backend --network my_network -p 8000:8000 -d my_image

# docker run --name backend -p 80:80 -it my_image /bin/bash

# docker exec -it backend bash

# docker stop backend

# docker rm backend
