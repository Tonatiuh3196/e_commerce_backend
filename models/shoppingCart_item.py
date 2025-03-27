from sqlmodel import SQLModel, Field, Relationship
from typing import Optional



class ShoppingCartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="shoppingcart.id")  
    product_id: int = Field(foreign_key="product.id")
    quantity: int = Field(default=1)

    # Relación con ShoppingCart (usamos string en vez de importación directa)
    cart: Optional["ShoppingCartItem"] = Relationship(back_populates="items")
