from sqlalchemy.orm import Session
from models.transacao_professor_aluno import TransacaoProfessorAluno
from models.professor import Professor
from models.aluno import Aluno
from models.transacao_professor_aluno import TransacaoProfessorAluno
from models.transacao_aluno_empresa import TransacaoAlunoEmpresa


from models.vantagem import Vantagem


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
    transacoes = db.query(TransacaoProfessorAluno).filter(TransacaoProfessorAluno.professor_id == professor_id).all()

    return transacoes


def get_transacoes_do_aluno(db: Session, aluno_id: int):
    transacoes_professor_aluno = (
        db.query(TransacaoProfessorAluno).filter(TransacaoProfessorAluno.aluno_id == aluno_id).all()
    )

    transacoes_aluno_empresa = db.query(TransacaoAlunoEmpresa).filter(TransacaoAlunoEmpresa.aluno_id == aluno_id).all()

    return transacoes_professor_aluno, transacoes_aluno_empresa


def registrar_compra_vantagem(db: Session, aluno_id: int, vantagem_id: int):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    vantagem = db.query(Vantagem).filter(Vantagem.id == vantagem_id).first()

    if not aluno:
        raise ValueError("Aluno não encontrado.")
    if not vantagem:
        raise ValueError("Vantagem não encontrada.")

    if aluno.saldo_moedas < vantagem.custo_moedas:
        raise ValueError("Saldo insuficiente do aluno.")

    aluno.saldo_moedas -= vantagem.custo_moedas

    transacao = TransacaoAlunoEmpresa(
        aluno_id=aluno_id, empresa_id=vantagem.empresa_id, vantagem_id=vantagem_id, valor=vantagem.custo_moedas
    )

    db.add(transacao)
    db.commit()
    db.refresh(transacao)

    return transacao


def listar_todas_vantagens(db: Session):
    vantagens = db.query(Vantagem).all()
    return vantagens
