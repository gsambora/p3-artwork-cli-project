from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.work import Work

def reset_database():
    Artist.drop_table()
    Work.drop_table()
    Artist.create_table()
    Work.create_table()

reset_database()
print("Database reset")