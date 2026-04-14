from fastapi import FastAPI
from app.routes import job
from app.db.base import Base
from app.db.session import engine

from app.models import job as job_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(job.router, prefix="/jobs")

@app.get("/")
def home():
    return {"msg": "Job Service Running"}