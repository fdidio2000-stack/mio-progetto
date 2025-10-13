from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Optional

class ContactCreate(BaseModel):
    full_name: str = Field(min_length=2)
    email: EmailStr
    phone: Optional[str] = None
    tags: List[str] = []

class ContactUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    tags: Optional[List[str]] = None

class ContactOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: Optional[str]
    tags: list[str]
    avatar_url: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)