from .user import User


class AlunoBase(User):
    cpf: str
    rg: str
    instituicao: str
    curso: str
    quantidade_moedas: int
    
    class Config:
        orm_mode = True


