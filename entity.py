import pygame

class Entity:
    def __init__(self, position):
        self.position = position
        self.direction: str = ""
        self.animation_walk: bool = False
        self.move_delay = 200
        self.last_move_time = pygame.time.get_ticks()

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

    def move(self):
        match self.direction:
            case "left":
                self.position = (self.position[0], self.position[1]-1)
                pass
            case "right":
                self.position = (self.position[0], self.position[1]+1)
                pass
            case "up":
                self.position = (self.position[0]-1, self.position[1])
                pass
            case "down":
                self.position = (self.position[0]+1, self.position[1])
                pass
            case _:
                pass
