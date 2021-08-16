from collections import deque
from time import time

from consts import *
from .utils import event_handler, helper


@helper
def bfs(start_vertex, end_vertex, grid, window):
    """breadth-first search"""
    start_time = time() 
    queue, visited = deque(), {}
    queue.append(start_vertex)
    visited[start_vertex] = True
    path = {}

    while queue:
        window.update(grid)
        event_handler(pg.event.get(), window)

        if window.paused:
            continue

        current = queue.popleft()

        if current == end_vertex:
            break

        for neighbor in current.neighbors:
            if visited.get(neighbor) is None:
                visited[neighbor] = True
                queue.append(neighbor)
                path[neighbor] = current
                neighbor.state = State.VISITING

        if current != start_vertex:
            current.state = State.VISITED

    finish_time = round((time() - start_time), 2)
    cost = grid.draw_path(path, start_vertex, end_vertex, window)
    return finish_time, len(visited), cost
