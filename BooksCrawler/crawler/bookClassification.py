# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup


def getContent(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        result = soup.select('div.articulum > p')
        content = result[0].text.encode("utf-8")
        if len(content) != 0:
            #TODO
            pass
        else:
            getContent(html)
    except:
        print("soup exception")

