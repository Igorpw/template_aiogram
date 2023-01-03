from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    """
    Фильтр типа чата

    :param chats_types: Типы чатов

    :return: bool
    """

    def __init__(self, chats_types: list) -> None:
        self.chats_types = chats_types

    async def __call__(self, event: Message) -> bool:
        return event.chat.type in self.chats_types
