# We will now start using a simple GUI included in python called TKinter.
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test() # This will pop up the TKinter GUI.

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x540+50+50") # Numbers meaning: (width x height + offset from the left + offset from the top)
mainWindow.mainloop()
