from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.job import JobCreate
from app.services import job_service
from app.db.session import get_db
from app.dependencies.auth import require_role

router = APIRouter()


# ✅CREATE JOB (Recruiter only)
@router.post("/")
def create_job(
    data: JobCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["recruiter"]))
):
    return job_service.create_job(db, data, user)


# GET ALL JOBS
@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return job_service.get_jobs(db)


# UPDATE JOB (OWNER ONLY)
@router.put("/{job_id}")
def update_job(
    job_id: int,
    data: JobCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["recruiter"]))
):
    return job_service.update_job(db, job_id, data, user)


# DELETE JOB (OWNER ONLY)
@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["recruiter"]))
):
    return job_service.delete_job(db, job_id, user)