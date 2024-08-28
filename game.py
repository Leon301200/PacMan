import pygame

import keylistener
from board import Board
from screen import Screen
from pacman import Pacman
from levels import board_level1
from keylistener import KeyListener


class Game:

    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.keylistener = KeyListener()
        self.pacman = Pacman((24, 15), self.keylistener)
        self.board = Board(self.screen, board_level1, self.pacman)

    def run(self):
        while self.running:
            self.handle_input()
            self.board.update()
            self.screen.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)
