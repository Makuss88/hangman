import pygame
import math
import random

#  start game
pygame.init()

WIDTH = 800
HEIGHT = 500
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HaNgMaN gAmE!")

#  word

WORDS_LIST = [line.rstrip('\n').upper() for line in open('words.txt')]
WORD = random.choice(WORDS_LIST)

guessed = []


#  img
images = []
hangman_image = 0

for i in range(7):
    image = pygame.image.load('./img/hang' + str(i) + '.png')
    images.append(image)

#  alphabet
RADIUS = 20
GAP = 15
letters = []  # ex [13, 240, 'A', True]
A = 65
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
FONT_IN_CIRCLE = pygame.font.SysFont('comicsans', 40)
FONT_IN_WORD = pygame.font.SysFont('monostyle', 60)

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
    scr.fill(WHITE)
    print(WORD)
    display_word = ''
    for let in WORD:
        if let in guessed:
            display_word += let + " "
        else:
            display_word += '_ '

    text = FONT_IN_WORD.render(display_word, 1, BLACK)
    scr.blit(text, (450, 200))

    for letter in letters:
        x, y, ltr, visible_ltr = letter
        if visible_ltr:
            pygame.draw.circle(scr, BLACK, (x, y), RADIUS, 2)
            text = FONT_IN_CIRCLE.render(ltr, 1, BLUE)
            scr.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    scr.blit(images[hangman_image], (0, 0))
    pygame.display.update()


def display_info(message: str):
    pygame.time.delay(1000)
    scr.fill(BLUE)
    text = FONT_IN_WORD.render(message, 1, BLACK)
    scr.blit(text, (WIDTH // 2 - text.get_width() // 2, 200))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    print(WORD)

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
                        guessed.append(ltr)
                        if ltr not in WORD:
                            hangman_image += 1

    win = True
    for letter in WORD:
        if letter not in guessed:
            win = False
            break

    draw()

    if win:
        display_info('You won this game!')
        break

    if hangman_image == 6:
        display_info('The hangman is death!')
        break

pygame.quit()
