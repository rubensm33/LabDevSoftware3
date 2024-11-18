from .user import User, UserBase
from pydantic import BaseModel
from .instituicao import InstituicaoBase

class AlunoBase(User):
    cpf: str
    rg: str
    instituicao_aluno: InstituicaoBase
    curso: str
    saldo_moedas: int

    class Config:
        orm_mode = True


class AlunoCreate(BaseModel):
    email: str
    nome: str
    cpf: str
    hashed_password: str
    rg: str
    instituicao: str
    curso: str

class AlunoSaldoResponse(BaseModel):
    aluno_id: int
    saldo_moedas: int

    class Config:
        orm_mode = True

class AlunoConsulta(UserBase):
    id: int
    instituicao_aluno: InstituicaoBase
    curso: str

    class Config:
        orm_mode = True

