from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .user import User


class Aluno(User):
    __tablename__ = "alunos"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))
    saldo_moedas = Column(Integer)

    instituicao = relationship("Instituicao", back_populates="alunos")
