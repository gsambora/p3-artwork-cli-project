from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Work:
    def __init__(self, title, year, medium, id=None):
        self.id = id
        self.title = title
        self.year = year
        self.medium = medium