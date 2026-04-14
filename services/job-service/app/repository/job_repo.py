from app.models.job import Job

def create_job(db, data, recruiter_id):
    job = Job(**data.dict(), recruiter_id=recruiter_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_jobs(db):
    return db.query(Job).all()


def get_job_by_id(db, job_id):
    return db.query(Job).filter(Job.id == job_id).first()


def update_job(db, job, data):
    for key, value in data.dict().items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job


def delete_job(db, job):
    db.delete(job)
    db.commit()