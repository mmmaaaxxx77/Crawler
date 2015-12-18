# -*- coding: utf-8 -*-
import uuid
import datetime
from peewee import Model, Field, CharField, DateField, TextField, DateTimeField, MySQLDatabase

johnnyNAS = MySQLDatabase("crawler_data", host="172.19.51.222", port=3306, user="crawler",
                          passwd="1130")

class Book(Model):
    # id
    id = CharField(max_length=255, primary_key=True, default=uuid.uuid1, unique=False)
    # ISBN
    isbn = CharField(max_length=255, default="Null")
    # 書名
    name = CharField(max_length=255, default="Null")
    # 書名2
    name2 = CharField(max_length=255, null=True)
    # 作者
    author = CharField(max_length=255, null=True)
    # 作者2
    author2 = CharField(max_length=255, null=True)
    # 譯者
    translator = CharField(max_length=255, null=True)
    # 出版社
    publisher = CharField(max_length=255, null=True)
    # 出版日期
    publicationDate = DateTimeField(null=True, formats="%Y-%m-%d %H:%M:%S")
    # 語言
    language = CharField(max_length=255, null=True)
    # 叢書系列
    collection = CharField(max_length=255, null=True)
    # 規格
    specification = CharField(max_length=255, null=True)
    # 出版地
    publication = CharField(max_length=255, null=True)
    # 分類
    classification = CharField(max_length=255, null=True)
    # 封面圖id
    coverImageId = CharField(max_length=255, null=True)
    # 封面圖網址
    coverImageUrl = CharField(max_length=255, null=True)
    # 原網址
    bookUrl = CharField(max_length=255, null=True)
    # 內容簡介
    bookIntroduction = TextField(null=True)
    # 作者簡介
    authorIntroduction = TextField(null=True)
    # 目錄
    catalog = TextField(null=True)
    # 序
    preface = TextField(null=True)
    # 出自哪一網站
    fromWhere = CharField(max_length=255, null=True)
    # 建立時間
    createTime = DateTimeField(default=datetime.datetime.now)
    # 修改時間
    updateTime = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = johnnyNAS
        db_table = 'books'