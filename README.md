# Phase 3 Artwork CLI Project

## Introduction

This is my project for Phase 3 at Flatiron School. I made a command-line-interface (CLI) application so a user can manage information about artists and their work. The data for artists and works are stored in two tables using SQL. 

There are two data models: artists and works. Each artist can have many works, and a work can only be attached to one artist. Artists must have a name, nationality, and movement (such as Impressionism or Surrealism). Works must have a title, year of creation, medium (such as Oil on canvas or Woodblock print), and an artist's ID. Works can only be created if their artist is already in the database.  

## Installation
To run this project, follow these steps:
* Make sure that Python and SQL are installed on your PC.
* Fork and clone this repository.
* Navigate to the project directory.
* Install the required dependencies.
    pip install
* If you would like to start with an empty database, run this command:
    python lib/reset.py
* If you would like some starting data in your database, run this command:
    python lib/seed.py
* Once your database is initialized, run the CLI application with this command:
    python lib/cli.py

## File Descriptions
* lib/cli.py contains most of the menus for navigating the application, and calls each helper function depending on which number the user types.
* lib/helpers.py is where the user input actually affects the artist and work objects, as well as the database. Some helper functions contain a mini-menu for the CLI in order to direct the user to another helper function. For example, if the user searches for an artist who is not yet in the database, the helper function will check if they want to add that artist to the database. If so, the helper function will call the add_artist function. 
* lib/reset.py deletes both the Artist and Work tables and creates new ones with no data. 
* lib.seed.py deletes and recreates both the Artist and Work tables and enters some starting data.
* The models folder contains both the artist and work models, which each have all ORM methods. The only nonstandard method is the artist delete method, which will delete all of the works attached to that artist before deleting the artist object.