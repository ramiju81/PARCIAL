from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import FileResponse, JSONResponse
from typing import List, Optional
from models import StudentGrade
from database import grades_db
from utils import (
    generate_individual_report,
    generate_bulk_report,
    generate_summary_report
)
import os

app = FastAPI(title="Gestión de Calificaciones API")

@app.get("/student/{student_id}/report")
def get_student_report(student_id: int = Path(..., gt=0)):
    student_grades = [g for g in grades_db if g.student_id == student_id]
    if not student_grades:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    filepath = generate_individual_report(student_id, student_grades)
    return FileResponse(path=filepath, media_type="text/plain", filename=os.path.basename(filepath))

@app.post("/grades/bulk")
def post_bulk_grades(grades: List[StudentGrade]):
    grades_db.extend(grades)
    filepath = generate_bulk_report(grades)
    return FileResponse(path=filepath, media_type="text/plain", filename=os.path.basename(filepath))

@app.get("/grades/summary")
def get_grades_summary(
    calificacion_minima: Optional[float] = Query(None, ge=0, le=5),
    materia: Optional[str] = None,
    formato: Optional[str] = Query("json", pattern="^(json|txt)$")
):
    filtered = grades_db
    if calificacion_minima is not None:
        filtered = [g for g in filtered if g.calificacion >= calificacion_minima]
    if materia:
        filtered = [g for g in filtered if g.materia.lower() == materia.lower()]

    if formato == "json":
        return JSONResponse(content=[g.dict() for g in filtered])

    filepath = generate_summary_report(filtered)
    return FileResponse(path=filepath, media_type="text/plain", filename=os.path.basename(filepath))
