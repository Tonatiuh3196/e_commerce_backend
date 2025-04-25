from pydantic import BaseModel,  HttpUrl
from uuid import UUID
from typing import Optional

class ProductCreate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    img:  HttpUrl  | None = None
    precio: int | None = None
    categoria: list[str] | None = None

class ProductRead(ProductCreate):
    id:UUID

class productUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    img: Optional[HttpUrl]
    precio: Optional[int]
    categoria: Optional[list[str]]