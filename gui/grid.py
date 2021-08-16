import pygame as pg

from consts import *
from .vertex import Vertex


class Grid:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.rows = 32
        self.cols = 32
        self.rect_size = self.width // self.cols
        self.grid = [[None for x in range(self.rows)] for y in range(self.cols)]
        
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y] = Vertex(x, y)
    
    def __call__(self):
        return self.grid

    def vertices(self):
        for x in range(self.rows):
            for y in range(self.cols):
                yield self.grid[x][y]

    def _draw(self, window): # draw grid lines
        for i in range(1, self.rows):
            pg.draw.line(window.screen, Color.BLACK, (i * self.rect_size, 0),
                         (i * self.rect_size, self.width))
            pg.draw.line(window.screen, Color.BLACK, (0, i * self.rect_size),
                         (self.height - 1, i * self.rect_size))

    def update(self, window):
        for vertex in self.vertices():
            vertex.draw(window, self)
            if vertex.weight == 5: # draw a 5 if it's weighted
                x = vertex.x * self.rect_size + 9
                y = vertex.y * self.rect_size + 2
                window.draw_text("5", x, y, color=Color.BLACK)
        self._draw(window)

    def reset(self):
        for vertex in self.vertices():
            vertex.reset()

    def clear(self):
        states = (State.VISITING, State.VISITED, State.PATH)
        for vertex in self.vertices():
            vertex.reset_scores() # must reset scores
            if vertex.state in states:
                vertex.clear()

    def get_vertex(self, pos):
        x, y = pos
        row = x // self.rect_size
        col = y // self.rect_size
        return self.grid[row][col]
    
    # path cost does not include start and end vertices
    def draw_path(self, path, start_vertex, end_vertex, window):
        end_vertex.state = State.END
        cost = 0

        current = end_vertex
        while current in path:
            if current not in (start_vertex, end_vertex):
                cost += current.weight
            current = path[current]
            current.state = State.PATH
            self.update(window)
            pg.display.update()

        start_vertex.state = State.START
        return cost if cost else "No solution"
