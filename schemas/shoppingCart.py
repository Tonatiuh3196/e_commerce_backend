from pydantic import BaseModel
from typing import List

class ShoppingCartItem(BaseModel):
    product_id: int
    quantity: int

class ShoppingCartItemCreate(ShoppingCartItem):
    """Esquema para agregar productos al carrito."""
    product_id:int
class ShoppingCartItemResponse(ShoppingCartItem):
    id: int
    user_id: int

class ShoppingCartResponse(BaseModel):
    user_id: int
    items: List[ShoppingCartItemResponse]