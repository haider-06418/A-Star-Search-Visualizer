import pygame as pg
import pygame
from constants import *
from helperFunctions import *




class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLACK
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows

    def getPos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == TURQUOISE

    def isOpen(self):
        return self.color == BLUE

    def isObstacle(self):
        return self.color == WHITE

    def isStart(self):
        return self.color == GREEN

    def isEnd(self):
        return self.color == ORANGE

    def reset(self):
        self.color = WHITE

    def MakeStart(self):
        self.color = RED

    def MakeClosed(self):
        self.color = TURQUOISE

    def MakeOpen(self):
        self.color = BLUE

    def MakeBarrier(self):
        self.color = WHITE

    def MakeEnd(self):
        self.color = YELLOW

    def MakePath(self):
        self.color = GREEN

    def draw(self, MAIN_WINDOW):
        pg.draw.rect(MAIN_WINDOW, self.color, (self.x, self.y, self.width, self.width))

    def UpdateNeighbours(self, grid):
        self.neighbours = []
        if self.row + 1 < self.totalRows and not grid[self.row + 1][self.col].isObstacle():  # DOWN
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isObstacle():  # UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col + 1 < self.totalRows and not grid[self.row][self.col + 1].isObstacle():  # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].isObstacle():  # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

