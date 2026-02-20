# app/database/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔹 Infos PostgreSQL (à adapter si tu changes le mot de passe)
DB_USER = "akomba_user"
DB_PASSWORD = "Andry13"       # mot de passe simple sans caractères spéciaux
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "backend_db"

# 🔹 URL complète SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 🔹 Création de l'engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  # echo=True affiche les requêtes SQL dans la console

# 🔹 Session pour FastAPI
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 🔹 Base pour les modèles SQLAlchemy
Base = declarative_base()

# 🔹 Dépendance FastAPI
def get_db():
    """
    Fournit une session DB à FastAPI via Depends.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
