import pygame

class Display:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720


class Color:
    BLACK = pygame.Color("black")
    WHITE = pygame.Color("white")
    RED = pygame.Color("red")


class Gameplay:
    FPS = 60
    ENEMY_SPAWN_RATE = 250
    CONTROLS = {
        "UP": [pygame.K_UP, pygame.K_w],
        "LEFT": [pygame.K_LEFT, pygame.K_a],
        "DOWN": [pygame.K_DOWN, pygame.K_s],
        "RIGHT": [pygame.K_RIGHT, pygame.K_d],
    }
