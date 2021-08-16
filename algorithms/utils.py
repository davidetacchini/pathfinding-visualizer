from consts import *


def event_handler(events, window, *, switch_fps=True):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit(); quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if window.buttons["pause"].is_clicked(pos, event): # pause algorithm
                window.paused = not window.paused
            elif switch_fps and window.buttons["fps"].is_clicked(pos, event): # switch fps
                if window.fps == 60:
                    window.fps = 90
                elif window.fps == 90:
                    window.fps = 120
                else:
                    window.fps = 60

def helper(func):
    
    def wrapper(*args, **kwargs):
        grid, window = args[2], args[3]
        grid.clear() # make sure grid is clear
        for vertex in grid.vertices(): # set neighbors
            vertex.add_neighbors(grid)
        window.executing = True
        time, visited, cost = func(*args, **kwargs)
        window.executing = False
        # update algorithm statistics
        window.statistics = (
            f"Algorithm: {func.__doc__}",
            f"Execution time: {time}s",
            f"Visited vertices: {visited}",
            f"Shortest path: {cost}",
        )

    return wrapper

def heuristic(current, target):
    """Manhattan Distance.
    Not using the Euclidean Distance algorithm: we have 
    no access to the diagonal vertices.
    """
    return abs(current.x - target.x) + abs(current.y - target.y)
