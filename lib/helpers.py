# lib/helpers.py
from models.artist import Artist
from models.work import Work

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")

def artist_by_name():
    name = input("Enter an artist's name: ")
    try:
        artist = Artist.find_by_name(name)
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    except Exception:
        print(f"Artist {name} not in database. Would you like to add them?")
        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_artist(name)
        else:
            pass
    
def artist_by_work():
    title = input("Enter the title of a work of art: ")
    try:
        work = Work.find_by_title(title)
        artist = Artist.find_by_id(work.artist_id)
        print(f"The work {title} was created by: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    except Exception:
        print(f"Work {title} not in database.")

def list_movement():
    movement = input("Enter an artistic movement: ")
    
    artists = Artist.get_all()
    [print(artist) for artist in artists if artist.movement == movement]

def list_nationality():
    nationality = input("Enter a nationality: ")

    artists = Artist.get_all()
    [print(artist) for artist in artists if artist.nationality == nationality]

def update_artist(artist):
    try:
        artist.name = input("Enter the artist's updated name: ")
        artist.nationality = input("Enter the artist's updated nationality: ")
        artist.movement = input("Enter the artist's updated artistic movement: ")

        artist.update()
        print(f"Success! Updated artist information: {artist.name} | {artist.nationality} | {artist.movement}")

    except Exception as exc:
        print("Error updating artist: ", exc)

def delete_artist(artist):
    try:
        name = artist.name
        artist.delete()
        print(f"Success! Removed {name} and their works of art from database")
    except Exception as exc:
        print("Error deleting artist: ", exc)

def add_artist(name):
    try:
        nationality = input("Enter the artist's updated nationality: ")
        movement = input("Enter the artist's updated artistic movement: ")

        Artist.create(name, nationality, movement)
        print(f"Success! The artist {name} has been added to the database.")
        print(f"Would you like to add any of {name}'s works of art to the database?")
        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_work()
        else:
            pass
    except Exception as exc:
        print("Error adding new artist: ", exc)


def artist_options():
    #print("The current artist is: ", Artist.current.name)
    print("0. Exit program")
    print("1. Update artist information")
    print("2. Remove artist from database")
    print("3. Add a new work of art made by this artist")
    print("4. Return to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        update_artist(Artist.current)
    elif choice == "2":
        delete_artist(Artist.current)
    elif choice == "3":
        pass
    elif choice == "4":
        pass

#ARTWORK HELPERS
def list_all_works():
    works = Work.get_all()
    for work in works:
        print(work)

def find_work():
    title = input("Enter the title of a work of art: ")
    try:
        work = Work.find_by_title(title)
        artist = Artist.find_by_id(work.artist_id)
        print(f"{title} is a/an {work.medium} piece and was created in {work.year} by {artist.name}.")
    except Exception:
        print(f"Work {title} not in database. Would you like to add it? ")
        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_work(title)
        else:
            pass

def add_work(title=None):
    if not title:
        title = input("Enter the title of the work: ")
    year = int( input("Enter the year the work was created: ") )
    medium = input("Enter the art medium of the work: ")
    artist_input = input("Enter the name of the artist of the work: ")
    try:
        artist = Artist.find_by_name(artist_input)
        Work.create(title, year, medium, artist.id)
        print(f"Success! The work {title} has been added to the database")
    except Exception as exc:
        #print("Error: ", exc)
        print("The artist must already be in the database before entering the work.")
        print(f"Would you like to add the artist {artist_input}?")

        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_artist(artist_input)
        else:
            pass

def exit_program():
    print("Goodbye!")
    exit()
