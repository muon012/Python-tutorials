
import sqlite3
import tkinter

db = sqlite3.connect("87-music.sqlite")

for row in db.execute("SELECT * FROM artists"):
	print(row)

db.close()
