# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from crawler import listCrawler
import urlList

__author__ = 'johnnytsai'


for l in urlList.booklist:
    html = requests.get(l, timeout=(10.0, 10.0)).text
    soup = BeautifulSoup(html, "html.parser")
    pageSize = listCrawler.getPageSize(soup)
    for index in range(pageSize):
        page = index+1
        html2 = requests.get(l + str(page), timeout=(10.0, 10.0)).text
        soup2 = BeautifulSoup(html2, "html.parser")
        print(listCrawler.getBookList(soup2))
