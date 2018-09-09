import tkinter

# print("---------------------------- 1 ----------------------------")
# # One example of a canvas.
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("Hello World")
# mainWindow.geometry("640x540+200+100")
#
# # Creating the labels to be put inside the window.
# label = tkinter.Label(mainWindow, text="Hello tiny world.")
# labelBottom = tkinter.Label(mainWindow, text="I'm down here!")
# labelRight = tkinter.Label(mainWindow, text="""右
# you4""")
# labelLeft = tkinter.Label(mainWindow, text="左\nzuo3")
#
# # Displaying the labels:
# label.pack(side="top")
# labelBottom.pack(side="bottom")
# labelLeft.pack(side="left")
# labelRight.pack(side="right")
#
# # Creating buttons
# button1 = tkinter.Button(mainWindow, text="Button1")
# button2 = tkinter.Button(mainWindow, text="Button2")
# button3 = tkinter.Button(mainWindow, text="Button3")
#
# # Displaying the buttons:
# button1.pack(side="top", anchor="w")
# button2.pack(side="top", anchor="center")
# button3.pack(side="top", anchor="e")
# # Values for "anchor= n, ne, e, se, s, sw, w, nw, or center"
# # The anchor value will only affect the element when obvious. An element with "side='top'" will not be affected by
# # "anchor='n,s'" since it is already placed in a vertical position.
#
#
# # Displaying the canvas:
# canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1) # "raised" makes the canvas have a z-index style;
# # Because the label was created before it, the canvas will move more to the right. The parameter "fill" will fill up
# # the y-axis if its value is "Y";
# # For expanding on the x-axis the value must be "X" but also pass another parameter called "expand=True";
# # If you want to expand in both directions use "BOTH";
# # You can also pass the " side='left/right' " parameter.
# canvas.pack(fill=tkinter.X, expand=True)
#
# mainWindow.mainloop()
#
print("---------------------------- 2 ----------------------------")
# A second way of using canvas.

mainWindow = tkinter.Tk()

# Creating window:
mainWindow.title("Hello World")
mainWindow.geometry("640x540+200+100")

# Labels:
labelX = tkinter.Label(mainWindow, text="世界你好")
labelX.pack(side="top")

# Frames for the canvas:
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=True)

# Buttons
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

mainWindow.mainloop()