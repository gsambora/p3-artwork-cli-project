# lib/helpers.py
from models.artist import Artist
from models.work import Work

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def artist_by_name():
    name = input("Enter an artist's name: ")
    artist = Artist.find_by_name(name)

    if artist :
        print(artist)
    else:
        print(f"Artist {name} not in database.")

def artist_by_id():
    id = input("Enter an artist's ID: ")
    artist = Artist.find_by_id(id)

    if artist:
        print(artist)
    else:
        print(f"Artist {id} not in database.")

def artist_by_work():
    title = input("Enter the title of a work of art: ")
    work = Work.find_by_title(title)

    if work:
        artist = Artist.find_by_id(work.artist_id)
        print(f"Work {title} was created by: {artist}")

def list_all_works():
    works = Work.get_all()
    for work in works:
        print(work)

def list_movement():
    input = input("Enter an artistic movement: ")
    
    artists = Artist.get_all()
    for artist in artists:
        if artist.movement == input :
            print(artist)


def exit_program():
    print("Goodbye!")
    exit()
