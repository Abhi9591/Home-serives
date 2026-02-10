from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class BookingCreate(BaseModel):
    service_id: UUID
    booking_time: Optional[datetime] = None  # Make optional
    address: str

class BookingOut(BaseModel):
    id: UUID
    customer_id: UUID
    service_id: UUID
    booking_time: datetime
    address: str
    status: str

    model_config = {
        "from_attributes": True
    }
