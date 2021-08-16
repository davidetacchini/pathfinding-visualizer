from queue import PriorityQueue
from time import time

from consts import *
from .utils import event_handler, helper


@helper
def dijkstra(start_vertex, end_vertex, grid, window):
    """dijkstra"""
    start_time = time() 
    path = {}
    unvisited, visited = PriorityQueue(), {}
    position = 0
   
    start_vertex.f_score = 0
    unvisited.put((start_vertex.f_score, position, start_vertex))
    visited[start_vertex] = True

    while not unvisited.empty():
        window.update(grid)
        event_handler(pg.event.get(), window)

        if window.paused:
            continue

        current = unvisited.get()[2] # get vertex instance from the queue

        if current == end_vertex:
            break
        
        f_score = current.f_score + current.weight
        for neighbor in current.neighbors:
            if f_score < neighbor.f_score:
                neighbor.f_score = f_score + neighbor.weight
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
