from constants import width, height, square_size, blue2, rows, cols
from node import Node
import pygame


class Window:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Pathfinding Visualizer by Jeffery Xie")
        self.font = pygame.font.SysFont("calibri", 15)
        self.win = pygame.display.set_mode((width, height))
        self.selected_algorithm = None
        self.speed = "Fast"
        self.previous_results = []

    def make_grid(self):
        # Make an N by N grid with each index implemented as a node
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                grid[i].append(Node(i, j))
        
        return grid

    def draw_grid(self):
        for i in range(rows + 1):
            pygame.draw.line(self.win, (0, 0, 0), (i * square_size, 0), (i * square_size, width), 1)
            pygame.draw.line(self.win, (0, 0, 0), (0, i * square_size), (width, i * square_size), 1)
    
    def draw_buttons(self):

        # A* Algorithm
        pygame.draw.rect(self.win, (0, 0, 0), (square_size, square_size * 41 + 10, square_size * 8, square_size * 2))
        if self.selected_algorithm == "a_star":
            pygame.draw.rect(self.win, blue2, (square_size + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (square_size + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("A* Search", True, (0, 0, 0))
        self.win.blit(text, (square_size * 2 + 10, square_size * 42))

        # Greedy BFS Algorithm
        pygame.draw.rect(self.win, (0, 0, 0), (square_size, square_size * 44, square_size * 8, square_size * 2))
        if self.selected_algorithm == "greedy_best_first_search":
            pygame.draw.rect(self.win, blue2, (square_size + 1, square_size * 44 + 1, square_size * 8 - 2, square_size * 2 - 2))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (square_size + 1, square_size * 44 + 1, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("Greedy Best First", True, (0, 0, 0))
        self.win.blit(text, (square_size + 2, square_size * 44 + 5))

        # BFS Algorithm
        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 19, square_size * 44, square_size * 8, square_size * 2))
        if self.selected_algorithm == "breadth_first_search":
            pygame.draw.rect(self.win, blue2, (square_size * 19 + 1, square_size * 44 + 1, square_size * 8 - 2, square_size * 2 - 2))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (square_size * 19 + 1, square_size * 44 + 1, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("Breadth First", True, (0, 0, 0))
        self.win.blit(text, (square_size * 20 + 4, square_size * 44 + 5))

        # Dijkstra's Algorithm
        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 10, square_size * 41 + 10, square_size * 8, square_size * 2))
        if self.selected_algorithm == "dijkstras":
            pygame.draw.rect(self.win, blue2, (square_size * 10 + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (square_size * 10 + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("Dijkstra's Algo.", True, (0, 0, 0))
        self.win.blit(text, (square_size * 10 + 10, square_size * 42))

        # DFS Algorithm
        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 19, square_size * 41 + 10, square_size * 8, square_size * 2))
        if self.selected_algorithm == "depth_first_search":
            pygame.draw.rect(self.win, blue2, (square_size * 19 + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        else:
            pygame.draw.rect(self.win, (255, 255, 255), (square_size * 19 + 1, square_size * 41 + 11, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("Depth First", True, (0, 0, 0))
        self.win.blit(text, (square_size * 20 + 8, square_size * 42))

        # Change Speed Button
        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 10, square_size * 44, square_size * 8, square_size * 2))
        pygame.draw.rect(self.win, (255, 255, 255), (square_size * 10 + 1, square_size * 44 + 1, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render(self.speed, True, (0, 0, 0))
        if self.speed in ("Fast", "Slow"):
            self.win.blit(text, (square_size * 13, square_size * 44 + 5))
        else:
            self.win.blit(text, (square_size * 12 + 5, square_size * 44 + 5))
    
    def draw_results(self):
        if self.previous_results:
            for i in range(len(self.previous_results)):
                text = self.font.render(self.previous_results[i], True, (0, 0, 0))
                self.win.blit(text, (square_size * 27 + 10, square_size * (41 + i) + 10))

    def draw_solution(self, start, end, path, draw):
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
        return cost
        
    def draw(self, grid):
        self.win.fill((255, 255, 255))
        
        for row in grid:
            for node in row:
                node.draw(self.win)
                if node.weight != 1:
                    text = self.font.render("9", True, (0, 0, 0))
                    self.win.blit(text, (node.row * square_size + 4, node.col * square_size))
        
        self.draw_grid()
        self.draw_buttons()
        self.draw_results()

        pygame.display.update()

    def get_mouse_position(self, pos):
        row = pos[0] // square_size
        col = pos[1] // square_size
        return row, col
