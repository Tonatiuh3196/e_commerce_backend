from fastapi import APIRouter, Depends
from gateways.shoppingCart import ShoppingCartGateway
from schemas.shoppingCart import ShoppingCartResponse, ShoppingCartItemCreate
from sqlmodel import Session
from database import get_session

router = APIRouter()

@router.get("/{user_id}", response_model=ShoppingCartResponse)
def get_shoppingCart(user_id: int, session: Session = Depends(get_session)):
    return ShoppingCartGateway.get_shoppingCart(user_id, session)

@router.post("/{user_id}", response_model=ShoppingCartResponse)
def add_to_cart(user_id: int, item: ShoppingCartItemCreate, session: Session = Depends(get_session)):
    return ShoppingCartGateway.add_shoppingCart(user_id, item.product_id, item.quantity, session)

@router.delete("/{user_id}/{product_id}", response_model=ShoppingCartResponse)
def delete_shoppingCart(user_id: int, product_id: int, session: Session = Depends(get_session)):
    return ShoppingCartGateway.delete_Shoppincart(user_id, product_id, session)

@router.delete("/{user_id}/clear", response_model=ShoppingCartResponse)
def clear_shoppingCart(user_id: int, session: Session = Depends(get_session)):
    return ShoppingCartGateway.clear_shoppingCart(user_id, session)