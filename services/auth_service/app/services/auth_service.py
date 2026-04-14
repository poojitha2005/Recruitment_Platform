from app.repository import user_repo
from app.repository import token_repo
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)


def register(db, data):
    # Check email
    if user_repo.get_user_by_email(db, data.email):
        return {"error": "Email already exists"}

    # Check phone
    if user_repo.get_user_by_phone(db, data.phone):
        return {"error": "Phone already exists"}

    # Hash password
    hashed = hash_password(data.password)

    # FIX: PASS ROLE HERE
    user = user_repo.create_user(
        db,
        data.name,
        data.email,
        data.phone,
        hashed,
        data.role  
    )

    return {
        "message": "User registered",
        "user_id": user.id,
        "role": user.role   
    }


def login(db, data):
    user = user_repo.get_user_by_email(db, data.email)

    if not user:
        return {"error": "Invalid email"}

    if not verify_password(data.password, user.password):
        return {"error": "Invalid password"}

    #  Ensure role is included
    payload = {
        "sub": user.email,
        "user_id": user.id,
        "role": user.role
    }

    access = create_access_token(payload)
    refresh = create_refresh_token(payload)

    token_repo.create_refresh_token(db, user.id, refresh)

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }