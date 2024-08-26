"""
The module describes the application database table models.
The sqlalchemy library is used to describe the models

В модуле описываются модели таблиц базы данных приложения.
Для описания моделей используется библиотека sqlalchemy
"""
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    mapped_column,
    Mapped,
    foreign_key 
)


from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs


Base = declarative_base(cls=AsyncAttrs)
class Table(Base):
    @declared_attr
    def __tablename__ (cls):
        return cls.__name__.lower()+"s"

