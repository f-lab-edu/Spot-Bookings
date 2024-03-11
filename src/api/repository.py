from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from models import UserDB


def get_user(session: Session) -> list[UserDB]:
    return list(session.scalars(select(UserDB)))


def get_user_id_select(session: Session, user_id: int) -> UserDB | None:
    return session.scalar(select(UserDB).where(UserDB.id == user_id))


def get_user_name_select(session: Session, user_name: str) -> UserDB | None:
    return session.scalar(select(UserDB).where(UserDB.name == user_name))


def create_user_id(session: Session, user: UserDB) -> UserDB:
    session.add(instance=user)
    session.commit()
    session.refresh(instance=user)
    return user


def update_user_repo(session: Session, user: UserDB) -> UserDB:
    session.add(instance=user)
    session.commit()
    session.refresh(instance=user)
    return user


def delete_user_repo(session: Session, user_id: int) -> None:
    session.execute(delete(UserDB).where(UserDB.id == user_id))
    session.commit()
