import pygame
import time

width = 400
height = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
line_color = (10, 10, 10)

pygame.init()
FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("OXO")

# x_img = pygame.image.load("assets/X.png");
# o_img = pygame.image.load("assets/O.png");

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.line(screen, line_color, (width / 2, 0), (width / 2, height), 7)
    # pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    # pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    # # Drawing horizontal lines
    # pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    # pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    #all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
# def game_opening():
#     screen.fill(WHITE)
#     pygame.display.update()
#     time.sleep(5)

# game_opening()