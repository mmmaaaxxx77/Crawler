# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
from requests.packages.urllib3 import Timeout
from requests.packages.urllib3.exceptions import ConnectionError
from book.models import Book
from crawlerCroe.booksCom import bookCrawler as crawler


def crawlerBook(url):
    try:
        print("now :" + url)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Connection': 'close'}
        req = requests.get(url, timeout=(120.0, 120.0), headers=header)
        if req.status_code == 408:
            print("CODE: 408......")
            time.sleep(120)
            crawlerBook(url)

        html = req.text
        req.close()
        soup = BeautifulSoup(html, "html.parser")

        book = Book(
            isbn=crawler.getIsbn(soup),
            name=crawler.getName(soup),
            name2=crawler.getName2(soup),
            author=crawler.getAuthor(soup),
            author2=crawler.getAuthor2(soup),
            translator=crawler.getTranslator(soup),
            publisher=crawler.getPublisher(soup),
            publicationDate=crawler.getPublicationDate(soup),
            language=crawler.getLanguage(soup),
            collection=crawler.getCollection(soup),
            specification=crawler.getSpecification(soup),
            publication=crawler.getPublication(soup),
            classification=crawler.getClassification(soup),
            coverImageUrl=crawler.getCoverImageUrl(soup),
            bookIntroduction=crawler.getBookIntroduction(soup),
            authorIntroduction=crawler.getAuthorIntroduction(soup),
            catalog=crawler.getCatalog(soup),
            preface=crawler.getPreface(soup),
            fromWhere="books"
        )
        soup = None
        book.bookUrl = url
        if book.coverImageUrl is not None:
            if book.isbn is not None:
                book.coverImageId = book.isbn + ".jpg"

        return book
    except ConnectionError as e:
        print("retry... " + url + e)
        crawlerBook(url)
        time.sleep(15)
    except Timeout as e:
        print("retry... " + url + e)
        crawlerBook(url)
        time.sleep(15)
    except Exception as e:
        print(e)
        print("retry :" + url)
        crawlerBook(url)
        time.sleep(15)
