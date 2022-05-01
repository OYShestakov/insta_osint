from aiogram import types
from aiogram.dispatcher.filters import Command, ContentTypeFilter
from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyb.Inline_keyboard import *
from keyb.Reply_keyboard import *
from test import *
from app import *
import os
a = 0
k = 0
username = ''

@dp.message_handler(commands="start")
async def stock(message: types.Message):
    await bot.send_message(message.chat.id,f'Здравствуйте,{message.chat.first_name}', reply_markup=keyboard_r)

@dp.message_handler(text="Меню")
async def stock(message: types.Message):
    await bot.send_message(message.chat.id,f'Меню', reply_markup=keyboard_i)

@dp.message_handler(text="Выгрузить БД")
async def stock(message: types.Message):
    global th1

    # th1.pause()


    # bot_start()
    export_to_csv('emails')
    export_to_csv('followers')
    export_to_csv('phones')
    # export_to_csv('users')

    await bot.send_document(message.chat.id, document = file_open('emails.csv'))
    os.remove(path='emails.csv')
    await bot.send_document(message.chat.id, document = file_open('followers.csv'))
    os.remove(path='followers.csv')
    await bot.send_document(message.chat.id, document = file_open('phones.csv'))
    os.remove(path='phones.csv')
    # await bot.send_document(816912146, document = file_open('users.csv'))
    # os.remove(path='users.csv')
    await bot.send_message(message.chat.id, 'База данных успешно выгружена')

    th1.start()

@dp.message_handler(text="Настройка аккаунтов")
async def stock(message: types.Message):
    await bot.send_message(message.chat.id,f'Меню настройки аккаунтов', reply_markup = keyboard_a)


@dp.callback_query_handler(lambda c: c.data)
async def poc_callback_but(call: types.CallbackQuery):
        global a
        if call.data == 'test':
            a = 1
            await  bot.send_message(call.message.chat.id,'Введите username профиля для проверки работы:')



        elif call.data == 'accounts':
            good, bad = acc.button_check()
            await  bot.send_message(call.message.chat.id,
                                    f'Количество работающих аккаутов равно {good}')
            await  bot.send_message(call.message.chat.id,
                                    f'Количество заблокированных аккаутов равно {bad}')

        elif call.data == 'photos':
            a = 3
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, откуда скачать фото:')
        elif call.data == 'stories':
            a = 4
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, откуда скачать сторис:')
        elif call.data == 'content':
            a = 5
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, откуда скачать контент:')

        elif call.data == 'test_c':
            a = 6
            await  bot.send_message(call.message.chat.id, 'Введите ссылку на пост:')
        elif call.data == 'geo':
            a = 7
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, по которому нужна информация о геолокации :')
        elif call.data == 'test_s':
            a = 8
            await  bot.send_message(call.message.chat.id,'Введите username профиля для проверки работы:')

        elif call.data == 'a_cred':
            a = 9
            await  bot.send_message(call.message.chat.id,'Введите username профиля:')
        elif call.data == 'd_cred':
            a = 10
            await  bot.send_message(call.message.chat.id, 'Введите username профиля:')

        elif call.data == 'l_monitor':
            file = open('usernames','r')
            user_str = ''
            usernames = file.read()
            user_list = str(usernames).split(',')
            for user in user_list:
                user_str = user_str + f'{user_list.index(user)+1}) {user}\n'
            await bot.send_message(call.message.chat.id,f'Список, пользователей, за которыми установлен мониторинг:\n{user_str}')

        elif call.data == 'a_monitor':
            a = 11
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, за которым хотите установить мониторинг:')
        elif call.data == 'd_monitor':
            a = 12
            await  bot.send_message(call.message.chat.id, 'Введите username профиля, за которым хотите прекратить мониторинг:')


