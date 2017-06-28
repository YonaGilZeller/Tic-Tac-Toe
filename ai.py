from random import randint

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
        free_buttons = self.getFreeButtons(vb)
        for b in free_buttons: 
            vb = board
            free_buttons = self.getFreeButtons(vb)
            vb[b[0]][1] = self.choice
            if self.check_winner(vb) == self.choice:
                return b

            else:
                return self.calculateMove(vb) 
            '''
            elif self.check_winner(vb) == self.op:
                pass
            '''
            
    def cvtBoard(self, buttons):
        finalBaord = []
        for b in buttons:
            print (b)
            finalBaord.append([int(b.id), b.text])
            print (finalBaord)
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