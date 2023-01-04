from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from bot.utils.for_staff.for_basic.callback_data_factories import BasicCallback, BasicAction


def ikb_basic() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Кнопка для руководства',
                   callback_data=BasicCallback(action=BasicAction.BUTTON_FOR_STAFF).pack())
    return builder.as_markup()
