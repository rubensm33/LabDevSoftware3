from sqlalchemy.orm import Session
from repository.transacao_repository import criar_transacao_professor_aluno, get_transacoes_por_professor_e_aluno
from schemas.transacao import TransacaoProfessorAlunoCreate, CompraVantagemRequest
from repository.transacao_repository import get_transacoes_do_aluno, registrar_compra_vantagem
from schemas.transacao import TransacaoProfessorAlunoResponse, TransacaoAlunoEmpresaResponse


def realizar_transacao_professor_aluno(db: Session, transacao_data: TransacaoProfessorAlunoCreate, current_user):
    try:
        transacao = criar_transacao_professor_aluno(
            db=db,
            professor_id=current_user.id,
            aluno_id=transacao_data.aluno_id,
            valor=transacao_data.valor,
            motivo=transacao_data.motivo,
        )
        return transacao
    except ValueError as e:
        raise e


def consultar_transacoes_professor_para_aluno(db: Session, professor_id: int):
    transacoes = get_transacoes_por_professor_e_aluno(db, professor_id)

    if not transacoes:
        raise ValueError("Nenhuma transação encontrada para este professor e aluno.")

    return transacoes


def consultar_transacoes_aluno(db: Session, aluno_id: int):
    transacoes_professor_aluno, transacoes_aluno_empresa = get_transacoes_do_aluno(db, aluno_id)

    transacoes_professor_aluno_response = [
        TransacaoProfessorAlunoResponse(
            professor_id=transacao.professor_id,
            aluno_id=transacao.aluno_id,
            valor=transacao.valor,
            motivo=transacao.motivo,
            data_transacao=transacao.data_transacao,
        )
        for transacao in transacoes_professor_aluno
    ]

    transacoes_aluno_empresa_response = [
        TransacaoAlunoEmpresaResponse(
            vantagem_id=transacao.vantagem_id,
            aluno_id=transacao.aluno_id,
            valor=transacao.valor,
            data_transacao=transacao.data_transacao,
        )
        for transacao in transacoes_aluno_empresa
    ]

    return transacoes_professor_aluno_response + transacoes_aluno_empresa_response





def realizar_compra_vantagem(db: Session, compra_data: CompraVantagemRequest):
    try:
        transacao = registrar_compra_vantagem(
            db=db,
            aluno_id=compra_data.aluno_id,
            vantagem_id=compra_data.vantagem_id
        )
        return transacao
    except ValueError as e:
        raise e

