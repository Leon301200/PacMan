import pygame
import math
from screen import Screen
from levels import board_level1
from pacman import Pacman
from entity import Entity


class Board:

    def __init__(self, screen: Screen, level, pacman: Pacman):
        self.screen = screen
        self.level = level
        self.width, self.height = self.screen.display.get_size()
        self.box_size = [(self.width // len(self.level[0])), ((self.height - 50) // len(self.level))]
        self.pacman = pacman

    def get_index(self, i, j):
        width_box, heigth_box = self.box_size
        return j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)

    def update(self):
        # Mises à jours des deplacement possible
        self.get_possible_moves(self.pacman)

        # Déplacement
        self.pacman.update()

        # Affichage
        self.draw_board()
        self.draw_pacman()

    def is_wall(self, position):
        return self.level[position[0]][position[1]] not in [0, 1, 2]

    def get_possible_moves(self, entity: Entity):
        entity.possible_moves.clear()
        if not self.is_wall(entity.get_left_box()):
            entity.possible_moves.append("left")
        if not self.is_wall(entity.get_right_box()):
            entity.possible_moves.append("right")
        if not self.is_wall(entity.get_up_box()):
            entity.possible_moves.append("up")
        if not self.is_wall(entity.get_down_box()):
            entity.possible_moves.append("down")

    def draw_board(self):
        width_box, heigth_box = self.box_size
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                    pygame.draw.circle(self.screen.display, 'white',
                                       (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 2:
                    pygame.draw.circle(self.screen.display, 'white',
                                       (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 8)
                elif self.level[i][j] == 3:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + (0.5 * width_box), i * heigth_box),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + heigth_box), 4)
                elif self.level[i][j] == 4:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + width_box, i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 5:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + (0.5 * width_box), i * heigth_box + heigth_box),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 6:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + (0.5 * width_box), i * heigth_box + heigth_box),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 7:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + (0.5 * width_box), i * heigth_box),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 8:
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                    pygame.draw.line(self.screen.display, 'blue',
                                     (j * width_box + (0.5 * width_box), i * heigth_box),
                                     (j * width_box + (0.5 * width_box), i * heigth_box + (0.5 * heigth_box)), 4)
                elif self.level[i][j] == 9:
                    pygame.draw.line(self.screen.display, 'white',
                                     (j * width_box, i * heigth_box + (0.5 * heigth_box)),
                                     (j * width_box + width_box, i * heigth_box + (0.5 * heigth_box)), 4)

    def draw_pacman(self):
        x, y = self.get_index(self.pacman.position[0], self.pacman.position[1])
        pygame.draw.circle(self.screen.display, 'orange', (x, y), 15)