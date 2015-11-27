from bs4 import BeautifulSoup
import requests
import time
from crawler import listCrawler
from runner import runner


class ListTask:
    url = None

    def __init__(self, url, *array, **dic):
        self.url = url


    def run(self):
        html = requests.get(self.url, timeout=(10.0, 10.0)).text
        soup = BeautifulSoup(html, "html.parser")
        pageSize = listCrawler.getPageSize(soup)
        for index in range(pageSize):
            page = index+1
            html2 = requests.get(self.url + str(page), timeout=(10.0, 10.0)).text
            soup2 = BeautifulSoup(html2, "html.parser")
            for bookurl in listCrawler.getBookList(soup2):
                runner.booksQueue.put(bookurl)
        time.sleep(1)


