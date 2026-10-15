from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

class EnderecoDTO(BaseModel):
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    principal: Optional[bool] = True

    class Config:
        from_attributes = True

class PetBaseDTO(BaseModel):
    id: int
    nome: str
    especie: str
    raca: Optional[str] = None
    data_nascimento: Optional[date] = None
    porte: Optional[str] = None
    observacoes: Optional[str] = None
    ativo: Optional[bool] = True

    class Config:
        from_attributes = True

class ClienteCreateDTO(BaseModel):
    nome: str
    email: Optional[str] = None
    telefone: str
    ativo: Optional[bool] = True
    enderecos: List[EnderecoDTO] = []

class ClienteResponseDTO(BaseModel):
    id: int
    nome: str
    email: Optional[str] = None
    telefone: str
    ativo: bool
    data_cadastro: datetime
    enderecos: List[EnderecoDTO] = []
    pets: List[PetBaseDTO] = []

    class Config:
        from_attributes = True