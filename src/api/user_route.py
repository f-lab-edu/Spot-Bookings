from typing import List

from connect import get_db
from fastapi import APIRouter, Body, Depends, HTTPException
from repository import (
    create_user_id,
    delete_user_repo,
    get_user,
    get_user_id_select,
    get_user_name_select,
    update_user_repo,
)
from schemas import UserRequest, UserSchema
from sqlalchemy.orm import Session

from models import UserDB

router = APIRouter(prefix="/user")


@router.get("/user", status_code=200)
def read_users(session: Session = Depends(get_db)):
    # repository 함수 import  repo get_user session / read_user session
    users: List[UserDB] = get_user(session=session)
    return users


@router.get("/user/{user_id}", status_code=200)
def read_user(user_id: int, session: Session = Depends(get_db)):
    user: UserDB | None = get_user_id_select(session=session, user_id=user_id)
    return user


@router.get("/user/{user_name}", status_code=200)
def read_user_name(user_name: str, session: Session = Depends(get_db)):
    user: UserDB | None = get_user_name_select(session=session, user_name=user_name)
    return user


@router.post("/users", status_code=201)
def create_user(
    request: UserRequest,
    session: Session = Depends(get_db),
) -> UserSchema | None:
    user: UserDB = UserDB.create(request=request)
    user: UserDB = create_user_id(session=session, user=user)
    return UserSchema.from_orm(user)


@router.patch("/users/{user_id}", status_code=200)
def update_user(
    user_id: int,
    user_update: UserSchema = Body(...),
    session: Session = Depends(get_db),
):
    user: UserDB | None = get_user_id_select(session=session, user_id=user_id)
    user.name = user_update.name
    user.password = user_update.password
    user.email = user_update.email
    user.phone = user_update.phone
    user = update_user_repo(session=session, user=user)
    return UserSchema.from_orm(user)


@router.delete("/user/{user_id}", status_code=204)
def delete_user(
    user_id: int,
    session: Session = Depends(get_db),
):
    user: UserDB | None = get_user_id_select(session=session, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user_repo(session=session, user_id=user_id)
