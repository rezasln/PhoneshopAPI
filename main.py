# Import necessary libraries and files
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import PhoneBase  # Import PhoneBase model from schemas.py
from models import models
from db import engine, SessionLocal

# Initialize FastAPI application
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency injection for database session
db_dependency = Depends(get_db)

# FastAPI endpoint to create a new phone record
@app.post("/phone/", tags=["Phone", "POST"])
async def create_phone(phone: PhoneBase, db: Session = db_dependency):
    db_phone = models.Phone(
        id=phone.id,
        model=phone.model,
        brand=phone.brand,
        price=phone.price,
        battery=phone.battery
    )
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

# FastAPI endpoint to retrieve all phone records
@app.get("/phone/", tags=["Phone","GET"])
async def get_phones(skip: int = 0, limit: int = 10, db: Session = db_dependency):
    return db.query(models.Phone).offset(skip).limit(limit).all()

# FastAPI endpoint to retrieve a specific phone record by ID
@app.get("/phone/{phone_id}", tags=["Phone","GET"])
async def get_phone(phone_id: int, db: Session = db_dependency):
    return db.query(models.Phone).filter(models.Phone.id == phone_id).first()

# FastAPI endpoint to update a phone record by ID
@app.put("/phone/{phone_id}", tags=["Phone", "PUT"])
async def update_phone(phone_id: str, phone: PhoneBase, db: Session = db_dependency):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if not db_phone:
        raise HTTPException(status_code=404, detail="Phone not found")
    
    db_phone.model = phone.model
    db_phone.brand = phone.brand
    db_phone.price = phone.price
    db_phone.battery = phone.battery
    
    db.commit()
    db.refresh(db_phone)
    return db_phone

# FastAPI endpoint to delete a phone record by ID
@app.delete("/phone/{phone_id}", tags=["Phone", "DELETE"])
async def delete_phone(phone_id: str, db: Session = db_dependency):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if not db_phone:
        raise HTTPException(status_code=404, detail="Phone not found")
    
    db.delete(db_phone)
    db.commit()
    return {"message": "Phone deleted successfully"}
