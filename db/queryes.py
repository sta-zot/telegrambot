
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
    AsyncEngine
)
from sqlalchemy import select, insert, update, delete

from settings.configuration import config

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
    yield async_sessionmaker(engine)

