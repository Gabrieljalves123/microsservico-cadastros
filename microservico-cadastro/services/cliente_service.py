from sqlalchemy.orm import Session
from repositories.cliente_repository import ClienteRepository
from dtos.cliente_dto import ClienteCreateDTO

class ClienteService:

    @staticmethod
    def criar(db: Session, cliente_data: ClienteCreateDTO):
        # Aqui pode adicionar validações de negócio futuras (ex: verificar se email já existe)
        return ClienteRepository.criar_cliente(db, cliente_data)

    @staticmethod
    def listar_todos(db: Session):
        return ClienteRepository.listar_clientes(db)

    @staticmethod
    def buscar_por_id(db: Session, cliente_id: int):
        cliente = ClienteRepository.buscar_por_id(db, cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado")
        return cliente