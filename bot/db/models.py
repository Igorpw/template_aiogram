from datetime import datetime as dt

from sqlalchemy import BigInteger, Column, DateTime, String

from bot.db.base import Base


class User(Base):
    """
    Основная модель пользователей
    """
    __tablename__ = "users"  # Имя таблицы
    telegram_id = Column(BigInteger, nullable=False, primary_key=True)  # Телеграм id пользователя
    role = Column(String, default='Воркер')  # Роль пользователя по умолчанию
    registration_date = Column(DateTime, default=dt.now())  # Дата регистрации пользователя

    def __str__(self) -> str:
        """
        Возвращает телеграм id текущего пользователя

        :param self: User

        :return: str
        """
        return f'User: {self.telegram_id}'

    @property
    def reg_date(self) -> str:
        """
        Возвращает прошедшее время с момента регистрации текущего пользователя

        :param self: User

        :return: str
        """
        new_date = dt.now() - self.registration_date
        return str(new_date).split('.')[0]
