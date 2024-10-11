from fastapi import HTTPException
from repository.aluno_repository import create_aluno, get_aluno_saldo
from repository.instituicao_repository import get_instituicao_by_name
from sqlalchemy.orm import Session
from schemas.aluno import AlunoCreate
from services.token_service import hash_password


def post_aluno(db: Session, aluno_data: AlunoCreate):
    instituicao_data = get_instituicao_by_name(db, aluno_data.instituicao)
    if not instituicao_data:
        raise HTTPException(status_code=404, detail="Instituição não encontrada")

    aluno_data.instituicao = instituicao_data.id

    aluno_data.hashed_password = hash_password(aluno_data.hashed_password)

    response = create_aluno(db=db, aluno=aluno_data)
    return response


def consultar_saldo_aluno(db: Session, aluno_id: int):
    try:
        saldo = get_aluno_saldo(db, aluno_id)
        return saldo
    except ValueError as e:
        raise e
