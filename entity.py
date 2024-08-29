import pygame
class Entity:
    def __init__(self, position):
        self.position = position
        self.direction: str = ""
        self.animation_walk: bool = False
        self.move_delay = 200
        self.last_move_time = pygame.time.get_ticks()
        self.possible_moves = []

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= self.move_delay:
            self.move()
            self.last_move_time = current_time

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def get_left_box(self):
        return self.position[0], self.position[1] - 1

    def get_right_box(self):
        return self.position[0], self.position[1] + 1

    def get_up_box(self):
        return self.position[0] - 1, self.position[1]

    def get_down_box(self):
        return self.position[0] + 1, self.position[1]

    def move(self):
        if self.direction == "left" and "left" in self.possible_moves:
            self.position = self.get_left_box()
        if self.direction == "right" and "right" in self.possible_moves:
            self.position = self.get_right_box()
        if self.direction == "up" and "up" in self.possible_moves:
            self.position = self.get_up_box()
        if self.direction == "down" and "down" in self.possible_moves:
            self.position = self.get_down_box()
