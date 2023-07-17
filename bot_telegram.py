from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_bd


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_bd.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)  # импорт последним, т.к. он пустой(общий)


executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup)  # пропускает сообщения, которые получал в оффлайн-моде
