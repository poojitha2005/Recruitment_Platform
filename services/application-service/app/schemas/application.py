from pydantic import BaseModel

class ApplyRequest(BaseModel):
    job_id: int


class UpdateStatus(BaseModel):
    status: str