from app.database.db import engine
from app.models.user import Base
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import engine
from models.user import Base
# Crée toutes les tables définies dans Base
Base.metadata.create_all(bind=engine)

print("Tables créées avec succès ! ✅")
