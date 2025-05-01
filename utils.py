import uuid
import os
from models import StudentGrade
from typing import List, Union

def _to_grade_line(g: StudentGrade) -> str:
    return f"ID: {g.student_id} | Nombre: {g.nombre} | Materia: {g.materia} | Nota: {g.calificacion} | Comentarios: {g.comentarios or 'N/A'}"

def generate_individual_report(student_id: int, grades: List[StudentGrade]) -> str:
    filename = f"report_{student_id}_{uuid.uuid4().hex}.txt"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "w") as f:
        f.write(f"Reporte de Calificaciones - Estudiante {student_id}\n\n")
        for g in grades:
            f.write(_to_grade_line(g) + "\n")
    return filepath

def generate_bulk_report(grades: List[StudentGrade]) -> str:
    filename = f"bulk_{uuid.uuid4().hex}.txt"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "w") as f:
        f.write("Carga Masiva de Calificaciones\n\n")
        for g in grades:
            f.write(_to_grade_line(g) + "\n")
    return filepath

def generate_summary_report(grades: List[StudentGrade]) -> str:
    filename = f"summary_{uuid.uuid4().hex}.txt"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "w") as f:
        f.write("Resumen de Calificaciones\n\n")
        for g in grades:
            f.write(_to_grade_line(g) + "\n")
    return filepath
