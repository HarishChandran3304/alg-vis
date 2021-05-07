# importing pygame
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
)

#DEFINES COLOURS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

#DISPLAYING WINDOW
screen = pygame.display.set_mode((900, 600))
  
#CUSTOMISING WINDOW
pygame.display.set_caption('Bubble sort')
  
#STARTING POSITIONS SO THAT EACH BAR IS IN THE CENTER
x_of_bar = 0
y_of_bar = 0
  
# WIDTH OF EACH BAR
width_of_bar = 20
  
#GENERATING RANDOM HEIGHTS FOR EACH BAR
height = []
for i in range (30):
    height.append(random.randint(10, 350))
  
#FUNCTION TO DISPLAY ALL THE BARS FORMED
def show(height):
  
    for i in range(len(height)):
  
        #MAKING A BAR EACH OF HEIGHT DEFINED IN LIST AND WITH A DISTANCE OF 30 PIXELS
        pygame.draw.rect(screen, blue, (x_of_bar + 30 * i, y_of_bar, width_of_bar, height[i]))

running = True
  
#MAKES SURE THE CODE KEEPS RUNNING
while running:
    
    #FLAG DEFINED TO SEE IF CORRECT KEY IS CLICKED BEFORE RUNNING
    flag = False
  
    #GETS INFO OF KEY PRESSED
    keys = pygame.key.get_pressed()
  
    #GETS ALL EVENTS LIKE WHICH KEY IS PRESSED
    for event in pygame.event.get():
        
        #IF A KEY IS PRESSED 
        if event.type == KEYDOWN:
            
            #IF ESCAPE KEY IS PRESSED THEN IT QUITS THE PROGRAM
            if event.key == K_ESCAPE:
                running = False
        
        #IF THE CROSS IS CLICKED IT QUITS IT
        elif event.type == pygame.QUIT:
            running = False
  
    #SPACEBAR IS PRESSED
    if keys[pygame.K_SPACE]:
        #MAKES FLAG TRUE SO THAT CODE CAN START RUNNING
        flag = True
  
    #CHECKS STATUS OF CODE, HAPPENS BEFORE SPACEBAR IS CLICKED
    if flag == False:
  
        
        screen.fill((0, 0, 0))
  
        #SEE THE OBJECTS FORMED
        show(height)
  
        # update the window
        pygame.display.update()
  
    #FLAG IS TRUE, HAPPENS AFTER SPACEBAR IS CLICKED
    else:
  
        #USES BUBBLE SORT
        for i in range(len(height) - 1):
  
            for elem_height in range(len(height) - i - 1):
  
                #CHECKS IF FIRST ELEMENT IS GREATER THAN NEXT ELEMENT 
                if height[elem_height] > height[elem_height + 1]:
  
                    #USING TEMPORARY VARIABLE WE STORE THE HEIGHT AND LATER SWITCH IT
                    temp_height = height[elem_height]
                    height[elem_height] = height[elem_height + 1]
                    height[elem_height + 1] = temp_height
  
                # fill the window with black color
                screen.fill((0, 0, 0))
  
                #MAKES SURE THAT ORIGNAL LIST IS RETAINED BY CALING FUNCTION
                show(height)
  
                #EACH ITERATION IS RUN AFTER A BREAK OF 50 MILLISECONDS
                pygame.time.delay(50)
  
                #CHANGES SHOULD BE REFLECTED
                pygame.display.update()
  
# exiting the main window
pygame.quit()