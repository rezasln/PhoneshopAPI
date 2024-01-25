# Import required SQLAlchemy classes for defining model columns
from sqlalchemy import Column, Integer, String, Float

# Import the Base class from db module, which serves as the declarative base for ORM classes
from db import Base

# Define the Phone class inheriting from the Base class
class Phone(Base):
    # Define the table name for the Phone model
    __tablename__ = "phones"

    # Define columns for the Phone table
    # - id: Primary key column for uniquely identifying each phone record
    id = Column(String, primary_key=True, index=True)
    
    # - model: Column to store the phone model name as a string
    model = Column(String)
    
    # - brand: Column to store the phone brand name as a string
    brand = Column(String)
    
    # - price: Column to store the phone price as a floating-point number
    price = Column(Float)
    
    # - battery: Column to store the phone battery capacity or type as an integer
    battery = Column(Integer)

# Note: The above code defines an SQLAlchemy model class named Phone 
#       with columns corresponding to the fields you want to store 
#       for each phone record in the "phones" table of your database.
