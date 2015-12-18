# -*- coding: utf-8 -*-
import Queue
from threading import Thread
import time
from crawlerCroe.booksCom.mainRunner import BooksCom

__author__ = 'johnnytsai'

THREAD_NUM = 5


class Worker(Thread):
    def __init__(self, requests):
        Thread.__init__(self)
        self.running = False
        self.requests = requests

    def run(self):
        try:
            while True:

                self.running = True
                request = self.requests.get()
                if request is not None and request is not False:
                    request.run()
                    time.sleep(5)
                    self.requests.task_done()
                elif request is False:
                    self.running = False
                    break
        except Exception as e:
            print(e)

    def isRunning(self):
        return self.running


class QueuePoolService:
    def __init__(self):
        self.thread_list = []
        self.running = False
        self.requests = Queue.Queue(0)

    def start(self):
        if self.running is not True:
            self.running = True
            for thr in range(THREAD_NUM):
                self.thread_list.append(Worker(self.requests))
            for thr in self.thread_list:
                if thr.isRunning() is False:
                    thr.start()
            print("--- start thread ---")
            #
            booksCom = BooksCom(self.requests)
            booksCom.run()
            #
        else:
            return False

    def putRequest(self, request):
        self.requests.put(request)

    def createThread(self):
        work = Worker(self.requests)
        work.start()
        self.thread_list.append(work)

    def isRunning(self):
        return self.running

    def getQueue(self):
        return self.requests

    def destory(self):
        for thr in range(THREAD_NUM):
            self.thread_list.append(False)
