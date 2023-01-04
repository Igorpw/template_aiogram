from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db.requests import add_user, is_user_exists


class RegistrationMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для регистрации
    """

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message | CallbackQuery, data: Dict[str, Any]) -> Any:
        db_pool: sessionmaker = data['db_pool']
        if not await is_user_exists(db_pool, event.from_user.id):
            await add_user(db_pool, event.from_user.id)

        return await handler(event, data)
