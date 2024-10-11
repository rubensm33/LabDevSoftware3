from sqlalchemy.orm import Session
from repository.transacao_repository import criar_transacao_professor_aluno, get_transacoes_por_professor_e_aluno
from schemas.transacao import TransacaoProfessorAlunoCreate

def realizar_transacao_professor_aluno(db: Session, transacao_data: TransacaoProfessorAlunoCreate, current_user):
    try:
        transacao = criar_transacao_professor_aluno(
            db=db,
            professor_id=current_user.id,
            aluno_id=transacao_data.aluno_id,
            valor=transacao_data.valor,
            motivo=transacao_data.motivo
        )
        return transacao
    except ValueError as e:
        raise e



def consultar_transacoes_professor_para_aluno(db: Session, professor_id: int):
    transacoes = get_transacoes_por_professor_e_aluno(db, professor_id)
    
    if not transacoes:
        raise ValueError("Nenhuma transação encontrada para este professor e aluno.")
    
    return transacoes
