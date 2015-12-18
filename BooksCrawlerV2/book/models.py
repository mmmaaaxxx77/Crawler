# -*- coding: utf-8 -*-
import uuid

from django.db import models

__author__ = 'johnnytsai'


class Book(models.Model):

    # id
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # ISBN
    isbn = models.CharField(max_length=255)
    # 書名
    name = models.CharField(max_length=255)
    # 書名2
    name2 = models.CharField(max_length=255, null=True)
    # 作者
    author = models.CharField(max_length=255, null=True)
    # 作者2
    author2 = models.CharField(max_length=255, null=True)
    # 譯者
    translator = models.CharField(max_length=255, null=True)
    # 出版社
    publisher = models.CharField(max_length=255, null=True)
    # 出版日期
    publicationDate = models.DateField(null=True)
    # 語言
    language = models.CharField(max_length=255, null=True)
    # 叢書系列
    collection = models.CharField(max_length=255, null=True)
    # 規格
    specification = models.CharField(max_length=255, null=True)
    # 出版地
    publication = models.CharField(max_length=255, null=True)
    # 分類
    classification = models.CharField(max_length=255, null=True)
    # 封面圖id
    coverImageId = models.CharField(max_length=255, null=True)
    # 封面圖網址
    coverImageUrl = models.CharField(max_length=255, null=True)
    # 原網址
    bookUrl = models.CharField(max_length=255, null=True)
    # 內容簡介
    bookIntroduction = models.TextField(null=True)
    # 作者簡介
    authorIntroduction = models.TextField(null=True)
    # 目錄
    catalog = models.TextField(null=True)
    # 序
    preface = models.TextField(null=True)
    # 出自哪一網站
    fromWhere = models.CharField(max_length=255, null=True)
    # 建立時間
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改時間
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'book'
        db_table = 'books'


