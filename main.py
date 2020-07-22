import pygame
import os

#  start game
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HaNgMaN gAmE!")

#  img
image = pygame.image.load('./img/hangman6.png')
images = [image]
# for i in range(1):
#     image = pygame.image.load('./img/hangman' + str(i) + '.png')
#     images.append(image)
hangman_image = 0


#  colors
WHITE = (255, 255, 255)

#  setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_image], (100, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
