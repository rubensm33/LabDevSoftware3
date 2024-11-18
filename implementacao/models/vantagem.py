from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.dialects.mysql import MEDIUMTEXT


class Vantagem(Base):
    __tablename__ = "vantagens"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    foto = Column(MEDIUMTEXT, nullable=True)
    custo_moedas = Column(Integer, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="vantagens")
