#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
import ipdb

def reset_database():
    Artist.drop_table()
    Artist.create_table()

ipdb.set_trace()
