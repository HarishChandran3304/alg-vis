# importing pygame
import pygame
import random

#DEFINES COLOURS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

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
  
pygame.init()
  
# setting window size
screen = pygame.display.set_mode((500, 400))
  
# setting title to the window
pygame.display.set_caption('Bubble sort')
  
# initial position
x = 0
y = 0
  
# width of each bar
width = 20
  
# height of each bar (data to be sorted)
height = []
for height_of_each_element in range(14):
    height.append(random.randint(20, 350))
  
running = True
  
# method to show the list of height
def show(height):
  
    # loop to iterate each item of list
    for i in range(len(height)):
  
        # drawing each bar with respective gap
        pygame.draw.rect(screen, blue, (x + 30 * i, y, width, height[i]))
  
#KEEPS CODE RUNNING
while running:
    #BLACK COLOUR BG
    screen.fill(black)
    
    flag = False
  
    # time delay
    pygame.time.delay(10)
  
    # getting keys pressed
    keys = pygame.key.get_pressed()
  
    # iterating events
    for event in pygame.event.get():
        
        #IF A KEY IS PRESSED 
        if event.type == KEYDOWN:
            
            #IF ESCAPE KEY IS PRESSED THEN IT QUITS THE PROGRAM
            if event.key == K_ESCAPE:
                running = False
        
        #IF THE CROSS IS CLICKED IT QUITS IT
        elif event.type == pygame.QUIT:
            running = False
  
    #IF SPACEBAR IS CLICKED IT STARTS TO EXECUTE
    if keys[pygame.K_SPACE]:
        # make flag flag to true
        flag = True
  
    # IF FLAG IS FALSE
    if flag == False:
  
        # BLACK COULOUR BACKGROUND
        screen.fill(black)
  
        # call the height method to show the list items
        show(height)
  
        # UPDATE THE SCREEN
        pygame.display.update()
  
    #IF FLAG IS TRUE
    else:
  
        #START USING BUBBLE SORT
        for i in range(len(height) - 1):
  
            # after this iteration max element will come at last
            for j in range(len(height) - i - 1):
  
                # starting is greater then next element
                if height[j] > height[j + 1]:
  
                    #SAVE AND SWAP THE VARIABLE
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t
  
                #CALL LIST TO SHOW DISPLAYED ITEMS
                show(height)
  
                # TIME DELAY
                pygame.time.delay(50)
  
                # DISPLAY UPDATED
                pygame.display.update()
  
# exiting the main window
pygame.quit()