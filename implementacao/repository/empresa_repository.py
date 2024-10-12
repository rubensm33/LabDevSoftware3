# repository/empresa_repository.py
from sqlalchemy.orm import Session
from models.empresa import Empresa
from models.vantagem import Vantagem
from models.scopes import UserScopes
from models.user import User
from services.token_service import hash_password


def criar_empresa_com_vantagens(db: Session, nome: str, email: str, senha: str, vantagens_data: list):
    hashed_password = hash_password(senha)
    empresa_user = Empresa(nome=nome, email=email, hashed_password=hashed_password, role="empresa")

    scope_me = UserScopes(user_id=empresa_user.id, scope="me")
    scope_empresa = UserScopes(user_id=empresa_user.id, scope="empresa")

    db.add(empresa_user)
    db.add(scope_me)
    db.add(scope_empresa)
    db.commit()
    db.refresh(empresa_user)

    for vantagem_data in vantagens_data:
        vantagem = Vantagem(
            descricao=vantagem_data.descricao,
            foto=vantagem_data.foto,
            custo_moedas=vantagem_data.custo_moedas,
            empresa_id=empresa_user.id,
        )
        db.add(vantagem)

    db.commit()

    return empresa_user
