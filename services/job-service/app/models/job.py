from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    salary = Column(String)
    recruiter_id = Column(Integer)