from pydantic import BaseModel, Field
from typing import Optional, List

class ProductBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: str
    precio: float = Field(..., gt=0)  # Precio debe ser mayor que 0
    stock: bool
    categoria: List[str]

class ProductCreate(ProductBase):
    """Esquema para crear un producto."""
    id:int

class ProductUpdate(BaseModel):
    """Esquema para actualizar productos, con todos los campos opcionales."""
    nombre: Optional[str]
    descripcion: Optional[str]
    precio: Optional[float]
    stock: Optional[bool]
    categoria: Optional[List[str]]

class ProductResponse(ProductBase):
    """Esquema de respuesta con `id`."""
    id: int
