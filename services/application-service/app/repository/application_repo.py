from app.models.application import Application

def create_application(db, job_id, candidate_id):
    app = Application(
        job_id=job_id,
        candidate_id=candidate_id
    )
    db.add(app)
    db.commit()
    db.refresh(app)
    return app


def get_application(db, job_id, candidate_id):
    return db.query(Application).filter(
        Application.job_id == job_id,
        Application.candidate_id == candidate_id
    ).first()


def get_by_job(db, job_id):
    return db.query(Application).filter(Application.job_id == job_id).first()


def get_all(db):
    return db.query(Application).all()


def update_status(db, app, status):
    app.status = status
    db.commit()
    db.refresh(app)
    return app


def delete_application(db, app):
    db.delete(app)
    db.commit()

def get_by_candidate(db, candidate_id):
    return db.query(Application).filter(
        Application.candidate_id == candidate_id
    ).all()


def get_by_job(db, job_id):
    return db.query(Application).filter(
        Application.job_id == job_id
    ).all()