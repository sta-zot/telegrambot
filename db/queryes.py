
"""
The module describes the data management functions in the application database

В модуле описываются функции по управлению данными в базе данных приложения
"""
import asyncio
from typing import List
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy import select, insert, update, delete

from configuration import config

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


async def get_session() -> AsyncSession:
    """
    The function returns an asynchronous database session

    Функция возвращает асинхронную сессию базы данных
    """
    yield async_sessionmaker(engine)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
if __name__ == "__main__":
    asyncio.run(main())
