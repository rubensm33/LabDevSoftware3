from sqlalchemy.orm import Session
from models.transacao_professor_aluno import TransacaoProfessorAluno
from models.professor import Professor
from models.aluno import Aluno


def criar_transacao_professor_aluno(db: Session, professor_id: int, aluno_id: int, valor: int, motivo: str):
    professor = db.query(Professor).filter(Professor.id == professor_id).first()
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not professor or not aluno:
        raise ValueError("Professor ou Aluno não encontrados")

    if professor.saldo_moedas < valor:
        raise ValueError("Saldo insuficiente do professor")

    professor.saldo_moedas -= valor
    aluno.saldo_moedas += valor

    transacao = TransacaoProfessorAluno(professor_id=professor_id, aluno_id=aluno_id, valor=valor, motivo=motivo)

    db.add(transacao)
    db.commit()
    db.refresh(transacao)

    return transacao

def get_transacoes_por_professor_e_aluno(db: Session, professor_id: int):
    transacoes = db.query(TransacaoProfessorAluno)\
                   .filter(TransacaoProfessorAluno.professor_id == professor_id)\
                   .all()

    return transacoes