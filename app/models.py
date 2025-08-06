from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    movie = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    seat = Column(String, nullable=False)
