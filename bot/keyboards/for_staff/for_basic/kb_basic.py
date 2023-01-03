from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def kb_basic() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text='Кнопка для руководства')
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Основное меню руководства')
