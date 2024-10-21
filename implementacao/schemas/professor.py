from pydantic import BaseModel

class ProfessorSaldoResponse(BaseModel):
    professor_id: int
    saldo_moedas: int

    class Config:
        orm_mode = True
