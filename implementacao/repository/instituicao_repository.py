from sqlalchemy.orm import Session

from models import user as user_model, instituicao as instituicao_model


def get_todas_instituicoes(db: Session):
    return db.query(instituicao_model.Instituicao).all()


def get_instituicao_by_name(db: Session, nome_instituicao: str):
    return (
        db.query(instituicao_model.Instituicao).filter(instituicao_model.Instituicao.nome == nome_instituicao).first()
    )
