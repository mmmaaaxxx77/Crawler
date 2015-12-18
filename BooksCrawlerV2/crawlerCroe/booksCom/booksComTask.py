# -*- coding: utf-8 -*-
import json
from requests import ConnectionError, Timeout, HTTPError, RequestException
from book.models import Book
from crawlerCroe.booksCom import bookRunner
from crawlerCroe.booksCom import bookCrawler as crawler

__author__ = 'johnnytsai'


class BookTask:
    soup = None
    url = None

    def __init__(self, soup, url, *array, **dic):
        self.soup = soup
        self.url = url

    def run(self):
        book = dict(
            isbn=crawler.getIsbn(self.soup),
            name=crawler.getName(self.soup),
            name2=crawler.getName2(self.soup),
            author=crawler.getAuthor(self.soup),
            author2=crawler.getAuthor2(self.soup),
            translator=crawler.getTranslator(self.soup),
            publisher=crawler.getPublisher(self.soup),
            publicationDate=crawler.getPublicationDate(self.soup),
            language=crawler.getLanguage(self.soup),
            collection=crawler.getCollection(self.soup),
            specification=crawler.getSpecification(self.soup),
            publication=crawler.getPublication(self.soup),
            classification=crawler.getClassification(self.soup),
            coverImageUrl=crawler.getCoverImageUrl(self.soup),
            bookIntroduction=crawler.getBookIntroduction(self.soup),
            authorIntroduction=crawler.getAuthorIntroduction(self.soup),
            catalog=crawler.getCatalog(self.soup),
            preface=crawler.getPreface(self.soup),
            fromWhere="books",
            bookUrl=self.url,
            coverImageId=None
        )
        #if book.coverImageUrl is not None:
        #    if book.isbn is not None:
        #        book.coverImageId = book.isbn + ".jpg"
        b = Book(isbn="123")
        b.save()
        Book.objects.create()
        print("save:" + self.url)

