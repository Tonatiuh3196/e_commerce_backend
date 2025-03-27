from sqlmodel import SQLModel, Field
from typing import List, Optional
from sqlalchemy import Column, JSON

class Product(SQLModel, table=True):
    id: int = Field( primary_key=True)
    nombre: str
    descripcion: str
    precio: int 
    stock: bool
    categoria: List[str] = Field(default_factory=list, sa_column=Column(JSON))