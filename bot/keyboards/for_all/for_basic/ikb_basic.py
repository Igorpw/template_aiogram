from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def ikb_basic() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Кнопка для всех', callback_data='button_for_all')
    return builder.as_markup()
