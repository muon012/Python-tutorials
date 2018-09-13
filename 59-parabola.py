
import tkinter as tk
import random

random.randint(2)

# Definition of a parabola;
def parabola(x):
	y = x ** 2 / 100
	return y

for x in range(-50, 51):
	print(parabola(x))

# Creating a window;
mainWindow = tk.Tk()
mainWindow.title("数学:Parabola")
mainWindow.geometry("500x400-363-110")

# Creating a canvas;
canvas = tk.Canvas(mainWindow, width=500, height=400)
canvas.grid(row=0, column=0)


# Drawing the x and y axis;
def draw_axes(canvas):
	canvas.update() # We need to call this function to be able to access the width and height of a window/canvas/widget.
	x_origin = canvas.winfo_width() / 2
	y_origin = canvas.winfo_height() / 2
	canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin)) # This is a box of the given dimensions.
	canvas.create_line(-x_origin, 0, x_origin, 0, fill="blue") # Creating the x-axis;
	canvas.create_line(0, y_origin, 0, -y_origin, fill="blue") # Creating the y-axis;


# You cannot create points with canvas, but you can create lines of length=1, which will serve as points;
# Function for plotting the lines;
def plot(canvas, x, y):
	canvas.create_line(x, y, x + 1, y + 1, fill="red")

# Call the canvas function;
draw_axes(canvas)

# Calling the function to plot the lines;
for x in range(-500, 500):
	y = parabola(x)
	plot(canvas, x, -y) # You shouldn't use "y" because in canvas, increasing values of y go downward.

# We run the loop so we can display the window:
mainWindow.mainloop()

# SCOPE IN FUNCTIONS
# In line 23, the function "draw_axes" uses a parameter named "canvas" but this name is also the name of a global
# variable,a variable outside the function and available to ALL the program in this code.
# Therefore, if you try to use "canvas", the global variable, inside this function, you won't be able to.
# The function NOW only recognizes "canvas" as a parameter and not as a variable to the program. 