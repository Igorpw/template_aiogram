from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db.models import User


async def is_user_exists(db_pool: sessionmaker, user_id: int) -> bool:
    """
    Существует ли пользователь

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id

    :return: bool
    """
    async with db_pool() as session:
        async with session.begin():
            user = await session.execute(select(User).where(User.telegram_id == user_id))
            return user.first()


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
