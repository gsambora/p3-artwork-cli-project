from models.__init__ import CURSOR, CONN

class Artist:
    all = {}

    def __init__(self, name, nationality, movement, id = None):
        self.id = id
        self.name = name
        self.nationality = nationality
        self.movement = movement

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def nationality(self):
        return self._nationality
    
    @nationality.setter
    def nationality(self, nationality):
        if isinstance(nationality, str) and len(nationality):
            self._nationality = nationality
        else:
            raise ValueError(
                "Nationality must be a non-empty string"
            )
    
    @property
    def movement(self):
        return self._movement
    
    @movement.setter
    def movement(self, movement):
        if isinstance(movement, str) and len(movement):
            self._movement = movement
        else:
            raise ValueError(
                "Movement must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists(
            id INTEGER PRIMARY KEY,
            name TEXT,
            nationality TEXT,
            movement TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO artists (name, nationality, movement)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.nationality, self.movement))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, nationality, movement):
        artist = cls(name, nationality, movement)
        artist.save()

        return artist