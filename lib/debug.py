#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
import ipdb

def reset_database():
    Artist.drop_table()
    Artist.create_table()

    Artist.create("Van Gogh", "Dutch", "Post-Impressionism")
    Artist.create("Claude Monet", "French", "Impressionism")
    Artist.create("Katsushika Hokusai", "Japanese", "Ukiyo-e")\

reset_database()
ipdb.set_trace()
