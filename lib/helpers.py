# lib/helpers.py
from models.artist import Artist
from models.work import Work

def list_artists():
    #List all artists in database and give user the option to add a new artist
    artists = Artist.get_all()
    for artist in artists:
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")

    print("Would you like to add a new work of art?")
    print("1. Yes")
    print("2. No")

    choice = input("> ")
    if choice == "1":
        add_artist()
    else:
        pass

def artist_by_name():
    #User can search for artist by name. 
    #If artist is found, user is given the artist_options menu. If not found, user can add the artist.
    name = input("Enter an artist's name: ")
    try:
        artist = Artist.find_by_name(name)
        print(f"Artist: {artist.name} | {artist.nationality} | {artist.movement}")
        Artist.current = artist
        artist_options()
    except Exception:
        artist_not_found(name)

def artist_not_found(name=None):
    #Function to be called when an artist is not found in the database. 
    #Calls add_artist with the name originally provided by user.
    print(f"Artist {name} not in database. Would you like to add them?")
    print("1. Yes")
    print("2. No")

    choice = input("> ")
    if choice == "1":
        add_artist(name)
    else:
        pass

def artist_by_work():
    #User can search for artist by work. 
    #If the work is found, the user is given the artist_options menu. If not found, the user can add the work.
    title = input("Enter the title of a work of art: ")
    try:
        work = Work.find_by_title(title)
        artist = Artist.find_by_id(work.artist_id)
        print(f'The work "{title}" was created by: {artist.name} | {artist.nationality} | {artist.movement}')
        Artist.current = artist
        artist_options()
    except Exception:
        work_not_found(title)

def list_movement():
    #User inputs an artistic movement and receives a list of the artists in that movement.
    #If there are no artists in the movement, user gets a message.
    movement = input("Enter an artistic movement: ")
    try:
        artists = Artist.get_all()
        [print(artist) for artist in artists if artist.movement == movement]
    except:
        print("There are no artists in that movement currently in the database.")

def list_nationality():
    #User inputs a nationality and receives a list of artists with that nationality.
    #If there are no corresponding artists, user gets an error message.
    nationality = input("Enter a nationality: ")
    try:
        artists = Artist.get_all()
        [print(artist) for artist in artists if artist.nationality == nationality]
    except:
        print("There are no artists in that movement currently in the database.")

def update_artist(artist=None):
    #Updates the artist information with user input. artist variable may be provided from the user finding an artist,
    #If called outside of the user finding an artist, then the user will enter the name of the artist to update.
    if not artist:
        name = input("Enter the name of the artist you want to update: ")
        artist = Artist.find_by_name(name)
    try:
        artist.name = input("Enter the artist's updated name: ")
        artist.nationality = input("Enter the artist's updated nationality: ")
        artist.movement = input("Enter the artist's updated artistic movement: ")

        artist.update()
        print(f"Success! Updated artist information: {artist.name} | {artist.nationality} | {artist.movement}")

    except Exception as exc:
        print("Error updating artist: ", exc)

def delete_artist(artist=None):
    #Deletes an artist from the database. artist variable may be provided from the user finding an artist.
    if not artist:
        name = input("Enter the name of the artist you want to remove: ")
        artist = Artist.find_by_name(name)
    try:
        name = artist.name
        artist.delete()
        print(f"Success! Removed {name} and their works of art from database")
    except Exception as exc:
        print("Error deleting artist: ", exc)

def add_artist(name=None):
    #Adds an artist to the database with user input. name may be provided from previous user search for that name.
    #Once the artist is added, the user gets an option to add works by that artist.
    if not name:
        name = input("Enter the artist's name: ")
    try:
        nationality = input("Enter the artist's nationality: ")
        movement = input("Enter the artist's primary artistic movement: ")

        Artist.create(name, nationality, movement)
        print(f"Success! The artist {name} has been added to the database.")
        print(f"Would you like to add any of {name}'s works of art to the database?")
        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_work(None, name)
        else:
            pass
    except Exception as exc:
        print("Error adding new artist: ", exc)


def artist_options():
    #Options to provide the user whenever they find an artist. 
    #They can easily update/remove the artist or add a new work made by the found artist.
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
    #List all works currently in the database. User can then add a new work.
    works = Work.get_all()
    for work in works:
        artist = Artist.find_by_id(work.artist_id)
        print(f'"{work.title}" | {work.year} | {work.medium} | {artist.name}')
    
    print("Would you like to add a new work of art?")
    print("1. Yes")
    print("2. No")

    choice = input("> ")
    if choice == "1":
        add_work()
    else:
        pass

