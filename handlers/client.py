from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_bd


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятно аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nt.me/Pizza_Sheeeeef_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands='Расположение')
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Колбасная 15', reply_markup=ReplyKeyboardRemove()) # удаляет клавиатуру


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_bd.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    # dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_open_command, lambda message: 'Режим работы' in message.text)
    dp.register_message_handler(pizza_place_command, lambda message: 'Расположение' in message.text)
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
