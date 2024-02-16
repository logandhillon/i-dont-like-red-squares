import pygame
from src.globals import Display, Gameplay, Color
from src.entity.player import Player
from src.entity.enemy import Enemy
from src.entity_groups import all_entities, enemies

pygame.init()

screen = pygame.display.set_mode((Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, Gameplay.ENEMY_SPAWN_RATE)

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

    screen.fill(Color.BLACK)

    for entity in all_entities:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    player.update(pygame.key.get_pressed())
    enemies.update()

    pygame.display.flip()

    clock.tick(Gameplay.FPS)
