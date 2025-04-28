from uuid import UUID, uuid4

from sqlalchemy.dialects import sqlite
from sqlmodel import Column, Field, SQLModel, Relationship

class CartProduct(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="product.id")
    cantidad: int
    cart_shopping_id:UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="cartshopping.id")

    cart_shopping: "CartShopping" = Relationship(back_populates="products")

class CartShopping(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(default_factory=uuid4, foreign_key="user.id")
    products: list[CartProduct] = Relationship(back_populates="cart_shopping")