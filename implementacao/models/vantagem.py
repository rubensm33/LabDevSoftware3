from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

from config.database import Base


class Vantagem(Base):
    __tablename__ = "vantagens"

    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    vantagens = relationship("Empresa", back_populates="vantagem")
