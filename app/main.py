# app/main.py

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from app.database.db import engine
from app.routers import users  # ton CRUD des users

app = FastAPI(title="Backend FastAPI + PostgreSQL")

from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
# 🔹 Inclure les routes CRUD utilisateurs
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
@app.get("/db-test")
def db_test():
    """
    Test rapide de la connexion à PostgreSQL.
    """
    try:
        conn = engine.connect()
        conn.close()
        return {"status": "Connexion PostgreSQL OK 🚀"}
    except SQLAlchemyError as e:
        return {"status": "Erreur", "detail": str(e)}
