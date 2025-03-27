from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserUpdate, UserResponse
from gateways.user import UserGateway
from sqlmodel import Session
from database import get_session

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return UserGateway.create_user(user, session)

@router.get("/", response_model=list[UserResponse])
def get_users(session: Session = Depends(get_session)):
    return UserGateway.get_users(session)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, session: Session = Depends(get_session)):
    return UserGateway.get_user(user_id, session)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(get_session)):
    return UserGateway.update_user(user_id, user, session)

@router.patch("/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, data: dict, session: Session = Depends(get_session)):
    return UserGateway.patch_user(user_id, data, session)

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    return UserGateway.delete_user(user_id, session)