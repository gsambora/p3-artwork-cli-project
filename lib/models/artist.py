from models.__init__ import CURSOR, CONN

class Artist:
    #Dictionary of data from all artist class instances
    all = {}

    def __init__(self, name, nationality, movement, id = None):
        #Each artist instance should have a name, nationality, and movement
        self.id = id
        self.name = name
        self.nationality = nationality
        self.movement = movement

    #Setting up name, nationality, and movement as attributes
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
        #Create an artists table in the database to hold data from the artist class instances
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
        #Drop the artists table from the database
        sql = """
            DROP TABLE IF EXISTS artists
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        #Save the current instance of the artist class as a row in the artists table and set the id attribute based on position in the table
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
        #Create a new instance of the artist class and call the save method
        artist = cls(name, nationality, movement)
        artist.save()

        return artist
    
    def update(self):
        #Update current artist's name, nationality, and movement
        sql = """
            UPDATE artists
            SET name = ?, nationality = ?, movement = ?
            WHERE id = ? 
        """
        CURSOR.execute(sql, (self.name, self.nationality, self.movement, self.id))
        CONN.commit()
    
    def delete(self):
        #Delete the current artist from the artists table and class dictionary
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

        #Delete dictionary entry using the id
        del type(self).all[self.id]

        #Set the id to none
        self.id = None