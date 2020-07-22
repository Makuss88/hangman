import pygame
import math

#  start game
pygame.init()

WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HaNgMaN gAmE!")

#  img
images = []
hangman_image = 6
for i in range(7):
    image = pygame.image.load('./img/hang' + str(i) + '.png')
    images.append(image)

#  buttons, and alphabet, and fonts
RADIUS = 20
GAP = 15
letters = []  # ex [13, 240, 'A', True]
A = 65
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (RADIUS * 2 + GAP))
    letters.append([x, y, chr(A + i), True])

#  colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#  setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


#  draw
def draw():
    win.fill(WHITE)

    for letter in letters:
        x, y, ltr, visible_ltr = letter
        if visible_ltr:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLUE)
            win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    win.blit(images[hangman_image], (0, 0))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible_ltr = letter
                if visible_ltr:
                    dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
pygame.quit()
