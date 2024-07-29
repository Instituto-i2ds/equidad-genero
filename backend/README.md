# 🚀 Equidad genero

Backend project with FastAPI on salary gap between men and women

## 📁 Estructura del Proyecto

```bash
.
├── .env                  # Archivo de configuración del entorno
├── .gitignore             # Archivos y carpetas a ignorar por Git
├── Dockerfile             # Archivo para construir la imagen Docker
├── LICENSE                # Licencia del proyecto
├── README.md              # Este archivo
├── app                    # Código fuente del proyecto
│   ├── __init__.py        # Inicialización del paquete
│   ├── api                # Módulo de API
│   │   └── users          # Gestión de usuarios
│   │       ├── __init__.py
│   │       ├── crud.py    # Operaciones CRUD
│   │       ├── models.py  # Modelos de datos
│   │       ├── routes.py  # Rutas de la API
│   │       └── schemas.py # Esquemas de datos
│   ├── core               # Configuración y seguridad
│   │   ├── config.py
│   │   └── security.py
│   ├── db                 # Configuración de la base de datos
│   │   ├── __init__.py
│   │   ├── database.py    # Conexión a la base de datos
│   │   └── session.py     # Sesión de la base de datos
│   ├── main.py            # Punto de entrada de la aplicación
│   └── tests              # Pruebas automatizadas
│       ├── __init__.py
│       └── test_users.py  # Pruebas para la gestión de usuarios
├── backup.py              # Script de respaldo (opcional)
├── docker-compose.yml     # Archivo de configuración para Docker Compose
├── requirements.txt       # Dependencias del proyecto
└── run.py                 # Script para ejecutar la aplicación
```

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el Repositorio

```bash
git clone https://github.com/naren-i2ds/rrhh_proyect.git
cd rrhh_proyect
```

### 2. Configurar el Entorno

Crear archvio .env y ajusta las variables de entorno según sea necesario.
```bash
touch .env
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar la Aplicación

Para ejecutar la aplicación sin Docker:

```bahs
python run.py
```

Para ejecutar la aplicación con Docker:
```bash
docker-compose up --build
```

### 5. Acceder a la Aplicación

La aplicación estará disponible en <http://localhost:8000>.
