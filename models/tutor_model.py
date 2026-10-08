from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class TutorModel(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String)

    pets = relationship("PetModel", back_populates="tutor", cascade="all, delete")