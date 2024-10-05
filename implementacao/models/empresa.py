from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship
from .user import User


class Empresa(User):
    __tablename__ = "empresas"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    vantagem = relationship("Vantagem", back_populates="empresa")
