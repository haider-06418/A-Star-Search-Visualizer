import pygame as pg
from constants import *
from helperFunctions import *

MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")

def main_func(MAIN_WINDOW, width):
    ROWS = 50
    grid = GridCreation(ROWS, width)
    start = None
    end = None

    while True:
        Create(MAIN_WINDOW, ROWS, grid, width)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                import os
                os.system('startscreen.py')
                return

            if pg.mouse.get_pressed()[0]:
                mouse_pos = pg.mouse.get_pos()
                r, c = getMouseXY(mouse_pos, ROWS, width)
                cell = grid[r][c]
                if not start and cell != end:
                    start = cell
                    start.MakeStart()
                elif not end and cell != start:
                    end = cell
                    end.MakeEnd()
                elif cell != end and cell != start:
                    cell.MakeBarrier()

            elif pg.mouse.get_pressed()[2]:
                mouse_pos = pg.mouse.get_pos()
                r, c = getMouseXY(mouse_pos, ROWS, width)
                cell = grid[r][c]
                cell.reset()
                if cell == start:
                    start = None
                if cell == end:
                    end = None

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if start and end:
                        for i in range(ROWS):
                            for j in range(ROWS):
                                grid[i][j].UpdateNeighbours(grid)
                        a_star_algo(lambda: Create(MAIN_WINDOW, ROWS, grid, width), grid, start, end)
                if event.key == pg.K_r:
                    start = None
                    end = None
                    grid = GridCreation(ROWS, width)

main_func(MAIN_WINDOW, SCREEN_WIDTH)
if __name__ == '__main__':
    main_func(MAIN_WINDOW, SCREEN_WIDTH)