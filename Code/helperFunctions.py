import pygame
from constants import *
from queue import PriorityQueue
import pygame as pg
from nodefile import Node

def showInstructions():
    # make a new screen
    screen = pygame.display.set_mode((900, 750))

    # show image on screen
    screen.blit(pygame.image.load("Code/Instructions_Screen.png"), (0, 0))

    # show the screen
    pygame.display.flip()

    # wait for the user to press a key
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            screen = pygame.display.set_mode((900, 750))
            screen.blit(pygame.image.load("Code/Start_Screen.png"), (0, 0))
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            break

def h(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

def MakeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def DrawGrid(MAIN_WINDOW, rows, width):
    gap = width // rows
    for i in range(rows):
        pg.draw.line(MAIN_WINDOW, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pg.draw.line(MAIN_WINDOW, WHITE, (j * gap, 0), (j * gap, width))

def Draw(MAIN_WINDOW, rows, grid, width):
    MAIN_WINDOW.fill(WHITE)
    for row in grid:
        for Node in row:
            Node.draw(MAIN_WINDOW)
    DrawGrid(MAIN_WINDOW, rows, width)
    pg.display.update()

def Mouse_coordinates(pos, rows, width):
    gap = width // rows
    y, x = pos
    return y // gap, x // gap

def CreatePath(parent, end, draw):
    while end in parent:
        end = parent[end]
        end.MakePath()
        draw()
    end.MakeStart()

def Astar_algorithm(draw, grid, start, end):
    count = 0
    parent = {}
    Open_Set = PriorityQueue()
    Open_Set.put((0, count, start))
    g_score = {val: float("inf") for row in grid for val in row}
    g_score[start] = 0
    f_score = {val: float("inf") for row in grid for val in row}
    f_score[start] = 0 + h(start.getPos(), end.getPos())

    Open_Set_check = {start}  # this is to check if a node is in the Priority Queue or not

    while not Open_Set.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.QUIT()

        # if esc is pressed
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            # run startscreen.py using system
            import os
            os.system('startscreen.py')

        current_node = Open_Set.get()[2]
        Open_Set_check.remove(current_node)

        if current_node == end:
            CreatePath(parent, end, draw)
            end.MakeEnd()
            return True

        for neighbor in current_node.neighbours:
            g_score_neighbor = g_score[current_node] + 1

            if g_score_neighbor < g_score[neighbor]:
                parent[neighbor] = current_node
                g_score[neighbor] = g_score_neighbor
                f_score[neighbor] = g_score_neighbor + h(neighbor.getPos(), end.getPos())

                if neighbor not in Open_Set_check:
                    count += 1
                    Open_Set.put((f_score[neighbor], count, neighbor))
                    Open_Set_check.add(neighbor)
                    neighbor.MakeOpen()
        draw()
        pg.time.delay(10)

        if current_node != start:
            current_node.MakeClosed()
    return False
