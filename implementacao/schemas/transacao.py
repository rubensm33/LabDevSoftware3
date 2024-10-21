from pydantic import BaseModel, conint
import datetime


class TransacaoProfessorAlunoCreate(BaseModel):
    aluno_id: int
    valor: int
    motivo: str


class TransacaoProfessorAlunoResponse(BaseModel):
    professor_id: int
    aluno_id: int
    valor: int
    motivo: str
    data_transacao: datetime.datetime

    class Config:
        orm_mode = True


class TransacaoAlunoEmpresaResponse(BaseModel):
    vantagem_id: int
    aluno_id: int
    valor: int
    data_transacao: datetime.datetime

    class Config:
        orm_mode = True


class CompraVantagemRequest(BaseModel):
    aluno_id: int
    vantagem_id: int


class VantagemRequest(BaseModel):
    vantagem_id: int
