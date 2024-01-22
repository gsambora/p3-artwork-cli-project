#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.work import Work

def reset_database():
    Artist.drop_table()
    Work.drop_table()
    Artist.create_table()
    Work.create_table()

def make_sample_data():
    Artist.create("Van Gogh", "Dutch", "Post-Impressionism")
    Artist.create("Claude Monet", "French", "Impressionism")
    Artist.create("Katsushika Hokusai", "Japanese", "Ukiyo-e")
    Artist.create("Frida Kahlo", "Mexican", "Surrealism")

    Work.create("Starry Night", 1889, "Oil on canvas", 1)
    Work.create("Skull of a Skeleton with Burning Cigarette", 1885, "Oil on canvas", 1)
    Work.create("The Broken Column", 1944, "Oil on masonite", 4)
    Work.create("The Two Fridas", 1939, "Oil on canvas", 4)

    Work.create("The Great Wave off Kanagawa", 1831, "Woodblock print", 3)


#reset_database()
breakpoint()
