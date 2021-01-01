from queue import PriorityQueue
from node import Node
import time
import pygame


def algorithm(start, end, grid, draw, win):
    """
    This implementation uses a priority queue for its frontier.
    Dijkstras is a weighted algorithm and guarantees the shortest path.
    
    Time complexity is O(E log N) 
    Space complexity is O(E log N)
    where E is the number of edges 
    and N is number of nodes
    """

    start_time = time.time()

    # Used for g score (the distance between current node and starting node)
    distance = 0

    # Priority Queue to pop the current best node (node with lowest f_score)
    # The frontier is the queue of nodes that are currently being considered
    frontier = PriorityQueue()
    frontier.put((0, distance, start))

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    # A set of all nodes that were visited
    visited = {start}

    # F score = G score (the distance between the current node and the starting node)
    # A dictionary that holds a Node mapped to its individual F score for every node in grid
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = 0

    # While there is still a possible path
    while not frontier.empty():

        # At the start of every iteration, pop the lowest f score node from priority queue
        current_node = frontier.get()[2]

        # If we found the solution, draw the path
        if current_node == end:
            time_taken = round(time.time() - start_time)
            time_seconds = time_taken % 60
            cost = win.draw_solution(start, end, path, draw)
            win.previous_results = [
                "Dijkstra's Algorithm Results", 
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

        # This will be the next g score for any good neighbours of current_node
        next_f_score = f_score[current_node] + current_node.weight

        for neighbour in current_node.neighbours:

            # If we found a neighbour node that takes us closer to end
            if next_f_score < f_score[neighbour]:
                f_score[neighbour] = next_f_score + neighbour.weight

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