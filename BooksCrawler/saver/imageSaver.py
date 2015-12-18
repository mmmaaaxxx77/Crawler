# -*- coding: utf-8 -*-
from ftplib import FTP
import urllib
import cStringIO
from PIL import Image

__author__ = 'johnnytsai'


def saveImageFile(path, imageUrl):
    urllib.urlretrieve(imageUrl,
                       path)


def saveImageFileToFTP(file_name, url):
    try:
        ftp = FTP(host="172.19.51.222", user="crawler", passwd="11301130")
        file = cStringIO.StringIO(urllib.urlopen(url).read())
        ftp.storbinary("STOR /CrawlerData/Book_Image/" + file_name, file)
        ftp.close()
    except Exception as e:
        print e
"""
ftp = FTP(host="172.19.51.222", user="crawler", passwd="11301130")
file = cStringIO.StringIO(urllib.urlopen("http://im1.book.com.tw/image/getImage?i=http://www.books.com.tw/img/001/069/48/0010694873.jpg&v=562e0123&w=348&h=348").read())
img = Image.open(file)
ftp.storbinary("STOR /CrawlerData/Book_Image/123.jpg", file)
ftp.close()
"""
