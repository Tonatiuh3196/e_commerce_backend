from sqlmodel import Session, select
from models.cartShopping import CartShopping
from schemas.cartShopping import CartShoppingCreate
from fastapi import HTTPException
from uuid import UUID

def create_cartShopping(session: Session, cartShopping_data: CartShoppingCreate):
    cartShopping = CartShopping(
        user_id=cartShopping_data.user_id,
        products=[item.model_dump() for item in cartShopping_data.productos]
    )
    session.add(cartShopping)
    session.commit()
    session.refresh(cartShopping)
    return cartShopping

def get_cartShopping(session: Session, cartShopping_id: UUID):
    cartShopping = session.exec(select(CartShopping).where(CartShopping.id == cartShopping_id)).first()
    if not cartShopping:
        raise HTTPException(status_code=404, detail="CartShopping not found")
    return cartShopping

def delete_cartShopping(session: Session, cartShopping_id: UUID):
    cartShopping = get_cartShopping(session, cartShopping_id)
    session.delete(cartShopping)
    session.commit()

def update_cartShopping(session: Session, cartShopping_id: UUID, cartShopping_data: CartShoppingCreate):
    cartShopping= get_cartShopping(session, cartShopping_id)
    cartShopping.user_id = cartShopping_data.user_id
    cartShopping.products = [item.model_dump() for item in cartShopping_data.productos]
    session.add(cartShopping)
    session.commit()
    session.refresh(cartShopping)
    return cartShopping

