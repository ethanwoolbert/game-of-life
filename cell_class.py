import pygame
import random

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.neighbors = []
        self.alive_neighbors = 0

    def update(self):
        self.rect.topleft = (self.grid_x * 20, self.grid_y * 20)

    # Fills in cell based off of state
    def draw(self):
        if self.alive:
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (1, 1, 18, 18))

        self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20))

    # Returns all neighboring cells of a cel
    def get_neighbors(self, grid):
        neighbor_list = [[1,1], [-1, -1], [-1, 1], [1, -1], [0, 1], [1, 0], [0, -1], [-1, 0]]

        for neighbor in neighbor_list:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y

        for neighbor in neighbor_list:
            if neighbor[0] < 0:
                neighbor[0] += 40
            if neighbor[0] > 39:
                neighbor[0] -= 40
            if neighbor[1] < 0:
                neighbor[1] += 40
            if neighbor[1] > 39:
                neighbor[1] -= 40

        for neighbor in neighbor_list:
            try:
                self.neighbors.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)

    # Checks every neighbor for state
    def live_neighbors(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.alive:
                count += 1

        self.alive_neighbors = count
