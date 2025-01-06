from pydantic import BaseModel
from typing import List, Optional

# Base User Schema for input and output
class UserBase(BaseModel):
    name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

    class config:
        orm_mode = True
