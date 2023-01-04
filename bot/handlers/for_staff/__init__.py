from aiogram import Router

from bot.filters import RoleCheckFilter
from .for_basic import router_for_basic

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(['Staff']))

# Регистрация маршрутизаторов
router.include_router(router_for_basic)

router_for_staff = router
