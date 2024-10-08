from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .user import User


class Professor(User):
    __tablename__ = "professores"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))
    saldo_moedas = Column(Integer, default=1000)

    instituicao = relationship("Instituicao", back_populates="professores")
