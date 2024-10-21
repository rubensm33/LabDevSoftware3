from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.user import User


class Aluno(User):
    __tablename__ = "alunos"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))
    cpf = Column(String(11), nullable=False)
    rg = Column(String(8), nullable=False)
    curso = Column(String(255), nullable=False)
    saldo_moedas = Column(Integer)

    instituicao_aluno = relationship("Instituicao", back_populates="alunos_instituicao")
