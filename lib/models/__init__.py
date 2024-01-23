import sqlite3

CONN = sqlite3.connect('artwork.db')
CURSOR = CONN.cursor()