@dp.message_handler()
async def stock(message: types.Message):
    global username
    global a
    global k
    global th1

    if a == 1:
        user_info = ''
        info_us = ac1(message.text)
        for user in  info_us:
            id = user.get("id")
            username = user.get("username")
            fullname = user.get("full_name")
            public_email = user.get("email")
            contact_phone_number = user.get("contact_phone_number")
            user_info = user_info + f'{info_us.index(user)+1}) id = {id}, username = {username}, full_name = {fullname}, email = {public_email}, phone = {contact_phone_number}\n'

        await bot.send_message(message.chat.id,f'{user_info}')
        a = 0


    elif a == 3 and k == 0:
        username = str(message.text)
        await  bot.send_message(message.chat.id,'Введите количество фото, которых нужно скачать :')
        k = 1
    elif a == 4 and k == 0:
        username = str(message.text)
        await  bot.send_message(message.chat.id, 'Введите количество сторис, которых нужно скачать :')
        k = 2
    elif a == 3 and k == 1:
        col = int(message.text)
        paths = photo_3(username,col)
        for path in paths:
            try:
                photo = open(f'{path}','rb')
                await bot.send_photo(message.chat.id,photo)
                os.remove(path)
            except Exception:
                await bot.send_message(message.chat.id, 'Ошибка')
        await  bot.send_message(message.chat.id, 'Успешно')
        a = 0
        k = 0


    elif a == 4 and  k == 2:
        col = int(message.text)
        paths = stories_4(username,col)
        for path in paths:
            try:
                if 'jpg' in path:
                    photo = open(f'{path}', 'rb')
                    await bot.send_photo(message.chat.id, photo)
                    os.remove(path)
                elif 'mp4' in path:
                    video = open(f'{path}', 'rb')
                    await  bot.send_video(message.chat.id,video)
                    os.remove(path)
            except Exception:
                await bot.send_message(message.chat.id, 'Ошибка')


        await  bot.send_message(message.chat.id, 'Успешно')
        k = 0
        a = 0

    elif a == 5:
        username = str(message.text)

        paths = get_content(username)
        p1 = paths[0]
        p2 = paths[1]
        for path in p1:
            try:
                if 'jpg' in path:
                    photo = open(f'{path}', 'rb')
                    await bot.send_photo(message.chat.id, photo)
                    os.remove(path)
                elif 'mp4' in path:
                    video = open(f'{path}', 'rb')
                    await  bot.send_video(message.chat.id, video)
                    os.remove(path)
            except Exception:
                await bot.send_message(message.chat.id, 'Ошибка')
        for path in p2:
            try:
                if 'jpg' in path:
                    photo = open(f'{path}', 'rb')
                    await bot.send_photo(message.chat.id, photo)
                    os.remove(path)
                elif 'mp4' in path:
                    video = open(f'{path}', 'rb')
                    await  bot.send_video(message.chat.id, video)
                    os.remove(path)
            except Exception:
                await bot.send_message(message.chat.id, 'Ошибка')
        await  bot.send_message(message.chat.id, 'Успешно')
        a = 0
    elif a == 6:
        url = message.text
        await  bot.send_message(message.chat.id, 'Ожидайте, идёт сбор данных.')
        user_info = ''
        info_us = post(url)
        u_l = info_us[0]
        u_c = info_us[1]
        for user in u_l:
            id = user.get("id")
            username = user.get("username")
            fullname = user.get("full_name")
            public_email = user.get("email")
            contact_phone_number = user.get("contact_phone_number")
            if public_email == None:
                public_email ='None'
            if contact_phone_number == None:
                contact_phone_number = 'None'
            user_info = user_info + f'{u_l.index(user) + 1}) id = {id}, username = {username}, full_name = {fullname}, email = {public_email}, phone = {contact_phone_number}\n'
        await bot.send_message(message.chat.id, f'Люди, которые лайкнули пост: \n {user_info}\n\n\n')
        user_info = ''
        for user in u_c:
            id = user.get("id")
            username = user.get("username")
            fullname = user.get("full_name")
            public_email = user.get("email")
            contact_phone_number = user.get("contact_phone_number")
            if public_email == None:
                public_email ='None'
            if contact_phone_number == None:
                contact_phone_number = 'None'
            user_info = user_info + f'{u_c.index(user) + 1}) id = {id}, username = {username}, full_name = {fullname}, email = {public_email}, phone = {contact_phone_number}\n'
        await bot.send_message(message.chat.id, f'Люди, которые прокомментировали пост: \n {user_info}')
        a = 0


    elif a == 7:
        await  bot.send_message(message.chat.id, 'Ожидайте, идёт сбор данных.')
        username = message.text
        geo_info = geo_7(username)

        for location in geo_info:
            place = location[0]
            data = location[1]
            g_info = f'{geo_info.index(location) + 1}) place = {place}, data = {data}\n'
            await bot.send_message(message.chat.id, f'{g_info}')
            time.sleep(0.2)


        await  bot.send_message(message.chat.id, 'Успешно')
        a = 0

    elif a == 8:
        user_info = ''
        info_us = ac8(message.text)
        for user in info_us:
            id = user.get("id")
            username =  user.get("username")
            fullname = user.get("full_name")
            user_info = user_info + f'{info_us.index(user) + 1}) id = {id}, username = {username}, full_name = {fullname}\n'

        await bot.send_message(message.chat.id, f'{user_info}')
        a = 0

    elif a == 9 and k == 0:
        file = open('credentials', 'r')
        user_str = ''
        usernames = file.read()
        file.close()
        user_list = str(usernames).split(',')
        for user in user_list:
            if message.text in user:
                status = True
            else:
                status = False
                k = 4
                await bot.send_message(message.chat.id, f'Введите пароль пользователя {message.text}  ')
                username = str(message.text)
                break

                # user_list.append(message.text)
                # for user in user_list:
                #     user_str = user_str + f'{user},'
                #
                #     user_str = user_str[:-1]
                #
                #     file = open('credentials', 'w')
                #     file.write(user_str)
                #     await bot.send_message(message.chat.id, 'Пользователь успешно удалён')

        if status == True:
            await bot.send_message(message.chat.id, 'Такой пользователь уже есть в списке. Повторите действие '
                                                    'и введите username другого пользователя')
            a = 0
            k = 0
    elif a == 9 and k == 4:
        file = open('credentials', 'r')
        user_str = ''
        usernames = file.read()
        file.close()
        user_list = str(usernames).split(',')
        user_list.append(f'{username}:{message.text}')

        for user in user_list:
            user_str = user_str + f'{user},'

        user_str = user_str[:-1]
        file = open('credentials', 'w')
        file.write(user_str)
        await bot.send_message(message.chat.id, 'Данные пользователя успешно добавлены')
        global th1
        sys.exit(th1)
        bot_start()
        th1.start()
        a = 0
        k = 0



    elif a == 10:
        file = open('credentials', 'r')
        user_str = ''
        usernames = file.read()
        file.close()
        user_list = str(usernames).split(',')
        for user in user_list:
            if message.text not in user:
                status = True
            else:
                status = False
                user_list.remove(user)
                for usern in user_list:
                    user_str = user_str + f'{usern},'

                user_str = user_str[:-1]

                file = open('credentials', 'w')
                file.write(user_str)
                await bot.send_message(message.chat.id, 'Пользователь успешно удалён')

                sys.exit(th1)
                bot_start()
                th1.start()
                break

        if status == True:
            await bot.send_message(message.chat.id, 'Такого пользователя нет в списке. Повторите действие '
                                                    'и введите username другого пользователя')



        a = 0

    elif a == 11:
        file = open('usernames', 'r')
        user_str = ''
        usernames = file.read()
        file.close()
        user_list = str(usernames).split(',')
        if message.text in user_list:
            await bot.send_message(message.chat.id, 'Такой пользователь уже есть в списке. Повторите действие '
                                                    'и введите username другого пользователя')
        else:
            user_list.append(message.text)
            for user in user_list:
                user_str = user_str + f'{user},'

            user_str = user_str[:-1]

            file = open('usernames','w')
            file.write(user_str)
            await bot.send_message(message.chat.id, 'Пользователь успешно добавлен')


        a = 0

    elif a == 12:
        file = open('usernames', 'r')
        user_str = ''
        usernames = file.read()
        file.close()
        user_list = str(usernames).split(',')
        if message.text not in user_list:
            await bot.send_message(message.chat.id, 'Такого пользователя нет в списке. Повторите действие '
                                                    'и введите username другого пользователя')
        else:

            user_list.remove(message.text)
            for user in user_list:
                user_str = user_str + f'{user},'

            user_str = user_str[:-1]

            file = open('usernames', 'w')
            file.write(user_str)
            await bot.send_message(message.chat.id, 'Пользователь успешно удалён')


        a = 0

