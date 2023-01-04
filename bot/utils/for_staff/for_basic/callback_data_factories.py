import enum

from aiogram.filters.callback_data import CallbackData


class BasicAction(enum.IntEnum):
    """
    Действия для руководства
    """
    BUTTON_FOR_STAFF = 0


class BasicCallback(CallbackData, prefix='for_staff_basic'):
    """
    Обработка действий для руководства
    """
    action: BasicAction
