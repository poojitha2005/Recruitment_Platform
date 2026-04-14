from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.application import ApplyRequest, UpdateStatus
from app.services import application_service
from app.db.session import get_db
from app.dependencies.auth import require_role

router = APIRouter()


#  Candidate apply
@router.post("/apply")
def apply(
    data: ApplyRequest,
    db: Session = Depends(get_db),
    user=Depends(require_role(["candidate"]))
):
    return application_service.apply_job(db, data, user)


#  Withdraw
@router.delete("/withdraw/{job_id}")
def withdraw(
    job_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["candidate"]))
):
    return application_service.withdraw_job(db, job_id, user)


# Recruiter update status
@router.put("/status/{job_id}")
def update_status(
    job_id: int,
    data: UpdateStatus,
    db: Session = Depends(get_db),
    user=Depends(require_role(["recruiter"]))
):
    return application_service.update_status(db, job_id, data)


# Get all
@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return application_service.get_all_applications(db)


@router.get("/my-applications")
def my_applications(
    db: Session = Depends(get_db),
    user=Depends(require_role(["candidate"]))
):
    return application_service.get_candidate_applications(db, user)


@router.get("/job/{job_id}")
def job_applications(
    job_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["recruiter"]))
):
    return application_service.get_job_applications(db, job_id)