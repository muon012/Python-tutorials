import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x540-363-110") # Use these values on MacBook Air 11" (2015) for window centered on screen;

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# We create a list element;
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief="sunken")

# This code will fill up the list element we just created with the computer's operating system files;
for zone in os.listdir('/usr/bin'):
	fileList.insert(tkinter.END, zone)

# We create a scrolling bar in the y direction and link it to the list element.
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview())
listScroll.grid(row=1, column=1, sticky='nws', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# We create a frame for the radio buttons;
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

# Create a variable that will be shared among all three radio buttons;
# This way after selecting one button, the previous one will be deselected automatically;
# Passing a value through ".set()" will default "rbValue" to that value;
rbValue = tkinter.IntVar()
rbValue.set(3)

# Creating radio buttons and displaying them;
radioButton1 = tkinter.Radiobutton(optionFrame, text="File Name", value=1, variable=rbValue)
radioButton2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radioButton3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radioButton1.grid(row=0, column=0, sticky='w')
radioButton2.grid(row=1, column=0, sticky='w')
radioButton3.grid(row=2, column=0, sticky='w')

mainWindow.mainloop()
