from sqlalchemy.orm import Session
from repository.empresa_repository import criar_empresa_com_vantagens
from schemas.empresa import EmpresaCreate

def cadastrar_empresa(db: Session, empresa_data: EmpresaCreate):
    try:
        empresa = criar_empresa_com_vantagens(
            db=db,
            nome=empresa_data.nome,
            email=empresa_data.email,
            senha=empresa_data.senha,
            vantagens_data=empresa_data.vantagens
        )
        return empresa
    except Exception as e:
        raise ValueError(f"Erro ao cadastrar empresa: {str(e)}")
