from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from app.messages import welcome_message, reg_message


router = Router()


class Register(StatesGroup):
    """
    Класс состояний для регистрации
    Содержит 3 состояния: location, age, gender
    
    location - для ввода региона проживания участника тестирования

    age - для ввода возраста участника тестирования

    gender - для выбора пола участника тестирования
    """
   
    location = State()
    age = State()
    gender = State()


class Testing(StatesGroup):
    """
    Класс состояний для тестирования
    Содержит 2 состояния: test и theme
    
    theme - для выбора темы тестирования
    
    test - для выбора проведения тестирования. 
    Вопросы тестов выбираются в соответствии с выбранной темой
    """
    test = State()
    theme = State()


class Questions(StatesGroup):
    """
    Класс состояний для добавления вопросов в БД
    Содержит 3 состояния:theme, question, answer
   
    theme - для выбора темы вопроса
    
    question - для ввода вопроса

    answer - для ввода ответа на вопрос
    """
    # question = State()
    # answer = State()
    question = State()
    answer = State()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(welcome_message)
    await state.update_data(name=message.from_user.first_name)
    await state.update_data(id=message.from_user.id)
    await message.answer(reg_message)
    await message.answer("Введите регион проживания")
    await state.set_state(Register.location)

@router.message(F.text, Register.location)
async def register_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("Введите возраст")
    await state.set_state(Register.age)
    
@router.message(F.text, Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите пол")
    await state.set_state(Register.gender)

@router.message(F.text, Register.gender)
async def register_gender(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена! Ваши данные: {data}")
    await state.clear()


@router.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)
    print(message.text)
