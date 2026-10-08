from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship
from database import Base

class PetModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=False)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    raca = Column(String)
    peso = Column(DECIMAL(5,2))
    data_nascimento = Column(Date)

    tutor = relationship("TutorModel", back_populates="pets")