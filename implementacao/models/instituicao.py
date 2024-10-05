from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Instituicao(Base):
    __tablename__ = "instituicoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)

    alunos = relationship("Aluno", back_populates="instituicao")
    professores = relationship("Professor", back_populates="instituicao")
