import enum

from aiogram.filters.callback_data import CallbackData


class BasicAction(enum.IntEnum):
    """
    Действия для всех
    """
    BUTTON_FOR_ALL = 0


class BasicCallback(CallbackData, prefix='for_all_basic'):
    """
    Обработка действий для всех
    """
    action: BasicAction
