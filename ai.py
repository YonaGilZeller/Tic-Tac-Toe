from random import randint

class Ai:
    def __init__(self, choice):
        self.choice = choice

    # Main function for bot making a move
    def make_move(self, board):
        self.make_random_move(board) # Do a random move

    # Makes a random move by generating a random integer and checking if the place is free
    def make_random_move(self, board):
        free_buttons = []
        for button in board: # Simple for loop to extract the free buttons
            if len(button.text.strip()) < 1: # If the button has no mark, stripping spaces...
                free_buttons.append(button)

        if len(free_buttons) > 1: # If any free buttons left... let's make the move
            rand = randint(0, len(free_buttons) - 1) # Generate a random integer from 0 to the length of the array
            free_buttons[rand].text = self.choice
            
    def calculateMinMax(self, buttons):
        pass
    
    def checkBoard(self, boardState):
        pass
    
    def calculateMoveOptions(self, buttons):
        free_buttons = []
        for b in buttons: # Simple for loop to extract the free buttons
            if len(b.text.strip()) < 1: # If the button has no mark, stripping spaces...
                free_buttons.append(b)