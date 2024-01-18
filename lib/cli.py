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
            list_all_works()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all artists")
    print("2. List all works of art")


if __name__ == "__main__":
    main()
