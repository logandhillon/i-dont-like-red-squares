import pygame
from game.globals import Display, Gameplay, Color
from game.entities.player import Player
from game.entities.enemy import Enemy
from game.entity_groups import ALL_ENTITIES, ENEMIES


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode(
        (Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT))
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
                Enemy()

        screen.fill(Color.BLACK)

        for entity in ALL_ENTITIES:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, ENEMIES):
            player.kill()
            running = False

        player.update(pygame.key.get_pressed())
        ENEMIES.update()

        pygame.display.flip()

        clock.tick(Gameplay.FPS)


if __name__ == "__main__":
    main()
