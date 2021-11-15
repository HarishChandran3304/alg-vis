choice = input('Enter choice (p, c or m) ').lower()
from csv import *
temp = []
with open('StudentMarks.csv', 'r') as file:
    reader_object = reader(file)
    for row in reader_object:
        temp.append(row)
    content = []
    for x in temp:
        if x != []:
            content.append(x)

#IMPORTING PYGAME
import pygame
import random

#MAKES IT EASY TO TRACK KEYS PRESSED
from pygame.locals import (
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

#**********************************************************************************************************************************#
pygame.font.init()

#OTHER VARIABLES
# Window size
width = 1250
length = 600
#DEFINING FONTS TO DISPLAY TEXT
font = pygame.font.SysFont('times new roman', 20)

#DISPLAYING WINDOW
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Bubble sort')

#USED TO DISPLAY TEXT ON THE SCREEN
def display_message():
    #TEXT MESSAGE
    txt = font.render('"SPACE" TO SORT', 1, white)
    #POSITION OF TEXT
    screen.blit(txt, (20, 20))
    # txt2 = font.render('"R" FOR NEW ARRAY', 1, white)
    # screen.blit(txt2, (20, 40))
    txt = font.render('ALGORITHM USED: "BUBBLE SORT"', 1, white)
    screen.blit(txt, (500, 30))


#ARRAY OF LENGTH 100 IS FORMED SIGNIFYING 100 BARS
number_of_items = len(content)
names = [x[0] for x in content]
phy_marks = [int(x[1]) for x in content]
chem_marks = [int(x[2]) for x in content]
math_marks = [int(x[3]) for x in content]

phy_colour = [white]*number_of_items
chem_colour = [red]*number_of_items
math_colour = [white]*number_of_items

height =[0]*70
all_colours =[green]*70
clr_ind = 0
colours = [orange, red, green, blue]

#FUNCTION REQUIRED TO CALL IT EACH TIME "R" IS PRESSED AND GENERATE AND A NEW ARRAY
'''def making_bars():
        #LOOP TO RANDOMLY GENERATE THE HEIGHT OF EACH BAR
        for i in range(1, 70):
            #SETS THE DEFAULT COULOUR OF EACH BAR TO BLUE
            all_colours[i] = blue
            height[i] = random.randrange(1, 90)

#MAKES THE BARS SO THAT THEY CAN BE USED LATER ON
making_bars()
'''

#FUNCTION TO DISPLAY THE BARS ON THE SCREEN
def display_bars(number_of_items=number_of_items):
    screen.fill(black)
    display_message()
    #DETERMINES THE WIDTH OF EACH BAR
    width_of_bar =(width-100)//100
    #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
    distance_of_each_bar = 900 / 50
    #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
    boundry_of_bars = 500 / 100
    # Drawing the array values as lines
    for i in range(number_of_items):
        pygame.draw.line(screen, phy_colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, phy_marks[i]*boundry_of_bars + 100), width_of_bar)

#AFTER COMPARING TWO LINES THIS IS USED
def refresh():
    display_bars()
    pygame.time.delay(2)
    pygame.display.update()

def sort():
    for i in range(len(phy_marks)-1):
        for elem_height in range(len(phy_marks) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

            #COLOUR CHANGES TO RED WHILE COMPARING
            phy_colour[elem_height] = colours[1]
            phy_colour[elem_height+1] = colours[1]
            pygame.time.delay(25)

            #IF THE ELEMENT ON THE LEFT ON THE LEFT IS GREATER IT GETS SWITCHED TO THE RIGHT
            if phy_marks[elem_height] > phy_marks[elem_height + 1]:
                
                #COLOUR CHANGES TO GREEN WHILE SWITCHING
                phy_colour[elem_height] = colours[2]
                phy_colour[elem_height+1] = colours[2]
                #USING TEMPORARY VARIABLE WE STORE THE HEIGHT AND LATER SWITCH IT
                temp_height = phy_marks[elem_height]
                phy_marks[elem_height] = phy_marks[elem_height + 1]
                phy_marks[elem_height + 1] = temp_height
                refresh()

            #COLOURS SET TO ORANGE INDICATING THEY HAVE BEEN TRAVERSED THROUGH
            phy_colour[elem_height] = colours[0]
            phy_colour[elem_height+1] = colours[0]

    for i in range(len(phy_marks)):
        phy_colour[i] = colours[-1]
        
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    sort()
            
                elif event.key == K_ESCAPE:
                    running = False

        display_bars()
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()