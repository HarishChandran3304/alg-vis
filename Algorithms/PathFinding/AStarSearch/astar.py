#IMPORTS
import pygame
import pygame_menu
import math
from queue import PriorityQueue


#CONSTANTS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


#CLASSES
class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.colour = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

    #CLASS METHODS
	def getpos(self):
		return self.row, self.col

	def isclosed(self):
		return self.colour == RED

	def isopen(self):
		return self.colour == GREEN

	def isbarrier(self):
		return self.colour == BLACK

	def isstart(self):
		return self.colour == ORANGE

	def isend(self):
		return self.colour == TURQUOISE

	def reset(self):
		self.colour = WHITE

	def makestart(self):
		self.colour = ORANGE

	def makeclosed(self):
		self.colour = RED

	def makeopen(self):
		self.colour = GREEN

	def makebarrier(self):
		self.colour = BLACK

	def makeend(self):
		self.colour = TURQUOISE

	def makepath(self):
		self.colour = PURPLE