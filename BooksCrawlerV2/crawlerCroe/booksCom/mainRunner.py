# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3 import Timeout
from requests.packages.urllib3.exceptions import ConnectionError
from crawlerCroe.booksCom import listCrawler
from crawlerCroe.booksCom.booksComTask import BookTask
from list import urlList

__author__ = 'johnnytsai'


class BooksCom:
    requests_list = None
    def __init__(self, requests_list, *array, **dic):
        self.requests_list = requests_list

    def getSoup(self, url):
        try:
            header = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
                'Connection': 'close'}
            req = requests.get(url, timeout=(120.0, 120.0), headers=header)
            if req.status_code == 408:
                print("CODE: 408......")
                time.sleep(120)
                self.getSoup(url)
        except ConnectionError as e:
            print("retry... " + url + e)
            self.getSoup(url)
            time.sleep(15)
        except Timeout as e:
            print("retry... " + url + e)
            self.getSoup(url)
            time.sleep(15)
        except Exception as e:
            print(e)
            print("retry :" + url)
            self.getSoup(url)
            time.sleep(15)
        return req

    def putBookUrl(self, url, index):
        page = index + 1
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Connection': 'close'}
        req = requests.get(url + str(page), timeout=(60.0, 60.0), headers=header)
        html2 = req.text
        req.close()
        soup2 = BeautifulSoup(html2, "html.parser")
        list = listCrawler.getBookList(soup2)
        for bookurl in list:
            print(bookurl)
            html = self.getSoup(bookurl).text
            soup = BeautifulSoup(html, "html.parser")
            self.requests_list.put(BookTask(soup, bookurl))
            time.sleep(2)
        time.sleep(3)
        print("get page list size: " + str(len(list)) + "; " + url)

    def run(self):
        ## 抓取book 各分類分頁page
        for url in urlList.booklist:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
                'Connection': 'close'}
            req = requests.get(url, timeout=(120.0, 120.0), headers=header)
            if req.status_code == 408:
                print("list get CODE: 408......")
                time.sleep(180)
                req = requests.get(url, timeout=(120.0, 120.0), headers=header)
                if req.status_code == 408:
                    print("list get CODE: 408......")
                    time.sleep(180)
                    req = requests.get(url, timeout=(120.0, 120.0), headers=header)
            html = req.text
            req.close()
            soup = BeautifulSoup(html, "html.parser")
            pageSize = listCrawler.getPageSize(soup)
            for index in range(pageSize):
                try:
                    self.putBookUrl(url, index)
                except:
                    time.sleep(3)
                    self.putBookUrl(url, index)
            time.sleep(1)
