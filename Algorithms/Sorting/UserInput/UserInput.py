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
name_text = ''
phy_text = ''
chem_text = ''
math_text = ''

colour = white

# timer_temp = 0
active = False

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Taking in user input')

name_input = pygame.Rect(800, 150, 140, 30)
phy_input = pygame.Rect(800, 250, 140, 30)
chem_input = pygame.Rect(800, 350, 140, 30)
math_input = pygame.Rect(800, 450, 140, 30)

def displaytext():
    global name_text, phy_text, chem_text, math_text, name_input, phy_input, chem_input, math_input
    screen.fill(black)
    
    pygame.draw.rect(screen, colour, name_input)
    text_surface = user_font.render(name_text, True, black)
    screen.blit(text_surface, (name_input.x+5, name_input.y+5))
    # MAKES SURE TEXT IS ALWAYS INSIDE BOX
    name_input.w = max(100, text_surface.get_width()+10)

    pygame.draw.rect(screen, colour, phy_input)
    text_surface = user_font.render(phy_text, True, black)
    screen.blit(text_surface, (phy_input.x+5, phy_input.y+5))
    # MAKES SURE TEXT IS ALWAYS INSIDE BOX
    phy_input.w = max(100, text_surface.get_width()+10)

    pygame.draw.rect(screen, colour, chem_input)
    text_surface = user_font.render(chem_text, True, black)
    screen.blit(text_surface, (chem_input.x+5, chem_input.y+5))
    # MAKES SURE TEXT IS ALWAYS INSIDE BOX
    chem_input.w = max(100, text_surface.get_width()+10)

    pygame.draw.rect(screen, colour, math_input)
    text_surface = user_font.render(math_text, True, black)
    screen.blit(text_surface, (math_input.x+5, math_input.y+5))
    # MAKES SURE TEXT IS ALWAYS INSIDE BOX
    math_input.w = max(100, text_surface.get_width()+10)

    txt = display_font.render('Enter name of student', 1, white)
    screen.blit(txt, (400, 150))
    txt = display_font.render('Enter Physics marks', 1, white)
    screen.blit(txt, (400, 250))
    txt = display_font.render('Enter Chem marks', 1, white)
    screen.blit(txt, (400, 350))
    txt = display_font.render('Enter Math marks', 1, white)
    screen.blit(txt, (400, 450))
    
    pygame.display.flip()

def main():
    global name_text, phy_text, chem_text, math_text, name_input, phy_input, chem_input, math_input

    name_active = False
    phy_active = False
    chem_active = False
    math_active = False
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # IF THE NAME_INPUT GETS FOCUS
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name_input.collidepoint(event.pos):
                    name_active = True
                    phy_active = False
                    chem_active = False
                    math_active = False

            # IF THE PHY_INPUT GETS FOCUS
                if phy_input.collidepoint(event.pos):
                    name_active = False
                    phy_active = True
                    chem_active = False
                    math_active = False

            # IF THE CHEM_INPUT GETS FOCUS
                if chem_input.collidepoint(event.pos):
                    name_active = False
                    phy_active = False
                    chem_active = True
                    math_active = False
            
             # IF THE CHEM_INPUT GETS FOCUS
                if math_input.collidepoint(event.pos):
                    name_active = False
                    phy_active = False
                    chem_active = False
                    math_active = True

            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if name_active == True:
                    if event.key == K_BACKSPACE:
                        name_text = name_text[:-1]
                    else:
                        name_text += event.unicode 

                if phy_active == True:
                    if event.key == K_BACKSPACE:
                        phy_text = phy_text[:-1]
                    else:
                        phy_text += event.unicode 
                
                if chem_active == True:
                    if event.key == K_BACKSPACE:
                        chem_text = chem_text[:-1]
                    else:
                        chem_text += event.unicode 

                if math_active == True:
                    if event.key == K_BACKSPACE:
                        math_text = math_text[:-1]
                    else:
                        math_text += event.unicode  
        
        displaytext()

    print([name_text, phy_text.strip(), chem_text.strip(), math_text])
    pygame.quit()

if __name__ == '__main__':
    main()