from sqlalchemy.orm import Session

from models import user as user_model, instituicao as instituicao_model


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_instituicao_by_name(db: Session, nome_instituicao: str):
    return (
        db.query(instituicao_model.Instituicao).filter(instituicao_model.Instituicao.nome == nome_instituicao).first()
    )
