from pydantic import BaseModel

# Define Pydantic models (schemas) for your API endpoints
class PhoneBase(BaseModel):
    id : str
    model: str
    brand: str
    price: float
    battery: int  # Assuming battery capacity is an integer

# Add more Pydantic models as needed for other endpoints or request/response structures
