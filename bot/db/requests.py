from aioredis import Redis
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db.models import User


async def is_user_exists(db_pool: sessionmaker, redis: Redis, user_id: int) -> bool:
    """
    Существует ли пользователь

    :param db_pool: Пул соединений с БД
    :param redis: Редис
    :param user_id: Телеграм id

    :return: bool
    """
    redis_get = await redis.get(f'user_exists:{user_id}')
    if not redis_get:
        async with db_pool() as session:
            async with session.begin():
                user = await session.execute(select(User).where(User.telegram_id == user_id))
                await redis.set(name=f'user_exists:{user_id}', value=1 if user else 0)
                return user.first()
    else:
        return redis_get


async def add_user(db_pool: sessionmaker, user_id: int) -> None:
    """
    Добавить пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id

    :return: None
    """
    async with db_pool() as session:
        async with session.begin():
            new_user = User(telegram_id=user_id)
            session.add(new_user)


async def get_user(db_pool: sessionmaker, user_id: int) -> User:
    """
    Получить пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id

    :return: User
    """
    async with db_pool() as session:
        async with session.begin():
            user = await session.execute(select(User).filter(User.telegram_id == user_id))
            return user.scalars().first()


async def update_user(db_pool: sessionmaker, user_id: int, **kwargs) -> None:
    """
    Обновить пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id
    :param kwargs: Данные которые нужно обновить

    :return: None
    """
    async with db_pool() as session:
        async with session.begin():
            await session.execute(update(User).where(User.telegram_id == user_id).values(kwargs))
