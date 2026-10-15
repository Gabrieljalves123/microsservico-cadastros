from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from messaging import publicar_evento_cadastro
from dtos.cliente_dto import ClienteCreateDTO  # <--- Nome correto da classe
from models.cliente_model import ClienteModel

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def criar_cliente(cliente_in: ClienteCreateDTO, db: Session = Depends(get_db)):  # <--- Atualizado aqui também
    # 1. Salva localmente na base de dados do microsserviço de Cadastro
    novo_cliente = ClienteModel(**cliente_in.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    
    # 2. Prepara e envia o evento para o Message Broker
    evento_payload = {
        "id_cliente": novo_cliente.id,
        "nome": novo_cliente.nome,
        "email": novo_cliente.email,
        "evento": "CLIENTE_CADASTRADO"
    }
    publicar_evento_cadastro(evento_payload)
    
    # 3. Retorna status 202 Accepted ao cliente
    return {
        "mensagem": "Cliente registado com sucesso e evento enviado para processamento assíncrono.",
        "dados": evento_payload
    }