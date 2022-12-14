import pygame as pg
import queue
from queue import PriorityQueue

# Setting up Visualizer window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")

# Colors to be used in project
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows

    def getPos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == RED

    def isOpen(self):
        return self.color == BLUE

    def isObstacle(self):
        return self.color == BLACK

    def isStart(self):
        return self.color == GREEN

    def isEnd(self):
        return self.color == ORANGE

    def reset(self):
        self.color = WHITE

    def MakeStart(self):
        self.color = GREEN

    def MakeClosed(self):
        self.color = RED

    def MakeOpen(self):
        self.color = BLUE

    def MakeBarrier(self):
        self.color = BLACK

    def MakeEnd(self):
        self.color = ORANGE

    def MakePath(self):
        self.color = PURPLE

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
        pg.draw.line(MAIN_WINDOW, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pg.draw.line(MAIN_WINDOW, BLACK, (j * gap, 0), (j * gap, width))


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


# # Optional implementation by bfs
# def bfs(draw, grid, start, end):
#     q = queue.Queue()
#     parent = {}
#     q.put(start)
#     done = {start}

#     while not q.empty():
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()

#         current = q.get()

#         if current == end:
#             CreatePath(parent, end, draw)
#             end.MakeEnd()
#             return True

#         for neighbour in current.neighbours:
#             if neighbour not in done:
#                 done.add(neighbour)
#                 parent[neighbour] = current
#                 q.put(neighbour)
#         draw()

#         if current != start:
#             current.MakeClosed()
#     return False


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

                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = MakeGrid(ROWS, width)
    pg.quit()


main1(MAIN_WINDOW, SCREEN_WIDTH)
