from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    nombre: str = Field(..., description="First name of the user.", example="Marco")
    apellido: str = Field(..., description="Last name of the user.", example="Lopez")
    email: EmailStr = Field(..., description="User's email address.", example="marco@example.com")

class UserCreate(UserBase):
    password: str = Field(..., description="User's password. Please choose a strong password.", example="••••••••")  # Use masked example for security

class UserUpdate(BaseModel):
    nombre: Optional[str] = Field(None, description="Optional: Update the user's first name.", example="New Name")
    apellido: Optional[str] = Field(None, description="Optional: Update the user's last name.", example="New Last Name")
    email: Optional[EmailStr] = Field(None, description="Optional: Update the user's email address.")
    password: Optional[str] = Field(None, description="Optional: Update the user's password. Please choose a strong password.", example="••••••••")

class User(UserBase):
    id: str = Field(..., description="Unique identifier for the user.", example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        # orm_mode = True  # Assuming usage with an ORM like SQLAlchemy
        from_attributes = True

