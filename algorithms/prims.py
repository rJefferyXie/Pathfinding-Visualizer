import random
import constants
import pygame

# I followed along with this guide to implement this algorithm into my program.
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e


def algorithm(grid, draw, win):
    # Choose a random starting point and reset all nodes
    grid, walls = init_path(grid)

    while walls:
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
        
        # Pick a random wall
        wall = walls.pop(int(random.random() * len(walls)) - 1)

        row, col = wall

        # Check if wall is to the left of the path
        if col != 0:
            if grid[row][col - 1].is_default() and grid[row][col + 1].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[row][col].draw_path()

                    walls, grid = top_wall(wall, walls, grid)
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)

        # Check if wall is above the path
        if row != 0:
            if grid[row - 1][col].is_default() and grid[row + 1][col].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[row][col].draw_path()

                    # Mark the new walls
                    walls, grid = top_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)
                    walls, grid = right_wall(wall, walls, grid)

        # Check if wall is below the path
        if row != constants.rows - 1:
            if grid[row + 1][col].is_default() and grid[row - 1][col].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[row][col].draw_path()

                    # Mark the new walls
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)
                    walls, grid = right_wall(wall, walls, grid)

        # Check if wall is to the right of the path
        if col != constants.cols - 1:
            if grid[row][col + 1].is_default() and grid[row][col - 1].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[row][col].draw_path()

                    # Mark the new walls
                    walls, grid = right_wall(wall, walls, grid)
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = top_wall(wall, walls, grid)

    return finish_path(grid, draw)


def top_wall(wall, walls, grid):
    row, col = wall
    if row != 0:
        if not grid[row - 1][col].is_path():
            grid[row - 1][col].place_wall()
        if [row - 1, col] not in walls:
            walls.append([row - 1, col])

    return walls, grid


def left_wall(wall, walls, grid):
    row, col = wall
    if col != 0:
        if not grid[row][col - 1].is_path():
            grid[row][col - 1].place_wall()
        if [row, col - 1] not in walls:
            walls.append([row, col - 1])

    return walls, grid


def bottom_wall(wall, walls, grid):
    row, col = wall
    if row != constants.rows - 1:
        if not grid[row + 1][col].is_path():
            grid[row + 1][col].place_wall()
        if [row + 1, col] not in walls:
            walls.append([row + 1, col])

    return walls, grid


def right_wall(wall, walls, grid):
    row, col = wall
    if col != constants.cols - 1:
        if not grid[row][col + 1].is_path():
            grid[row][col + 1].place_wall()
        if [row, col + 1] not in walls:
            walls.append([row, col + 1])

    return walls, grid


def init_path(grid):
    # Reset grid
    for row in grid:
        for Node in row:
            Node.reset_color()
            Node.reset_weight()
    
    # Choose a random starting point
    starting_height = int(random.random() * constants.rows)
    starting_width = int(random.random() * constants.cols)

    # Make sure we are not starting on the border of the grid
    if starting_height == 0:
        starting_height += 1
    elif starting_height == constants.rows - 1:
        starting_height -= 1
    
    if starting_width == 0:
        starting_width += 1
    elif starting_width == constants.cols - 1:
        starting_width -= 1
    
    # This is where the maze generation starts at
    grid[starting_height][starting_width].draw_path()

    # Initialize the walls list with the walls adjacent to start point
    walls = [[starting_height - 1, starting_width], [starting_height, starting_width - 1],
             [starting_height, starting_width + 1], [starting_height + 1, starting_width]]

    # Place starting walls
    grid[starting_height - 1][starting_width].place_wall()
    grid[starting_height][starting_width - 1].place_wall()
    grid[starting_height][starting_width + 1].place_wall()
    grid[starting_height + 1][starting_width].place_wall()

    return grid, walls


def finish_path(grid, draw):
    start = end = None

    # Turn the remaining default nodes into walls
    for i in range(0, constants.rows):
        for j in range(0, constants.cols):
            if grid[i][j].is_default():
                grid[i][j].place_wall()
                draw()
    
    # Set start and end nodes
    for i in range(0, constants.cols):
        if grid[1][i].is_path():
            start = grid[0][i]
            start.place_start()
            break

    for i in range(constants.cols - 1, 0, -1):
        if grid[constants.rows - 2][i].is_path():
            end = grid[constants.rows - 1][i]
            end.place_end()
            break
    
    # Reset path nodes
    for row in grid:
        for Node in row:
            if Node.is_path():
                Node.reset_color()

    return start, end, grid


def get_path_neighbours(node, grid):
    neighbours = 0
    row, col = node

    # Up
    if grid[row - 1][col].is_path():
        neighbours += 1

    # Down
    if grid[row + 1][col].is_path():
        neighbours += 1

    # Left
    if grid[row][col - 1].is_path():
        neighbours += 1

    # Right
    if grid[row][col + 1].is_path():
        neighbours += 1

    return neighbours
