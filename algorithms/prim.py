from random import randint

from consts import *
from .utils import event_handler


# using prim's algorithm
def prim(grid, window):
    window.executing = True
    window.fps = 0 # max fps
    grid.reset()
    for vertex in grid.vertices(): # set vertices neighbors
        vertex.add_neighbors(grid)
    
    # subtract 3 because rows and cols are set to 32. We need to
    # get all the vertices less than 30 or we'll get IndexError
    # when trying to check for the neighbors. Then 32 - 3 = 29
    x, y = randint(2, grid.rows - 3), randint(2, grid.cols - 3)

    # set random vertex as visiting
    grid()[x][y].state = State.VISITING

    walls = []

    # set random vertex's neighbors as walls
    for neighbor in grid()[x][y].neighbors:
        neighbor.state = State.WALL
        walls.append((neighbor.x, neighbor.y))

    while walls:
        window.update(grid)
        event_handler(pg.event.get(), window, switch_fps=False)

        if window.paused:
            continue
        
        # pop random wall from walls
        x_, y_ = walls.pop(randint(1, len(walls)) - 1)
        current = grid()[x_][y_]
        # bind each neighbor
        top = current.neighbors[0]
        right = current.neighbors[1]
        bottom = current.neighbors[2]
        left = current.neighbors[3]
        n = visiting_neighbors(current)

        if left.is_empty() and right.state is State.VISITING and n < 2:
            current.state = State.VISITING
            set_walls(current, grid, walls, right)

        if top.is_empty() and bottom.state is State.VISITING and n < 2:
            current.state = State.VISITING
            set_walls(current, grid, walls, bottom)

        if right.is_empty() and left.state is State.VISITING and n < 2:
            current.state = State.VISITING
            set_walls(current, grid, walls, left)

        if bottom.is_empty() and top.state is State.VISITING and n < 2:
            current.state = State.VISITING
            set_walls(current, grid, walls, top)
   
    for vertex in grid.vertices():
        if vertex.is_empty(): # set wall if empty
            vertex.state = State.WALL
        elif vertex.state is State.VISITING: # reset visiting vertices
            vertex.clear()
   
    window.executing = False
    window.fps = 60 # set fps back to 60

    return set_start_end(grid)

def visiting_neighbors(vertex):
    return sum(1 for n in vertex.neighbors if n.state is State.VISITING)
    
def set_walls(vertex, grid, walls, to_skip):
    for neighbor in vertex.neighbors:
        if neighbor == to_skip:
            continue
        x, y = neighbor.x, neighbor.y
        if 0 < x < grid.rows - 1 and 0 < y < grid.cols - 1:
            if neighbor.state is not State.VISITING:
                neighbor.state = State.WALL
            if (x, y) not in walls: # append to walls if not in already
                walls.append((x, y))

def set_start_end(grid):
    start = end = None

    for i in range(grid.rows):
        if grid()[1][i].is_empty():
            grid()[0][i].state = State.START
            start = grid()[0][i]
            break

    for i in range(grid.cols - 1, 0, -1):
        if grid()[grid.rows - 2][i].is_empty():
            grid()[grid.rows - 1][i].state = State.END
            end = grid()[grid.rows - 1][i]
            break

    return start, end
