# -*- coding: utf-8 -*-
import datetime
import base64

__author__ = 'johnnytsai'


class Book:
    # ISBN
    isbn = None
    # 書名
    name = None
    # 書名2
    name2 = None
    # 作者
    author = None
    # 作者2
    author2 = None
    # 譯者
    translator = None
    # 出版社
    publisher = None
    # 出版日期
    publicationDate = None
    # 語言
    language = None
    # 叢書系列
    collection = None
    # 規格
    specification = None
    # 出版地
    publication = None
    # 分類
    classification = None
    # 封面圖id
    coverImageId = None
    # 封面圖網址
    coverImageUrl = None
    # 原網址
    bookUrl = None
    # 內容簡介
    bookIntroduction = None
    # 作者簡介
    authorIntroduction = None
    # 目錄
    catalog = None
    # 序
    preface = None
    # 出自哪一網站
    fromWhere = None
    # 建立時間
    createDate = datetime.datetime.now()
    # 修改時間
    updateDate = datetime.datetime.now()

    def __init__(self, **dic):
        self.isbn = dic["isbn"]
        self.name = base64.b64encode(dic["name"])
        self.name2 = None if 'name2' not in dic else (None if dic["name2"] is None else base64.b64encode(dic["name2"]))
        self.author = None if 'author' not in dic else (None if dic["author"] is None else base64.b64encode(dic["author"]))
        self.author2 = None if 'author2' not in dic else (None if dic["author2"] is None else base64.b64encode(dic["author2"]))
        self.translator = None if 'translator' not in dic else (None if dic["translator"] is None else base64.b64encode(dic["translator"]))
        self.publisher = None if 'publisher' not in dic else (None if dic["publisher"] is None else base64.b64encode(dic["publisher"]))
        self.publicationDate = None if 'publicationDate' not in dic else dic["publicationDate"]
        self.language = None if 'language' not in dic else (None if dic["language"] is None else base64.b64encode(dic["language"]))
        self.collection = None if 'collection' not in dic else (None if dic["collection"] is None else base64.b64encode(dic["collection"]))
        self.specification = None if 'specification' not in dic else (None if dic["specification"] is None else base64.b64encode(dic["specification"]))
        self.publication = None if 'publication' not in dic else (None if dic["publication"] is None else base64.b64encode(dic["publication"]))
        self.classification = None if 'classification' not in dic else (None if dic["classification"] is None else base64.b64encode(dic["classification"]))
        self.coverImageId = None if 'coverImageId' not in dic else dic["coverImageId"]
        self.coverImageUrl = None if 'coverImageUrl' not in dic else dic["coverImageUrl"]
        self.bookUrl = None if 'bookUrl' not in dic else dic["bookUrl"]
        self.bookIntroduction = None if 'bookIntroduction' not in dic else (None if dic["bookIntroduction"] is None else base64.b64encode(dic["bookIntroduction"]))
        self.authorIntroduction = None if 'authorIntroduction' not in dic else (None if dic["authorIntroduction"] is None else base64.b64encode(dic["authorIntroduction"]))
        self.catalog = None if 'catalog' not in dic else (None if dic["catalog"] is None else base64.b64encode(dic["catalog"]))
        self.preface = None if 'preface' not in dic else (None if dic["preface"] is None else base64.b64encode(dic["preface"]))
        self.fromWhere = None if 'fromWhere' not in dic else dic["fromWhere"]


