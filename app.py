from aiogram import executor, Dispatcher
import concurrent.futures
from loader import dp
import  multiprocessing
from multiprocessing import process
import logging
from  handlers.handlers import *
from loguru import logger
logging.basicConfig(level=logging.INFO)

import threading

processes = []


def fol_l():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(followers_loop())
    loop.close()

class MyPausableThread(threading.Thread):

    def __init__(self, group=None, target=fol_l, name=None, args=(), kwargs={}):
        self._event = threading.Event()
        if target:

            args = ((lambda: self._event.wait()),) + args
        super(MyPausableThread, self).__init__(group, target, name, args, kwargs)

    def pause(self):
        self._event.clear()

    def resume(self):
        print(1)
        self._event.set()




def bot_start():

   executor.start_polling(dp, skip_updates=True)

def login_l():

    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    loop.run_until_complete(login_loop())

    print(1)
    loop.close()




# th1 = MyPausableThread()
#
th1 = threading.Thread(target=fol_l)
th2 = threading.Thread(target=login_l)
if __name__ == '__main__':

    # th1.start()
    # th2.start()  # th1.resume()
    bot_start()


    # for func in [fol_l,bot_start]:
    #     processes.append(multiprocessing.Process(target=func ))
    #     processes[-1].start()
    # print(1)
    # # Do stuff
    #
    # while True:
    #     time.sleep(600)  # sleep for 10 minutes
    #     living_processes = [p.is_alive() for p in processes]
    #     if len(living_processes) < 2:
    #         for p in living_processes:
    #             p.terminate()
    #
    #         print("Oops: Some processes died")
    # # # th1.run()
    # # bot_start()

















