from pydantic import BaseModel
from typing import List, Optional

class PetBaseDTO(BaseModel):
    id: int
    nome: str
    especie: str
    raca: Optional[str] = None

    class Config:
        from_attributes = True

class TutorResponseDTO(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str
    email: Optional[str] = None
    pets: List[PetBaseDTO] = []

    class Config:
        from_attributes = True