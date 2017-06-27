from random import randint

class Ai:
    def __init__(self, choice, op):
        self.choice = choice
        self.op = op  #opponects character

    # Main function for bot making a move
    def make_move(self, board):
        #self.make_random_move(board)
        self.calculateMove(board).text = self.choice


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
        for button in board: # Simple for loop to extract the free buttons
            if len(button.text.strip()) < 1: # If the button has no mark, stripping spaces...
                free_buttons.append(button)
        return free_buttons

    def calculateMove(self, board):
        vb = board
        free_buttons = self.getFreeButtons(vb)
        for b in free_buttons: #max
            vb = board
            free_buttons = self.getFreeButtons(vb)
            vb[int(b.id)].text = self.choice
            if self.check_winner(vb) == self.choice:
                return b

            else:
                return self.calculateMove(vb) 
            '''
            elif self.check_winner(vb) == self.op:
                pass
            '''
            
        

    def check_winner(self, board):
        if (board[0].text == board[1].text == board[2].text == "X" or
            board[3].text == board[4].text == board[5].text == "X" or
            board[6].text == board[7].text == board[8].text == "X" or
            board[0].text == board[3].text == board[6].text == "X" or
            board[1].text == board[4].text == board[7].text == "X" or
            board[2].text == board[5].text == board[8].text == "X" or
            board[0].text == board[4].text == board[8].text == "X" or
            board[2].text == board[4].text == board[6].text == "X"):
                return 'X' 

        elif (board[0].text == board[1].text == board[2].text == "O" or
              board[3].text == board[4].text == board[5].text == "O" or
              board[6].text == board[7].text == board[8].text == "O" or
              board[0].text == board[3].text == board[6].text == "O" or
              board[1].text == board[4].text == board[7].text == "O" or
              board[2].text == board[5].text == board[8].text == "O" or
              board[0].text == board[4].text == board[8].text == "O" or
              board[2].text == board[4].text == board[6].text == "O"):
                return 'O'
        else:
            return 'n'