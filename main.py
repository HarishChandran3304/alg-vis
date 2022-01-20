#IMPORTS
import pygame
import pygame_menu
from Algorithms.PathFinding import pathfinding
from Algorithms.Sorting.BubbleSort import bubblesort
from Algorithms.Sorting.MergeSort import mergesort
from Algorithms.Sorting.QuickSort import quicksort


#CONSTANTS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


#SETUP
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("Logo.svg")
pygame.display.set_icon(icon)
pygame.display.set_caption('Alg-Vis')


#HELPER FUNCTIONS
def main_menu():
    mainmenu = pygame_menu.Menu(720, 1280, "Home", theme=pygame_menu.themes.THEME_DARK)
    mainmenu.add.image("Logo.svg", scale=(1.5, 1.5))
    mainmenu.add.label("Alg-Vis", max_char=-1, font_size=100, font_color="white")
    mainmenu.add.vertical_margin(100)
    mainmenu.add.button("Start", select_menu, font_size=75)
    mainmenu.add.vertical_margin(20)
    mainmenu.add.button("Quit", pygame_menu.events.EXIT, font_size=75)
    mainmenu.mainloop(screen)

def select_menu():
    selectmenu = pygame_menu.Menu(720, 1280, "Algorithms", theme=pygame_menu.themes.THEME_DARK)
    selectmenu.add.button("Path-Finding Algorithms", pathfinding_instructions, font_size=50)
    selectmenu.add.vertical_margin(50)
    selectmenu.add.button("Sorting Algorithms", sorting_menu, font_size=50)
    selectmenu.add.vertical_margin(150)
    selectmenu.add.button("Back", main_menu, font_size=50)
    selectmenu.mainloop(screen)
    
def sorting_menu():
    smenu = pygame_menu.Menu(720, 1280, "Sorting Algorithms", theme=pygame_menu.themes.THEME_DARK)
    smenu.add.button("Bubble Sort", launch_bubblesort, font_size=50)
    smenu.add.vertical_margin(50)
    smenu.add.button("Merge Sort", launch_mergesort, font_size=50)
    smenu.add.vertical_margin(100)
    smenu.add.button("Quick Sort", launch_quicksort, font_size=50)
    smenu.add.vertical_margin(150)
    smenu.add.button("Back", select_menu, font_size=50)
    smenu.mainloop(screen)

def pathfinding_instructions():
    instruc = pygame_menu.Menu(720, 1280, "Instructions", theme=pygame_menu.themes.THEME_DARK)
    instruc.add.label("- Left Click to add start and end nodes first\n- Left Click to then add barrier nodes\n- Right Click to remove nodes", max_char=-1, font_size=50, font_color="white")
    instruc.add.vertical_margin(100)
    instruc.add.button("Launch", launch_pathfinding_client, font_size=50)
    instruc.add.vertical_margin(50)
    instruc.add.button("Back", select_menu, font_size=25)
    instruc.mainloop(screen)

def launch_pathfinding_client():
    pathfinding.main(screen, 720)

def launch_bubblesort():
    bubblesort.main()

def launch_mergesort():
    mergesort.main()

def launch_quicksort():
    quicksort.main()


#MAIN LOOP
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        main_menu()


#MAIN CALL
if __name__ == "__main__":
    main()