from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base


class TransacaoProfessorAluno(Base):
    __tablename__ = "transacoes_professor_aluno"

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    valor = Column(Integer, nullable=False)
    motivo = Column(String(255), nullable=False)
    data_transacao = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    professor = relationship("Professor")
    aluno = relationship("Aluno")
