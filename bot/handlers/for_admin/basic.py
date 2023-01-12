from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db.requests import get_user
from bot.keyboards.for_admin.kb_basic import kb_basic
from bot.keyboards.for_admin.ikb_basic import ikb_basic


async def start(m: Message, db_pool: sessionmaker) -> None:
    _get_user = await get_user(db_pool, m.from_user.id)
    await m.answer('Главное меню,\n\n'
                   f'Твой роль: {_get_user.role}\n'
                   f'Время в боте: {_get_user.reg_date}', reply_markup=kb_basic())
    await m.answer('Текст с кнопкой', reply_markup=ikb_basic())


async def clicked_kb(m: Message) -> None:
    await m.answer('Вы нажали на кнопку')


async def clicked_ikb(c: CallbackQuery) -> None:
    await c.message.edit_text('Вы нажали на кнопку')
    await c.answer('Вы нажали на кнопку')
