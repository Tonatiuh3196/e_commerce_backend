from fastapi import APIRouter, Depends, HTTPException

from schemas.user import UserCreate, UserRead, UserUpdate
from crud.user import create_user, get_user, delete_user, update_user, patch_user 
from db.session import get_session

router = APIRouter()

@router.post("/user", response_model=UserRead)
def create(user: UserCreate, session=Depends(get_session)):
    return create_user(session, user)

@router.get("/user/{user_id}", response_model=UserRead)
def read(user_id: int, session = Depends(get_session)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.delete("/user/{user_id}", status_code=204)
def delete(user_id: int, session = Depends(get_session)):
    delete_user(session, user_id)

@router.put("/user/{user_id}", response_model=UserRead)
def update(user_id: int, user_update: UserUpdate, session = Depends(get_session)):
    return update_user(session, user_id, user_update)

@router.patch("/user/{user_id}", response_model=UserRead)
def patch(user_id: int, user_patch: UserCreate, session=Depends(get_session)):
    return patch_user(session, user_id, user_patch)
