from fastapi import APIRouter, Depends, HTTPException, Security
from typing import Annotated
from models.user import User
from sqlalchemy.orm import Session
from schemas.transacao import (
    CompraVantagemRequest,
    TransacaoAlunoEmpresaResponse,
    TransacaoProfessorAlunoCreate,
    TransacaoProfessorAlunoResponse,
)
from services.transacao_service import realizar_compra_vantagem, realizar_transacao_professor_aluno
from services.user_service import get_current_user
from utils.email_templates import email_compra_template, email_notificacao_empresa, email_professor_moedas
from utils.email_sender import enviar_email
from config.database import get_db
import random

router = APIRouter(prefix="/transacoes")


@router.post("/professor_aluno", response_model=TransacaoProfessorAlunoResponse)
def criar_transacao(
    transacao_data: TransacaoProfessorAlunoCreate,
    current_user: Annotated[User, Security(get_current_user, scopes=["professor"])],
    db: Session = Depends(get_db),
):
    try:
        transacao = realizar_transacao_professor_aluno(db=db, transacao_data=transacao_data, current_user=current_user)

        conteudo_email = email_professor_moedas(
            professor_nome=current_user.nome, valor=transacao.valor, motivo=transacao.motivo
        )
        enviar_email(transacao.aluno.email, "Você recebeu moedas!", conteudo_email)
        return transacao
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/compra", response_model=TransacaoAlunoEmpresaResponse)
def comprar_vantagem(
    vantagem_id: int,
    current_user: Annotated[User, Security(get_current_user, scopes=["aluno"])],
    db: Session = Depends(get_db),
):
    try:
        compra_data = CompraVantagemRequest(aluno_id=current_user.id, vantagem_id=vantagem_id)
        transacao = realizar_compra_vantagem(db=db, compra_data=compra_data)

        codigo_vantagem = f"{random.randint(100, 999)}-{random.randint(100, 999)}"

        conteudo_email_aluno = email_compra_template(
            codigo=codigo_vantagem,
        )
        enviar_email(current_user.email, "Confirmação de Compra", conteudo_email_aluno)

        conteudo_email_empresa = email_notificacao_empresa(
            aluno_nome=current_user.nome,
            vantagem_descricao=transacao.vantagem.descricao,
            codigo=codigo_vantagem,
        )
        enviar_email(transacao.empresa.email, "Nova Compra Realizada", conteudo_email_empresa)
        return transacao
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
