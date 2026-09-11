from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_time = pygame.time.Clock()
    dt: float = 0.0

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player_object = Player(player_x, player_y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_object.draw(screen)
        pygame.display.flip()
        dt = game_time.tick(60)/1000


if __name__ == "__main__":
    main()
