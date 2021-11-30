import tkinter as tk
from tkinter import constants
from services.play_service import play_service


class TicTacToeView:

    def __init__(self, root):
        self._root = root
        self._frame = None
        self.player1 = play_service.get_player_1()
        self.player2 = play_service.get_player_2()
        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _handle_board(self):

        b1 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b1, status_label, 0, 0))
        b2 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b2, status_label, 0, 1))
        b3 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b3, status_label, 0, 2))
        b4 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b4, status_label, 1, 0))
        b5 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b5, status_label, 1, 1))
        b6 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b6, status_label, 1, 2))
        b7 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b7, status_label, 2, 0))
        b8 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b8, status_label, 2, 1))
        b9 = tk.Button(master=self._frame, text="", height=6, width=11,
                       command=lambda: self._handle_make_move(b9, status_label, 2, 2))

        status_label = tk.Label(self._frame, text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")

        status_label.grid(row=0, columnspan=6)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)

    def _handle_make_move(self, button, label, row, column):

        if play_service.get_winner() == 'No winner yet':

            if button['text']:

                label.config(text="Sorry, that box is already taken! Select another box")

            elif play_service.player_1_turn() is True:

                play_service.player_1_move(row, column)
                button.config(text="X")
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player2}'s turn to make a move")

            elif play_service.player_1_turn() is False:

                play_service.player_2_move(row, column)
                button.config(text="O")
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")

        if play_service.get_winner() != 'No winner yet':
            self._handle_end_game(label)

    def _handle_end_game(self, label):

        if play_service.get_winner() == 'No winner':
            label.config(text="The Game is over! No winner for this round")
        else:
            label.config(text=f"The Game is over! Winner is {play_service.get_winner()}")

        # self._frame.after(10000, self._frame.destroy)

    def _initialize(self):

        self._frame = tk.Frame(master=self._root)

        self._handle_board()

        # self._frame.grid_columnconfigure(0, weight=1, minsize=200)
