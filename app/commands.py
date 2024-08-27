from aiogram.types.bot_command import BotCommand
import emoji

general_commands = [
    BotCommand(
        command='reg',
        description=emoji.emojize('\U0001F5A5 Регистрация')
    ),
    BotCommand(
        command='test',
        description=emoji.emojize(
            ':exclamation_question_mark: Пройти тестирование'
            )
    ),
    BotCommand(
        command='materials',
        description=emoji.emojize(
            ':books: Материалы по финансовой грамотности'
        )
    )
]