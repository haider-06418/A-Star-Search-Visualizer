import pygame as pg
import pygame

# Setting up Visualizer window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")

# make a new screen with a size of 900x750
screen = pygame.display.set_mode((900, 750))

# show image on screen
screen.blit(pygame.image.load("CS 351 - Aritificial Intelligence.png"), (0, 0))

# show the screen
pygame.display.flip()
