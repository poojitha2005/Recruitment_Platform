from fastapi import APIRouter

router = APIRouter()

@router.post("/forgot")
def forgot(email: str):
    return {"msg": "Reset link sent"}

@router.post("/reset")
def reset():
    return {"msg": "Password reset successful"}