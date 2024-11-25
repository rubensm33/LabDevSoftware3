from pydantic import BaseModel
from typing import List

class VantagemCreate(BaseModel):
    descricao: str
    foto: str
    custo_moedas: int

class VantagemUpdate(BaseModel):
    descricao: str
    foto: str
    custo_moedas: int

class VantagemResponse(BaseModel):
    id: int
    descricao: str
    foto: str
    custo_moedas: int
    empresa_id: int

    class Config:
        orm_mode = True

class ListaVantagensResponse(BaseModel):
    vantagens: List[VantagemResponse]

    class Config:
        orm_mode = True