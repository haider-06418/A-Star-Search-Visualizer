# visualization.py
from tkinter import Canvas, ALL
from config import *
from time import time 


current_time_millis = lambda: int(round(time() * 1000))


class Visualization(Canvas):
    """The canvas on which a visualization of the A* Algorithm is drawn on."""

    def __init__(self, master, node_map, **options):
        # Initialize canvas
        Canvas.__init__(self, master, **options) # Initialize parent class
        self.grid(row=0, column=0)

        self.last_update = current_time_millis() # FPS

        # Control variables
        self.x_offset, self.y_offset = 0, 0
        self.scale = 1

        self.node_map = node_map

        # Mouse events
        self.mouse_x_offset, self.mouse_y_offset = 0, 0
        self.bind("<Button-1>", self.mouse1_down)
        self.bind("<B1-Motion>", self.mouse1_drag)
        self.bind("<MouseWheel>", self.mouse_scroll) # Windows
        self.bind("<Button-4>", self.mouse_scroll) # Linux
        self.bind("<Button-5>", self.mouse_scroll) # Linux


    def mouse1_down(self, event):
        self.mouse_x_offset = self.x_offset - event.x
        self.mouse_y_offset = self.y_offset - event.y

    def mouse1_drag(self, event):
        self.x_offset = event.x + self.mouse_x_offset
        self.y_offset = event.y + self.mouse_y_offset

    def mouse_scroll(self, event):
        if event.num == 5 or event.delta == -120:
            self.scale /= ZOOM_RATE
        elif event.num == 4 or event.delta == 120:
            self.scale *= ZOOM_RATE
        print(self.scale)

    def tick(self):
        if current_time_millis() - self.last_update >= 1000/CANVAS_FPS:
            self.logic()
            self.draw()
            self.last_update = current_time_millis()

    def logic(self):
        pass

    def draw(self):
        self.delete(ALL) # Delete all objects from the previous draw loop
        self.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill=BACKGROUND_COLOR, width=0) # Clear the screen

        # Draw the nodes
        node_width = 50 * self.scale
        for y, row in enumerate(self.node_map):
            for x, node in enumerate(row):
                # Determine the color of the node
                color = NODE_DEFAULT
                if node is not None:
                    color = node[0]
                # Determine the position of the node
                x1, y1 = x * node_width + self.x_offset, y * node_width + self.y_offset
                x2, y2 = x1 + node_width, y1 + node_width
                # Draw the node
                self.create_rectangle(x1, y1, x2, y2, fill=color, outline='black', width=1)
                # Draw more info if zoomed enough
                if self.scale > ZOOM_TEXT_SHOW_MIN:
                    if node is not None and node[0] is not NODE_WALL and node[0] is not NODE_START and node[0] is not NODE_END:
                        self.create_text(x1+25, y1+20, text="F: " + str(node[1].f))
                        self.create_text(x2-25, y1+20, text="G: " + str(node[1].g))
                        self.create_text(x2-25, y2-20, text="H: " + str(node[1].h))