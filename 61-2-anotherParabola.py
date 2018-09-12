import tkinter as tk


# Graph to be plotted;
def graph(page, exponent, size, color):
	for x in range(-size, size):
		y = x ** exponent / size
		plot(page, x, y, color)


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
def plot(quadrant, x, y, color):
	quadrant.create_line(x, -y, x + 1, -y + 1, fill=color) # Remember to change the y value to -y;


# Call the canvas function;
draw_axes(canvas)

# Call the function to draw the graph;
graph(canvas, 3, 100, "red")
graph(canvas, 2, 100, "green")
graph(canvas, 4, 10000, "black")

# We run the loop so we can display the window and everything inside it:
mainWindow.mainloop()