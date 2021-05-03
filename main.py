#IMPORTS
import pygame
import pygame_menu
from Algorithms.PathFinding.DijkstrasAlgorithm import dijkstra
from Algorithms.PathFinding.AStarSearch import astar
from Algorithms.Sorting.BinarySort import binarysort
from Algorithms.Sorting.BubbleSort import bubblesort


#CONSTANTS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


#SETUP
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#HELPER FUNCTIONS
def main_menu():
    main_menu = pygame_menu.Menu(720, 1280, 'Welcome', theme=pygame_menu.themes.THEME_DARK)
    main_menu.add.button('Start', select_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.mainloop(screen)
    
def select_menu():
    select_menu = pygame_menu.Menu(720, 1280, 'Algorithms', theme=pygame_menu.themes.THEME_DARK)
    select_menu.add.button('Path-Finding Algorithms', pathfinding_menu)
    select_menu.add.button('Sorting Algorithms', sorting_menu)
    select_menu.add.button('Back', main_menu)
    select_menu.mainloop(screen)

def pathfinding_menu():
    main_menu = pygame_menu.Menu(720, 1280, 'Path-Finding Algorithms', theme=pygame_menu.themes.THEME_DARK)
    main_menu.add.button('A* Search', foo)
    main_menu.add.button('Dijkstra\'s Algorithm', foo)
    main_menu.add.button('Back', select_menu)
    main_menu.mainloop(screen)
    
def sorting_menu():
    main_menu = pygame_menu.Menu(720, 1280, 'Sorting Algorithms', theme=pygame_menu.themes.THEME_DARK)
    main_menu.add.button('Alg-1', foo)
    main_menu.add.button('Alg-2', foo)
    main_menu.add.button('Alg-3', foo)
    main_menu.add.button('Back', select_menu)
    main_menu.mainloop(screen)

def foo():
    pass


#MAIN LOOP
def mainloop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        main_menu()


#MAIN CALL
if __name__ == "__main__":
    mainloop()
