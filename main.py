#IMPORTS
import pygame
import pygame_menu
from Algorithms.PathFinding.DijkstrasAlgorithm import dijkstra
from Algorithms.PathFinding.AStarSearch import astar
from Algorithms.Sorting.MergeSort import mergesort
from Algorithms.Sorting.BubbleSort import bubblesort


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
    selectmenu.add.button("Path-Finding Algorithms", pathfinding_menu, font_size=50)
    selectmenu.add.vertical_margin(50)
    selectmenu.add.button("Sorting Algorithms", sorting_menu, font_size=50)
    selectmenu.add.vertical_margin(150)
    selectmenu.add.button("Back", main_menu, font_size=50)
    selectmenu.mainloop(screen)

def pathfinding_menu():
    pfmenu = pygame_menu.Menu(720, 1280, "Path-Finding Algorithms", theme=pygame_menu.themes.THEME_DARK)
    pfmenu.add.button("A* Search", foo, font_size=50)
    pfmenu.add.vertical_margin(50)
    pfmenu.add.button("Dijkstra\'s Algorithm", foo, font_size=50)
    pfmenu.add.vertical_margin(150)
    pfmenu.add.button("Back", select_menu, font_size=50)
    pfmenu.mainloop(screen)
    
def sorting_menu():
    smenu = pygame_menu.Menu(720, 1280, "Sorting Algorithms", theme=pygame_menu.themes.THEME_DARK)
    smenu.add.button("Bubble Sort", foo, font_size=50)
    smenu.add.vertical_margin(50)
    smenu.add.button("Merge Sort", foo, font_size=50)
    smenu.add.vertical_margin(150)
    smenu.add.button("Back", select_menu, font_size=50)
    smenu.mainloop(screen)

def foo():
    pass


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
