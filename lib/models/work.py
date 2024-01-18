from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Work:
    all = {}
    def __init__(self, title, year, medium, artist_id, id=None):
        self.id = id
        self.title = title
        self.year = year
        self.medium = medium
        self.artist_id = artist_id
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a non-empty string"
            )
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self._year= year
        else:
            raise ValueError(
                "Year must be an integer (Can't include B.C. or A.D.)"
            )
    
    @property
    def medium(self):
        return self._medium

    @medium.setter
    def medium(self, medium):
        if isinstance(medium, str) and len(medium):
            self._medium = medium
        else:
            raise ValueError(
                "Medium must be a non-empty string"
            )
    
    @property
    def artist_id(self):
        return self._artist_id
    
    @artist_id.setter
    def artist_id(self, artist_id):
        if isinstance(artist_id, int) and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError(
                "Artist ID must correspond with an artist in the database"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS works(
            id INTEGER PRIMARY KEY,
            title TEXT,
            year INTEGER,
            medium TEXT,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS works
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO works (title, year, medium, artist_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.year, self.medium, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, year, medium, artist_id):
        work = cls(title, year, medium, artist_id)
        work.save()

        return work
    