# The grid for the scrollbars is the same as its parent box, it is not making the parent box the new grid;
# We comment the "artistScroll" and "albumScroll" out because we created a subclass "ScrollBox" that contains
# a modified "grid()" method that we created;
# Look at the method "insert()" to see how to add a data into the list box. You can add elements starting at the
# specified index;
# See also how we bind a function to a selected value from a list using the "bind()" method;
# When you bind an event to calling a function by writing the "()" at the end of the function, what you are doing
# is actually biding the return value of such function to the event. All functions that don't have a return value
# return "None". You should instead just write the function's name without the "()" at the end;


import sqlite3
import tkinter


class ScrollBox(tkinter.Listbox):

	def __init__(self, window, **kwargs):
		super().__init__(window, **kwargs)

		self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

	def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
		super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
		self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
		self["yscrollcommand"] = self.scrollbar.set


class DataListBox(ScrollBox):

	def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
		super().__init__(window, **kwargs)

		self.linked_box = None
		self.linked_field = None

		self.cursor = connection.cursor()
		self.table = table
		self.field = field

		self.bind("<<ListboxSelect>>", self.on_select)

		self.sql_select = "SELECT " + self.field + ", _id FROM " + self.table
		if sort_order:
			self.sql_sort = " ORDER BY " + ",".join(sort_order)
		else:
			self.sql_sort = " ORDER BY " + self.field

	def clear(self):
		self.delete(0, tkinter.END)

	def link(self, widget, link_field):
		self.linked_box = widget
		widget.linked_field = link_field

	def requery(self, link_value=None):
		self.link_value = link_value # Store the id so we know the "master" record we are populating from;
		if link_value and self.linked_field:
			sql = self.sql_select + " WHERE " + self.linked_field + "= ?" + self.sql_sort
			print(1, sql)
			self.cursor.execute(sql, (link_value,))
		else:
			print(2, self.sql_select + self.sql_sort)
			self.cursor.execute(self.sql_select + self.sql_sort)

		# Clear the listbox contents before reloading
		self.clear()
		for value in self.cursor:
			self.insert(tkinter.END, value[0])

		if self.linked_box:
			self.linked_box.clear()

	def on_select(self, event):
		if self.linked_box:
			index = self.curselection()[0]
			value = self.get(index),

			# Get the id from the database row;
			# Make sure we are getting the correct one by including the link_value if appropriate;
			if self.link_value:
				value = value[0], self.link_value
				sql_where = " WHERE " + self.field + " = ? AND " + self.linked_field + " = ?"
			else:
				sql_where = " WHERE " + self.field + " = ?"

			# We change "db" into "self.cursor" in case this method is used in other programs where "db" is already defined;
			link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
			self.linked_box.requery(link_id)
			print(3, self.curselection())


# # We change this code into a method instead of a function after we have DataListBox class;
# def get_albums(event):
# 	lb = event.widget
# 	index = lb.curselection()[0]
# 	artist_name = lb.get(index),
#
# 	# Get the artist ID from the database row
# 	artist_id = db.execute("SELECT _id FROM artists WHERE name = ?", artist_name).fetchone()
# 	aList = []
# 	for row in db.execute("SELECT name FROM albums WHERE artist = ? ORDER BY name", artist_id):
# 		aList.append(row[0])
# 	albumVariable.set(tuple(aList))


# # This code is no longer necessary after the creation of the "DataListBox" class;
# def get_songs(event):
# 	lb = event.widget
# 	index = int(lb.curselection()[0])
# 	album_name = lb.get(index),
#
# 	# Get the artist ID from the database row
# 	album_id = db.execute("SELECT _id FROM albums WHERE name = ?", album_name).fetchone()
# 	aList = []
# 	for row in db.execute("SELECT title FROM songs WHERE album = ? ORDER BY track", album_id):
# 		aList.append(row[0])
# 	songVariable.set(tuple(aList))

if __name__ == "__main__":
	db = sqlite3.connect("87-music.sqlite")

	mainWindow = tkinter.Tk()
	mainWindow.title("Music DB Browser")
	mainWindow.geometry("1024x768")

	mainWindow.columnconfigure(0, weight=2)
	mainWindow.columnconfigure(1, weight=2)
	mainWindow.columnconfigure(2, weight=2)
	mainWindow.columnconfigure(3, weight=1)

	mainWindow.rowconfigure(0, weight=1)
	mainWindow.rowconfigure(1, weight=5)
	mainWindow.rowconfigure(2, weight=5)
	mainWindow.rowconfigure(3, weight=1)

	# ------ Labels------
	tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
	tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
	tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

	# ------ Artists Box ------
	# We change artistList from "ScrollBox" to "DataListBox";
	artistsList = DataListBox(mainWindow, db, "artists", "name", background="yellow")
	artistsList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
	artistsList.config(border=2, relief="sunken")

	# This code for using the class "ScrollBox";
	# for artist in db.execute("SELECT name FROM artists ORDER BY name"):
	# 	artistsList.insert(tkinter.END, artist[0])

	artistsList.requery()

	# # We don't need this method anymore since we added methods to DataListBox class;
	# artistsList.bind("<<ListboxSelect>>", get_albums)

	# This code is for using no classes:
	# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistsList.yview)
	# artistScroll.grid(row=1, column=0, sticky="nse", rowspan=2)
	# artistsList["yscrollcommand"] = artistScroll.set

	# ------ Albums Box ------
	# We change albumList from "ScrollBox" to "DataListBox";
	albumVariable = tkinter.Variable(mainWindow)
	albumVariable.set(("Choose an artist",))
	albumsList = DataListBox(mainWindow, db, "albums", "name", ("name",), listvariable=albumVariable)
	albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
	albumsList.config(border=2, relief="sunken")

	# albumsList.requery() # This just populates the box with data for testing purposes;
	# albumsList.bind("<<ListboxSelect>>", get_songs)
	artistsList.link(albumsList, "artist")

	# This code is for using no classes:
	# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumsList.yview)
	# albumScroll.grid(row=1, column=1, sticky="nse", rowspan=1)
	# albumsList["yscrollcommand"] = albumScroll.set

	# ------ Song Box ------
	# We change songList from "ScrollBox" to "DataListBox";
	songVariable = tkinter.Variable(mainWindow)
	songVariable.set(("Choose an album",))
	songList = DataListBox(mainWindow, db, "songs", "title", ("track", "title"), listvariable=songVariable)
	songList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
	albumsList.config(border=2, relief="sunken")

	# songList.requery() # This just populates the box with data for testing purposes;
	albumsList.link(songList, "album")

	# ------ Mainloop ------
	mainWindow.mainloop()

	db.close()
