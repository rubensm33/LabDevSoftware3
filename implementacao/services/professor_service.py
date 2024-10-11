from sqlalchemy.orm import Session
from repository.professor_repository import get_professor_saldo

def consultar_saldo_professor(db: Session, professor_id: int):
    try:
        saldo = get_professor_saldo(db, professor_id)
        return saldo
    except ValueError as e:
        raise e
