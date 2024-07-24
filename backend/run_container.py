import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # La ubicación de tu aplicación FastAPI.
        # Escucha en todas las interfaces de red, lo que permite el acceso desde fuera del contenedor.
        host="0.0.0.0",
        port=8000,  # Puerto en el que se ejecutará el servidor.
        reload=True  # Habilita el recargado automático durante el desarrollo.
    )
