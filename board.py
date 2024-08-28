import pygame
import math
from screen import Screen
from levels import board_level1
from pacman import Pacman


class Board:

    def __init__(self, screen: Screen, level, pacman: Pacman):
        self.screen = screen
        self.level = level
        self.width, self.height = self.screen.display.get_size()
        self.case_size = [(self.width // len(self.level[0])), ((self.height - 50) // len(self.level))]
        self.pacman = pacman

    def get_index(self, i, j):
        width_case, heigth_case = self.case_size
        return j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)

    def update(self):
        self.pacman.update()
        self.draw_board()
        self.draw_pacman()
    def draw_board(self):
        width_case, heigth_case = self.case_size
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                    pygame.draw.circle(self.screen.display, 'white',
                                       (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 2:
                    pygame.draw.circle(self.screen.display, 'white',
                                       (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 8)
                elif self.level[i][j] == 3:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + (0.5 * width_case), i * heigth_case),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + heigth_case), 4)
                elif self.level[i][j] == 4:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + width_case, i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 5:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + (0.5 * width_case), i * heigth_case + heigth_case),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 6:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + (0.5 * width_case), i * heigth_case + heigth_case),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 7:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + (0.5 * width_case), i * heigth_case),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 8:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_case + (0.5 * width_case), i * heigth_case),
                                     (j * width_case + (0.5 * width_case), i * heigth_case + (0.5 * heigth_case)), 4)
                elif self.level[i][j] == 9:
                    pygame.draw.line(self.screen.display, 'white',
                                     (j * width_case, i * heigth_case + (0.5 * heigth_case)),
                                     (j * width_case + width_case, i * heigth_case + (0.5 * heigth_case)), 4)

    def draw_pacman(self):
        x, y = self.get_index(self.pacman.position[0], self.pacman.position[1])
        pygame.draw.circle(self.screen.display, 'orange', (x, y), 15)