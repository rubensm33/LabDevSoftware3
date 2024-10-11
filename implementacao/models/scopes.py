from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from config.database import Base


class ScopeEnum(enum.Enum):
    admin = "admin"
    me = "me"
    items = "items"
    professor = "professor"
    empresa= "empresa"
    aluno = "aluno"

class UserScopes(Base):
    __tablename__ = "user_scopes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scope = Column(Enum(ScopeEnum), nullable=False)

    user = relationship("User", back_populates="user_scopes")
