# lib/helpers.py
from models.artist import Artist
from models.work import Work

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")

def artist_by_name():
    name = input("Enter an artist's name: ")
    artist = Artist.find_by_name(name)

    if artist:
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    else:
        print(f"Artist {name} not in database.")

def artist_by_id():
    id = input("Enter an artist's ID: ")
    artist = Artist.find_by_id(id)

    if artist:
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    else:
        print(f"Artist {id} not in database.")
    
def artist_by_work():
    title = input("Enter the title of a work of art: ")
    work = Work.find_by_title(title)

    if work:
        artist = Artist.find_by_id(work.artist_id)
        print(f"The work {title} was created by: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    else:
        print(f"The work {title} is not in database.")
    
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

def update_artist(artist):
    pass

def artist_options():
    #print("The current artist is: ", Artist.current.name)
    print("0. Exit program")
    print("1. Update artist information")
    print("2. Remove artist from database")
    print("3. Return to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass

def exit_program():
    print("Goodbye!")
    exit()
