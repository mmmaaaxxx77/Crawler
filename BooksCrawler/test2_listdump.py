import time
from bookthread.bookTask import BookTask
from crawler import listCrawler
import urlList
from bs4 import BeautifulSoup
import requests

f = file("/Users/johnnytsai/books/list.txt", "w")

for url in urlList.booklist:
    html = requests.get(url, timeout=(1000.0, 1000.0)).text
    soup = BeautifulSoup(html, "html.parser")
    pageSize = listCrawler.getPageSize(soup)
    for index in range(pageSize):
        page = index+1
        html2 = requests.get(url + str(page), timeout=(1000.0, 1000.0)).text
        soup2 = BeautifulSoup(html2, "html.parser")
        for bookurl in listCrawler.getBookList(soup2):
            print("get and put url: " + bookurl)
            total_url_str = bookurl + "\n"
            f.write(total_url_str)
        time.sleep(1)
        print("get page: " + url + str(page))
    time.sleep(1)

f.close()
