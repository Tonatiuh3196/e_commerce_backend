from uuid import UUID, uuid4

from sqlalchemy.dialects import sqlite 
from sqlmodel import Column, Field, SQLModel

class Product(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    descripcion: str
    img: str
    precio: int
    categoria: list[str] = Field(sa_column=Column(sqlite.JSON))