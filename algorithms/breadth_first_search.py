from queue import Queue
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
    frontier = [start]

    # Keeps track of the paths by saving references to where each node came from
    path = {}

    # A set of all nodes that were visited
    visited = {start}

    # While there is still a possible path
    while frontier:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    win.paused = not win.paused
            
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

        if win.paused:
            continue

        # At the start of every iteration, pop the first element from the queue (dequeue)
        current_node= frontier.pop(0)

        # If we found the solution, draw the path
        if current_node == end:
            time_taken = float(round(time.time() - start_time, 2))
            cost = win.draw_solution(start, end, path, draw)
            win.previous_results = [
                "Breadth First Search Results", 
                "Total Cost of Path: " + str(cost), 
                "Time Taken: " + str(time_taken) + " seconds",
                "Visited Nodes: " + str(len(visited))]
            return True

        for neighbour in current_node.neighbours:

            # Make sure not to add duplicate nodes into the frontier and path
            if neighbour not in visited:
                path[neighbour] = current_node
                visited.add(neighbour)
                frontier.append(neighbour)
                neighbour.draw_open()

        # Close off the current node because we will not need to look at it again
        if current_node not in (start, end):
            current_node.draw_visited()
        
    return False
