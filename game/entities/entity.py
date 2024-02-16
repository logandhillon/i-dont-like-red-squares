from game.entity_groups import ALL_ENTITIES
import pygame.sprite
from game.globals import Display
from abc import ABC, abstractmethod


class Entity(pygame.sprite.Sprite, ABC):
    def __init__(self, size: int, speed: int, color: pygame.color):
        super(Entity, self).__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.speed = speed
        ALL_ENTITIES.add(self)

    @abstractmethod
    def update(self):
        pass
