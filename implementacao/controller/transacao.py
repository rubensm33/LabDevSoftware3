from fastapi import APIRouter, Depends, HTTPException, Security
from typing import Annotated
from models.user import User
from sqlalchemy.orm import Session
from services.user_service import get_current_user
from config.database import get_db
from services.transacao_service import realizar_transacao_professor_aluno
from schemas.transacao import TransacaoProfessorAlunoCreate, TransacaoProfessorAlunoResponse

router = APIRouter(prefix="/transacoes")


@router.post("/professor_aluno", response_model=TransacaoProfessorAlunoResponse)
def criar_transacao(
    transacao_data: TransacaoProfessorAlunoCreate,
    current_user: Annotated[User, Security(get_current_user, scopes=["professor"])],
    db: Session = Depends(get_db),
):
    try:
        transacao = realizar_transacao_professor_aluno(db=db, transacao_data=transacao_data, current_user=current_user)
        return transacao
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
