from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from schemas.instituicao import InstituicaoBase
from services.instituicao_service import consultar_todas_instituicoes

from config.database import get_db


router = APIRouter(prefix="/instituicoes")


@router.post("/", response_model=list[InstituicaoBase])
def listar_instituicoes(
    db: Session = Depends(get_db),
):
    try:
        transacao = consultar_todas_instituicoes(db=db)
        return transacao
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
