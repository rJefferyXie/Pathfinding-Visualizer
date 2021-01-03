import pygame
from constants import white, red, green, gray, purple, blue1, blue2, square_size, width


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * square_size
        self.y = col * square_size
        self.color = white
        self.weight = 1
        self.neighbours = []
    
    def get_position(self):
        return self.row, self.col

    def is_wall(self):
        return self.color == gray
    
    def is_default(self):
        return self.color == white

    def is_path(self):
        return self.color == purple
    
    def reset_color(self):
        self.color = white
    
    def reset_weight(self):
        self.weight = 1

    # User places these node objects with mouse clicks
    def place_start(self):
        self.color = green
    
    def place_end(self):
        self.color = red

    def place_wall(self):
        self.color = gray
    
    def place_weight(self):
        self.weight = 9

    # These three draw functions will be called by algorithm, not by user
    def draw_open(self):
        self.color = blue1
    
    def draw_visited(self):
        self.color = blue2
    
    def draw_path(self):
        self.color = purple

    def add_neighbours(self, grid):
        self.neighbours = []

        # Up
        if self.row > 0:
            neighbour = grid[self.row - 1][self.col]
            if not neighbour.is_wall(): 
                self.neighbours.append(neighbour)
        
        # Right
        if self.col < width // square_size - 1:
            neighbour = grid[self.row][self.col + 1]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)
            
        # Down
        if self.row < width // square_size - 1:
            neighbour = grid[self.row + 1][self.col]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)

        # Left
        if self.col > 0:
            neighbour = grid[self.row][self.col - 1]
            if not neighbour.is_wall():
                self.neighbours.append(neighbour)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, square_size, square_size))
