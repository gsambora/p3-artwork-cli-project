# lib/helpers.py
from models.artist import Artist
from models.work import Work

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def list_all_works():
    works = Work.get_all()
    for work in works:
        print(work)

def exit_program():
    print("Goodbye!")
    exit()
