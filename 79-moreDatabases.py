# Cursors, transactions, connections;
# It is best to use cursors when making an update and then committing that cursors as opposed to committing the whole
# database;
# It is best not to type ";" at the end of each sql query in python;

import sqlite3

db = sqlite3.connect("78-contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE name = 'Brian'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} row(s) updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

# The update has been committed and can now be seeing when accesing the database from any file, not just this one;
for name, phone, email in db.execute("SELECT * FROM contacts"):
	print(name)
	print(phone)
	print(email)
	print("=" * 20)

db.close()
