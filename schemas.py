from pydantic import BaseModel, EmailStr

class ClassOut(BaseModel):
    id: str
    name: str
    datetime: str
    instructor: str
    available_slots: int

class BookingIn(BaseModel):
    class_id: str
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: str
    class_id: str
    class_name: str
    client_name: str
    client_email: EmailStr
    booked_at: str
