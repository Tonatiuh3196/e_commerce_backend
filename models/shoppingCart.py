from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from models.shoppingCart_item import ShoppingCartItem

class ShoppingCart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")  # Asegúrate de que sea correcto

    # Relación con ShoppingCartItem (usamos string para evitar importación circular)
    items: List["ShoppingCartItem"] = Relationship(back_populates="cart")
