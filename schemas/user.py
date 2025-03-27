from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    apellido_paterno: str = Field(..., min_length=2, max_length=50)
    apellido_materno: str = Field(..., min_length=2, max_length=50)
    fecha_nacimiento: str
    email: EmailStr
    telefono: str = Field(..., min_length=10, max_length=15)
    sexo: str
    password: str

class UserCreate(UserBase):
    """Esquema para crear usuarios. Extiende UserBase y no necesita `id`."""
    id: int
class UserUpdate(BaseModel):
    """Esquema para actualizar datos de usuario, todos los campos opcionales."""
    nombre: Optional[str]
    apellido_paterno: Optional[str]
    apellido_materno: Optional[str]
    fecha_nacimiento: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]
    sexo: Optional[str]
    password: Optional[str]

class UserResponse(UserBase):
    """Esquema para devolver datos del usuario con `id`."""
    id: int