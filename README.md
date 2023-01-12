**Шаблон для телеграм бота**

## **Что есть в шаблоне бота ?**

     1. Анти-флуд
     2. База данных
     3. Регистрациия
     4. Система ролей
     5. Проверка типа чата

## **Используемые бибилиотеки**

 

1. aiogram **3.0.0b6** *Modern and fully asynchronous framework for Telegram Bot API*
 2. redis **4.4.2** *Python client for Redis database and key-value store*
 3. aioredis **2.0.1**  *asyncio (PEP 3156) Redis support*
 4. sqlalchemy **1.4.46** *Database Abstraction Library*
 5. alembic **1.9.1**  *A database migration tool for SQLAlchemy.*
 6. flake8 **6.0.0** *the modular source code checker: pep8 pyflakes and co*
 7. asyncpg **0.27.0** *An asyncio PostgreSQL driver*


## **Установка и настройка**

    1. pip install poetry - Хорошая альтернатива pip
    2. cd template_aiogram - Переходим в установленный каталог
    3. poetry install - Устанавливаем все необходимые пакеты

**Отккрываем файл bot.ini и настраиваем его**

![enter image description here](https://raw.githubusercontent.com/FastCodeProfile/template_aiogram/master/image.png)


## Запуск

     1. poetry run bot


