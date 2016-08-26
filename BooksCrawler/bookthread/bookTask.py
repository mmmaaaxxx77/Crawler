import json
from runner import bookRunner
import time
import runner


class BookTask:
    url = None

    def __init__(self, url, *array, **dic):
        self.url = url


    def run(self):
        book = bookRunner.crawlerBook(self.url, "/Users/johnnytsai/books/image/")
        print(json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False))
        if(book.isbn != None):
            content = json.dumps(book.__dict__, encoding="utf-8", ensure_ascii=False)
            ff = open("/Users/johnnytsai/books/json/" + book.isbn + "-" + book.fromWhere + ".json", 'a')
            ff.write(content)
        else:
            print("error book")
        time.sleep(1)

