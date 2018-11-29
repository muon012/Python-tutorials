# Create a program that ask the user for a name and then retrieve that name's row from the database
# In python, specifying a tuple that has one value is doing so by writing a comma afterwards the first value
# i.e. "(value1,)";

import sqlite3

db = sqlite3.connect("78-contacts.sqlite")

name_search = input("Whose record are you looking for?: ")

search_command = "SELECT * FROM contacts WHERE name LIKE ?"
for row in db.execute(search_command, (name_search,)):
	print(row)

db.close()