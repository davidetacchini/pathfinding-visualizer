from consts import *


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = State.EMPTY
        self.weight = 1
        self.g_score = float("inf") # for A*
        self.h_score = float("inf") # for both A* and greedy
        self.f_score = float("inf") # distance from start_vertex
        self.neighbors = []

    def draw(self, window, grid):
        color = COLOR_LOOKUP.get(self.state)
        x, y = self.x * grid.rect_size, self.y * grid.rect_size
        pg.draw.rect(window.screen, color, (x, y, grid.rect_size, grid.rect_size))

    def is_empty(self):
        return self.state is State.EMPTY

    def reset(self):
        self.state = State.EMPTY
        self.weight = 1
        self.reset_scores()
    
    def clear(self):
        self.state = State.EMPTY

    def reset_scores(self):
        self.g_score = self.h_score = self.f_score = float("inf")

    def add_neighbors(self, grid):
        self.neighbors.clear() # make sure we recompute neighbors every time
        vertices, rows, cols = grid(), grid.rows, grid.cols
        if self.y > 0 and not vertices[self.x][self.y - 1].state is State.WALL: # up
            self.neighbors.append(vertices[self.x][self.y - 1])
        if self.x < rows - 1 and not vertices[self.x + 1][self.y].state is State.WALL: # right
            self.neighbors.append(vertices[self.x + 1][self.y])
        if self.y < cols - 1 and not vertices[self.x][self.y + 1].state is State.WALL: # down
            self.neighbors.append(vertices[self.x][self.y + 1])
        if self.x > 0 and not vertices[self.x - 1][self.y].state is State.WALL: # left
            self.neighbors.append(vertices[self.x - 1][self.y])
