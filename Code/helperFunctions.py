import pygame
from constants import *
from queue import PriorityQueue
import pygame as pg
import os
from nodefile import Node


def showInstructions():
    screen = pygame.display.set_mode((900, 750))
    screen.blit(pygame.image.load("Code/Instructions_Screen.png"), (0, 0))
    pygame.display.flip()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            screen = pygame.display.set_mode((900, 750))
            screen.blit(pygame.image.load("Code/Start_Screen.png"), (0, 0))
            pygame.display.flip()
            break

def nodes(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

def GridCreation(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def GridDrawing(MAIN_WINDOW, rows, width):
    gap = width // rows
    for i in range(rows):
        pg.draw.line(MAIN_WINDOW, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pg.draw.line(MAIN_WINDOW, GREY, (j * gap, 0), (j * gap, width))

def Create(MAIN_WINDOW, rows, grid, width):
    MAIN_WINDOW.fill(WHITE)
    for i in range(rows):
        for j in range(rows):
            grid[i][j].draw(MAIN_WINDOW)
    GridDrawing(MAIN_WINDOW, rows, width)
    pg.display.update()

def getMouseXY(pos, rows, width):
    gap = width // rows
    row = pos[0] // gap
    col = pos[1] // gap
    return row, col

def pathMaking(parent, end, draw):
    while end in parent:
        end = parent[end]
        end.MakePath()
        draw()
    end.MakeStart()

def a_star_algo(draw, grid, start, end):
    count = 0
    parent = {}
    collection_set = PriorityQueue()
    collection_set.put((0, count, start))
    goal_count = {val: float("inf") for row in grid for val in row}
    goal_count[start] = 0
    find_count = {val: float("inf") for row in grid for val in row}
    find_count[start] = 0 + nodes(start.getPos(), end.getPos())

    collec_set_check = {start}  

    while not collection_set.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.QUIT()
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            os.system('startscreen.py')

        current_node = collection_set.get()[2]
        collec_set_check.remove(current_node)

        if current_node == end:
            pathMaking(parent, end, draw)
            end.MakeEnd()
            return True

        for neighbor in current_node.neighbours:
            g_score_neighbor = goal_count[current_node] + 1

            if g_score_neighbor < goal_count[neighbor]:
                parent[neighbor] = current_node
                goal_count[neighbor] = g_score_neighbor
                find_count[neighbor] = g_score_neighbor + nodes(neighbor.getPos(), end.getPos())

                if neighbor not in collec_set_check:
                    count += 1
                    collection_set.put((find_count[neighbor], count, neighbor))
                    collec_set_check.add(neighbor)
                    neighbor.MakeOpen()
        draw()
        pg.time.delay(10)

        if current_node != start:
            current_node.MakeClosed()
    return False