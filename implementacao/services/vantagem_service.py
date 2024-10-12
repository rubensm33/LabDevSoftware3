from sqlalchemy.orm import Session
from repository.transacao_repository import listar_todas_vantagens


def listar_vantagens(db: Session):
    return listar_todas_vantagens(db)
