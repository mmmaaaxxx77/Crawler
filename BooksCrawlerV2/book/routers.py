__author__ = 'johnnytsai'

class MyDB2Router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'book':
            return 'book'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'book':
            return 'book'
        return None

    def allow_syncdb(self, db, model):
        if db == 'book' or model._meta.app_label == "book":
            return True
        else:
            return True
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'book' or \
           obj2._meta.app_label == 'book':
           return True
        return None

    def allow_migrate(self, db, model):
        if db == 'book':
            return model._meta.app_label == 'book'
        else:
            return True
        return None