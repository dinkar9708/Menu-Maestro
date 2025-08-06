from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class RestaurantDTO(BaseModel):
    def __init__(self, name, address, phone_number=None, email=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


class RestaurantCreate(BaseModel):
    name: str
    address: str
    phone_number: str | None
    email: EmailStr


class RestaurantResponse(BaseModel):
    id: UUID
    name: str
    address: str
    phone_number: str
    email: EmailStr
    created_at: datetime
    is_active: bool
    owner_id: UUID
    class Config:
        orm_mode = True


