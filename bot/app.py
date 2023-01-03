from asyncio import run
from contextlib import suppress
from logging import DEBUG, basicConfig

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from aioredis import Redis

from bot.loader import config
from bot.middlewares import RegistrationMiddleware, AntiFloodMiddleware
from bot.handlers import router_for_staff, router_for_all


async def main() -> None:
    # Запись на стандартный вывод
    basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # Создание движка БД для Postgres
    engine = create_async_engine(url=config.postgres_dsn, echo=True, pool_pre_ping=True)

    # Создание пула соединений с БД
    db_pool = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    # Создание редиса
    redis = Redis()

    # Создание бота и его диспетчера
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    # Регистрация промежуточного ПО
    dp.message.outer_middleware(RegistrationMiddleware())
    dp.message.middleware(AntiFloodMiddleware())

    # Регистрация маршрутизаторов
    dp.include_router(router_for_staff)
    dp.include_router(router_for_all)

    # Запуск навсегда
    await dp.start_polling(bot, db_pool=db_pool, redis=redis)


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):  # Игнорирование ошибок при остановке
        run(main())  # Запуск асинхронной функции
