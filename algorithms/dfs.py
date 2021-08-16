from collections import deque
from time import time

from consts import *
from .utils import helper, event_handler


@helper
def dfs(start_vertex, end_vertex, grid, window):
    """depth-first search"""
    start_time = time()
    stack, visited = deque(), {}
    stack.append(start_vertex)
    visited[start_vertex] = True
    path = {}
    
    while stack:
        event_handler(pg.event.get(), window)

        if window.paused:
            window.update(grid)
            continue

        current = stack.pop()

        if current not in (start_vertex, end_vertex):
            current.state = State.VISITING

        if current == end_vertex:
            break
                
        if visited.get(current) is None:
            visited[current] = True

        for neighbor in current.neighbors:
            if visited.get(neighbor) is None:
                stack.append(neighbor)
                path[neighbor] = current
        
        # update before setting the vertex as visited
        # or it won't be shown as visiting
        window.update(grid)

        if current != start_vertex:
            current.state = State.VISITED

    finish_time = round((time() - start_time), 2)
    cost = grid.draw_path(path, start_vertex, end_vertex, window)
    return finish_time, len(visited), cost
