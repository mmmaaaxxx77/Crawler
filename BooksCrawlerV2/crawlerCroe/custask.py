__author__ = 'johnnytsai'


class custask:
    num = 0

    def __init__(self, n, *array, **dic):
        self.num = n


    def run(self):
        print("hello:" + str(self.num))
