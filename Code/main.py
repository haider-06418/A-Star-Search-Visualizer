import pygame as pg
from queue import PriorityQueue
from constants import *
from helperFunctions import *
from nodefile import Node


# Setting up Visualizer window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")



def main1(MAIN_WINDOW, width):
    ROWS = 50
    grid = MakeGrid(ROWS, width)

    start = None
    end = None

    run_algo = True
    done = 0

    while run_algo:
        Draw(MAIN_WINDOW, ROWS, grid, width)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_algo = False
                import os
                os.system('startscreen.py')

            if pg.mouse.get_pressed()[0]:
                mouse_pos = pg.mouse.get_pos()
                r, c = Mouse_coordinates(mouse_pos, ROWS, width)
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
                r, c = Mouse_coordinates(mouse_pos, ROWS, width)
                cell = grid[r][c]
                cell.reset()
                if cell == start:
                    start = None
                if cell == end:
                    end = None

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if start and end:
                        for row in grid:
                            for Node in row:
                                Node.UpdateNeighbours(grid)
                        Astar_algorithm(lambda: Draw(MAIN_WINDOW, ROWS, grid, width), grid, start, end)
                    # bfs(lambda: Draw(MAIN_WINDOW, ROWS, grid, width), grid, start, end)
                if event.key == pg.K_r:
                    start = None
                    end = None
                    grid = MakeGrid(ROWS, width)
    pg.quit()

main1(MAIN_WINDOW, SCREEN_WIDTH)
if __name__ == '__main__':
    main1(MAIN_WINDOW, SCREEN_WIDTH)