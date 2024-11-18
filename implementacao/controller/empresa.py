from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.vantagem import ListaVantagensResponse
from services.empresa_service import cadastrar_empresa
from schemas.empresa import EmpresaCreate, EmpresaResponse, EmpresaHome
from services.vantagem_service import listar_vantagens
from models.empresa import Empresa

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


@router.get("/", response_model=list[EmpresaHome])
def listar_empresas(db: Session = Depends(get_db)):
    try:
        empresas = db.query(Empresa).all()
        empresas_response = []
        for empresa in empresas:

            empresas_response.append(
                {
                    "id": empresa.id,
                    "nome": empresa.nome,
                    "email": empresa.email,
                }
            )

        return empresas_response

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar empresas: {str(e)}")


@router.get("/{empresa_id}/vantagens", response_model=list[dict])
def listar_vantagens_empresa(empresa_id: int, db: Session = Depends(get_db)):
    try:
        empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
        if not empresa:
            raise HTTPException(status_code=404, detail="Empresa não encontrada")

        vantagens = [
            {
                "id": vantagem.id,
                "descricao": vantagem.descricao,
                "foto": f"data:image/jpeg;base64,{vantagem.foto}" if vantagem.foto else None,
                "custo_moedas": vantagem.custo_moedas,
            }
            for vantagem in empresa.vantagens
        ]

        return vantagens

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar vantagens: {str(e)}")
