from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Veneto Digital - P2")

# Inclui as rotas que definiremos no outro arquivo
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Veneto Digital API está online!"}