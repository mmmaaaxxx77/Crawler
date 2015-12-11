import json
from requests import ConnectionError, HTTPError, Timeout, RequestException
from runner import bookRunner
import time
import runner


class BookTask:
    url = None

    def __init__(self, url, *array, **dic):
        self.url = url


    def run(self):
        try:
            book = bookRunner.crawlerBook(self.url, "/Users/udnDigital/Desktop/books/image2/")
            if book == None:
                book = bookRunner.crawlerBook(self.url, "/Users/udnDigital/Desktop/books/image2/")
            if book.__dict__ == None:
                book = bookRunner.crawlerBook(self.url, "/Users/udnDigital/Desktop/books/image2/")
            print(json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False))
            if(book.isbn != None):
                content = json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False)
                ff = open("/Users/udnDigital/Desktop/books/json2/" + book.isbn + "-" + book.fromWhere + ".json", 'a')
                ff.write(content)
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



