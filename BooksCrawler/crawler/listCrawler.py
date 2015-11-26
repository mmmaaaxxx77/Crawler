# -*- coding: utf-8 -*-


def getPageSize(soup):
    try:
        p = soup.select('div.page > span')
        page = int(p[0].text.encode("utf-8"))
        return page
    except:
        print("getPageSize exception")
        return 0


def getBookList(soup):
    list = []
    try:
        p = soup.select('div.item > a')
        for o in p:
            list.append(o['href'].encode("utf-8"))
        return list
    except:
        print("getBookList exception")
        return list