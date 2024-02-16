from game.entities.entity import Entity
import pygame
from game.globals import Color, Display

class Player(Entity):
    def __init__(self):
        super().__init__(50, 5, Color.WHITE)

    def update(self, pressed_keys):
        dx = 0
        dy = 0
        if pressed_keys[pygame.K_UP]:       dy -= self.speed
        if pressed_keys[pygame.K_DOWN]:     dy += self.speed
        if pressed_keys[pygame.K_LEFT]:     dx -= self.speed
        if pressed_keys[pygame.K_RIGHT]:    dx += self.speed

        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT))