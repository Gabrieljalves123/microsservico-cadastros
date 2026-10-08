from sqlalchemy.orm import Session
from models.tutor_model import TutorModel

class TutorRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar_todos(self):
        return self.db.query(TutorModel).all()

    def buscar_por_id(self, tutor_id: int):
        return self.db.query(TutorModel).filter(TutorModel.id == tutor_id).first()