from http.client import HTTPException
from fastapi import Depends, HTTPException, status, Path, APIRouter
from models import ToDos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user


router = APIRouter(
prefix = '/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todos", status_code=status.HTTP_200_OK)
async def readall(user: user_dependency, db: db_dependency):
    if user is None  or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authenticated Failed')
    return db.query(ToDos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,db: db_dependency, todo_id: int = Path(gt=0)):

    # CHECK IF USER IS REAL ADMIN
    if user is None  or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authenticated Failed')

    todo_model = db.query(ToDos).filter(ToDos.id == todo_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail='Todo Not Found !')
    db.query(ToDos).filter(ToDos.id == todo_id).delete()
    db.commit()
