# lib/cli.py

from helpers import (
    exit_program,
    list_artists,
    list_all_works,
    artist_by_work,
    artist_by_name,
    list_movement,
    list_nationality,
    find_work,
    works_by_artist,
    works_by_medium,
    add_artist,
    update_artist,
    delete_artist
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_artists()
        elif choice == "2":
            artist_loop()
        elif choice == "3":
            list_movement()
        elif choice == "4":
            list_nationality()
        elif choice == "5":
            list_all_works()
        elif choice == "6":
            find_work()
        elif choice == "7":
            works_by_artist()
        elif choice == "8":
            works_by_medium()
        else:
            print("Invalid choice")

def artist_loop():
    find_artist_menu()
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        artist_by_name()
    elif choice == "2":
        artist_by_work()
    elif choice == "3":
        # go back to previous menu
        main()
    else:
        print("Invalid choice")

def database_loop():
    database_menu()
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        add_artist()
    elif choice == "2":
        update_artist()
    elif choice == "3":
        delete_artist()
    elif choice == "4":
        list_nationality()
    elif choice == "5":
        list_all_works()
    elif choice == "6":
        find_work()

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all artists")
    print("2. Find an artist") #Find artist menu
    print("3. List artists by movement")
    print("4. List artists by nationality")
    print("5. List all works of art")
    print("6. Find a work of art") #Find work menu
    print("7. List works by artist")
    print("8. List works by medium")
    print("9. Add, update, or remove database information") #Database menu


def find_artist_menu():
    print("0. Exit the program")
    print("1. Find artist by name")
    print("2. Find artist by work")
    print("3. Return to main menu")

def database_menu():
    print("0. Exit the program")
    print("1. Add an artist to the database")
    print("2. Update an artist's information")
    print("3. Remove an artist from the database")

    print("4. Add a work of art to the database")
    print("5. Update a work's information")
    print("6. Remove a work of art from the database")

if __name__ == "__main__":
    main()
