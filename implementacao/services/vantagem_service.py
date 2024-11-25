from sqlalchemy.orm import Session
from repository.transacao_repository import listar_todas_vantagens
from repository.empresa_repository import criar_vantagem, atualizar_vantagem


def listar_vantagens(db: Session):
    return listar_todas_vantagens(db)


def criar_vantagem_service(db: Session, empresa_id: int, descricao: str, foto: str, custo_moedas: int):
    return criar_vantagem(db, empresa_id, descricao, foto, custo_moedas)

def atualizar_vantagem_service(db: Session, vantagem_id: int, descricao: str, foto: str, custo_moedas: int):
    return atualizar_vantagem(db, vantagem_id, descricao, foto, custo_moedas)