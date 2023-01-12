import configparser
from dataclasses import dataclass


@dataclass
class DB:
    user: str
    password: str
    database: str
    host: str


@dataclass
class Bot:
    token: str
    admin_id: int


@dataclass
class Redis:
    host: str
    username: str
    password: str


@dataclass
class Config:
    db: DB
    bot: Bot
    redis: Redis


def load_config(path: str):
    file_config = configparser.ConfigParser()
    file_config.read(path)
    return Config(
        db=DB(**file_config["db"]),
        bot=Bot(**file_config["bot"]),
        redis=Redis(**file_config['redis'])
    )


config = load_config('bot.ini')
