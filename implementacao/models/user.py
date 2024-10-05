from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    user_scopes = relationship("UserScopes", back_populates="user")
    instituicao = relationship("Instituicao", back_populates="aluno")