from app.models.refresh_token import RefreshToken

def create_refresh_token(db, user_id, token):
    obj = RefreshToken(user_id=user_id, token=token)
    db.add(obj)
    db.commit()
    return obj

def get_token(db, token):
    return db.query(RefreshToken).filter(RefreshToken.token == token).first()