from pydantic  import BaseModel, Field
from uuid import UUID, uuid4

class items(BaseModel):
    product_id: UUID = Field(default_factory=uuid4)
    cantidad:int | None = None

class CardShoppingCreate(BaseModel):
    user_id: UUID = Field(default_factory=uuid4) 
    productos: list[items] | None = None

