import math

# These heuristics are used for A* search and Greedy Best First Search


def h1(point1, point2):
    """
    This is the Manhattan Distance algorithm. 
    This is an admissible algorithm which means it never overestimates the cost of reaching the goal node.
    It is an estimate of the total nodes along axes at right angles from point1 to point2.
    """
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def h2(point1, point2):
    """
    This is the Euclidean Distance (Pythagorean's theorem) Algorithm.
    I am currently not using this heuristic because it is not admissible with 4 neighbour adjacency.
    It also consistently returns worse results than h1.
    """
    x1, y1 = point1
    x2, y2 = point2

    x = abs(x2 - x1)
    y = abs(y2 - y1)
    return x + y + (math.sqrt(2) - 2) * min(x, y)
