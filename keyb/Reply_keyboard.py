from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton



keyboard_r = ReplyKeyboardMarkup(resize_keyboard = True,one_time_keyboard=True) #
key_data = KeyboardButton(text='Меню',command='menu')
key_bd = KeyboardButton(text='Выгрузить БД',command='bd')
key_account = KeyboardButton(text='Настройка аккаунтов')
keyboard_r.row(key_data,key_bd,key_account)


