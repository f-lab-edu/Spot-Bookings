from schemas import UserRequest
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserDB(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    phone = Column(String(256), nullable=False)

    @classmethod
    def create(cls, request: UserRequest) -> "UserDB":
        return cls(
            name=request.name,
            password=request.password,
            email=request.email,
            phone=request.phone,
        )


class RoomDB(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True, index=True)
    room_type = Column(String(30), unique=True, nullable=False)
    room_num = Column(Integer, nullable=False)
