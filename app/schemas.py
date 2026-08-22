from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    first_name: str

class UserResponse(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: str

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_done: bool
    created_at: datetime

    class Config:
        from_attributes = True
class TaskUpdate(BaseModel):
    is_done: bool
