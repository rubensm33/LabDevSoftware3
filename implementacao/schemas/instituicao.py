from pydantic import BaseModel


class InstituicaoBase(BaseModel):
    id: int
    nome: str
    
    class Config:
        orm_mode = True
