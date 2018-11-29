# Database Terminology
# Database: The container for all the data that you store;
# Table: A collection of related data held in a database;
# Column/Field: Basic unit of data in a a table;
# Row/Record: A single set of data containing all the columns in a table;
# 
# An example of a double join using the music.db:
# SELECT artists.name, albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id ORDER BY artists.name, albums.name, songs.track;

# The cursor down there is a "generator." It can be used in a for loop but it doesn't keep track of the previous rows
# it read, so if you try to do a second for loop it will be empty because the cursor has stopped at the last
# row already. Cursors don't store data in the memory;

# If you don't use "commit()" the data will not be saved in the database. It is best to commit after you are happy
# with the changes, not necessarily just before the "close()" function. The best time to commit though,
# could be before close(), it will depend on what you're trying to do;

import sqlite3

db = sqlite3.connect("78-contacts.sqlite")
db.execute("create table if not exists contacts (name text, phone integer, email text)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# # This creates a list of each row as tuple, but can't iterate again with cursor;
# cursor_list = cursor.fetchall()

# # You can also print one row at a time;
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

for row in cursor:
	print(row)
cursor.close()
db.commit()
db.close()
