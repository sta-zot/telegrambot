"""
The module describes the application database table models.
The sqlalchemy library is used to describe the models

В модуле описываются модели таблиц базы данных приложения.
Для описания моделей используется библиотека sqlalchemy
"""

from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped
from sqlalchemy.types import BigInteger, String, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


class Role(Base):
    """
    Таблица ролей пользователей приложения с полями:
    id - уникальный идентификатор роли, берётся из telegram id
    name - название роли, не может быть пустым, уникальное поле
    """
    
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    users: Mapped[list["User"]] = relationship(back_populates="role")

    def __repr__(self):
        return f"Role(id={self.id}, name='{self.name}')"


class User(Base):
    """
    Таблица пользователей приложения с полями:
    id - уникальный идентификатор пользователя, берётся из telegram id
    email - электронная почта пользователя, уникальное поле и не может быть пустой,
    является индексом для поиска пользователя
    age - возраст пользователя, не может быть пустым
    sex - пол пользователя, не может быть пустым
    role_id - связь с таблицей ролей, не может быть пустой. Указывает к какой
    роли относится пользователь
    location_id - связь с таблицей локаций, не может быть пустой.
    Указывает регион проживания пользователя
    """

    id: Mapped[BigInteger] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    # Связь с таблицей ролей
    # Relationship with the "Role" table
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"), nullable=False)
    role: Mapped["Role"] = relationship(back_populates="users")
    # Связь с таблицей локаций
    # Relationship with the "Location" table
    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"), nullable=False)
    location: Mapped["Location"] = relationship(back_populates="users")


class Location(Base):
    """
    Таблица локаций пользователей приложения с полями:
    id - уникальный идентификатор локации, берётся из telegram id
    name - название локации, не может быть пустым, уникальное поле
    """

    id: Mapped[str] = mapped_column(
        String(3), primary_key=True, nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    # Связь с таблицей регионов
    # Relationship with the "District" table
    district_id: Mapped[str] = mapped_column(
        String(4), ForeignKey("districts.id"), nullable=False
    )
    district: Mapped["District"] = relationship(back_populates="locations")
    # Список пользователей в данной локации
    users: Mapped[list["User"]] = relationship(back_populates="location")


class District(Base):
    """
    Таблица регионов пользователей приложения с полями:
    id - уникальный идентификатор региона, берётся из telegram id
    name - название региона, не может быть пустым, уникальное поле
    """

    id: Mapped[str] = mapped_column(
        String(4), primary_key=True, nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    locations: Mapped[list["Location"]] = relationship(
        back_populates="district")


class Theme(Base):
    """
    Таблица тематик вопросов с полями:
    id - уникальный идентификатор темы
    name - название темы, не может быть пустым, значение поля уникальное
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    questions: Mapped[list["Question"]] = relationship(back_populates="theme")


class Question(Base):
    """
    Таблица вопросов с полями:
    id - уникальный идентификатор вопроса
    text - текст вопроса, не может быть пустым
    theme_id - связь с таблицей тематик, не может быть пустой.
    Указывает тему вопроса
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    theme_id: Mapped[int] = mapped_column(
        ForeignKey("themes.id"), nullable=False)
    theme: Mapped["Theme"] = relationship(back_populates="questions")

    answers: Mapped[list["Answer"]] = relationship(back_populates="question")


class Answer(Base):
    """
    Таблица ответов с полями:
    id - уникальный идентификатор ответа
    text - текст ответа, не может быть пустым
    is_correct - флаг правильности ответа
    question_id - связь с таблицей вопросов, не может быть пустой.
    Указывает вопрос, к которому относится ответ
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    is_correct: Mapped[bool] = mapped_column(nullable=False)
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id"), nullable=False)
    question: Mapped["Question"] = relationship(back_populates="answers")


class Test(Base):
    """
    Таблица тестов с полями:
    id - уникальный идентификатор теста

    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_time = mapped_column(
        DateTime, nullable=False, server_default=func.now())
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="tests")

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id"), nullable=False)
    question: Mapped["Question"] = relationship(back_populates="tests")
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers.id"), nullable=False)
    answer: Mapped["Answer"] = relationship(back_populates="tests")
    point: Mapped[int] = mapped_column(Integer, nullable=False)


