from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove


b1 = KeyboardButton('Режим работы')
b2 = KeyboardButton('Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard скрывает после нажатия


kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5) #add-новая кнопка снизу, insert-сбоку
# kb_client.row(b1, b2, b3) # в строку
