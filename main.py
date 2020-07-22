import pygame
import os

pygame.init()
WIDTH = 800
HEIGHT = 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HaNgMaN gAmE!")

FPS = 60
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
