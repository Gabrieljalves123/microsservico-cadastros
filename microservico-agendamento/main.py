from fastapi import FastAPI
from controller import router

app = FastAPI(
    title="Microserviço de Agendamentos",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def inicio():
    return {"mensagem": "Microserviço de Agendamentos funcionando!"}