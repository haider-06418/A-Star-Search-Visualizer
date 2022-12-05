# astar.py
from config import *


get_distance_to_end = lambda node, end: abs(end[0] - node.x) + abs(end[1] - node.y)

class AStar:
    """The A* search Algorithm."""

    # Level map node constants
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3

    def __init__(self, level_map):
        self.level_map = level_map
        # Find the start/end nodes
        self.start, self.end = self.read_level_map(self.level_map)

        print("Start node found:", self.start)
        print("End node found:", self.end)

        # Initialize start node
        self.start_node = Node(self.start[0], self.start[1])
        self.start_node.g = 0
        self.start_node.h = get_distance_to_end(self.start_node, self.end)

        # Initialize the open/closed lists
        self.open = self.get_nodes_around(self.start_node)
        self.closed = [self.start_node]

        # Initialize the result variables
        self.end_path = None

    def read_level_map(self, level_map):
        """Reads a 2D list and returns the start and end nodes.
           Raises an error if there are no start or end nodes."""
        start = None
        end = None
        
        # Find the start/end nodes
        for y, row in enumerate(level_map):
            for x, node in enumerate(row):
                if node == self.START:
                    if start is None:
                        start = (x, y)
                    else:
                        raise InvalidStartError("There are multiple start nodes on the map.")
                elif node == self.END:
                    if end is None:
                        end = (x, y)
                    else:
                        raise InvalidEndError("There are multiple end nodes on the map.")
        
        # Check if there any start/end nodes were found.
        if start is None:
            raise InvalidStartError("There is no start node on the map.")
        if end is None:
            raise InvalidEndError("There is no end node on the map.")

        return start, end

    def advance(self):
        """Advances the search."""
        # Check if there is an open node
        if len(self.open) == 0:
            print("No path available")
            return "NO_PATH"
        # Check fi already solved
        if self.end_path is not None:
            print("End path found")
            return "SOLVED"
        # Get the node on the open list which has the lowest score (S).
        S = self.open[0]
        for node in self.open:
            if node.f < S.f:
                S = node
        # Remove S from the open list and add it to the closed list
        self.open.remove(S)
        self.closed.append(S)
        # For each node T in S's walkable adjacent tiles:
        for T in self.get_nodes_around(S):
            g, h = self.calculate_score(T)
            T.update_score(g, h)
            # - If T is in the closed list: 
            #       Ignore it.
            in_closed = False
            for node in self.closed:
                if node.pos() == T.pos():
                    in_closed = True
            if in_closed: continue
            
            T_old = None
            for node in self.open:
                if node.pos() == T.pos():
                    T_old = node
            # - If T is not in the open list: 
            #       Add it and compute its score.
            if T_old is None:
                self.open.append(T)
            # - If T is already in the open list: 
            #       Check if the F score is lower when we use the 
            #       current generated path to get there. 
            #       If it is, update its score and update its parent as well.
            else:
                if T.f < T_old.f:
                    self.open.remove(T_old)
                    self.open.append(T.f)
            # - If T is the end node:
            if T.pos() == self.end:
                self.end_path = T
                return "SOLVED"
        return "SOLVING"

    def get_nodes_around(self, node):
        """Returns a list of coordinates around (up, down, left, right) a node."""
        x, y = node.x, node.y
        coords = []

        # Up
        if y-1 >= 0 and self.level_map[y-1][x] is not self.WALL:
            coords.append(Node(x, y-1, node))
        # Down
        if y+1 < len(self.level_map) and self.level_map[y+1][x] is not self.WALL:
            coords.append(Node(x, y+1, node))
        # Left
        if x-1 >= 0 and self.level_map[y][x-1] is not self.WALL:
            coords.append(Node(x-1, y, node))
        # Right
        if x+1 < len(self.level_map[y]) and self.level_map[y][x+1] is not self.WALL:
            coords.append(Node(x+1, y, node))

        return coords

    def calculate_score(self, node):
        """Calculates and returns G, H for a node."""
        # Calculate G: the movement cost from the start node to the current node
        g = node.parent.g + 1

        # Calculate H: the estimated movement cost from the current node to the end node
        # Manhattan distance method: # of horizontal + # of vertical squares to reach the end
        h = get_distance_to_end(node, self.end)

        return g, h

    def get_final_path(self):
        """Returns an ordered list of Nodes leading from the start to the end."""
        if self.end_path is not None:
            node = self.end_path
            path = [self.end_path]
            
            while node.parent is not None:
                path = [node.parent] + path
                node = node.parent
            
            return path

    def get_node_map(self):
        """Returns a 2D list of Nodes representing the map."""
        node_map = self.gen_empty_map()
        
        for y, row in enumerate(node_map):
            for x, point in enumerate(row):
                if self.level_map[y][x] == self.WALL:
                    node_map[y][x] = (NODE_WALL,)
                elif self.level_map[y][x] == self.START:
                    node_map[y][x] = (NODE_START,)
                elif self.level_map[y][x] == self.END:
                    node_map[y][x] = (NODE_END,)
                else:
                    # If in the open list
                    for node in self.open:
                        if node.pos() == (x, y):
                            node_map[y][x] = (NODE_OPEN, node)

                    # If in the closed list
                    for node in self.closed:
                        if node.pos() == (x, y):
                            node_map[y][x] = (NODE_CLOSED, node)
                        
        return node_map

    def get_node_map_path(self):
        """Returns a 2D list of Nodes with the path."""
        node_map = self.gen_empty_map()
        path = self.get_final_path()

        for y, row in enumerate(node_map):
            for x, point in enumerate(row):
                if self.level_map[y][x] == self.WALL:
                    node_map[y][x] = (NODE_WALL,)
                elif self.level_map[y][x] == self.START:
                    node_map[y][x] = (NODE_START,)
                elif self.level_map[y][x] == self.END:
                    node_map[y][x] = (NODE_END,)
                else:
                    for node in path:
                        if node.pos() == (x, y):
                            node_map[y][x] = (NODE_PATH, node)

        return node_map

    def gen_empty_map(self):
        node_map = []
        # Create empty 2D list with the same size as level_map
        for y, row in enumerate(self.level_map):
            node_map.append([])
            for x, point in enumerate(row):
                node_map[y].append(None)
        return node_map

    @staticmethod
    def load_level_map_from_file(path):
        level_map = []

        with open(path) as file:
            for i, line in enumerate(file):
                level_map.append([])
                for point in line.split(" "):
                    level_map[i].append(int(point))

        return level_map


class Node:
    """A node on the map"""

    def __init__(self, x, y, parent=None):
        self.x, self.y = x, y
        self.f, self.g, self.h = 0, 0, 0
        self.parent = parent

    def update_score(self, g, h):
        self.f, self.g, self.h = g+h, g, h

    def pos(self):
        return (self.x, self.y)

    def __str__(self):
        return "Node(" + str(self.x) + ", " + str(self.y) + "): F=" + str(self.f) + " G=" + str(self.g) + " H=" + str(self.h)


class InvalidStartError(Exception):
    pass

class InvalidEndError(Exception):
    pass