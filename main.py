from fastapi import FastAPI
from router import router

app = FastAPI(title="Color Converter API", version="1.0.0")
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в Color Converter API",
        "docs": "/docs",
    }