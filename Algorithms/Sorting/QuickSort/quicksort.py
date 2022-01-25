# IMPORTING PYGAME
import pygame
import random
from datetime import datetime

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
start_time = datetime.now()
#DEFINING FONTS TO DISPLAY TEXT
font = pygame.font.SysFont('times new roman', 20)
small_font = pygame.font.SysFont('times new roman', 12)

#DISPLAYING WINDOW
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Quick sort')

#USED TO DISPLAY TEXT ON THE SCREEN
def display_message():
    #TEXT MESSAGE
    txt = font.render('"SPACE" TO SORT', 1, white)
    #POSITION OF TEXT
    screen.blit(txt, (20, 20))
    txt = font.render('"R" FOR NEW ARRAY', 1, white)
    screen.blit(txt, (20, 40))
    txt = font.render('ALGORITHM USED: "QUICK SORT"', 1, white)
    screen.blit(txt, (500, 30))

#ARRAY OF LENGTH 100 IS FORMED SIGNIFYING 100 BARS
height =[0]*70
all_colours =[green]*70
clr_ind = 0
colours = [orange, red, green, blue]

#FUNCTION REQUIRED TO CALL IT EACH TIME "R" IS PRESSED AND GENERATE AND A NEW ARRAY
def making_bars():
    #LOOP TO RANDOMLY GENERATE THE HEIGHT OF EACH BAR
    for i in range(1, 70):
        #SETS THE DEFAULT COULOUR OF EACH BAR TO BLUE
        all_colours[i] = blue
        height[i] = random.randrange(1, 90)

#MAKES THE BARS SO THAT THEY CAN BE USED LATER ON
making_bars()

#FUNCTION TO DISPLAY THE BARS ON THE SCREEN
def display_bars():
    screen.fill(black)       
    display_message()
    #DETERMINES THE WIDTH OF EACH BAR
    width_of_bar =(width-100)//100
    #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
    distance_of_each_bar = 900 / 50
    #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
    boundry_of_bars = 500 / 100
    # Drawing the array values as lines
    for i in range(1, 70):
        pygame.draw.line(screen, all_colours[i], (distance_of_each_bar * i-3, 100), (distance_of_each_bar * i-3, height[i]*boundry_of_bars + 100), width_of_bar)
        txt = small_font.render(str(height[i]), 1, white)
        # font.render()
        #POSITION OF TEXT
        screen.blit(txt, (distance_of_each_bar * i-5, height[i]*boundry_of_bars + 105))
#AFTER COMPARING TWO LINES THIS IS USED
def refresh():
    display_bars()
    pygame.time.delay(25)
    pygame.display.update()
	
# RECURSIVE FUNCTION TO KEEP EXECUTING TILL SORTED
def quicksort(height, l, r):
	if l<r:
		pi = partition(height, l, r)
		quicksort(height, l, pi-1)
		refresh()
		for i in range(0, pi + 1):
            # COLOUR CHANGES TO BLUE ONCE IN FINAL POSITION
			all_colours[i]= colours[3]	
		quicksort(height, pi + 1, r)
		
# TO PERFORM SORTING
def partition(height, lower, higher):
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

    pygame.event.pump()
    pivot = height[higher]
    # COLOUR TURNS GREEN
    all_colours[higher]= colours[2]
    i = lower - 1
    for j in range(lower, higher):
		# COLOURS TURN RED WHILE BEING COMPARED
        all_colours[j] = colours[1]
        refresh()
        all_colours[higher] = colours[2]
        all_colours[j] = colours[0]
        all_colours[i] = colours[0]

        if height[j] < pivot:
            i += 1
            all_colours[i]= colours[1]
            height[i], height[j]= height[j], height[i]

    refresh()
    all_colours[i]= colours[0]
    all_colours[higher]= colours[0]
    height[i + 1], height[higher] = height[higher], height[i + 1]
	
    return i + 1
	
def main():
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quicksort(height, 1, len(height)-1)	
                elif event.key == pygame.K_r:
                    making_bars()
                elif event.key == K_ESCAPE:
                    running = False

        display_bars()
        pygame.display.update()
	
    pygame.quit()

if __name__ == '__main__':
    main()
