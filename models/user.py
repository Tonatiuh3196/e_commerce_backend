from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id:int = Field( primary_key=True)
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    fecha_nacimiento: str
    email: str
    telefono: str
    sexo: str
    password: str