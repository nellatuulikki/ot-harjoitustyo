from tkinter import Tk
from ui.play_view import Tic_tac_toe_UI
from repositories.player_repository import Player
import os


def main():
    player1 = Player('Mikko')
    player2 = Player('Nella')
    window = Tk()
    window.title('Tic Tac Toe game')
    ui = Tic_tac_toe_UI(window, player1, player2)
    ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()