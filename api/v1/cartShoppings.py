from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from db.session import get_session
from sqlmodel import Session
from schemas.cartShopping import CartShoppingCreate
from models.cartShopping import CartShopping
from crud.cartShopping import create_cartShopping, get_cartShopping, delete_cartShopping, update_cartShopping

router = APIRouter()

@router.post("/cartShopping", response_model=CartShopping)
def create(cartShopping_data: CartShoppingCreate, session: Session = Depends(get_session)):
    return create_cartShopping(session, cartShopping_data)

@router.get("/cartShopping/{cartShopping_id}", response_model=CartShopping)
def read(cartShopping_id: UUID, session: Session = Depends(get_session)):
    return get_cartShopping(session, cartShopping_id)

@router.delete("/cartShopping/{cartShopping_id}", status_code=204)
def delete(cartShopping_id: UUID, session: Session = Depends(get_session)):
    delete_cartShopping(session, cartShopping_id)

@router.put("/cartShopping/{cartShopping_id}", response_model=CartShopping)
def update(cartShopping_id: UUID, cartShopping_data: CartShoppingCreate, session: Session = Depends(get_session)):
    return update_cartShopping(session, cartShopping_id, cartShopping_data)
