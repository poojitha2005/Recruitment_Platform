from app.repository import job_repo
from app.core.exceptions import NotFoundException, ForbiddenException


def create_job(db, data, user):
    return job_repo.create_job(db, data, user["user_id"])


def get_jobs(db):
    return job_repo.get_jobs(db)


def update_job(db, job_id, data, user):
    job = job_repo.get_job_by_id(db, job_id)

    if not job:
        raise NotFoundException("Job not found")

    #  Ownership check
    if job.recruiter_id != user["user_id"]:
        raise ForbiddenException("You are not allowed to update this job")

    return job_repo.update_job(db, job, data)


def delete_job(db, job_id, user):
    job = job_repo.get_job_by_id(db, job_id)

    if not job:
        raise NotFoundException("Job not found")

    # 🔥 Ownership check
    if job.recruiter_id != user["user_id"]:
        raise ForbiddenException("You are not allowed to delete this job")

    job_repo.delete_job(db, job)

    return {"message": "Job deleted successfully"}