import tkinter as tk
from tkinter import constants
from services.play_service import play_service


class TicTacToeView:

    def __init__(self, root, handle_end_view):
        self._root = root
        self._frame = None
        self.handle_end_view = handle_end_view
        self.player1 = play_service.get_player_1()
        self.player2 = play_service.get_player_2()
        self.buttons = []
        play_service.start_new_game()
        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _handle_board(self):

        status_label = tk.Label(self._frame, text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")
        status_label.grid(row=0, columnspan=6)

        for row in range(0, play_service.get_height()):
            list_of_buttons = []
            for col in range(0, play_service.get_width()):
                button = tk.Button(master=self._frame,
                                   text="",
                                   height=6,
                                   width=11,
                                   command=lambda row=row, col=col: self._handle_make_move(row, col, status_label))

                button.grid(row=row + 1, column=col)
                list_of_buttons.append(button)
            self.buttons.append(list_of_buttons)

    def _handle_make_move(self, row, column, label):

        if play_service.get_winner() == 'No winner yet':

            if self.buttons[row][column]['text']:

                label.config(text="Sorry, that box is already taken! Select another box")

            elif play_service.player_1_turn() is True:

                play_service.player_1_move(row, column)
                self.buttons[row][column].config(text="X")
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player2}'s turn to make a move")

            elif play_service.player_1_turn() is False:

                play_service.player_2_move(row, column)
                self.buttons[row][column].config(text="O")
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")

        if play_service.get_winner() != 'No winner yet':
            self._frame.after(5000, self.handle_end_view())

    def _initialize(self):

        self._frame = tk.Frame(master=self._root)

        self._handle_board()
