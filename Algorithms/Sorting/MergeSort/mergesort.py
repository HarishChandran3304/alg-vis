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
    K_SPACE
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
font = pygame.font.SysFont('times new roman', 20)


#DISPLAYING WINDOW
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Merge sort')


#USED TO DISPLAY TEXT ON THE SCREEN
def display_message():

    #TEXT MESSAGE
    txt1 = font.render('"SPACE" TO SORT', 1, white)
    #POSITION OF TEXT
    screen.blit(txt1, (20, 20))
    
    txt2 = font.render('"R" FOR NEW ARRAY', 1, white)
    screen.blit(txt2, (20, 40))

    txt3 = font.render('ALGORITHM USED: "MERGE SORT"', 1, white)
    screen.blit(txt3, (500, 30))


#ARRAY OF LENGTH 100 IS FORMED SIGNIFYING 100 BARS
height =[0]*70
all_colours =[green]*70
clr_ind = 0
colours =[orange, red, green, blue]

#FUNCTION REQUIRED TO CALL IT EACH TIME "R" IS PRESSED AND GENERATE AND A NEW ARRAY
def making_bars():

    #LOOP TO RANDOMLY GENERATE THE HEIGHT OF EACH BAR
    for i in range(1, 70):
        
        #SETS THE DEFAULT COULOUR OF EACH BAR TO BLUE
        all_colours[i] = colours[-1]
        height[i] = random.randrange(1, 90)


#MAKES THE BARS SO THAT THEY CAN BE USED LATER ON
making_bars()


#FUNCTION TO DISPLAY THE BARS ON THE SCREEN
def displaying_bars():

    #DETERMINES THE WIDTH OF EACH BAR
    width_of_bar =(width-100)//100

    #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
    distance_of_each_bar = 900 / 50

    #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
    boundry_of_bars = 500 / 100
      
    #DISPLAYS THE BARS ON THE SCREEN
    for i in range(1, 70):
        pygame.draw.line(screen, all_colours[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, height[i]*boundry_of_bars + 100), width_of_bar)


#AFTER COMPARING TWO LINES THIS IS USED
def refresh():

    screen.fill(black)
    display_message()
    displaying_bars()
    pygame.time.delay(25)
    pygame.display.update()
    


def merge(height, x1, y1, x2, y2):
    i = x1
    j = x2
    temp =[]

    pygame.event.pump()

    #RED SIGNIFIES THAT THE TWO BARS ARE BEING COMPARED
    #GREEN SIGNIFIES THAT THE BAR HAS JUST BEEN MOVED TO TEMPORARY CORRECT POSITION (RECENT)
    #ORANGE SIGNIFIES THAT THE BAR IS IN CORRECT PLACE (FOR CURRENT ITERATION)
    while i<= y1 and j<= y2:

        all_colours[i]= colours[1]
        all_colours[j]= colours[1]

        refresh()

        if height[i] < height[j]:
            
            #IF THE HEIGHT IS SMALLER COMPARED TO NEXT THEN IT IS ADDED TO A VARIABLE CALLED TEMP
            #TEMP STANDS FOR TEMPORARY

            temp.append(height[i])
            i+= 1

        else:
            
            #IF THE ONE ON THE RIGHT WAS RIGHT WAS SMALLER THEN IT GETS ADDED TO THE VARIABLE TEMP
            temp.append(height[j])
            j+= 1

    while i<= y1:

        all_colours[i]= colours[1]

        refresh()

        temp.append(height[i])
        i+= 1

    while j<= y2:

        all_colours[j]= colours[1]

        refresh()

        temp.append(height[j])
        j+= 1

    j = 0

    for i in range(x1, y2 + 1):

        pygame.event.pump()

        height[i]= temp[j]
        j+= 1

        all_colours[i]= colours[2]

        refresh()

        if y2-x1 == len(height)-2:

            all_colours[i]= colours[3]
        
        else:

            all_colours[i]= colours[0]

#ALGORITHIM FOR MERGE SORT
def mergesort(height, l, r):
    
    for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == K_ESCAPE:

                        pygame.quit()

    mid =(l + r)//2

    if l<r:

        mergesort(height, l, mid)
        mergesort(height, mid + 1, r)
        merge(height, l, mid, mid + 1, r)
  


def main():

    running = True 
    # Infinite loop to keep the window open
    while running:
        # background
        screen.fill(black)
        
        #GETS ALL EVENTS LIKE WHICH KEY IS PRESSED
        for event in pygame.event.get():

            # If we click Close button in window
            if event.type == pygame.QUIT:
                running = False

            #IF A KEY IS PRESSED 
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    making_bars() 

                elif event.key == K_SPACE:
                    mergesort(height, 1, len(height)-1)
                
                #IF ESC KEY IS PRESSED IT QUITS THE PROGRAM
                elif event.key == K_ESCAPE:
                    running = False
        
        display_message()
        displaying_bars()

        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()