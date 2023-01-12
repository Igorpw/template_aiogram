from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from bot.utils.for_admin.callback_data_factories import BasicCallback, BasicAction


def ikb_basic() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Кнопка для админов',
                   callback_data=BasicCallback(action=BasicAction.BUTTON_FOR_ADMIN).pack())
    return builder.as_markup()
