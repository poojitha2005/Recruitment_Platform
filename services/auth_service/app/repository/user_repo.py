from app.models.user import User

def get_user_by_email(db, email):
    return db.query(User).filter(User.email == email).first()


def get_user_by_phone(db, phone):
    return db.query(User).filter(User.phone == phone).first()


# role added
def create_user(db, name, email, phone, password, role):
    user = User(
        name=name,
        email=email,
        phone=phone,
        password=password,
        role=role   
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user