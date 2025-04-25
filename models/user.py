from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field

from datetime import date

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    ap_paterno: str
    ap_materni: str
    fecha: date
    email: str
    telefono: str
    sexo: str
    password: str