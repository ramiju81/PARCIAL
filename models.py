from pydantic import BaseModel, Field
from typing import Optional

class StudentGrade(BaseModel):
    student_id: int = Field(..., gt=0 ) 
    nombre: str
    materia: str
    calificacion: float = Field(..., ge=0, le=5)
    comentarios: Optional[str] = None

class StudentGradeResponse(StudentGrade):
    id: int  # Este sería el ID autoincremental desde la base de datos

    class Config:
        orm_mode = True
