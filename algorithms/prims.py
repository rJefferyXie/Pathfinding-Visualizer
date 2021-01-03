import random
import constants

# I followed along with this guide to implement this algorithm into my program.
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e


def algorithm(grid, draw):
    # Choose a random starting point and reset all nodes
    grid, walls = init_path(grid)

    while walls:
        
        # Pick a random wall
        wall = walls.pop(int(random.random() * len(walls)) - 1)

        # Check if wall is to the left of the path
        if wall[1] != 0:
            if grid[wall[0]][wall[1] - 1].is_default() and grid[wall[0]][wall[1] + 1].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[wall[0]][wall[1]].draw_path()

                    walls, grid = top_wall(wall, walls, grid)
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)

        # Check if wall is above the path
        if wall[0] != 0:
            if grid[wall[0] - 1][wall[1]].is_default() and grid[wall[0] + 1][wall[1]].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[wall[0]][wall[1]].draw_path()

                    # Mark the new walls
                    walls, grid = top_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)
                    walls, grid = right_wall(wall, walls, grid)

        # Check if wall is below the path
        if wall[0] != constants.rows - 1:
            if grid[wall[0] + 1][wall[1]].is_default() and grid[wall[0] - 1][wall[1]].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[wall[0]][wall[1]].draw_path()

                    # Mark the new walls
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = left_wall(wall, walls, grid)
                    walls, grid = right_wall(wall, walls, grid)

        # Check if wall is to the right of the path
        if wall[1] != constants.cols - 1:
            if grid[wall[0]][wall[1] + 1].is_default() and grid[wall[0]][wall[1] - 1].is_path():
                neighbours = get_path_neighbours(wall, grid)

                if neighbours < 2:
                    # Denote the new path
                    grid[wall[0]][wall[1]].draw_path()

                    # Mark the new walls
                    walls, grid = right_wall(wall, walls, grid)
                    walls, grid = bottom_wall(wall, walls, grid)
                    walls, grid = top_wall(wall, walls, grid)

        draw()

    return finish_path(grid, draw)


def top_wall(wall, walls, grid):
    if wall[0] != 0:
        if not grid[wall[0] - 1][wall[1]].is_path():
            grid[wall[0] - 1][wall[1]].place_wall()
        if [wall[0] - 1, wall[1]] not in walls:
            walls.append([wall[0] - 1, wall[1]])

    return walls, grid


def left_wall(wall, walls, grid):
    if wall[1] != 0:
        if not grid[wall[0]][wall[1] - 1].is_path():
            grid[wall[0]][wall[1] - 1].place_wall()
        if [wall[0], wall[1] - 1] not in walls:
            walls.append([wall[0], wall[1] - 1])

    return walls, grid


def bottom_wall(wall, walls, grid):
    if wall[0] != constants.rows - 1:
        if not grid[wall[0] + 1][wall[1]].is_path():
            grid[wall[0] + 1][wall[1]].place_wall()
        if [wall[0] + 1, wall[1]] not in walls:
            walls.append([wall[0] + 1, wall[1]])

    return walls, grid


def right_wall(wall, walls, grid):
    if wall[1] != constants.cols - 1:
        if not grid[wall[0]][wall[1] + 1].is_path():
            grid[wall[0]][wall[1] + 1].place_wall()
        if [wall[0], wall[1] + 1] not in walls:
            walls.append([wall[0], wall[1] + 1])

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
    if grid[node[0] - 1][node[1]].is_path():
        neighbours += 1
    if grid[node[0] + 1][node[1]].is_path():
        neighbours += 1
    if grid[node[0]][node[1] - 1].is_path():
        neighbours += 1
    if grid[node[0]][node[1] + 1].is_path():
        neighbours += 1

    return neighbours
