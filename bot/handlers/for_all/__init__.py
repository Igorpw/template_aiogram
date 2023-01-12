from aiogram import Router, F
from aiogram.filters import CommandStart, Text

from bot.filters import RoleCheckFilter
from bot.handlers.for_all.basic import start, clicked_kb, clicked_ikb
from bot.utils.for_all.callback_data_factories import BasicCallback, BasicAction

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(['User', 'Admin']))

# Регистрация обработчиков
router.message.register(start, CommandStart())
router.message.register(clicked_kb, Text(text='Кнопка для всех'))
router.callback_query.register(clicked_ikb, BasicCallback.filter(F.action == BasicAction.BUTTON_FOR_ALL))

router_for_all = router
