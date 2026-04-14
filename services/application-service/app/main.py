from fastapi import FastAPI
from app.routes import application
from app.db.base import Base
from app.db.session import engine

from app.models import application as app_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(application.router, prefix="/applications")

@app.get("/")
def home():
    return {"msg": "Application Service Running"}