# Pathfinding Visualizer

A pathfinding visualizer made in Python using pygame. Includes:

- [Dijkstra](#dijkstra)
- [Greedy](#greedy)
- [A\*](#a*)
- [Breadth-first search](#breadth-first-search)
- [Depth-first search](#depth-first-search)
- [Prim's Algorithm](#prims-algorithm)

## Controls

- Right mouse button click: either set or remove both the start and the end vertex.
- Left mouse button hold: draw walls.
- Right mouse button hold: delete walls.
- Right mouse button hold along with <kbd>W</kbd>: add weights.

## Demo

Check out the images [here](https://github.com/davidetacchini/pathfinding-visualizer/tree/main/assets/showcase)

## Algorithms

### Dijkstra
- Weighted
- Guarantees the shortest path
- Father of the pathfinding algorithms

### Greedy best-first
- Weighted
- Does not guarantee the shortest path
- Uses heuristic to compute end vertex position

### A*
- Weighted
- Guarantees the shortest path
- The best algorithm for pathfinding

### Depth-first search
- Unweighted
- Does not guarantee the shortest path
- Pretty bad algorithm for pathfinding

### Breadth-first search
- Unweighted
- Guarantess the shortest path

### Prim's Algorithm
- Usuful to generate random mazes

## Links

- http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- https://en.wikipedia.org/wiki/Best-first_search
- https://en.wikipedia.org/wiki/A*_search_algorithm
- https://en.wikipedia.org/wiki/Depth-first_search
- https://en.wikipedia.org/wiki/Breadth-first_search
- https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
