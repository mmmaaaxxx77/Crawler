# -*- coding: utf-8 -*-
import Queue
from threading import Thread, Condition
import time

__author__ = 'johnnytsai'

requestList = Queue.Queue(0)


class Worker(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.isContinue = False
        self.con = Condition()
        self.request = None

    def run(self):
        try:
            while self.isContinue:
                self.condition.acquire()
                self.condition.wait()
                self.request()
                self.request = None
                self.condition.release()

        except Exception as e:
            print(e)

    def setRequest(self, request):
        self.con.acquire()
        if self.isIdle():
            self.request = request
        self.con.notify()
        self.con.release()

    def isIdle(self):
            return self.request is None

    def terminate(self):
        self.isContinue = False
        self.setRequest(lambda: None)


class ThreadPool(object):
    def __init__(self):
        self.workerThreads = []

    def service(self, request):
        idleNotFound = True
        for workerThread in self.workerThreads:
            if workerThread.isIdle():
                workerThread.setRequest(request)
                idleNotFound = False
                break
        if idleNotFound:
            workerThread = self.createWorkerThread()
            workerThread.setRequest(request)

    def cleanIdle(self):
        for workerThread in self.workerThreads:
            if workerThread.isIdle():
                self.workerThreads.remove(workerThread)
                workerThread.terminate()

    def createWorkerThread(self):
        workerThread = Worker()
        workerThread.start()
        self.workerThreads.append(workerThread)
        time.sleep(1)
        return workerThread


