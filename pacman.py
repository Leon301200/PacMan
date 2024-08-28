import pygame

from entity import Entity
from keylistener import KeyListener

class Pacman(Entity):
    def __init__(self, position, keylistener: KeyListener):
        super().__init__(position)
        self.keylistener = keylistener

    def update(self):
        self.check_move()
        super().update()

    def check_move(self):
        if self.keylistener.key_pressed(pygame.K_LEFT):
            self.move_left()
        elif self.keylistener.key_pressed(pygame.K_RIGHT):
            self.move_right()
        elif self.keylistener.key_pressed(pygame.K_UP):
            self.move_up()
        elif self.keylistener.key_pressed(pygame.K_DOWN):
            self.move_down()

