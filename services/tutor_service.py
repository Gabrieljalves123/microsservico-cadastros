from sqlalchemy.orm import Session
from repositories.tutor_repository import TutorRepository
from fastapi import HTTPException

class TutorService:
    def __init__(self, db: Session):
        self.repository = TutorRepository(db)

    def listar_tutores(self):
        return self.repository.listar_todos()

    def obter_tutor_por_id(self, tutor_id: int):
        tutor = self.repository.buscar_por_id(tutor_id)
        if not tutor:
            raise HTTPException(status_code=404, detail="Tutor não encontrado no sistema.")
        return tutor