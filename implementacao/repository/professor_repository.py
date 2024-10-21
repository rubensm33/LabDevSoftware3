from sqlalchemy.orm import Session
from models.professor import Professor

def get_professor_saldo(db: Session, professor_id: int):
    professor = db.query(Professor).filter(Professor.id == professor_id).first()

    if not professor:
        raise ValueError("Professor não encontrado")

    return professor.saldo_moedas
