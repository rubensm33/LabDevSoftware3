from sqlalchemy import ForeignKey, Column, Integer

from config.database import Base


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    receiver_id = Column(Integer)
    payer_id = Column(Integer)

