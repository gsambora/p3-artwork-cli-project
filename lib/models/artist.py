from models.__init__ import CURSOR, CONN

class Artist:
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