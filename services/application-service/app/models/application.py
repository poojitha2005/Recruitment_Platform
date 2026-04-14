from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer)
    candidate_id = Column(Integer)
    status = Column(String, default="applied")