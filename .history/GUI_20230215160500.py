# GUI.py
import pygame
from solver import solve, is_valid
import time
pygame.font.init()

class Grid:
   board = [
      [7,8,0,4,0,0,1,2,0],
      [6,0,0,0,7,5,0,0,9],
      [0,0,0,6,0,1,0,7,8],
      [0,0,7,0,4,0,2,6,0],
      [0,0,1,0,5,0,9,3,0],
      [9,0,4,0,6,0,0,0,5],
      [0,7,0,3,0,0,0,1,2],
      [1,2,0,0,0,7,4,0,0],
      [0,4,9,2,0,6,0,0,7]
   ]
   
   def __init__(self, rows, cols, width, height):
      self.rows = rows
      self.cols = cols
      self.cubes = [[Square(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
      self.width = width
      self.height = height
      self.model = None
      self.selected = None
      
class Square:
   rows = 9
   cols = 9
   
   def __init__(self, value, row, col, width, height):
      self.value = value
      self.temp = 0
      self.row = row
      self.col = col
      self.width = width
      self.height = height
      self.selected = False
      
   def draw(self, win):
      fnt = pygame.font.SysFont('comicsans', 40)
      gap = self.width / 9
      x = self.col * gap
      y = self.row * gap
   
      if self.temp != 0 and self.value == 0:
         text = fnt.render(str(self.temp), 1, (128,128,128))
         win.blit(text, (x + 5, y + 5))
      
      elif not(self.value == 0):
         text = fnt.render(str(self.value), 1, (0,0,0))
         win.blit(text, (x + (gap/2 - text.get_width()/2)))