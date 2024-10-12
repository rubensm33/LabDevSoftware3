from sqlalchemy.orm import Session
from models import aluno as aluno_model, scopes as scopes_model
from schemas.aluno import AlunoCreate
from sqlalchemy.orm import joinedload


def create_aluno(db: Session, aluno: AlunoCreate):
    dict_aluno_data = aluno.__dict__.copy()
    dict_aluno_data["role"] = "aluno"
    dict_aluno_data["saldo_moedas"] = 0
    dict_aluno_data["instituicao_id"] = dict_aluno_data.pop("instituicao")

    db_aluno = aluno_model.Aluno(**dict_aluno_data)

    db_scope_me = scopes_model.UserScopes(user_id=db_aluno.id, scope="me")
    db_scope_aluno = scopes_model.UserScopes(user_id=db_aluno.id, scope="aluno")
    db.add(db_aluno)
    db.add(db_scope_me)
    db.add(db_scope_aluno)
    db.commit()
    db.refresh(db_aluno)
    db_aluno = (
        db.query(aluno_model.Aluno)
        .options(joinedload(aluno_model.Aluno.instituicao_aluno))
        .filter(aluno_model.Aluno.id == db_aluno.id)
        .first()
    )

    return db_aluno


def get_aluno(db: Session, aluno_id: int):
    return db.query(aluno_model.Aluno).filter(aluno_model.Aluno.id == aluno_id).first()


def get_aluno_by_email(db: Session, email: str):
    return db.query(aluno_model.Aluno).filter(aluno_model.Aluno.email == email).first()


def get_aluno_saldo(db: Session, aluno_id: int):
    aluno = db.query(aluno_model.Aluno).filter(aluno_model.Aluno.id == aluno_id).first()

    if not aluno:
        raise ValueError("Aluno não encontrado")

    return aluno.saldo_moedas


def get_todos_alunos(db: Session):
    return db.query(aluno_model.Aluno).all()
