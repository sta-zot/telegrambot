"""
The module describes the data management functions in the application database

В модуле описываются функции по управлению данными в базе данных приложения
"""

import asyncio
from typing import List
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import joinedload


from settings.configuration import config
from sqlalchemy.orm import joinedload

from db.models import (
    Base,
    User,
    Theme,
    Test,
    Question,
    Answer,
    District,
    Location
)

engine = create_async_engine(config.db_url, echo=True)


async def create_db(engine: AsyncEngine) -> None:
    """
    The function creates the database tables

    Функция создает таблицы базы данных
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    """
    The function returns an asynchronous database session

    Функция возвращает асинхронную сессию базы данных
    """
    return async_sessionmaker(engine, class_=AsyncSession)()


async def get_user(session: AsyncSession, user_id: int) -> User:
    """
    The function returns a record of users from the database

    Функция возвращает запись о пользователе из базы данных
    """
    query = (
        select(User)
        .where(User.id == user_id)
        .options(
            joinedload(User.role),
            joinedload(User.location)
            )
        
    async with session:
        result=await session.scalar(query)
    return result


async def get_location(
        session: AsyncSession,
        location_id: str) -> Location:
            
    """
    The function returns location from the database

    Функция возвращает запись с регионом из базы данных
    """
    
    query=select(Location).where(Location.id == location_id)
    async with session:
        result=await session.scalar(query)
    return result
