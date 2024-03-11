from typing import List

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    name: str
    password: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True


class Room(BaseModel):
    id: int
    room_type: str
    room_num: int

    class Config:
        orm_mode = True


class UserRequest(BaseModel):
    name: str
    password: str
    email: EmailStr
    phone: str


class UserResponse(BaseModel):
    response_user: List[UserSchema]

    class Config:
        orm_mode: True
