from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routes import auth, refresh, password
from app.db.base import Base
from app.db.session import engine

from app.models import user, refresh_token


Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBearer()

app.include_router(auth.router, prefix="/auth")
app.include_router(refresh.router, prefix="/auth")
app.include_router(password.router, prefix="/password")

@app.get("/")
def home():
    return {"msg": "Auth Service Running"}