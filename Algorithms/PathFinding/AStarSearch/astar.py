#IMPORTS
import pygame
import pygame_menu
import math
from queue import PriorityQueue


#CONSTANTS
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
RED = (255, 0, 0) #Visited but close nodes
GREEN = (0, 255, 0) #Visited and open nodes
BLUE = (0, 255, 0)  #Path nodes
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) #Empty nodes
BLACK = (0, 0, 0) #Barrier nodes
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0) #Start node
GREY = (128, 128, 128) #Grid lines
TURQUOISE = (64, 224, 208) #Destination node


#CLASSES
class Node:
	def __init__(self, row, col, width, totalrows):
		'''
		Constructor
		To initialize attributes to a new instance when created
		'''
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.colour = WHITE
		self.neighbours = []
		self.width = width
		self.totalrows = totalrows

    #CLASS METHODS
	def getpos(self):
		'''
		Returns coordinate of a node in the form (row, column)
		'''
		return self.row, self.col

	def reset(self):
		'''
		Resets colour attribute of node back to white
		'''
		self.colour = WHITE


	def isclosed(self):
		'''
		Returns True if a node has been visited but is closed, else returns False
		'''
		return self.colour == RED

	def isopen(self):
		'''
		Returns True if a node has been visited and is open, else returns False
		'''
		return self.colour == GREEN

	def isbarrier(self):
		'''
		Returns True if a node is a barrier node, else returns False
		'''
		return self.colour == BLACK

	def isstart(self):
		'''
		Returns True if a node is the start node, else returns False
		'''
		return self.colour == ORANGE

	def isend(self):
		'''
		Returns True if a node is the destination node, else returns False
		'''
		return self.colour == TURQUOISE

	def ispath(self):
		'''
		Returns True if a node is a part of the path nodes, else returns False
		'''
		self.colour == PURPLE


	def makeclosed(self):
		'''
		Changes the colour attribute of a node to Red
		'''
		self.colour = RED

	def makeopen(self):
		'''
		Changes the colour attribute of a node to Green
		'''
		self.colour = GREEN

	def makebarrier(self):
		'''
		Changes the colour attribute of a node to Black
		'''
		self.colour = BLACK

	def makestart(self):
		'''
		Changes the colour attribute of a node to Orange
		'''
		self.colour = ORANGE

	def makeend(self):
		'''
		Changes the colour attribute of a node to Turquoise
		'''
		self.colour = TURQUOISE

	def makepath(self):
		'''
		Changes the colour attribute of a node to Purple
		'''
		self.colour = PURPLE


	def draw(self, surface):
		'''
		Draws the node on the surface, with the colour self.colour, as a square of side self.width, at self.x, self.y
		'''
		pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.width))

	def updateneighbours(self, grid):
		self.neighbours = []
		if self.row < self.totalrows-1 and not grid[self.row+1][self.col].isbarrier(): #Below Neighbour
			self.neighbours.append(grid[self.row+1][self.col])

		if self.row > 0 and not grid[self.row-1][self.col].isbarrier(): #Above Neighbour
			self.neighbours.append(grid[self.row-1][self.col])

		if self.col < self.totalrows-1 and not grid[self.row][self.col+1].isbarrier(): #Right Neighbour
			self.neighbours.append(grid[self.row][self.col+1])

		if self.col > 0 and not grid[self.row][self.col-1].isbarrier(): #Left Neighbour
			self.neighbours.append(grid[self.row][self.col-1])

	def __lt__(self, other): #"lt" stands for lesser than
		'''
		Compares current node with another node
		'''
		return False



#HELPER FUNCTIONS
def h(node1, node2):
    '''
    Heuristic function [h(n)] for the algorithm
    #Uses Manhattan-Distance [L-Distance]
    Returns the absolute distance between the current node and the destination node
    '''
    x1, y1 = node1
    x2, y2 = node2
    return abs(x2-x1) + abs(y2-y1)

def algorithm(draw, grid, start, end):
    count = 0
    openset = PriorityQueue()
    openset.put((0, count, start))
    camefrom = {}
    gscore = {node: float("inf") for row in grid for node in row}
    gscore[start] = 0
    fscore = {node: float("inf") for row in grid for node in row}
    fscore[start] = h(start.getpos(), end.getpos())
    
    opensethash = {start}
    
    while not openset.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = openset.get()[2]
        opensethash.remove(current)
        
        if current == end:
            return True
        
        for neighbour in current.neighbours:
            tempgscore = gscore[current]+1
            
            if tempgscore < gscore[neighbour]:
                camefrom[neighbour] = current
                gscore[neighbour] = tempgscore
                fscore[neighbour] = tempgscore + h(neighbour.getpos(), end.getpos())
                if neighbour not in opensethash:
                    count += 1
                    openset.put((fscore[neighbour], count, neighbour))
                    opensethash.add(neighbour)
                    neighbour.makeopen()
        
        draw()
        
        if current != start:
            current.makeclosed()
        
    return False

def makegrid(rows, width):
    '''
    Creates the grid and returns it in the form of a 2D list
    '''
    grid = []
    gap = width//rows #Width of each node
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

def drawgrid(surface, rows, width):
    '''
    Draws the lines of the grid in grey color
    '''
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(surface, GREY, (0, i*gap), (width, i*gap))
    for j in range(rows):
        pygame.draw.line(surface, GREY, (j*gap, 0), (j*gap, width))

def draw(surface, grid, rows, width):
    '''
    Main draw function to draw the entire grid
    '''
    surface.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(surface)
    
    drawgrid(surface, rows, width)
    pygame.display.update()

def getclickedpos(pos, rows, width):
    '''
    Returns the row and column of the node that was clicked on
    '''
    gap = width//rows
    y, x = pos
    
    row = y//gap
    col = x//gap
    
    return row, col

def main(surface, width):
    rows = 50 
    grid = makegrid(rows, width)
    
    start = None 
    end = None
    
    run = True
    started = False
    while run:
        draw(surface, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]: #Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = getclickedpos(pos, rows, width)
                node = grid[row][col]
                
                if not start and node!=end:
                    start = node
                    start.makestart()
                
                elif not end and node!=start:
                    end = node
                    end.makeend()
                
                elif node!=start and node!=end:
                    node.makebarrier()
            
            elif pygame.mouse.get_pressed()[2]: #Right mouse button
                pos = pygame.mouse.get_pos()
                row, col = getclickedpos(pos, rows, width)
                node = grid[row][col]
                
                if node == start:
                    start = None
                
                elif node == end:
                    end = None
                
                node.reset()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.updateneighbours(grid)
                        
                    algorithm(lambda: draw(surface, grid, rows, width), grid, start, end)

main(WIN, WIDTH)