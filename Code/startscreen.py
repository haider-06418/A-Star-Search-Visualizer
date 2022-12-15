import pygame as pg
from constants import *
from helperFunctions import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")
window_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
clock = pg.time.Clock()
pygame.font.init()

def text_objects(text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

def btn(msg, x, y, w, h, ic, ac):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(MAIN_WINDOW, ac, (x, y, w, h))
    else:
        pg.draw.rect(MAIN_WINDOW, ic, (x, y, w, h))
    if click[0] == 1:
        if mouse[0] > x and mouse[0] < x + w and mouse[1] > y and mouse[1] < y + h:
            import sys
            import main
            sys.exit(main.main_func(MAIN_WINDOW, SCREEN_WIDTH))  
        # pass
    small_text = pg.font.SysFont("comicsansms", 25)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    MAIN_WINDOW.blit(text_surf, text_rect)

def btn1(msg, x1, y1, w1, h1, ic1, ac1):
    mouse1 = pg.mouse.get_pos()
    click1 = pg.mouse.get_pressed()
    if x1 + w1 > mouse1[0] > x1 and y1 + h1 > mouse1[1] > y1:
        pg.draw.rect(MAIN_WINDOW, ac1, (x1, y1, w1, h1))
    else:
        pg.draw.rect(MAIN_WINDOW, ic1, (x1, y1, w1, h1))
    if click1[0] == 1:
        if mouse1[0] > x1 and mouse1[0] < x1 + w1 and mouse1[1] > y1 and mouse1[1] < y1 + h1:
            showInstructions()
    small_text = pg.font.SysFont("comicsansms", 25)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x1 + (w1 / 2)), (y1 + (h1 / 2)))
    MAIN_WINDOW.blit(text_surf, text_rect)

intro = True
while intro:
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    MAIN_WINDOW.fill(WHITE)
    MAIN_WINDOW.blit(pygame.image.load("Code/Main_Screen.png"), ((0), (0)))
    btn("GO!", (window_size[0] - 100) / 2, window_size[1] / 2+30, 100, 50, WHITE, WHITE)
    btn1("INSTRUCTIONS!", (window_size[0] - 100) / 2 - 100, window_size[1] / 2+100, 300, 50, WHITE, WHITE)

    pg.display.update()
    clock.tick(15)