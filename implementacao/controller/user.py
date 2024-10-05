from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from schemas import user, items
from models import user as user_model, scopes as scopes_model, items as items_model
from repository import user_repository
from config.database import SessionLocal, engine, get_db
from services.user_service import get_current_active_user

router = APIRouter(prefix="/users")
@router.post("/", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = user_repository.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repository.create_user(db=db, user=user)

@router.get("/me", response_model=user.User)
async def read_users_me(
    current_user: Annotated[user_model.User, Depends(get_current_active_user)]
):
    return current_user

@router.get("/", response_model=list[user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_repository.get_users(db, skip=skip, limit=limit)
    print(users[0].user_scopes)
    return users


@router.get("/{user_id}", response_model=user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/items", response_model=items.Item)
def create_item_for_user(
    user_id: int, item: items.ItemCreate, db: Session = Depends(get_db)
):
    return user_repository.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items", response_model=list[items.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = user_repository.get_items(db, skip=skip, limit=limit)
    return items