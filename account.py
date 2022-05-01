import os
from src.Osintgram import Osintgram
from instagram_private_api import ClientError
from loader import bot
from data import config

class MainAccount:
    def __init__(self):
        self.clean_cache()
        self.u = str()
        self.p = str()
        self.api: Osintgram = NotImplemented
        self.status = dict()
        self.file = open('credentials', 'rt').read()
        self.isLogged = False
        self.cred = dict()
        if len(self):
            self.creds = self.file.split(',')
            print(self.creds)
            # self.ch_status()
            self.select_account()
        else:
            print("Аккаунтов нет!")

    def select_account(self):
        self.ch_status()
        for u in self.cred:
            if self.cred[u]['status']:
                self.clean_cache()
                print(self.cred[u])
                self.u = u
                self.p = self.cred[u]['password']
                self.api = Osintgram(self.u, self.p, self.cred[u]['settings'])
                self.isLogged = True
                print(f'Вход под логином - {self.u}')
        if not self.isLogged:
            print("Нет валидных аккаунтов!")

    def __len__(self):
        if len(self.file) == 0:
            return 0
        else:
            return len(self.file.split(','))

    def ch_status(self):
        start = self.cred
        for cred in self.creds:
            self.clean_cache()
            u, p = cred.split(':')
            self.cred[u] = {'password': p, 'status': bool(), 'settings': dict()}
            try:
                print(self.cred[u])
                api = Osintgram(u, p, self.cred[u]['settings'])
                self.cred[u]['status'] = True
                self.cred[u]['settings'] = api.api.settings
            except ClientError as e:
                print(f'Login: {u}. Error: {e}')
                self.cred[u]['status'] = False
        return start, self.cred

    # Добавить MessageID
    def check_status(self):
        start, cred = self.ch_status()
        # for u in cred:
        #     if start[u]['status'] != start[u]['status']:
        #         if start[u]['status']:
        #              bot.send_message(config.ADMINS, f'{u} заблокирован.')
        #         else:
        #              bot.send_message(config.ADMINS, f'{u} снова активен.')
        return self.cred

    def button_check(self):
        good = bad = 0
        for cred in self.cred:
            if self.cred[cred]['status']:
                good += 1
            else:
                bad += 1
        return good, bad

    def clean_cache(self):
        settings_file = "config/settings.json"
        if os.path.isfile(settings_file):
            os.remove(settings_file)