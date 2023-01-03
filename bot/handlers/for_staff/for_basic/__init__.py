from aiogram import Router
from aiogram.filters import CommandStart, Text

from .basic import start, clicked_kb, clicked_ikb

# Создание маршрутизатора
router = Router()

# Регистрация обработчиков
router.message.register(start, CommandStart())
router.message.register(clicked_kb, Text(text='Кнопка для всех'))
router.callback_query.register(clicked_ikb, Text(text='button_for_staff'))

router_for_basic = router
