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

def solve(board):
   '''
   solves a sudoku board using backtracking
   input -> list[list[int]]
   return -> list[list[int]]
   '''
   find = find_empty(board)
   if not find:
      return True
   else:
      row, col = find
   
   #loop through 1-9 and plug it in the board
   for i in range(1, 10):
      if is_valid(board, i, (row, col)):
         board[row][col] = i
         
         if solve(board):
            return True
   
         board[row][col] = 0
   return False

def print_board(board):
   '''
   prints out the board
   input -> list[list[int]]
   return -> none
   '''
   for i in range(len(board)):
      if i % 3 == 0 and i != 0:
         print('-----------------------')

      for j in range(len(board[0])):
         if j % 3 == 0 and j != 0:
            print(' | ', end = '')

         if j == 8:
            print(board[i][j])
         
         else:
            print(str(board[i][j]) + ' ', end='')
            
def find_empty(board):
   '''
   finds the empty spots in the board denoted by int value 0
   input -> list[list[int]]
   return -> tuple
   '''
   for i in range(len(board)):
      for j in range(len(board[0])):
         if board[i][j] == 0:
            return (i, j) # row, col
   
   #if no empty spots then
   return None

def is_valid(board, num, pos):
   '''
   check if the number inputed in the board is a valid input
   input -> list[list[int]], int, tuple
   return -> boolean
   '''
   #check row
   for i in range(len(board[0])):
      if board[pos[0]][i] == num and pos[1] != i:
         return False
   
   #check column
   for i in range(len(board)):
      if board[i][pos[1]] == num and pos[0] != i:
         return False

   #check 3x3 box
   #determine which box we're in
   box_x = pos[1] // 3
   box_y = pos[0] // 3
   
   for i in range(box_y * 3, box_y * 3 + 3):
      for j in range(box_x * 3, box_x * 3 + 3):
         if board[i][j] == num and (i, j) != pos:
            return False
   
   #nothing wrong then
   return True
   
print_board(board)
print('/n')
solve(board)
print('/n')

print_board(board)