import psycopg2
from config import configure
from src.Osintgram import Osintgram
from src.config import *
import time
import csv

# from instagram_private_api import ClientError
from src import config
import asyncio

from account import MainAccount

browser = None
class Account:
    def __init__(self, username):
        self.id = int()
        self.username = username
        self.fullname = str()
        self.followers = list()
        self.followings = list()
        self.email = str()
        self.phone = str()

Us = []
# api = Osintgram()
acc = MainAccount()

def ac1(username):

    acc.api.setTarget(username)

    info = acc.api.get_followers_te(True, True)

    #api.get_fwersemail()
    #api.get_followings()
    #mail = api.get_fwersemail()
   # phone = api.get_fwingsnumber()


    return  info

def photo_3(uname, limit):
    acc.api.setTarget(uname)
    paths = acc.api.get_user_photo(limit)
    return paths


def stories_4(uname, limit):
    acc.api.setTarget(uname)
    paths = acc.api.get_user_stories(limit)
    return paths


def geo_7(uname):
    acc.api.setTarget(uname)
    geo = acc.api.get_geo_addrs()
    return geo


def ac8(username):

    acc.api.setTarget(username)

    info = acc.api.get_followers(True, False)
    return info


def get_content(username):
    paths = []
    acc.api.setTarget(username)
    paths.append(acc.api.get_us_stories())
    paths.append(acc.api.get_us_photo())
    return paths


def post(url):

    likers = post_likers(acc.api.get_media_id(url))
    user_likers = acc.api.get_user_for_list(likers)
    time.sleep(5)

    comments = post_coments(acc.api.get_media_id(url))
    user_comments = acc.api.get_user_for_comments(comments)

    users = []
    users.append(user_likers)
    users.append(user_comments)

    return users


def post_likers(url):
    like_p = acc.api.api.media_likers(url)
    return like_p


def post_coments(url):
    comments_p = acc.api.api.media_comments(url)

    return comments_p


def connect():
    conn = None
    try:
        params = configure()
        conn = psycopg2.connect(**params)
        print('База подключена')
    except (Exception, psycopg2.DatabaseError):
        print('Нет подключения!')
    return conn


def disconnect(conn):
    if conn is not None:
        conn.close()


async def fwers_monitoring():
    con = connect()

    for uname in open('usernames', 'rt').read().split(','):
        acc.api.setTarget(uname)
        acc.api.get_fwers_info(con)
        print('Пользователь отработан')
        await asyncio.sleep(30)
    disconnect(con)


async def login_loop():


    while True:
        await asyncio.sleep(180)
        acc.check_status()


async def followers_loop():
    while True:
        # try:

        await fwers_monitoring()
        print('Поток отработан')
        await asyncio.sleep(300)

        # except:
        #     await asyncio.sleep(5)


async def main_loop():
    tasks = await asyncio.gather(
        # login_loop(),
        followers_loop(),
        return_exceptions=True
        )
    return tasks


def export_to_csv(table_name):
    con = connect()
    cur = con.cursor()
    cur.execute(u"SELECT * from " + table_name + u";")

    rows = cur.fetchall()
    print(rows)

    with open(f'{table_name}.csv', 'w',encoding='utf-16') as csvfile:
        cwriter = csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            cwriter.writerow(row)
    csvfile.close()
    disconnect(con)

def file_open(filename):
    file = open(filename,'rb')

    return file
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop())





if __name__ == '__main__':
    main()

