import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

BG = pygame.transform.scale(
    pygame.image.load("space.jpg").convert(),
    (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60


def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()



def main():
    run = True
    player = pygame.Rect(200, HEIGHT- PLAYER_HEIGHT)


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()
    
if __name__ == "__main__":
    main()


