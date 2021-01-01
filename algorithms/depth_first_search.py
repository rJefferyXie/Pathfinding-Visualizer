from node import Node
from constants import width, square_size
import time
import pygame

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
        "Depth First Search Results", 
        "Total Cost of Path: " + str(cost), 
        "Time Taken: " + str(time) + " seconds", 
        "Visited Nodes: " + str(len(visited))]

def algorithm(start, end, grid, draw, win):
    """
    Depth First Search uses LIFO (stack).
    
    Time complexity is O(N + E), where N is number of nodes and E is number of edges
    Space complexity is O(N), where N is the number of nodes in the call stack
    The order of traversal for DFS is Up, Right, Down, Left
    """

    start_time = time.time()

    # Frontier is the stack of nodes that are currently being considered
    frontier = [start]

    # A set of all nodes that were visited
    visited = {start}

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    current_node = start
    # While there is still a possible path
    while len(frontier) > 0:
        if current_node not in (start, end):
            current_node.draw_open()

        # At the start of every iteration, pop the top element from the queue
        current_node = frontier.pop()

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

        if current_node not in visited:
            visited.add(current_node)

        for neighbour in current_node.neighbours:

            # Make sure not to add duplicate nodes into the frontier and path
            if neighbour not in visited:
                path[neighbour] = current_node
                frontier.append(neighbour)
        
        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()

        draw()
    
    return False
