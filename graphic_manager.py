import tkinter as tk
import time
import numpy as np

class GraphicManager:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Sorting Visualizer")
        self.sorting_array = np.random.randint(1,100,10)

        self.c_width = 1000  # Define it's width
        self.c_height = 500  # Define it's height
        self. c = tk.Canvas(self.root, width=self.c_width, height=self.c_height, bg='white')
        self.c.pack()

        # The variables below size the bar graph
        self.y_stretch = 1  # The highest y = max_data_value * y_stretch
        self.y_gap = 20  # The gap between lower canvas edge and x axis
        self.x_stretch = 5  # Stretch x wide enough to fit the variables
        self.x_width = 10  # The width of the x-axis
        self.x_gap = 20  # The gap between left canvas edge and y axis

        self.root.mainloop()
        self.draw(self.sorting_array)

    def draw(self, data):
        for x, y in enumerate(data):
            # coordinates of each bar

            # Bottom left coordinate
            x0 = x * self.x_stretch + x * self.x_width + self.x_gap

            # Top left coordinates
            y0 = self.c_height - (y * self.y_stretch + self.y_gap)

            # Bottom right coordinates
            x1 = x * self.x_stretch + x * self.x_width + self.x_width + self.x_gap

            # Top right coordinates
            y1 = self.c_height - self.y_gap

            # Draw the bar
            self.c.create_rectangle(x0, y0, x1, y1, fill="red")

    def resize(self, size):
        self.sorting_array = np.random.randint(1,100,size)
