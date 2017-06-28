from random import randint
from audioop import minmax, findmax

class Ai:
    def __init__(self, choice, op):
        self.choice = choice
        self.op = op  #opponects character

    # Main function for bot making a move
    def make_move(self, board):
        #self.make_random_move(board)
        arryBoard = self.cvtBoard(board)
        board[self.calculateMove(arryBoard)[0]].text = self.choice


    # Makes a random move by generating a random integer and checking if the place is free
    def make_random_move(self, board):
        free_buttons = []
        for button in board: # Simple for loop to extract the free buttons
            if len(button.text.strip()) < 1: # If the button has no mark, stripping spaces...
                free_buttons.append(button)

        if len(free_buttons) > 1: # If any free buttons left... let's make the move
            rand = randint(0, len(free_buttons) - 1) # Generate a random integer from 0 to the length of the array
            free_buttons[rand].text = self.choice

    def getFreeButtons(self, board):
        free_buttons = []
        for b in board: # Simple for loop to extract the free buttons
            if len(b[1]) < 1: # If the button has no mark, stripping spaces...
                free_buttons.append(b)
        return free_buttons

    def calculateMove(self, board):
        vb = board
        min = self.findMin(vb)
        vb[min[0]] = min[1]
        self.findMax(vb)
          
    def findMin(self, board):
        OBoard = board          #original board
        vb = board
        free_buttons = self.getFreeButtons(vb)
        avlMoves = []
        for b in free_buttons: 
            vb = OBoard
            free_buttons = self.getFreeButtons(vb)
            vb[b[0]][1] = self.op
            avlMoves.append([self.boardScore(vb), b])
        
        final = [0, None]
        for m in avlMoves:
            if m[0] < final[0]:
                final = m
                
        return final[1]
                       
    
    def findMax(self, board):
        vb = board
        free_buttons = self.getFreeButtons(vb)
        avlMoves = []
        for b in free_buttons: 
            vb = board
            free_buttons = self.getFreeButtons(vb)
            vb[b[0]][1] = self.choice
            avlMoves.append([self.boardScore(vb), b])
        
        final = [0, None]
        for m in avlMoves:
            if m[0] > final[0]:
                final = m
                
        return final[1]
            
    def cvtBoard(self, buttons):
        finalBaord = []
        for b in buttons:
            #print b
            finalBaord.append([int(b.id), b.text])
            print finalBaord
        return finalBaord

    def check_winner(self, board):
        if (board[0][1] == board[1][1] == board[2][1] == "X" or
            board[3][1] == board[4][1] == board[5][1] == "X" or
            board[6][1] == board[7][1] == board[8][1] == "X" or
            board[0][1] == board[3][1] == board[6][1] == "X" or
            board[1][1] == board[4][1] == board[7][1] == "X" or
            board[2][1] == board[5][1] == board[8][1] == "X" or
            board[0][1] == board[4][1] == board[8][1] == "X" or
            board[2][1] == board[4][1] == board[6][1] == "X"):
                return 'X' 

        elif (board[0][1] == board[1][1] == board[2][1] == "O" or
              board[3][1] == board[4][1] == board[5][1] == "O" or
              board[6][1] == board[7][1] == board[8][1] == "O" or
              board[0][1] == board[3][1] == board[6][1] == "O" or
              board[1][1] == board[4][1] == board[7][1] == "O" or
              board[2][1] == board[5][1] == board[8][1] == "O" or
              board[0][1] == board[4][1] == board[8][1] == "O" or
              board[2][1] == board[4][1] == board[6][1] == "O"):
                return 'O'
        else:
            return 'n'
        
    def boardScore(self, board):
        if self.check_winner(board) == self.op:
            return -1
        elif self.check_winner(board) == self.choice:
            return 1
        else:
            return 0
    