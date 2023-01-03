from aiogram import Router

from .for_basic import router_for_basic

# Создание маршрутизатора
router = Router()

# Регистрация маршрутизаторов
router.include_router(router_for_basic)

router_for_all = router
