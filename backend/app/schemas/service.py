from pydantic import BaseModel
from uuid import UUID

class ServiceOut(BaseModel):
    id: UUID
    name: str
    description: str
    price: int

    model_config = {
        "from_attributes": True
    }
