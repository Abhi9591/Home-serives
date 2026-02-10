from fastapi import APIRouter, Depends, Header, HTTPException, Response
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime
from app.database import get_db
from app.models.customer import Customer
from app.models.booking import Booking
from app.models.service import Service
from app.schemas.booking import BookingCreate, BookingOut

router = APIRouter(prefix="/api/bookings", tags=["Bookings"])

@router.post("", response_model=BookingOut, status_code=201)
def create_booking(
    payload: BookingCreate,
    response: Response,
    x_customer_id: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    # 1️⃣ Resolve or create customer
    if x_customer_id:
        try:
            customer_uuid = UUID(x_customer_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid X-Customer-Id header")
        customer = db.get(Customer, customer_uuid)
        if not customer:
            customer = Customer(id=customer_uuid)
            db.add(customer)
            db.commit()
            db.refresh(customer)
    else:
        # Create a new customer and return its id in response headers
        new_id = uuid4()
        customer = Customer(id=new_id)
        db.add(customer)
        db.commit()
        db.refresh(customer)
        response.headers["X-Customer-Id"] = str(customer.id)

    # 2️⃣ Validate service exists
    service = db.get(Service, payload.service_id)
    if not service:
        raise HTTPException(status_code=400, detail="Service does not exist")

    # 3️⃣ Use default booking_time if not provided
    booking_time = payload.booking_time or datetime.utcnow()

    # 4️⃣ Create booking
    booking = Booking(
        customer_id=customer.id,
        service_id=service.id,
        booking_time=booking_time,
        address=payload.address,
        status="CREATED"
    )

    # 5️⃣ Save booking safely
    try:
        db.add(booking)
        db.commit()
        db.refresh(booking)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    # Always include customer id in response header so client can persist it
    response.headers.setdefault("X-Customer-Id", str(customer.id))
    return booking
