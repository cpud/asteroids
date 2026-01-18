import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    # game loop
    while True:
        log_state()
        
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #new_player.update(dt)
        updatable.update(dt)    
        screen.fill("black")
        #new_player.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        # limit 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
