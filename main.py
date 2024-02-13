import pygame
import src.globals as globals
import random

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(globals.WHITE)
        self.rect = self.surf.get_rect()
        self.speed = 5

    def update(self, pressed_keys):
        dx = 0
        dy = 0
        if pressed_keys[pygame.K_UP]:       dy -= self.speed
        if pressed_keys[pygame.K_DOWN]:     dy += self.speed
        if pressed_keys[pygame.K_LEFT]:     dx -= self.speed
        if pressed_keys[pygame.K_RIGHT]:    dx += self.speed

        self.rect.move_ip(dx, dy)

        # force player in screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > globals.SCREEN_WIDTH:
            self.rect.right = globals.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.rect.bottom = globals.SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(globals.RED)
        self.rect = self.surf.get_rect(center=(
            random.randint(globals.SCREEN_WIDTH + 20,
                           globals.SCREEN_WIDTH + 100),
            random.randint(0, globals.SCREEN_HEIGHT),
        ))
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, globals.ENEMY_SPAWN_RATE)

player = Player()

enemies = pygame.sprite.Group()
all_entities = pygame.sprite.Group()
all_entities.add(player)

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
            all_entities.add(e)
            enemies.add(e)

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
