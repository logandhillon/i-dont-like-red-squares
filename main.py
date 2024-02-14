import pygame
import src.globals as globals
import random

pygame.init()

enemies = pygame.sprite.Group()
all_entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, size: int, speed: int, color: pygame.color):
        super(Entity, self).__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.speed = speed
        all_entities.add(self)

class Player(Entity):
    def __init__(self):
        super().__init__(50, 5, globals.WHITE)

    def update(self, pressed_keys):
        dx = 0
        dy = 0
        if pressed_keys[pygame.K_UP]:       dy -= self.speed
        if pressed_keys[pygame.K_DOWN]:     dy += self.speed
        if pressed_keys[pygame.K_LEFT]:     dx -= self.speed
        if pressed_keys[pygame.K_RIGHT]:    dx += self.speed

        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

class Enemy(Entity):
    def __init__(self):
        super().__init__(25, random.randint(5, 10), globals.RED)
        self.rect = self.surf.get_rect(center=(
            random.randint(globals.SCREEN_WIDTH + 20,
                           globals.SCREEN_WIDTH + 100),
            random.randint(0, globals.SCREEN_HEIGHT),
        ))
        enemies.add(self)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, globals.ENEMY_SPAWN_RATE)

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == ADD_ENEMY:
            e = Enemy()

    screen.fill(globals.BLACK)

    for entity in all_entities:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    player.update(pygame.key.get_pressed())
    enemies.update()

    pygame.display.flip()

    clock.tick(globals.FPS)
