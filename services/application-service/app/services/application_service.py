from app.repository import application_repo
from app.core.exceptions import BadRequestException, NotFoundException


def apply_job(db, data, user):
    if user["role"] != "candidate":
        raise BadRequestException("Only candidates can apply")

    existing = application_repo.get_application(
        db,
        data.job_id,
        user["user_id"]
    )

    if existing:
        raise BadRequestException("Already applied")

    return application_repo.create_application(
        db,
        data.job_id,
        user["user_id"]
    )


def withdraw_job(db, job_id, user):
    app = application_repo.get_application(
        db,
        job_id,
        user["user_id"]
    )

    if not app:
        raise NotFoundException("Application not found")

    application_repo.delete_application(db, app)

    return {"message": "Application withdrawn"}


def update_status(db, job_id, data):
    app = application_repo.get_by_job(db, job_id)

    if not app:
        raise NotFoundException("Application not found")

    return application_repo.update_status(db, app, data.status)


def get_all_applications(db):
    return application_repo.get_all(db)

def get_candidate_applications(db, user):
    return application_repo.get_by_candidate(db, user["user_id"])


def get_job_applications(db, job_id):
    apps = application_repo.get_by_job(db, job_id)

    if not apps:
        raise NotFoundException("No applications found")

    return apps