from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from services.tutor_service import TutorService
from dtos.tutor_dto import TutorResponseDTO

router = APIRouter(prefix="/tutores", tags=["Tutores"])

@router.get("", response_model=List[TutorResponseDTO])
def listar_tutores(db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.listar_tutores()

@router.get("/{tutor_id}", response_model=TutorResponseDTO)
def obter_tutor(tutor_id: int, db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.obter_tutor_por_id(tutor_id)