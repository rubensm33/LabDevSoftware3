from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Vantagem(Base):
    __tablename__ = "vantagens"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    foto = Column(String(255), nullable=True)
    custo_moedas = Column(Integer, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="vantagens")
