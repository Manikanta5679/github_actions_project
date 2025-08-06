from sqlalchemy.orm import Session
from . import models, schemas

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_all_bookings(db: Session):
    return db.query(models.Booking).all()