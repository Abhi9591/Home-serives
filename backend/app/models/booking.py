import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.models.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"))
    booking_time = Column(DateTime(timezone=True), nullable=False)
    address = Column(String, nullable=False)
    status = Column(String, default="CREATED")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
