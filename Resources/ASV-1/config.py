# config.py
# Stores program-wide configurations


# Window
SIZE = WIDTH, HEIGHT = 1280, 720


# Canvas
CANVAS_SIZE = CANVAS_WIDTH, CANVAS_HEIGHT = WIDTH*4/5, HEIGHT
CANVAS_FPS = 60

BACKGROUND_COLOR = "white"

ZOOM_RATE = 1.1
ZOOM_TEXT_SHOW_MIN = 1.7 # Minimum zoom level at which more info is shown


# Node colors
NODE_DEFAULT = "#cccccc"
NODE_WALL = "#282828"
NODE_START = "#333355"
NODE_END = "#543232"
NODE_CLOSED = "#d33f3f"
NODE_OPEN = "#3ed243"
NODE_PATH = "#c0d13d"


# Algorithm
MAPS_DIR = "maps/"