class Movie(object):

    def __init__(self, title='', year='2000'):
        self.title = title
        self.year = year

    @classmethod
    def random(cls):
        from random import randint
        return cls(title='title' + str(randint(0, 1000000)))