from queue import PriorityQueue
from algorithms.heuristics import h1
import time
import pygame


def algorithm(start, end, grid, draw, win):
    """
    This implementation uses a priority queue for its frontier.
    The runtime and space complexity depends on the heuristic.

    This is a version of weighted A* search which can calculate 
    shortest path when the path weights are not all the same.
    A* Search is guaranteed to return the shortest path.

    The theoretical time complexity is O(b ^ d)
    The space complexity is also O(b ^ d)
    where b is the branching factor (number of successor nodes per state)
    and d is the depth of the shortest path to the end node
    """

    start_time = time.time()

    # Used for a tiebreaker in case of two nodes with similar F scores
    distance = 0

    # Priority Queue to pop the current best node (node with lowest f_score)
    # The frontier is the queue of nodes that are currently being considered
    frontier = PriorityQueue()
    frontier.put((0, distance, start))

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    # A set of all nodes that were visited
    visited = {start}

    # G score is the distance (num of nodes) between the current node and the starting node
    # A dictionary that holds a Node mapped to its individual G score for every node in grid
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0

    # F score = G score + H score, where H score is the Heuristic (manhattan distance)
    # A dictionary that holds a Node mapped to its individual F score for every node in grid
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = h1(start.get_position(), end.get_position())

    # While there is still a possible path
    while not frontier.empty():

        # At the start of every iteration, pop the lowest f score node from priority queue
        current_node = frontier.get()[2]

        # If we found the solution, draw the path
        if current_node == end:
            time_taken = float(round(time.time() - start_time, 2))
            cost = win.draw_solution(start, end, path, draw)
            win.previous_results = [
                "A* Search Results", 
                "Total Cost of Path: " + str(cost), 
                "Time Taken: " + str(time_taken) + " seconds",
                "Visited Nodes: " + str(len(visited))]
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if pygame.mouse.get_pressed(3)[0]:
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

        # This will be the next g score for any neighbours with lower costs
        next_g_score = g_score[current_node] + current_node.weight

        for neighbour in current_node.neighbours:
            
            # If we found a neighbour node that has a lower cost for reaching goal node
            if next_g_score < g_score[neighbour]:
                g_score[neighbour] = next_g_score
                f_score[neighbour] = next_g_score + h1(neighbour.get_position(), end.get_position()) + neighbour.weight

                # Make sure not to add duplicate nodes into the frontier and path
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
