from pathlib import Path

from pydantic import BaseSettings, PostgresDsn, SecretStr


class Settings(BaseSettings):
    """
    Настройки проекта
    """

    # Настройка бота
    bot_token: SecretStr

    # Настройка базы данных
    postgres_dsn: PostgresDsn

    # Рабочая директория
    workdir = Path(__file__).parent

    class Config:
        """
        Конфигурация проекта
        """

        env_file = '.env'  # Файл
        env_file_encoding = 'utf-8'  # Кодировка


config = Settings()
