from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def ikb_basic() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Кнопка для руководства', callback_data='button_for_staff')
    return builder.as_markup()
