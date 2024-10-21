# controllers/professor_controller.py
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from config.database import get_db
from models.user import User
from schemas.aluno import AlunoConsulta
from services.aluno_service import consultar_todos_alunos
from services.professor_service import consultar_saldo_professor
from services.transacao_service import consultar_transacoes_professor_para_aluno
from schemas.professor import ProfessorSaldoResponse
from schemas.transacao import TransacaoProfessorAlunoResponse
from services.user_service import get_current_user

router = APIRouter(prefix="/professores")


@router.get("/saldo", response_model=ProfessorSaldoResponse)
def consultar_saldo(
    current_user: Annotated[User, Security(get_current_user, scopes=["professor"])],
    db: Session = Depends(get_db),
):

    try:
        professor_id = current_user.id
        saldo = consultar_saldo_professor(db=db, professor_id=professor_id)
        return {"professor_id": professor_id, "saldo_moedas": saldo}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/transacoes", response_model=list[TransacaoProfessorAlunoResponse])
def consultar_transacoes(
    current_user: Annotated[User, Security(get_current_user, scopes=["professor"])], db: Session = Depends(get_db)
):
    try:

        transacoes = consultar_transacoes_professor_para_aluno(db=db, professor_id=current_user.id)
        return transacoes
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/alunos", response_model=list[AlunoConsulta])
def listar_todos_alunos(
    current_user: Annotated[User, Security(get_current_user, scopes=["professor"])], db: Session = Depends(get_db)
):
    try:
        alunos = consultar_todos_alunos(db=db)
        return alunos
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# Rota para enviar moedas para um aluno
@router.post("/professor/enviar-moedas")
def enviar_moedas(aluno_id: int, valor: int, motivo: str, db: Session = Depends(get_db)):
    # Cria a transação de envio de moedas
    transacao = transacao_model.TransacaoProfessorAluno(aluno_id=aluno_id, valor=valor, motivo=motivo)
    db.add(transacao)
    db.commit()
    return {"message": "Moedas enviadas com sucesso"}