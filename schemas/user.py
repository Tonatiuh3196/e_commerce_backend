from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Optional


class UserCreate(BaseModel):
    nombre: Optional[str] = None
    ap_paterno: Optional[str] = None
    ap_materno: Optional[str] = None
    fecha: Optional[date] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    sexo: Optional[str] = None
    password: Optional[str] = None

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
