from aiogram import Router, F
from aiogram.filters import CommandStart, Text

from bot.filters import RoleCheckFilter
from bot.utils.for_admin.callback_data_factories import BasicCallback, BasicAction
from .basic import start, clicked_kb, clicked_ikb

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(['Admin']))

# Регистрация обработчиков
router.message.register(start, CommandStart())
router.message.register(clicked_kb, Text(text='Кнопка для админов'))
router.callback_query.register(clicked_ikb, BasicCallback.filter(F.action == BasicAction.BUTTON_FOR_ADMIN))

router_for_admin = router
