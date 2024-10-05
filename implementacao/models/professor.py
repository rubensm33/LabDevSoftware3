from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from .user import User
from config.database import Base


class Professor(User):
    __tablename__ = "professores"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))

    instituicao = relationship("Instituicao", back_populates="professores")
