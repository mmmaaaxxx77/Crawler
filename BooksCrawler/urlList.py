# -*- coding: utf-8 -*-


booklist = []
"""
    # 翻譯文學
    "http://www.books.com.tw/web/sys_midme/books/0101/?o=1&v=1&page=",
    # 華文創作
    "http://www.books.com.tw/web/sys_midme/books/0102/?o=1&v=1&page=",
    # 詩
    "http://www.books.com.tw/web/sys_midme/books/0103/?o=1&v=1&page=",
    # 文學研究
    "http://www.books.com.tw/web/sys_midme/books/0104/?o=1&v=1&page=",
    # 中國古典文學
    "http://www.books.com.tw/web/sys_midme/books/0105/?o=1&v=1&page=",
    # 國學常識
    "http://www.books.com.tw/web/sys_midme/books/0106/?o=1&v=1&page=",
    # 世界經典文學
    "http://www.books.com.tw/web/sys_midme/books/0107/?o=1&v=1&page=",
    # 懸疑/推理小說
    "http://www.books.com.tw/web/sys_midme/books/0108/?o=1&v=1&page=",
    # 科幻/奇幻小說
    "http://www.books.com.tw/web/sys_midme/books/0109/?o=1&v=1&page=",
    # 恐怖/驚悚小說
    "http://www.books.com.tw/web/sys_midme/books/0110/?o=1&v=1&page=",
    # 溫馨/療癒小說
    "http://www.books.com.tw/web/sys_midme/books/0111/?o=1&v=1&page=",
    # 愛情小說
    "http://www.books.com.tw/web/sys_midme/books/0112/?o=1&v=1&page=",
    # 同性愛小說
    "http://www.books.com.tw/web/sys_midme/books/0113/?o=1&v=1&page=",
    # 羅曼史/言情小說
    "http://www.books.com.tw/web/sys_midme/books/0114/?o=1&v=1&page=",
    # 歷史/武俠小說
    "http://www.books.com.tw/web/sys_midme/books/0115/?o=1&v=1&page=",
    # 其他文學小說
    "http://www.books.com.tw/web/sys_midme/books/0116/?o=1&v=1&page=",
    #
    #
    "http://www.books.com.tw/web/sys_midme/books/0201/?o=1&v=1&page=",
    "http://www.books.com.tw/web/sys_midme/books/0202/?o=1&v=1&page=",
    "http://www.books.com.tw/web/sys_midme/books/0203/?o=1&v=1&page=",
    "http://www.books.com.tw/web/sys_midme/books/0204/?o=1&v=1&page=",
    "http://www.books.com.tw/web/sys_midme/books/0201/?o=1&v=1&page=",
]"""

# 文學小說
for i in range(16):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/01" + s + "/?o=1&v=1&page=")

# 商業理財
for i in range(11):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/02" + s + "/?o=1&v=1&page=")


# 藝術設計
for i in range(13):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/03" + s + "/?o=1&v=1&page=")


# 人文史地
for i in range(7):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/04" + s + "/?o=1&v=1&page=")


# 社會科學
for i in range(15):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/05" + s + "/?o=1&v=1&page=")


# 自然科普
for i in range(8):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/06" + s + "/?o=1&v=1&page=")


# 心理勵志
for i in range(15):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/07" + s + "/?o=1&v=1&page=")


# 醫療保健
for i in range(7):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/08" + s + "/?o=1&v=1&page=")


# 飲食
for i in range(8):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/09" + s + "/?o=1&v=1&page=")


# 生活風格
for i in range(9):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/10" + s + "/?o=1&v=1&page=")


# 旅遊
for i in range(10):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/11" + s + "/?o=1&v=1&page=")


# 宗教命理
for i in range(10):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/12" + s + "/?o=1&v=1&page=")


# 親子教養
for i in range(5):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/13" + s + "/?o=1&v=1&page=")


# 童書/青少年文學
for i in range(13):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/14" + s + "/?o=1&v=1&page=")


# 輕小說
for i in range(4):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/15" + s + "/?o=1&v=1&page=")


# 漫畫
for i in range(14):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/16" + s + "/?o=1&v=1&page=")


# 語言學習
for i in range(6):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/17" + s + "/?o=1&v=1&page=")


# 考試用書
for i in range(14):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/18" + s + "/?o=1&v=1&page=")


# 電腦資訊
for i in range(14):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/19" + s + "/?o=1&v=1&page=")


# 專業/教科書/政府出版品
for i in range(20):
    p = i+1
    s = str(p) if p >= 10 else "0" + str(p)
    booklist.append("http://www.books.com.tw/web/sys_midme/books/20" + s + "/?o=1&v=1&page=")