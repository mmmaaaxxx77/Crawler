# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import crawler.bookCrawler as crawler
from model.book import Book
from saver import imageSaver

def crawlerBook(url, imagePath):
    try:
        print("now :" + url)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 'Connection': 'close'}
        req = requests.get(url, timeout=(60.0, 60.0), headers=header)
        if req.status_code == 408:
            print("CODE: 408......")
            time.sleep(120)
            crawlerBook(url, imagePath)

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
        print("soup: " + str(soup))
        soup = None
        # save image
        book.bookUrl = url
        if book.coverImageUrl != None:
            if book.isbn != None:
                book.coverImageId = book.isbn + "-" + book.fromWhere + ".jpg"
                imageSaver.saveImageFile(imagePath + book.coverImageId, book.coverImageUrl)

        return book
    except:
        print("retry :" + url)
        crawlerBook(url, imagePath)
        time.sleep(15)



"""
html = requests.get("http://www.books.com.tw/products/0010692781?loc=P_004_050", timeout=(10.0, 10.0)).text
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
    preface=crawler.getPreface(soup)
)
# save image
book.coverImageId = book.isbn + ".jpg"
imageSaver.saveImageFile("/Users/johnnytsai/Desktop/test/" + book.coverImageId, book.coverImageUrl)


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
#print("BookUrl: " + ("None" if book.publication == None else book.bookUrl))
print("BookIntroduction: " + ("None" if book.bookIntroduction == None else book.bookIntroduction))
print("AuthorIntroduction: " + ("None" if book.authorIntroduction == None else book.authorIntroduction))
print("Catalog: " + ("None" if book.catalog == None else book.catalog))
print("Preface: " + ("None" if book.preface == None else book.preface))
"""

