import math
import tkinter as tk


def circle(page,radius, h, k):
	for x in range(h, h + radius):
		y = k + (math.sqrt(radius ** 2 - ((x - h) ** 2)))
		plot(page, x, y) # Quadrant I
		plot(page, -x, y) # Quadrant II
		plot(page, -x, -y) # Quadrant III
		plot(page, x, -y) # Quadrant IV
		# Now we run a second loop but this time using x so that the graph has more points on it. So that the lines
		# are more "filled";
	for y in range(k, k + radius):
		x = h + (math.sqrt(radius ** 2 - ((y - k) ** 2)))
		plot(page, x, y) # Quadrant I
		plot(page, -x, y) # Quadrant II
		plot(page, -x, -y) # Quadrant III
		plot(page, x, -y) # Quadrant IV


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


# # You cannot create points with canvas, but you can create lines of length=1, which will serve as points;
# Function for plotting the lines;
def plot(quadrant, x, y):
	quadrant.create_line(x, -y, x + 1, -y + 1, fill="green") # Remember to change the y value to -y;


# Call the canvas function;
draw_axes(canvas)

# Calling the circle function;
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)


# Another way of creating circles using the "create_oval()" method. This is a "method()" because "Canvas" is a class,
# and all the functions of a class are called methods, not functions.
# On the function below, by passing a value to the parameter "color" we have established a default value if one is not
# given.
def circle_method(page, radius, h, k, color="red"):
	page.create_oval(h + radius, k + radius, h - radius, k - radius, outline=color, width=2)


# We call that new method;
circle_method(canvas, 20, 0, 0, "blue")
circle_method(canvas, 25, 0, 0)

# We run the loop so we can display the window and everything inside it:
mainWindow.mainloop()
