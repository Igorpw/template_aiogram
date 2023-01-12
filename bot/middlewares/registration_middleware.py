from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db.requests import add_user, is_user_exists, update_user
from bot.loader import config


class RegistrationMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для регистрации
    """

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message | CallbackQuery, data: Dict[str, Any]) -> Any:
        db_pool: sessionmaker = data['db_pool']
        user_id = event.from_user.id
        if not await is_user_exists(db_pool, user_id):
            await add_user(db_pool, user_id)
            if user_id == int(config.bot.admin_id):
                await update_user(db_pool, user_id, role='Admin')

        return await handler(event, data)
