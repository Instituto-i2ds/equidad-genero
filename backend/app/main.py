from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# * Importar rutas
from app.api.users.routes import router as users_router
from app.db.database import engine
from app.api.users.models import Base
from app.core.config import settings

# * Create all tables
Base.metadata.create_all(engine)

app = FastAPI(title="User Management API", version="0.1", tags=["main_tag"])

app.include_router(users_router)

# * Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}
