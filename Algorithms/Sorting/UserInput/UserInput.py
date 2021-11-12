#IMPORTING PYGAME
import pygame

#MAKES IT EASY TO TRACK KEYS PRESSED
from pygame.locals import (
    K_BACKSPACE,
    K_KP_ENTER,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_r  
)

#DEFINES COLOURS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,100,255)
orange = (255, 165, 0)

pygame.font.init()

#OTHER VARIABLES
# Window size
width = 1250
length = 600
#DEFINING FONTS TO DISPLAY TEXT
display_font = pygame.font.SysFont('times new roman', 20)
user_font = pygame.font.SysFont('times new roman', 24)
user_text = ''

colour_active = green
colour_passive = white
colour = colour_passive
# timer_temp = 0

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Taking in user input')

input_rect = pygame.Rect(200, 200, 140, 200)

active = False
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    if active:
        colour = colour_active
    else:
        colour = colour_passive

    screen.fill(black)
    pygame.draw.rect(screen, colour, input_rect)

    text_surface = user_font.render(user_text, True, white)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()

print(user_text)
pygame.quit()
