from pydantic import BaseModel
from .scopes import Scope


class UserBase(BaseModel):
    email: str
    nome: str
    role: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    user_scopes: list[Scope] = []

    class Config:
        orm_mode = True
