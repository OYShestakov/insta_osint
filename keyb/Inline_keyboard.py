from aiogram.types.inline_keyboard import  InlineKeyboardMarkup, InlineKeyboardButton

keyboard_i = InlineKeyboardMarkup(2)
key_test = InlineKeyboardButton(text='Тест работы', callback_data='test')
key_accounts = InlineKeyboardButton(text='Проверка заблокированных аккаунтов', callback_data='accounts')
key_photos = InlineKeyboardButton(text='Скачать фото', callback_data='photos')
key_stories = InlineKeyboardButton(text='Скачать сторис', callback_data='stories')
key_content = InlineKeyboardButton(text='Скачать контент с аккаунта', callback_data='content')
key_test_c = InlineKeyboardButton(text='Тест работы на конкретный пост или сторис', callback_data='test_c')
key_geo = InlineKeyboardButton(text='ГЕО адреса фото', callback_data='geo')
key_test_s = InlineKeyboardButton(text='Тест работы сбора', callback_data='test_s')
keyboard_i.add(key_test,key_accounts,key_photos,key_stories,key_content,key_test_c,key_geo,key_test_s)



keyboard_a = InlineKeyboardMarkup(2)
key_acred = InlineKeyboardButton(text='Добавить данные для авторизации', callback_data='a_cred')
key_dcred = InlineKeyboardButton(text='Удалить данные для авторизации', callback_data='d_cred')
key_lmonitor = InlineKeyboardButton(text='Список пользователей для мониторинга', callback_data='l_monitor')
key_amonitor = InlineKeyboardButton(text='Добавить пользьзователя для мониторинга', callback_data='a_monitor')
key_dmonitor = InlineKeyboardButton(text='Удаление пользователь для мониторинга', callback_data='d_monitor')
keyboard_a.add(key_acred,key_dcred,key_lmonitor,key_amonitor,key_dmonitor)