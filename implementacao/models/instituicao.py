from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Instituicao(Base):
    __tablename__ = "instituicoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)

    professores_instituicao = relationship("Professor", back_populates="instituicao_professor")
    alunos_instituicao = relationship("Aluno", back_populates="instituicao_aluno")
