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


    def run(self):
        try:
            book = bookRunner.crawlerBook(self.url)
            if book == None:
                book = bookRunner.crawlerBook(self.url)
            print(json.dumps(book, encoding="utf-8", ensure_ascii=False))
            if(book["isbn"] != None):
                """content = json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False)
                ff = open("/Users/udnDigital/Desktop/books/json2/" + book.isbn + "-" + book.fromWhere + ".json", 'a')
                ff.write(content)"""
                try:
                    Book.get(isbn=book["isbn"])
                except DoesNotExist as e:
                    Book.create(**book)
            else:
                print("error book")
        except ConnectionError as e:
            print("error cannot handel... " + e)
        except Timeout as e:
            print("error cannot handel... " + e)
        except HTTPError as e:
            print("error cannot handel... " + e)
        except RequestException as e:
            print("error cannot handel... " + e)
        except:
            print("book == null")



