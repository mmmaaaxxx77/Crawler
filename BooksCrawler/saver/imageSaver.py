# -*- coding: utf-8 -*-
import urllib


__author__ = 'johnnytsai'


def saveImageFile(path, imageUrl):
    urllib.urlretrieve(imageUrl,
                       path)


