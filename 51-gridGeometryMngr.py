import tkinter
print("---------------------------- 1 ----------------------------")
# Using the grid manager

mainWindow = tkinter.Tk()

# Creating window:
mainWindow.title("Hello World")
mainWindow.geometry("640x540+200+100")

# Labels:
labelX = tkinter.Label(mainWindow, text="世界你好")
labelX.grid(row=0, column=0)

# Frames for the canvas:
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')
# The "sticky' property allows for a widget(element) to expand in that direction.
# It contains the same values as "anchor" and can also have multiple values.

# Buttons
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the columns:
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
# Make sure that the columns have the "weight" property otherwise the elements within it, won't be affected by it.

mainWindow.mainloop()