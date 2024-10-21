from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.vantagem import ListaVantagensResponse
from services.empresa_service import cadastrar_empresa
from schemas.empresa import EmpresaCreate, EmpresaResponse
from services.vantagem_service import listar_vantagens

router = APIRouter(prefix="/empresas")

@router.post("/", response_model=EmpresaResponse)
def criar_empresa(empresa_data: EmpresaCreate, db: Session = Depends(get_db)):
    try:
        empresa = cadastrar_empresa(db=db, empresa_data=empresa_data)
        return empresa
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/vantagens", response_model=ListaVantagensResponse)
def consultar_vantagens(db: Session = Depends(get_db)):
    try:
        vantagens = listar_vantagens(db=db)
        return {"vantagens": vantagens}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))