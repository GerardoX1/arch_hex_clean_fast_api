from datetime import datetime

from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    username: str
    email: str


class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
