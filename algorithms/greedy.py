from queue import PriorityQueue
from time import time

from consts import *
from .utils import event_handler, helper, heuristic


@helper
def greedy(start_vertex, end_vertex, grid, window):
    """greedy"""
    start_time = time()
    path = {}
    unvisited, visited = PriorityQueue(), {}
    position = 0

    start_vertex.f_score = heuristic(start_vertex, end_vertex)
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
        
        for neighbor in current.neighbors:
            # we only care about the current heuristic
            neighbor.f_score = heuristic(neighbor, end_vertex) + neighbor.weight
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
