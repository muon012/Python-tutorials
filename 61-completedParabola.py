
import tkinter as tk


# Definition of a parabola;
def parabola(page, size):
	for x in range(-size, size):
		y = x ** 2 / size
		plot(page, x, y)


# Creating a window;
mainWindow = tk.Tk()
mainWindow.title("数学:Parabola")
mainWindow.geometry("500x400-363-110")

# Creating a canvas;
canvas = tk.Canvas(mainWindow, width=500, height=400)
canvas.grid(row=0, column=0)


# Drawing the x and y axis;
def draw_axes(page):
	page.update() # We need to call this function to be able to access the width and height of a window/canvas/widget.
	x_origin = page.winfo_width() / 2
	y_origin = page.winfo_height() / 2
	page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin)) # This is a box of the given dimensions.
	page.create_line(-x_origin, 0, x_origin, 0, fill="blue") # Creating the x-axis;
	page.create_line(0, y_origin, 0, -y_origin, fill="blue") # Creating the y-axis;


# You cannot create points with canvas, but you can create lines of length=1, which will serve as points;
# Function for plotting the lines;
def plot(quadrant, x, y):
	quadrant.create_line(x, -y, x + 1, -y + 1, fill="red") # Remember to change the y value to -y;


# Call the canvas function;
draw_axes(canvas)

# Call the function to draw the graph;
parabola(canvas, 500)
parabola(canvas, 100)

# We run the loop so we can display the window and everything inside it:
mainWindow.mainloop()

# See line 35, use y instead of -y on the second parameter for a cool effect similar to finding the integral
# of the parabola.