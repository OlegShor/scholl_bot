import asyncio
from aiogram import executor
from db import sqlite_db
from create_bot import dp


async def on_startup(_):
    print("Bot start")
    sqlite_db.sql_start()

from handler import admin_handler

admin_handler.register_message_Admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
