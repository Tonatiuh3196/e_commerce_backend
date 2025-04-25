from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate, UserUpdate
from pydantic import TypeAdapter
from fastapi import HTTPException

adapter_create = TypeAdapter(UserCreate)
adapter_update = TypeAdapter(UserUpdate)

def create_user(session: Session, user_create: UserCreate):
    user_data = adapter_create.validate_python(user_create)
    user = User(**user_data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(session: Session, user_id: int):
    return session.exec(select(User).where(User.id == user_id)).first()

def delete_user(session: Session, user_id: int):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()

def update_user(session: Session, user_id: int, user_update: UserCreate):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = adapter_create.validate_python(user_update).model_dump()
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def patch_user(session: Session, user_id, user_patch: UserUpdate):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = adapter_update.validate_python(user_patch).model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user