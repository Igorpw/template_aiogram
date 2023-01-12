from asyncio import run
from contextlib import suppress
from logging import DEBUG, basicConfig

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aioredis import Redis
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.handlers import router_for_admin, router_for_all
from bot.loader import config
from bot.middlewares import RegistrationMiddleware, AntiFloodMiddleware


async def main() -> None:
    # Logging
    basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # Postgres
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=config.db.user,
        password=config.db.password,
        database=config.db.database,
        host=config.db.host
    )
    engine = create_async_engine(url=postgres_url, echo=True, pool_pre_ping=True)
    db_pool = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    # Redis
    redis = Redis(
        # host=config.redis.host,
        # username=config.redis.username,
        # password=config.redis.password
    )

    # Bot, Dispatcher
    bot = Bot(config.bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    # Register Middlewares
    dp.message.outer_middleware(RegistrationMiddleware())
    dp.message.middleware(AntiFloodMiddleware())

    # Register Routers
    dp.include_router(router_for_admin)
    dp.include_router(router_for_all)

    # Run Forever
    await dp.start_polling(bot, db_pool=db_pool, redis=redis)


def bot_run():
    with suppress(KeyboardInterrupt):  # Игнорирование ошибок при остановке
        run(main())  # Запуск асинхронной функции
