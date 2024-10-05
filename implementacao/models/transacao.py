from sqlalchemy import  Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base
import enum


class TipoTransacao(enum.Enum):
    professor_para_aluno = "professor_para_aluno"
    aluno_para_empresa = "aluno_para_empresa"


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    tipo_transacao = Column(Enum(TipoTransacao), nullable=False)

    payer_id = Column(Integer)
    payer_type = Column(String(50))

    receiver_id = Column(Integer)
    receiver_type = Column(String(50))

    valor = Column(Integer, nullable=False)
    motivo = Column(String(255), nullable=False)

    aluno_payer = relationship("Aluno", foreign_keys=[payer_id], uselist=False)
    professor_payer = relationship("Professor", foreign_keys=[payer_id], uselist=False)
    aluno_receiver = relationship("Aluno", foreign_keys=[receiver_id], uselist=False)
    empresa_receiver = relationship("Empresa", foreign_keys=[receiver_id], uselist=False)
