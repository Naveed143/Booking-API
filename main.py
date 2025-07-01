from fastapi import FastAPI, HTTPException, Query
from pydantic import EmailStr
from datetime import datetime
import pytz
from typing import List, Optional
import uuid
import logging

from database import classes, bookings
from schemas import ClassOut, BookingIn, BookingOut
from utils import convert_to_timezone


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Fitness Booking API")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Fitness Booking API. Visit /docs for Swagger UI."
    }

@app.get("/classes", response_model=List[ClassOut])
def get_classes(timezone: Optional[str] = Query(default="Asia/Kolkata")):
    return [
        {
            "id": c["id"],
            "name": c["name"],
            "datetime": convert_to_timezone(c["datetime"], timezone),
            "instructor": c["instructor"],
            "available_slots": c["available_slots"]
        }
        for c in classes
    ]

@app.post("/book", response_model=BookingOut)
def book_class(booking: BookingIn):
    for c in classes:
        if c["id"] == booking.class_id:
            if c["available_slots"] <= 0:
                raise HTTPException(status_code=400, detail="No slots available")
            c["available_slots"] -= 1
            booking_id = str(uuid.uuid4())
            booked_at = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M %Z')
            new_booking = {
                "id": booking_id,
                "class_id": c["id"],
                "class_name": c["name"],
                "client_name": booking.client_name,
                "client_email": booking.client_email,
                "booked_at": booked_at
            }
            bookings.append(new_booking)
            return new_booking
    raise HTTPException(status_code=404, detail="Class ID not found")

@app.get("/bookings", response_model=List[BookingOut])
def get_bookings(client_email: EmailStr):
    return [b for b in bookings if b["client_email"] == client_email]
