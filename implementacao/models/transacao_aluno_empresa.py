from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base


class TransacaoAlunoEmpresa(Base):
    __tablename__ = "transacoes_aluno_empresa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    vantagem_id = Column(Integer, ForeignKey("vantagens.id"), nullable=False)
    valor = Column(Integer, nullable=False)
    data_transacao = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    aluno = relationship("Aluno")
    empresa = relationship("Empresa")
    vantagem = relationship("Vantagem")