def work_not_found(title=None):
    #Display when a user searches for a work and it is not found. User gets option to add work by the provided name.
    print(f"Work {title} not in database. Would you like to add it? ")
    print("1. Yes")
    print("2. No")

    choice = input("> ")
    if choice == "1":
        add_work(title)
    else:
        pass

def find_work():
    #User can search for a work by name. If found, user sees the work_options menu.
    #If not found, user gets work_not_found menu with option to add the work.
    title = input("Enter the title of a work of art: ")
    try:
        work = Work.find_by_title(title)
        artist = Artist.find_by_id(work.artist_id)
        print(f'"{title}" is a/an {work.medium} piece and was created in {work.year} by {artist.name}.')
        Work.current = work
        work_options()
    except Exception:
        work_not_found(title)

def works_by_artist():
    #User can search for all works made by an artist, then gets an opportunity to add a new work by that artist.
    #If the artist provided is not in the database, the user gets an opportunity to add the artist.
    name = input("Enter an artist's name: ")
    try: 
        artist = Artist.find_by_name(name)
        works = artist.works()
        [print(f'The work "{work.title}" was created by: {artist.name} | {artist.nationality} | {artist.movement}') for work in works]
        print(f"Would you like to add a new work by {name}?")
        print("1. Yes")
        print("2. No")

        choice = input("> ")
        if choice == "1":
            add_work()
        else:
            pass
    except Exception as exc:
        #print("Error: ", exc)
        artist_not_found(name)

def works_by_medium():
    #User can search for all works made with the provided medium.
    #If there are no corresponding works, user receives an error message.
    medium = input("Enter an artistic medium: ")
    try:
        works = Work.get_all()
        [print(f'"{work.title}" is a/an {work.medium} piece and was created in {work.year} by {Artist.find_by_id(work.artist_id).name}.') for work in works if work.medium == medium]
    except:
        print(f"There are no {medium} works currently in the database.")

def add_work(title=None, artist_input=None):
    #User can add a work. Title and artist's name may be provided from previous user input.
    #If the artist of the work is not in the database, the user can add that artist.
    if not title:
        title = input("Enter the title of the work: ")
    year = int( input("Enter the year the work was created: ") )
    medium = input("Enter the art medium of the work: ")
    if not artist_input:
        artist_input = input("Enter the name of the artist of the work: ")
    try:
        artist = Artist.find_by_name(artist_input)
        Work.create(title, year, medium, artist.id)
        print(f"Success! The work {title} has been added to the database")
    except Exception as exc:
        #print("Error: ", exc)
        print("The artist must already be in the database before entering the work.")
        artist_not_found(artist_input)

def update_work(work=None):
    #User can update a work's title, year, medium, and artist. The work may be provided from a previous user step. 
    if not work:
        title = input("Enter the title of the work you want to update: ")
        work = Work.find_by_title(title)
    
    try:
        work.title = input("Enter the updated title of the work: ")
        work.year = int( input("Enter the updated year the work was created: ") )
        work.medium = input("Enter the updated art medium of the work: ")
        artist = input("Enter the updated name of the work's artist: ")
        print(Artist.find_by_name(artist).id)
        work.artist_id = int( Artist.find_by_name(artist).id )

        work.update()
        print(f"Success! Updated work information: {work.title} | {work.year} | {work.medium}")
    
    except Exception as exc:
        print("Error updating work: ", exc)

def delete_work(work=None):
    #User can delete a work by providing a title. Title may already be provided from previous step.
    if not work:
        title = input("Enter the title of the work you want to delete: ")
        work = Work.find_by_title(title)

    try:
        title = work.title
        work.delete()
        print(f"Success! Removed {title} from database")
    except Exception as exc:
        print("Error deleting work: ", exc)

def work_options():
    #Options to display whenever user finds a work. User can update or remove the found work.
    print("0. Exit program")
    print("1. Update work information")
    print("2. Remove work from database")
    print("3. Return to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        update_work(Work.current)
    elif choice == "2":
        delete_work(Work.current)
    elif choice == "3":
        pass

def exit_program():
    print("Goodbye!")
    exit()
