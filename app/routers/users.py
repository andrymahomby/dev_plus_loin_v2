from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models import crud_user
from app.schemas.user import UserCreate
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return crud_user.create_user(db, username, email, password)

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)
