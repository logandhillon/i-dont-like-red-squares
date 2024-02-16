from game.entities.entity import Entity
import pygame
from game.globals import Color, Display, Gameplay

class Player(Entity):
    def __init__(self):
        super().__init__(50, 5, Color.WHITE)

    def update(self, pressed_key):
        dx = 0
        dy = 0
        
        if any(pressed_key[key] for key in Gameplay.CONTROLS["UP"]):
            dy -= self.speed
        if any(pressed_key[key] for key in Gameplay.CONTROLS["DOWN"]):
            dy += self.speed
        if any(pressed_key[key] for key in Gameplay.CONTROLS["LEFT"]):
            dx -= self.speed
        if any(pressed_key[key] for key in Gameplay.CONTROLS["RIGHT"]):
            dx += self.speed

        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT))