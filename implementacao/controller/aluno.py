from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter, Security
from sqlalchemy.orm import Session

from models.user import User
from schemas import aluno as aluno_schema
from repository import aluno_repository
from schemas.transacao import TransacaoAlunoEmpresaResponse, TransacaoProfessorAlunoResponse
from services import aluno_service
from config.database import get_db
from services.user_service import get_current_user
from services.transacao_service import consultar_transacoes_aluno

router = APIRouter(prefix="/alunos")


@router.post("/", response_model=aluno_schema.AlunoBase)
def create_aluno(aluno: aluno_schema.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = aluno_repository.get_aluno_by_email(db, email=aluno.email)
    if db_aluno:
        raise HTTPException(status_code=400, detail="Email already registrado")

    db_aluno = aluno_service.post_aluno(db=db, aluno_data=aluno)

    return aluno_schema.AlunoBase.model_validate(db_aluno, from_attributes=True)


@router.get("/saldo", response_model=aluno_schema.AlunoSaldoResponse)
def consultar_saldo(
    current_user: Annotated[User, Security(get_current_user, scopes=["aluno"])],
    db: Session = Depends(get_db),
):

    try:
        aluno_id = current_user.id
        saldo = aluno_service.consultar_saldo_aluno(db=db, aluno_id=aluno_id)
        return {"aluno_id": aluno_id, "saldo_moedas": saldo}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/transacoes", response_model=list[TransacaoProfessorAlunoResponse | TransacaoAlunoEmpresaResponse])
def consultar_transacoes(
    current_user: Annotated[User, Security(get_current_user, scopes=["aluno"])], db: Session = Depends(get_db)
):
    try:

        transacoes = consultar_transacoes_aluno(db=db, aluno_id=current_user.id)
        return transacoes
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
