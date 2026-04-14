from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt
from app.repository import token_repo
from app.core.security import create_access_token
from app.db.session import get_db
from app.core.config import settings

router = APIRouter()

@router.post("/refresh")
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    
    # 1️ Check if token exists in DB
    token_data = token_repo.get_token(db, refresh_token)

    if not token_data:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    # 2️ Decode refresh token
    try:
        payload = jwt.decode(
            refresh_token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    # 3️ Create new access token with SAME payload
    new_access = create_access_token({
        "sub": payload["sub"],
        "user_id": payload["user_id"],
        "role": payload["role"]
    })

    return {
        "access_token": new_access,
        "token_type": "bearer"
    }