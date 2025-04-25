from uuid import UUID, uuid4

from sqlalchemy.dialects import sqlite
from sqlmodel import Column, Field, SQLModel

class product(SQLModel, table=True):
    product_id: UUID = Field(default_factory=uuid4, foreign_key="product.id")
    cantidad: int

class CardShopping(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(default_factory=uuid4, foreign_key="user.id")
    products: list[product] = Field(sa_column=Column(sqlite.JSON))