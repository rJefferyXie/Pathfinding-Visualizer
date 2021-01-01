from queue import Queue
from constants import width, square_size
import time
import pygame


def algorithm(start, end, grid, draw, win):
    """
    Breadth First Search uses FIFO (queue).
    Breadth First Search is not a weighted algorithm and guarantees the shortest path.

    Time complexity is O(N + E), where N is number of nodes and E is number of edges
    Space complexity is O(N) where N is the number of nodes in the call stack
    """

    start_time = time.time()

    # Frontier is the queue of nodes that are currently being considered
    frontier = Queue()
    frontier.put((start, 0))

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    # A set of all nodes that were visited
    visited = {start}

    # Make sure we are moving outwards on each iteration
    # A dictionary that holds a Node mapped to its individual distance for every node in grid
    distances = {Node: float("inf") for row in grid for Node in row}
    distances[start] = 0

    # While there is still a possible path
    while not frontier.empty():

        # At the start of every iteration, pop the first element from the queue (dequeue)
        current_node = frontier.get()[0]

        # If we found the solution, draw the path
        if current_node == end:
            time_taken = round(time.time() - start_time)
            time_seconds = time_taken % 60
            cost = win.draw_solution(start, end, path, draw)
            win.previous_results = [
                "Breadth First Search Results", 
                "Total Cost of Path: " + str(cost), 
                "Time Taken: " + str(time_seconds) + " seconds", 
                "Visited Nodes: " + str(len(visited))]
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

        next_distance = distances[current_node] + 1

        for neighbour in current_node.neighbours:
            if next_distance < distances[neighbour]:
                distances[neighbour] = next_distance

                # Make sure not to add duplicate nodes into the frontier and path
                if neighbour not in visited:
                    path[neighbour] = current_node
                    visited.add(neighbour)
                    neighbour.draw_open()

                    frontier.put((neighbour, distances[neighbour]))

        draw()

        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()
        
    return False
