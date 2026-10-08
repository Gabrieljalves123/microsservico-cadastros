from fastapi import FastAPI
from database import engine, Base
from controllers import tutor_controller, pet_controller

# Cria as tabelas automaticamente no SQLite ao iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microsserviço de Cadastros - PetShop",
    version="1.0.0"
)

# Registra os Controllers (Rotas)
app.include_router(tutor_controller.router)
app.include_router(pet_controller.router)

@app.get("/")
def raiz():
    return {"status": "Microsserviço de Cadastros rodando com sucesso!"}