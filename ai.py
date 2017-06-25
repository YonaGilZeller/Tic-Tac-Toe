from random import randint

class Ai:
    def __init__(self, choice):
        self.choice = choice

    free_buttons = []
    # Main function for bot making a move
    def make_move(self, board):
        self.make_random_move(board) # Do a random move

    # Makes a random move by generating a random integer and checking if the place is free
    def make_random_move(self, board):

        for button in board: # Simple for loop to extract the free buttons
            if len(button.text.strip()) < 1: # If the button has no mark, stripping spaces...
                self.free_buttons.append(button)

        if len(self.free_buttons) > 1: # If any free buttons left... let's make the move
            rand = randint(0, len(self.free_buttons) - 1) # Generate a random integer from 0 to the length of the array
            self.free_buttons[rand].text = self.choice

    def tree(self):
        for x in range(self.free_buttons):
            pass