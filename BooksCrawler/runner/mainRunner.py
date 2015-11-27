# -*- coding: utf-8 -*-
import Queue
from threading import *
import time
from bookthread.bookTask import BookTask
from crawler import listCrawler
import urlList
from bs4 import BeautifulSoup
import requests

__author__ = 'johnnytsai'

threadPool = Queue.Queue(0)

class Worker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cond = Condition()
        self.idel = True

    def run(self):
        while (True):
            task = threadPool.get()
            self.idel = False
            if task != None:
                self.cond.acquire()
                task.run()
                self.cond.release()
            threadPool.task_done()
            self.idel = True

checkergo = False
class Checker(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while (True):
            num = 0
            for wok in iter(threadPool.get, None):
                if wok.idel == True:
                    num += 1

            if num == 5:
                print("--------- all finish ---------")
                break
            else:
                print("--------- working ---------")
            time.sleep(10)



## book url queue
booksQueue = Queue.Queue(0)

## 啟動 worker
for i in xrange(5):
    Worker().start()
print("--------- worker started ---------")


## 抓取book 各分類分頁page
for url in urlList.booklist:
    html = requests.get(url, timeout=(10.0, 10.0)).text
    soup = BeautifulSoup(html, "html.parser")
    pageSize = listCrawler.getPageSize(soup)
    for index in range(pageSize):
        page = index+1
        html2 = requests.get(url + str(page), timeout=(10.0, 10.0)).text
        soup2 = BeautifulSoup(html2, "html.parser")
        for bookurl in listCrawler.getBookList(soup2):
            #booksQueue.put(bookurl)
            threadPool.put(BookTask(bookurl))
            print("get and put url: " + bookurl)
            if checkergo == False:
                Checker().start()
                checkergo = True
        time.sleep(1)
        print("get page: " + url + str(page))
    time.sleep(1)

#print("booksQueue size: " + str(booksQueue.qsize()))
print("--------- booksQueue finish ---------")


## 抓取book
##for bookUrl in iter(booksQueue.get, None):
##    threadPool.put(BookTask(bookUrl))