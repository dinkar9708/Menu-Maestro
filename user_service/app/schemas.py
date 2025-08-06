from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

# Input for user creation
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Output model
class UserOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# For authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str
