from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from config.database import Base


class Aluno(User):
    __tablename__ = "alunos"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))

    instituicao = relationship("Instituicao", back_populates="alunos")
