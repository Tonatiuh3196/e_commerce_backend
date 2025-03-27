from sqlmodel import Session, select
from models.shoppingCart import ShoppingCart
from models.shoppingCart_item import ShoppingCartItem
from fastapi import Depends, HTTPException
from database import get_session

class ShoppingCartGateway:
    @classmethod
    def get_shoppingCart(cls, user_id: int, session: Session = Depends(get_session)):
        cart = session.exec(select(ShoppingCart).where(ShoppingCart.user_id == user_id)).first()
        if not ShoppingCart:
            new_shoppingCart = ShoppingCart(user_id=user_id)
            session.add(new_shoppingCart)
            session.commit()
            session.refresh(new_shoppingCart)
        return new_shoppingCart

    @classmethod
    def add_shoppingCart(cls, user_id: int, product_id: int, quantity: int, session: Session = Depends(get_session)):
        cart = cls.get_shoppingCart(user_id, session)

        item = session.exec(
            select(ShoppingCartItem).where(
                ShoppingCartItem.user_id == user_id, ShoppingCartItem.product_id == product_id
            )
        ).first()

        if item:
            item.quantity += quantity
        else:
            item = ShoppingCartItem(user_id=user_id, product_id=product_id, quantity=quantity)
            session.add(item)

        session.commit()
        session.refresh(item)
        return cart

    @classmethod
    def remove_from_cart(cls, user_id: int, product_id: int, session: Session = Depends(get_session)):
        item = session.exec(
            select(ShoppingCartItem).where(
                ShoppingCartItem.user_id == user_id, ShoppingCartItem.product_id == product_id
            )
        ).first()

        if not item:
            raise HTTPException(status_code=404, detail="Item not found in cart")

        session.delete(item)
        session.commit()

        return cls.get_shopping_cart(user_id, session)

    @classmethod
    def clear_cart(cls, user_id: int, session: Session = Depends(get_session)):
        session.exec(select(ShoppingCartItem).where(ShoppingCartItem.user_id == user_id)).delete()
        session.commit()
        return cls.get_shopping_cart(user_id, session)