#IMPORTS
import pygame
import random
import csv
from tkinter import *
from tkinter import filedialog
from time import time


#CONSTANTS
DELAY = 50
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
THEMEGREY = (40, 41, 35) #Theme primary
THEMEPURPLE = (71, 63, 255) #Theme secondary
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,100,255)
ORANGE = (255, 165, 0)
STATERED = (198, 10, 9) #Status red colour
STATEGREEN = (142, 200, 19) #Status green colour
STATEYELLOW = (255, 218, 66) #Status yellow colour


#VARIABLES
elapsed = ""
og_array = [0]*25
bar_colours = [None]*25
state_clr = STATEYELLOW
state = "Ready to visualize!"


#SETUP
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("Logo.svg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Sorting Visualizer")

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_SPACE, K_r)

pygame.font.init()
font = pygame.font.SysFont('verdana', 20)
small_font = pygame.font.SysFont('verdana', 20)


#CLASSES
class Button():
    def __init__(self, colour, x, y, width, height, text="", font="verdana", fontsize=25, fontcolour=(0,0,0)):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.fontsize = fontsize
        self.fontcolour = fontcolour
    
    #CLASS METHODS
    def draw(self, surface, outlinecolour=None):
        '''
        Draws the button on the screen
        '''
        if outlinecolour:
            pygame.draw.rect(surface, outlinecolour, (self.x-2,self.y-2,self.width+4,self.height+4), 0)
            
        pygame.draw.rect(surface, self.colour, (self.x,self.y,self.width,self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont(self.font, self.fontsize)
            text = font.render(self.text, 1, self.fontcolour)
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isclicked(self, pos):
        '''
        Returns True if the x, y coordinates entered happens to fall on the button
        '''
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#BUTTON CLASS INSTANCES
vis_bubble_btn = Button(THEMEPURPLE, 10, 10, 200, 50, "Bubble Sort") #Visualize Bubble Sort Button
vis_merge_btn = Button(THEMEPURPLE, 10, 70, 200, 50, "Merge Sort") #Visualize Merge Sort Button
vis_quick_btn = Button(THEMEPURPLE, 10, 130, 200, 50, "Quick Sort") #Visualize Quick Sort Button
reset_btn = Button(THEMEPURPLE, SCREEN_WIDTH-210, 10, 200, 50, "Reset")  #Reset Button
randomize_btn = Button(THEMEPURPLE, SCREEN_WIDTH-210, 70, 200, 50, "Randomize") #Randomize Button
load_btn = Button(THEMEPURPLE, SCREEN_WIDTH-210, 130, 200, 50, "Load") #Load Array Button


#HELPER FUNCTIONS
def generate_random_array():
    '''
    Generates a random array
    '''
    global og_array
    for i in range(len(og_array)):
        og_array[i] = random.randrange(1, 90)
        bar_colours[i] = BLUE
    save_og(og_array)
    
    return og_array

def display_status(surface, state, state_clr, font="verdana", fontsize=50, fontcolour=WHITE):
    '''
    Displays the status of the algorithm
    '''
    font1 = pygame.font.SysFont(font, fontsize)
    text1 = font1.render("Status: ", 1, fontcolour) 
    text2 = font1.render(state, 1, state_clr)
    surface.blit(text1, (230, 20))
    surface.blit(text2, (230+text1.get_width(), 20))

def display_timer(surface, font="verdana", fontsize=30, fontcolour=WHITE):
    '''
    Displays the time elapsed for the algorithm
    '''
    global elapsed
    
    font = pygame.font.SysFont(font, fontsize)
    text = font.render(f'Time Elapsed: {elapsed}', 1, fontcolour)
    surface.blit(text, (230, 100))

def display_ui(surface):
    '''
    Displays all UI components
    '''
    global elapsed, state, state_clr
    display_status(surface, state, state_clr)
    display_timer(surface, elapsed)
    vis_bubble_btn.draw(screen, THEMEPURPLE)
    vis_merge_btn.draw(screen, THEMEPURPLE)
    vis_quick_btn.draw(screen, THEMEPURPLE)
    reset_btn.draw(screen, THEMEPURPLE)
    randomize_btn.draw(screen, THEMEPURPLE)
    load_btn.draw(screen, THEMEPURPLE)
    pygame.display.update()

def display_bars(arr):
    '''
    Displays the elements of the array as bars where the height of the bar corresponds the value of the array
    '''
    screen.fill(BLACK)
    
    dist_buffer = 5
    bar_width = (SCREEN_WIDTH-50-len(arr)*dist_buffer)//len(arr)
    bar_dist = dist_buffer+bar_width
    bar_scale = 5
    
    for i in range(len(arr)):
        pygame.draw.line(screen, bar_colours[i], ((bar_dist*i)+50, 700), ((bar_dist*i)+50, 700-arr[i]*bar_scale), bar_width)
        txt = small_font.render(str(arr[i]), 1, WHITE)
        screen.blit(txt, ((bar_dist * i)+40, 700-arr[i]*bar_scale-25))

def refresh(surface, arr):
    '''
    Refreshes the screen and redraws all components
    '''
    
    display_bars(arr)
    display_ui(surface)
    pygame.time.delay(DELAY)
    pygame.display.update()

def save_og(arr):
    '''
    Saves each new array in a csv file so that it can be retrieved back on reset
    '''
    with open("./Algorithms/Sorting/saved/OgArray.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(arr)

def load_og():
    '''
    Loads the saved array from a csv file on reset
    '''
    with open("./Algorithms/Sorting/saved/OgArray.csv", "r") as file:
        arr = list(csv.reader(file))[0]
        for i in range(len(arr)):
            arr[i] = int(arr[i])
    
    return arr

def load_csv():
    '''
    Load an array from an existing csv file on the computer
    '''
    global og_array, bar_colours
    
    tkwin = Tk()
    tkwin.withdraw()
    filename = filedialog.askopenfilename(initialdir="./Algorithms/Sorting/saved/", title="Select file", filetypes=(("CSV Files","*.csv"),("All","*.*")))
    tkwin.destroy()
    
    if filename is None or filename == "":
        return og_array

    with open(filename, "r") as file:
        og_array = list(csv.reader(file))[0]
        for i in range(len(og_array)):
            og_array[i] = int(og_array[i])
    
    for i in range(len(og_array)):
        bar_colours[i] = BLUE
    
    save_og(og_array)
    
    return og_array

def handle_left_click(surface, pos, arr):
    '''
    Handles all button clicks
    '''
    global state, state_clr, elapsed
    
    if vis_bubble_btn.isclicked(pos):
        state_clr = STATERED
        state = "Visualizing Bubble Sort..."
        elapsed = ""
        start = time()
        arr = bubble_sort(arr)
        for i in range(len(arr)):
            bar_colours[i] = BLUE
        end = time()
        elapsed = elapsed = f'{round(end-start, 2)} sec'
        state_clr = STATEGREEN
        state = "Bubble Sort Complete!"
    
    elif vis_merge_btn.isclicked(pos):
        state_clr = STATERED
        state = "Visualizing Merge Sort..."
        elapsed = ""
        start = time()
        arr = merge_sort(arr, 0, len(arr)-1)
        for i in range(len(arr)):
            bar_colours[i] = BLUE
        end = time()
        elapsed = elapsed = f'{round(end-start, 2)} sec'
        state_clr = STATEGREEN
        state = "Merge Sort Complete!"
    
    elif vis_quick_btn.isclicked(pos):
        state_clr = STATERED
        state = "Visualizing Quick Sort..."
        elapsed = ""
        start = time()
        arr = quick_sort(arr, 0, len(arr)-1)
        for i in range(len(arr)):
            bar_colours[i] = BLUE
        end = time()
        elapsed = elapsed = f'{round(end-start, 2)} sec'
        state_clr = STATEGREEN
        state = "Quick Sort Complete!"
    
    elif randomize_btn.isclicked(pos):
        arr = generate_random_array()
        elapsed = ""
        state_clr = STATEYELLOW
        state = "Ready to visualize!"
    
    elif reset_btn.isclicked(pos):
        arr = load_og()
        elapsed = ""
        state_clr = STATEYELLOW
        state = "Ready to visualize!"
    
    elif load_btn.isclicked(pos):
        arr = load_csv()
        elapsed = ""
        state_clr = STATEYELLOW
        state = "Ready to visualize!"
    
    return arr


#ALGORITHM IMPLEMENTATIONS
def bubble_sort(arr):
    '''
    Bubble sort algorithm implementation
    '''
    for i in range(len(arr)-1):
        for elem_height in range(len(arr) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

            #Colour of the 2 bars changes to red during comparison
            bar_colours[elem_height] = RED
            bar_colours[elem_height+1] = RED

            #Swaping
            if arr[elem_height] > arr[elem_height + 1]:
                
                #Colour of the 2 bars changes to green while swapping
                bar_colours[elem_height] = GREEN
                bar_colours[elem_height+1] = GREEN
                
                #Swaping using temporary variable
                temp_height = arr[elem_height]
                arr[elem_height] = arr[elem_height + 1]
                arr[elem_height + 1] = temp_height
                refresh(screen, arr)

            #Colour changes to orange indicating that they have been traversed through
            bar_colours[elem_height] = ORANGE
            bar_colours[elem_height+1] = ORANGE
        
    return arr

def merge(arr, x1, y1, x2, y2):
    '''
    Mechanism used in merge sort to merge two sorted arrays
    '''
    #Red signifies that the two bars are being compared
    #Green signifies that the bar has just been moved to temporary correct position (recent)
    #Orange signifies that the bar is in correct place (for current iteration)
    
    i = x1
    j = x2
    temp =[]
    pygame.event.pump()
    while i<= y1 and j<= y2:
        bar_colours[i]= RED
        bar_colours[j]= RED
        refresh(screen, arr)
        if arr[i] < arr[j]:
            temp.append(arr[i]) #If the height is smaller compared to next then it is added to a variable called temp
            i+= 1

        else:
            temp.append(arr[j]) #If the one on the right was right was smaller then it gets added to the variable temp
            j+= 1

    while i<= y1:
        bar_colours[i]= RED
        refresh(screen, arr)
        temp.append(arr[i])
        i+= 1

    while j<= y2:
        bar_colours[j]= RED
        refresh(screen, arr)
        temp.append(arr[j])
        j+= 1

    j = 0

    for i in range(x1, y2 + 1):
        pygame.event.pump()
        arr[i]= temp[j]
        j+= 1
        bar_colours[i]= GREEN
        refresh(screen, arr)
        if y2-x1 == len(arr)-2:
            bar_colours[i]= BLUE
        else:
            bar_colours[i]= ORANGE

def merge_sort(arr, l, r):
    '''
    Merge sort algorithm implementation
    '''
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

    mid =(l + r)//2

    if l<r:
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, mid + 1, r)
    
    return arr

def partition(arr, lower, higher):
    '''
    Mechanism used in quick sort to partition the array
    '''
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

    pygame.event.pump()
    pivot = arr[higher]
    bar_colours[higher]= GREEN #Colour changes to green to indicate that the pivot is being compared
    i = lower - 1
    for j in range(lower, higher):
        bar_colours[j] = RED #Colour of the 2 bars changes to red during comparison
        refresh(screen, arr)
        bar_colours[higher] = GREEN
        bar_colours[j] = ORANGE
        bar_colours[i] = ORANGE

        if arr[j] < pivot:
            i += 1
            bar_colours[i]= RED
            arr[i], arr[j]= arr[j], arr[i]

    refresh(screen, arr)
    bar_colours[i]= ORANGE
    bar_colours[higher]= ORANGE
    arr[i + 1], arr[higher] = arr[higher], arr[i + 1]
    
    return i + 1

def quick_sort(arr, l, r):
    '''
    Implementation of quick sort algorithm
    '''
    if l<r:
        pi = partition(arr, l, r)
        quick_sort(arr, l, pi-1)
        refresh(screen, arr)
        for i in range(0, pi + 1):
            bar_colours[i]= BLUE #Colour changes to blue once the pivot is in the correct position
        quick_sort(arr, pi + 1, r)
        
    return arr


#MAIN LOOP
def main(surface):
    '''
    Main loop of the program
    '''
    running = True
    
    og_array = generate_random_array()
    arr = og_array
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if pygame.mouse.get_pressed()[0]: #Left mouse button
                pos = pygame.mouse.get_pos()
                arr = handle_left_click(surface, pos, arr)
                refresh(surface, arr)

        display_bars(arr)
        display_ui(surface)
        pygame.display.update()

    pygame.quit()


#MAIN CALL
if __name__ == '__main__':
    main(screen)