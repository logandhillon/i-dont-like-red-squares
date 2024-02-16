from src.entity.entity import Entity
from src.entity_groups import enemies
from src.globals import Color, Display
import random


class Enemy(Entity):
    def __init__(self):
        super().__init__(25, random.randint(5, 10), Color.RED)
        self.rect = self.surf.get_rect(center=(
            random.randint(Display.SCREEN_WIDTH + 20,
                           Display.SCREEN_WIDTH + 100),
            random.randint(0, Display.SCREEN_HEIGHT),
        ))
        enemies.add(self)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
