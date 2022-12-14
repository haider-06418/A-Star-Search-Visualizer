import pygame as pg
import pygame
# import main.py as main

# Setting up Visualizer window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A-Star Search Algorithm Visualizer")

# Colors to be used in project
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (102, 204, 255)
BLUE = (0, 100, 230)
DARK_BLUE = (0, 0, 100)
DARK_GREEN = (0, 200, 0)
GREY = (204, 204, 204)
LEFT = 1
RIGHT = 3





def text_objects(text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

window_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
clock = pg.time.Clock()
# pygame.init()
pygame.font.init()

def showInstructions():
    pg.display.set_caption("A-Star Search Algorithm Visualizer")
    MAIN_WINDOW.fill(GREY)
    large_text = pg.font.SysFont("comicsansms", 115)
    text_surf, text_rect = text_objects("A-Star Search Algorithm Visualizer", large_text)
    text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    MAIN_WINDOW.blit(text_surf, text_rect)
    button("Start", 150, 450, 100, 50, GREEN, DARK_GREEN, game_intro)
    button("Quit", 550, 450, 100, 50, RED, DARK_RED, quitgame)
    pg.display.update()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(MAIN_WINDOW, ac, (x, y, w, h))
        pass

        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(MAIN_WINDOW, ic, (x, y, w, h))

    small_text = pg.font.SysFont("comicsansms", 25)
    text_surf, text_rect = text_objects(msg, small_text)
    
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    MAIN_WINDOW.blit(text_surf, text_rect)


intro = True
while intro:
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    MAIN_WINDOW.fill(WHITE)
    text_font_1 = pg.font.Font('freesansbold.ttf', 45) 
    text_font_2 = pg.font.Font('freesansbold.ttf', 35) 
    text_font_3 = pg.font.Font('freesansbold.ttf', 25) 

    # text_surf, text_rect = text_objects("A-Star Search Algorithm Visualizer", text_font_1)
    # text_rect.center = ((window_size[0] / 2), (window_size[1] / 4))
    # text_rect.center = ((window_size[0] // 2), (window_size[1] // 2))
    # MAIN_WINDOW.blit(text_surf, text_rect)
    

    # # create a rectangular object for the
    # # text surface object
    # textRect = text.get_rect()

    # # set the center of the rectangular object.
    # textRect.center = (X // 2, Y // 2)

    # display_surface.blit(text, textRect)

    # here
    # text_surf_2, text_rect_2 = text_objects("CS 351: Artificial Intelligence", text_font_2)
    # text_rect_2.center = ((window_size[0] - 300)// 2, (window_size[1] - 300) // 2)
    # MAIN_WINDOW.blit(text_surf_2, text_rect_2)

    # text_surf_3, text_rect_3 = text_objects("Fall 2022", text_font_2)
    # text_rect_3.center = ((window_size[0] / 2), (window_size[1] / 4))
    # MAIN_WINDOW.blit(text_surf_3, text_rect_3)

    # text_surf_4, text_rect_4 = text_objects("Semester Project", text_font_2)
    # text_rect_4.center = ((window_size[0] / 2), (window_size[1] / 4))
    # MAIN_WINDOW.blit(text_surf_4, text_rect_4)

    # # A* Search Algorithm Visualization done in lines 63-66

    # text_surf_5, text_rect_5 = text_objects("Group Members:", text_font_2)
    # text_rect_5.center = ((window_size[0] / 2), (window_size[1] / 4))
    # MAIN_WINDOW.blit(text_surf_5, text_rect_5)

    # text_surf_6, text_rect_6 = text_objects("Mohammed Haider Abbas, Asad Raza, Ali Zain Sardar", text_font_2)
    # text_rect_6.center = ((window_size[0] / 2), (window_size[1] / 4))
    # MAIN_WINDOW.blit(text_surf_6, text_rect_6)
    # # till here


    
    # show image on screen
    MAIN_WINDOW.blit(pygame.image.load("Code/img.png"), ((0), (0)))

    # button("GO!", (window_size[0] - 100) / 2, window_size[1] / 2,
    #             100, 50, BLUE, GREEN, 'nextscreen')

    # make a button with no hover color
    button("GO!", (window_size[0] - 100) / 2, window_size[1] / 2+30,
                        100, 50, WHITE, WHITE, 'nextscreen')

    # make an instructions button which will be used to show instructions
    button("INSTRIUCTIONS!", (window_size[0] - 100) / 2 - 100, window_size[1] / 2+100,
                        300, 50, WHITE, WHITE, "showInstructions()")
    



    pg.display.update()
    clock.tick(15) 