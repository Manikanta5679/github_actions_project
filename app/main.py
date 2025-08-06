from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    bookings = crud.get_all_bookings(db)
    return templates.TemplateResponse("index.html", {"request": request, "bookings": bookings})

@app.post("/book")
def book_movie(
    name: str = Form(...),
    movie: str = Form(...),
    date: str = Form(...),
    seat: str = Form(...),
    db: Session = Depends(get_db),
):
    booking = schemas.BookingCreate(name=name, movie=movie, date=date, seat=seat)
    crud.create_booking(db, booking)
    return {"message": "Booking successful"}
