import enum

from aiogram.filters.callback_data import CallbackData


class BasicAction(enum.IntEnum):
    """
    Действия для администраторов
    """
    BUTTON_FOR_ADMIN = 0


class BasicCallback(CallbackData, prefix='for_admin_basic'):
    """
    Обработка действий для администраторов
    """
    action: BasicAction
