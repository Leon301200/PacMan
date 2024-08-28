import pygame


class Screen():

    def __init__(self):
        self.display = pygame.display.set_mode((900, 950))
        pygame.display.set_caption("PacMan")
        self.clock = pygame.time.Clock()
        self.framerate = 60

    def update(self):
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(self.framerate)
        self.display.fill('black')
