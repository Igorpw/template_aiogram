from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from bot.utils.for_all.callback_data_factories import BasicAction, BasicCallback


def ikb_basic() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Кнопка для всех',
                   callback_data=BasicCallback(action=BasicAction.BUTTON_FOR_ALL).pack())
    return builder.as_markup()
