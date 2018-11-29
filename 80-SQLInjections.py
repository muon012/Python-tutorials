# Parameter substitution: Using variables or replacements fields to substitute the value later;
# Placeholders: In SQL, the placeholders are the "?" inside the SQL statements;
# Never use parameters from external functions or user input in sql queries, use placeholders instead;
# When calling the cursor's method "execute()" make sure you pass the SQL query, as the 1st parameter and then a
# tuple containing the variables that will substitute the placeholders;
# Use a "?" when you want a value to be inserted and provides the values as a tuple when you call the execute() method
# on a cursor or connection;
# The method "executescript()" from cursor() is used to run multiple sql statements separated by a ";" executed
# one after the other;

import sqlite3

db = sqlite3.connect("78-contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} row(s) updated".format(update_cursor.rowcount))

print("\nAre connections the same: {}\n".format(update_cursor.connection == db))

update_cursor.connection.commit()
update_cursor.close()

# The update has been committed and can now be seeing when accesing the database from any file, not just this one;
for name, phone, email in db.execute("SELECT * FROM contacts"):
	print(name)
	print(phone)
	print(email)
	print("=" * 20)

db.close()
