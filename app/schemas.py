from pydantic import BaseModel
from datetime import date

class BookingCreate(BaseModel):
    name: str
    movie: str
    date: date
    seat: str

class BookingOut(BookingCreate):
    id: int

    class Config:
        orm_mode = True
