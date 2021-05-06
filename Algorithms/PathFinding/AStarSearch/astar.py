#IMPORTS
import pygame
import pygame_menu
import math
from queue import PriorityQueue


#CONSTANTS
RED = (255, 0, 0) #Visited but close nodes
GREEN = (0, 255, 0) #Visited and open nodes
BLUE = (0, 255, 0) 
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) #Empty nodes
BLACK = (0, 0, 0) #Barrier nodes
PURPLE = (128, 0, 128) #Path nodes
ORANGE = (255, 165 ,0) #Start node
GREY = (128, 128, 128)
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
		self.neighbors = []
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
		pass

	def __lt__(self, other): #"lt" stands for lesser than
		'''
		Compares current node with another node
		'''
		return False