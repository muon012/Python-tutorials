# This is much better way to show the local time using sqlite;
# We saved this code into file# 84 as a view;

import sqlite3

db = sqlite3.connect("84-accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT strftime('%Y-%m-%d, %H:%M:%f', history.time, 'localtime') AS localtime,"
					  " history.account, history.amount FROM history ORDER BY history.time"):
	print(row)

db.close()