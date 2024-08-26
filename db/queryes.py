
"""
The module describes the data management functions in the application database

В модуле описываются функции по управлению данными в базе данных приложения
"""
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select, insert, update, delete
from configuration import config
