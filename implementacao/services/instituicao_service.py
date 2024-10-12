from repository.instituicao_repository import get_todas_instituicoes
from sqlalchemy.orm import Session


def consultar_todas_instituicoes(db: Session):
    alunos = get_todas_instituicoes(db)
    if not alunos:
        raise ValueError("Nenhum aluno encontrado.")
    return alunos
