from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from ai import Ai
from random import randint
import time

class TicTacToe(App):

    title = 'Tic Tac Toe'
    board = []
    choices = ["X","O"]

    # On application build handler
    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        self.layout = StackLayout()
        for x in range(9): # range() explanation: http://pythoncentral.io/pythons-range-function-explained/
            bt = Button(text='', font_size=200, width=200, height=200, size_hint=(None, None), id=str(x))
            bt.bind(on_release=self.btn_pressed)
            self.board.append(bt)
            self.layout.add_widget(bt)
        return self.layout

    # On application start handler
    def on_start(self):
        self.init_players();
        greeting = "Hello Player! You are playing with \"" + self.player + "\""
        self.popup_message(greeting)


    # On button pressed handler
    def btn_pressed(self, button):
        if len(button.text.strip()) < 1: # Continue only if the button has no mark on it...
            button.text = self.player
            self.check_winner()
            self.bot.make_move(self.board)


    # Initializes players
    def init_players(self):
        rand_choice = randint(0,1);
        self.bot = Ai(self.choices[rand_choice], abs(rand_choice - 1));
        self.player = self.choices[0] if rand_choice == 1 else self.choices[1]

    # Checks winner after every move...
    def check_winner(self):
        if (self.board[0].text == self.board[1].text == self.board[2].text == "X" or
            self.board[3].text == self.board[4].text == self.board[5].text == "X" or
            self.board[6].text == self.board[7].text == self.board[8].text == "X" or
            self.board[0].text == self.board[3].text == self.board[6].text == "X" or
            self.board[1].text == self.board[4].text == self.board[7].text == "X" or
            self.board[2].text == self.board[5].text == self.board[8].text == "X" or
            self.board[0].text == self.board[4].text == self.board[8].text == "X" or
            self.board[2].text == self.board[4].text == self.board[6].text == "X"):
            popup = Popup(title="Game OVER", content=Label(text="X player WON"), size=(300, 100),
                                       size_hint=(None, None))

            popup.open()

        elif (self.board[0].text == self.board[1].text == self.board[2].text == "O" or
              self.board[3].text == self.board[4].text == self.board[5].text == "O" or
              self.board[6].text == self.board[7].text == self.board[8].text == "O" or
              self.board[0].text == self.board[3].text == self.board[6].text == "O" or
              self.board[1].text == self.board[4].text == self.board[7].text == "O" or
              self.board[2].text == self.board[5].text == self.board[8].text == "O" or
              self.board[0].text == self.board[4].text == self.board[8].text == "O" or
              self.board[2].text == self.board[4].text == self.board[6].text == "O"):
                 popup = Popup(title="GAME OVER", content=Label(text="O player WON"), size=(300, 100),
                               size_hint=(None, None))
                 popup.open()

    def popup_message(self, msg):
        popup = Popup(title="Welcome!", content=Label(text=msg), size=(300, 100), size_hint=(None, None))
        popup.open()


if __name__ == '__main__':
    TicTacToe().run()