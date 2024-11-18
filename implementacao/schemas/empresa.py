# schemas/empresa.py
from pydantic import BaseModel
from typing import List, Optional

class VantagemCreate(BaseModel):
    descricao: str
    foto: Optional[str]
    custo_moedas: int

class EmpresaCreate(BaseModel):
    nome: str
    email: str
    senha: str
    vantagens: List[VantagemCreate]

class EmpresaResponse(BaseModel):
    id: int
    nome: str
    email: str
    vantagens: List[VantagemCreate]

    class Config:
        orm_mode = True

class VantagemResponse(BaseModel):
    id: int
    descricao: str
    foto: Optional[str]
    custo_moedas: int

    class Config:
        orm_mode = True
class EmpresaHome(BaseModel):
    id: int
    nome: str
    email: str


    class Config:
        orm_mode = True

