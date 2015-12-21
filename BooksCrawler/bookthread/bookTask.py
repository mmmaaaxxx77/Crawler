import json
from peewee import DoesNotExist
from requests import ConnectionError, HTTPError, Timeout, RequestException
from model.book import Book
from runner import bookRunner
import time
import runner


class BookTask:
    url = None

    def __init__(self, url, *array, **dic):
        self.url = url
        self.num = 0

    def run(self):
        try:
            self.getBook()
        except ConnectionError as e:
            print("error cannot handel... " + e)
            if(self.num <=5):
                self.getBook()
            self.num += 1
        except Timeout as e:
            print("error cannot handel... " + e)
            if(self.num <=5):
                self.getBook()
            self.num += 1
        except HTTPError as e:
            print("error cannot handel... " + e)
            if(self.num <=5):
                self.getBook()
            self.num += 1
        except RequestException as e:
            print("error cannot handel... " + e)
            if(self.num <=5):
                self.getBook()
            self.num += 1
        except:
            print("book == null")
            if(self.num <=5):
                self.getBook()
            self.num += 1

    def getBook(self):
        book = bookRunner.crawlerBook(self.url)
        if book == None:
            book = bookRunner.crawlerBook(self.url)
        print(json.dumps(book, encoding="utf-8", ensure_ascii=False))
        if (book["isbn"] != None):
            """content = json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False)
                ff = open("/Users/udnDigital/Desktop/books/json2/" + book.isbn + "-" + book.fromWhere + ".json", 'a')
                ff.write(content)"""
            try:
                Book.get(isbn=book["isbn"])
            except DoesNotExist as e:
                Book.create(**book)
        else:
            print("error book")
            if(self.num <=5):
                self.getBook()
            self.num += 1
