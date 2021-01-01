from queue import PriorityQueue
from node import Node
import time
import math
import pygame

def h1(point1, point2):
    """
    This is the Manhattan Distance algorithm.
    """
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def h2(point1, point2):
    """
    This is the Euclidian Distance (pythagoreans theorem) Algorithm.
    I am currently not using this heuristic because it is not admissible with 4 neighbour adjacency.
    """
    x1, y1 = point1
    x2, y2 = point2

    x = abs(x2 - x1)
    y = abs(y2 - y1)
    return x + y + (math.sqrt(2) - 2) * min(x, y)

def draw_solution(start, end, path, draw, time, visited, win):
    # Total cost (sum of the weights of all nodes from start to end) of path found
    cost = 0

    end.place_end()

    # Backtrack from end node to start node and draw the path found
    current = end
    while current in path:
        if current not in (start, end):
            cost += current.weight
        current = path[current]
        current.draw_path()
        draw()

    start.place_start()
    
    win.previous_results = [
        "Greedy Best First Results", 
        "Total Cost of Path: " + str(cost), 
        "Time Taken: " + str(time) + " seconds", 
        "Visited Nodes: " + str(len(visited))]

def algorithm(start, end, grid, draw, win):
    """
    This implementation uses a priority queue for its frontier.
    The runtime and space complexity depends on the heuristic.

    Worst case time complexity is O(b ^ m)
    Worst space complexity is O(b ^ m)
    where b is the branching factor (number of successor nodes per state)
    and m is the maximum depth of the search space
    """

    start_time = time.time()

    # Distance from start node
    distance = 0

    # Priority Queue to pop the current best node (node with lowest f_score)
    frontier = PriorityQueue()
    frontier.put((0, distance, start))

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    # A set of all nodes that were visited
    visited = {start}

    # F score = H score, where H score is the Heuristic (manhattan distance)
    # A dictionary that holds a Node mapped to its individual F score for every node in grid
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = h1(start.get_position(), end.get_position())

    # While there is still a possible path
    while not frontier.empty():

        # At the start of every iteration, pop the lowest f score node from priority queue
        current_node = frontier.get()[2]

        # If we found the end node, draw the path
        if current_node == end:
            time_taken = round(time.time() - start_time)
            time_seconds = time_taken % 60
            draw_solution(start, end, path, draw, time_seconds, visited, win)
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if 660 <= pos[1] <= 690:
                    if 150 <= pos[0] <= 270:
                        if win.speed == "Fast":
                            win.speed = "Medium"
                        elif win.speed == "Medium":
                            win.speed = "Slow"
                        else:
                            win.speed = "Fast"

        if win.speed == "Medium":
            pygame.time.wait(10)
        elif win.speed == "Slow":
            pygame.time.wait(50)

        for neighbour in current_node.neighbours:
            f_score[neighbour] = h1(neighbour.get_position(), end.get_position()) + neighbour.weight

            # Make sure not to add duplicate nodes into the frontier / path
            if neighbour not in visited:
                path[neighbour] = current_node
                visited.add(neighbour)
                neighbour.draw_open()

                # Increment distance because we are adding a new node
                distance += 1
                frontier.put((f_score[neighbour], distance, neighbour))

        draw()

        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()
        
    return False