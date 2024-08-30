
"""
The module describes the data management functions in the application database

В модуле описываются функции по управлению данными в базе данных приложения
"""
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy import select, insert, update, delete
from configuration import config

from db.models import (
    Table,
    User,
    Theme,
    Test,
    Question,
    Answer,
    District,
    Location
)


engine = create_async_engine(config.db_url, echo=True)


async def get_session() -> AsyncSession:
    """
    The function returns an asynchronous database session

    Функция возвращает асинхронную сессию базы данных
    """
   passs