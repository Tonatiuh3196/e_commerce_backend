from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Optional


class UserCreate(BaseModel):
    nombre: str | None = None
    ap_paterno: str | None = None
    ap_materno: str | None = None
    fecha: date | None = None
    email: str | None = None
    telefono: str | None = None
    sexo: str | None = None
    password : str | None = None

class UserRead(UserCreate):
    id: UUID

class UserUpdate(BaseModel):
    nombre: Optional[str] 
    ap_paterno: Optional[str] 
    ap_materno: Optional[str] 
    fecha: Optional[date] 
    email: Optional[str] 
    telefono: Optional[str] 
    sexo: Optional[str] 
    password : Optional[str]  
