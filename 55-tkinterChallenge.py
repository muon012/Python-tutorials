# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter as tk

mainWindow = tk.Tk()

mainWindow.title("ji4suan4qi4")
mainWindow.geometry("540x440-363-0")
padding = 10
mainWindow['padx'] = padding
mainWindow['pady'] = padding

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

# Frame for the buttons at the top;
functionBtnsFrame = tk.Frame(mainWindow)
functionBtnsFrame.grid(row=0, column=0, columnspan=4, sticky='nesw')

# Buttons at the top;
closeBtn = tk.Button(functionBtnsFrame, text='X', command=mainWindow.quit)
minBtn = tk.Button(functionBtnsFrame, text='-')
maxBtn = tk.Button(functionBtnsFrame, text='☐')
closeBtn.grid(row=0, column=0, sticky='e')
minBtn.grid(row=0, column=1, sticky="e")
maxBtn.grid(row=0, column=3, sticky="e")

# Label at the top;
label = tk.Label(functionBtnsFrame, text="计算器")
label.grid(row=0, column=4, sticky='e')


# Buttons to be displayed;
buttonList = [[("C", 0), ("CE", 1)],
			  [("7", 0), ("8", 1), ("9", 2), ("+", 3)],
			  [("4", 0), ("5", 1), ("6", 2), ("-", 3)],
			  [("1", 0), ("2", 1), ("3", 2), ("*", 3)],
			  [("0", 0), ("=", 1), ("/", 2)]
			  ]
# Display box;
result = tk.Entry(mainWindow)
result.grid(row=1, column=0, columnspan=3, sticky='nesw')

# Frame for the buttons.
keyPad = tk.Frame(mainWindow)
keyPad.grid(row=2, column=1, columnspan=2, sticky='nesw')

# Creating the buttons using a loop:
row = 0
for rows in buttonList:
	for key in rows:
		tk.Button(keyPad, text=key[0]).grid(row=row, column=key[1], columnspan=1, sticky="ew")
	row += 1

# After creating the buttons, we will update the size of the widgets;
mainWindow.update()
mainWindow.minsize(keyPad.winfo_width(), result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 100, result.winfo_height() + keyPad.winfo_height() + 50)

mainWindow.mainloop()