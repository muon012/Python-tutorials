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

# -------------------------- Continue with the gui below -----------------------------------------------

# Widget to display the results:
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24))) # This will count [0, 24);
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59) # This will count [0, 59];
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 30 # Adding some padding in the x-direction to the time spinners.

# Frame for the date spinners;
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date labels;
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date spinners;
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=1980, to=2099)
daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)

mainWindow.mainloop()

