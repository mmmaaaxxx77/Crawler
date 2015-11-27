# -*- coding: utf-8 -*-
from datetime import datetime
from bs4 import BeautifulSoup
import pytz
from urlparse import urlparse, parse_qs, urlunparse
from urllib import urlencode

__author__ = 'johnnytsai'


def isFiledSame(soup, soupeSelect, name):
    try:
        result = soup.select(soupeSelect)
        content = result[0].text.encode("utf-8")
        if content.find(name) != -1:
            return True
        else:
            return  False
    except:
        return False


def findSameTextFieldInList(soup, soupeSelect, name):
    try:
        result = soup.select(soupeSelect)
        for txt in result:
            if txt.text.encode("utf-8").find(name) != -1:
                return txt
        return None
    except:
        return None

def findTargetReturnNeeds(soup, target, name, check):
    try:
        result = soup.select(target)
        for txt in result:
            s = BeautifulSoup(str(txt), "html.parser")
            r = s.select(check)
            if r[0].text.encode("utf-8").find(name) != -1:
                return txt
        return None
    except:
        return None


def getIsbn(soup):
    try:
        result = soup.select('meta[itemprop="productID"]')
        content = result[0]['content'].encode("utf-8")
        if len(content) != 0:
            return content.split(":")[1]
        else:
            getIsbn(soup)
    except:
        print("getIsbn exception")
    return None


def getName(soup):
    try:
        result = soup.select('h1[itemprop="name"]')
        content = result[0].text.encode("utf-8")
        if len(content) != 0:
            return content
        else:
            getName(soup)
    except:
        print("getName exception")
    return None


def getName2(soup):
    try:
        # 確認欄位
        result = soup.select('div.mod.type02_p002.clearfix > h2 > a')
        content = result[0].text.encode("utf-8")
        if len(content) != 0:
            return content
        else:
            getName2(soup)
    except:
        print("getName2 exception")
    return None


def getAuthor(soup):
    if isFiledSame(soup, 'div.type02_p003.clearfix > ul > li[itemprop="author"]', "作者："):
        try:
            result = soup.select('div.type02_p003.clearfix > ul > li[itemprop="author"] > a')
            content = ""
            for n in result:
                if(n['href'].find("prod_search") != -1):
                    content += n.text.encode("utf-8") + ","
            if len(content) != 0:
                return content[:-1]
            else:
                getAuthor(soup)
        except:
            print("getAuthor exception")
    else:
        return None


def getAuthor2(soup):
    if isFiledSame(soup, 'div.type02_p003.clearfix > ul > li[itemprop="author"]', "原文作者："):
        try:
            result = soup.select('div.type02_p003.clearfix > ul > li[itemprop="author"] > a')
            content = ""
            for n in result:
                if(n['href'].find("prod_search") != -1):
                    content += n.text.encode("utf-8") + ","
            if len(content) != 0:
                return content[:-1]
            else:
                getAuthor(soup)
        except:
            print("getAuthor2 exception")
    else:
        return None


def getTranslator(soup):
    field = findSameTextFieldInList(soup, "div.type02_p003.clearfix > ul > li", "譯者：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1]
            else:
                getAuthor2(soup)
        except:
            print("getTranslator exception")
    else:
        return None


def getPublisher(soup):
    try:
        result = soup.select('span[itemprop="brand"]')
        content = result[0].text.encode("utf-8")
        if len(content) != 0:
            return content
        else:
            getAuthor2(soup)
    except:
        print("getPublisher exception")
    return None


def getPublicationDate(soup):
    field = findSameTextFieldInList(soup, "div.type02_p003.clearfix > ul > li", "出版日期：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return str(datetime.strptime(content.split("：")[1],
                                                    "%Y/%m/%d").replace(tzinfo=pytz.utc))
            else:
                getAuthor2(soup)
        except:
            print("getPublicationDate exception")
    else:
        return None


def getLanguage(soup):
    field = findSameTextFieldInList(soup, "div.type02_p003.clearfix > ul > li", "語言：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1].replace(" ","")
            else:
                getAuthor2(soup)
        except:
            print("getLanguage exception")
    else:
        return None


def getCollection(soup):
    field = findSameTextFieldInList(soup, "div.bd > ul > li", "叢書系列：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1]
            else:
                getAuthor2(soup)
        except:
            print("getCollection exception")
    else:
        return None


def getSpecification(soup):
    field = findSameTextFieldInList(soup, "div.bd > ul > li", "規格：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1].replace(" ", "")
            else:
                getAuthor2(soup)
        except:
            print("getSpecification exception")
    else:
        return None


def getPublication(soup):
    field = findSameTextFieldInList(soup, "div.bd > ul > li", "出版地：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1].replace(" ","")
            else:
                getAuthor2(soup)
        except:
            print("getPublication exception")
    else:
        return None


def getClassification(soup):
    field = findSameTextFieldInList(soup, "div.bd > ul > li", "本書分類：")
    if field != None:
        try:
            content = field.text.encode("utf-8")
            if len(content) != 0:
                return content.split("：")[1].replace(" ", "")
            else:
                getAuthor2(soup)
        except:
            print("getClassification exception")
    else:
        return None


def getCoverImageUrl(soup):
    try:
        result = soup.select('div.cnt_mod002.cover_img > img')
        content = result[0]['src'].encode("utf-8")
        if len(content) != 0:
            u = urlparse(content)
            query = parse_qs(u.query)
            query.pop('h', None)
            query.pop('w', None)
            u = u._replace(query=urlencode(query, True))
            #pasr = urlparse(content).query[2:]
            if(urlunparse(u).find("comingsoon_sq.jpg") != -1):
                return None
            return urlunparse(u)
        else:
            getCoverImageUrl(soup)
    except:
        return None
    return None


def getBookIntroduction(soup):
    try:
        result = soup.select('div.content')
        content = result[0].text.encode("utf-8").lstrip()
        if len(content) != 0:
            return content
        else:
            getBookIntroduction(soup).lstrip()
    except:
        print("getBookIntroduction exception")
    return None


def getAuthorIntroduction(soup):
    try:
        result = findTargetReturnNeeds(soup, 'div.mod_b.type02_m057.clearfix', "作者介紹", 'h3')
        return (BeautifulSoup(str(result), "html.parser")).select('div.content')[0].text.encode("utf-8").lstrip()
    except:
        print("getAuthorIntroduction exception")
    return None


def getCatalog(soup):
    try:
        result = findTargetReturnNeeds(soup, 'div.mod_b.type02_m057.clearfix', "目錄", 'h3')
        return (BeautifulSoup(str(result), "html.parser")).select('div.content')[0].text.encode("utf-8").lstrip()
    except:
        print("getCatalog exception")
    return None


def getPreface(soup):
    try:
        result = findTargetReturnNeeds(soup, 'div.mod_b.type02_m057.clearfix', "序", 'h3')
        return (BeautifulSoup(str(result), "html.parser")).select('div.content')[0].text.encode("utf-8").lstrip()
    except:
        print("getPreface exception")
    return None