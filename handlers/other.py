import json
import string
from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message): # должен распологаться ниже хэндлеров, где есть команды! иначе запросы не пройдут через них.
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
