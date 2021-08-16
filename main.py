import pygame as pg

from algorithms import astar, dijkstra, bfs, dfs, greedy, prim
from consts import *
from gui import Grid, Window

def main():
    window = Window()
    grid = Grid()
    start_vertex = None
    end_vertex = None

    running = True
    while running:
        window.update(grid)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if event.button == 3: # right click
                    try:
                        vertex = grid.get_vertex(pos)
                    except IndexError:
                        continue
                    if vertex.is_empty(): # set start or end vertex
                        if not start_vertex:
                            vertex.state = State.START
                            start_vertex = vertex
                        elif not end_vertex:
                            vertex.state = State.END
                            end_vertex = vertex
                    elif vertex == start_vertex: # remove start vertex
                        vertex.state = State.EMPTY
                        start_vertex = None
                    elif vertex == end_vertex: # remove end vertex
                        vertex.state = State.EMPTY
                        end_vertex = None
                if start_vertex and end_vertex:
                    if window.buttons["dijkstra"].is_clicked(pos, event):
                        dijkstra(start_vertex, end_vertex, grid, window)
                    elif window.buttons["bfs"].is_clicked(pos, event):
                        bfs(start_vertex, end_vertex, grid, window)
                    elif window.buttons["dfs"].is_clicked(pos, event):
                        dfs(start_vertex, end_vertex, grid, window)
                    elif window.buttons["astar"].is_clicked(pos, event):
                        astar(start_vertex, end_vertex, grid, window)
                    elif window.buttons["greedy"].is_clicked(pos, event):
                        greedy(start_vertex, end_vertex, grid, window)
                if window.buttons["clear"].is_clicked(pos, event):
                    grid.clear()
                elif window.buttons["reset"].is_clicked(pos, event):
                    start_vertex = end_vertex = None
                    grid.reset()
                elif window.buttons["prim"].is_clicked(pos, event):
                    start_vertex = end_vertex = None
                    prim(grid, window)
                elif window.buttons["fps"].is_clicked(pos, event):
                    if window.fps == 60:
                        window.fps = 90
                    elif window.fps == 90:
                        window.fps = 120
                    else:
                        window.fps = 60
            elif event.type == pg.MOUSEMOTION: # mouse buttons pressed
                try:
                    vertex = grid.get_vertex(pg.mouse.get_pos())
                except IndexError:
                    continue
                if event.buttons[0] and vertex.is_empty():
                    keys = pg.key.get_pressed()
                    if keys[pg.K_w]: # if 'w' is pressed along with the left mouse button, add weight
                        vertex.weight = 5
                    elif vertex.weight == 1: # add wall vertex is not weighted
                        vertex.state = State.WALL
                elif event.buttons[2]:
                    if vertex.state is State.WALL: # remove wall
                        vertex.state = State.EMPTY
                    elif vertex.weight == 5:
                        vertex.weight = 1

    pg.quit()


if __name__ == "__main__":
    main()
