from queue import PriorityQueue
from time import time

from consts import *
from .utils import event_handler, helper, heuristic


@helper
def astar(start_vertex, end_vertex, grid, window):
    """A*"""
    start_time = time()
    path = {}
    unvisited, visited = PriorityQueue(), {}
    position = 0

    start_vertex.g_score = 0 # distance from start vertex
    start_vertex.h_score = heuristic(start_vertex, end_vertex) # distance from end vertex (heuristic)
    start_vertex.f_score = start_vertex.g_score + start_vertex.h_score # sum of g_score + h_score
    unvisited.put((start_vertex.f_score, position, start_vertex))
    visited[start_vertex] = True

    while not unvisited.empty():
        window.update(grid)
        event_handler(pg.event.get(), window)

        if window.paused:
            continue

        current = unvisited.get()[2]

        if current == end_vertex:
            break
        
        g_score = current.g_score + current.weight
        for neighbor in current.neighbors:
            if g_score < neighbor.g_score:
                neighbor.g_score = g_score
                neighbor.f_score = g_score + heuristic(neighbor, end_vertex) + neighbor.weight
                if visited.get(neighbor) is None:
                    path[neighbor] = current
                    visited[neighbor] = True
                    neighbor.state = State.VISITING
                    position += 1
                    unvisited.put((neighbor.f_score, position, neighbor))

        if current != start_vertex:
            current.state = State.VISITED

    finish_time = round((time() - start_time), 2) 
    cost = grid.draw_path(path, start_vertex, end_vertex, window)
    return finish_time, len(visited), cost
