from aiogram import Router, F
from aiogram.filters import CommandStart, Text

from .basic import start, clicked_kb, clicked_ikb
from bot.utils.for_staff.for_basic.callback_data_factories import BasicCallback, BasicAction
# Создание маршрутизатора
router = Router()

# Регистрация обработчиков
router.message.register(start, CommandStart())
router.message.register(clicked_kb, Text(text='Кнопка для всех'))
router.callback_query.register(clicked_ikb, BasicCallback.filter(F.action == BasicAction.BUTTON_FOR_STAFF))

router_for_basic = router
