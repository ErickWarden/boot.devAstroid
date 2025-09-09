# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    # game while loop
    while True:
        # quit game if screen X clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # main screen presentation
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()
