# -*- coding: utf-8 -*-
import json
import time

from bs4 import BeautifulSoup
import requests

import bookRunner
from crawler import listCrawler
import urlList

__author__ = 'johnnytsai'

now_save = 0
now_error = []

for l in urlList.booklist:
    html = requests.get(l, timeout=(10.0, 10.0)).text
    soup = BeautifulSoup(html, "html.parser")
    pageSize = listCrawler.getPageSize(soup)
    for index in range(pageSize):
        page = index+1
        html2 = requests.get(l + str(page), timeout=(10.0, 10.0)).text
        soup2 = BeautifulSoup(html2, "html.parser")
        #print(listCrawler.getBookList(soup2))
        for bookurl in listCrawler.getBookList(soup2):
            book = bookRunner.crawlerBook(bookurl, "/Users/johnnytsai/Desktop/books/image2/")
            """
            print("ISBN: " + ("None" if book.isbn == None else book.isbn))
            print("Name: " + ("None" if book.name == None else book.name))
            print("Name2: " + ("None" if book.name2 == None else book.name2))
            print("Author: " + ("None" if book.author == None else book.author))
            print("Author2: " + ("None" if book.author2 == None else book.author2))
            print("Translator: " + ("None" if book.translator == None else book.translator))
            print("Publisher: " + ("None" if book.publisher == None else book.publisher))
            print("PublicationDate: " + ("None" if book.publicationDate == None else book.publicationDate))
            print("Language: " + ("None" if book.language == None else book.language))
            print("Collection: " + ("None" if book.collection == None else book.collection))
            print("Specification: " + ("None" if book.specification == None else book.specification))
            print("Publication: " + ("None" if book.publication == None else book.publication))
            print("Classification: " + ("None" if book.classification == None else book.classification))
            print("CoverImageId: " + ("None" if book.publication == None else book.coverImageId))
            print("CoverImageUrl: " + ("None" if book.coverImageUrl == None else book.coverImageUrl))
            print("BookUrl: " + ("None" if book.publication == None else book.bookUrl))
            print("BookIntroduction: " + ("None" if book.bookIntroduction == None else book.bookIntroduction))
            print("AuthorIntroduction: " + ("None" if book.authorIntroduction == None else book.authorIntroduction))
            print("Catalog: " + ("None" if book.catalog == None else book.catalog))
            print("Preface: " + ("None" if book.preface == None else book.preface))
            print("--------------------")
            """
            print(json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False))
            if(book.isbn != None):
                content = json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False)
                ff = open("/Users/johnnytsai/Desktop/books/json2/" + book.isbn + "-" + book.fromWhere + ".json", 'a')
                ff.write(content)
                now_save += 1
            else:
                print("error book")
                now_error.append(book)
            print("now_save: " + str(now_save))
            print("now_error: " + str(len(now_error)))
            print("now_error: " + str(now_error))
            time.sleep(1)
        time.sleep(5)
