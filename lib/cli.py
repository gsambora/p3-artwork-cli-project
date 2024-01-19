# lib/cli.py

from helpers import (
    exit_program,
    list_artists,
    list_all_works
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
            pass
        elif choice == "3":
            list_movement()
        elif choice == "4":
            pass #list_nationality()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0.  Exit the program")
    print("1.  List all artists")
    print("2.  Find an artist") #Find artist menu
    print("3.  List artists by movement")
    print("4.  List artists by nationality")
    print("5.  List all works of art")
    print("6.  Find a work of art") #Find work menu
    print("7. List works by artist")
    print("8. List works by medium")
    print("9. List works in chronological order")
    print("10. Add, update, or remove database information") #Database menu


def find_artist_menu():
    print("1. Find artist by name")
    print("2. Find artist by ID")
    print("3. Find artist by work")

def find_work_menu():
    print("1. Find work by title")
    print("2. Find work by ID")

def database_menu():
    print("1. Add an artist to the database")
    print("2. Update an artist's information")
    print("3. Remove an artist from the database")

    print("4. Add a work of art to the database")
    print("5. Update a work's information")
    print("6. Remove a work of art from the database")

if __name__ == "__main__":
    main()
