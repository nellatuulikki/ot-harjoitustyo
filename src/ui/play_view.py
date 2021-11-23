import tkinter as tk
import os


class Tic_tac_toe_UI:

    def __init__(self, root, player1, player2):
        self._root = root
        self.player1 = player1.get_name()
        self.player2 = player2.get_name()
        self.player_1_turn = True
        self.game_board = None
        self.winner = None

    def start(self):

        self.game_board = self.create_board(height=3, length=3)

        b1 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b1, status_label, 0, 0))
        b2 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b2, status_label, 0, 1))
        b3 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b3, status_label, 0, 2))
        b4 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b4, status_label, 1, 0))
        b5 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b5, status_label, 1, 1))
        b6 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b6, status_label, 1, 2))
        b7 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b7, status_label, 2, 0))
        b8 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b8, status_label, 2, 1))
        b9 = tk.Button(master=self._root, text="", height=6, width=11,
                       command=lambda: self.make_move(b9, status_label, 2, 2))

        status_label = tk.Label(text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")

        status_label.grid(row=0, columnspan= 4)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)

    def create_board(self, height, length):

        board = []

        for i in range(0, height):
            row = []
            for j in range(0, length):
                row.append("")
            board.append(row)

        return board

    def make_move(self, button, label, row, column):

        if self.winner is None:

            if button['text']:

                label.config(text="Sorry, that box is already taken! Select another box")

            elif self.player_1_turn is True:

                button.config(text="X")
                self.game_board[row][column] = 'X'
                self.player_1_turn = False
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player2}'s turn to make a move")

            elif self.player_1_turn is False:

                button.config(text="O")
                self.game_board[row][column] = 'O'
                self.player_1_turn = True
                label.config(text=f"Let's play Tic Tac Toe! It's {self.player1}'s turn to make a move")

        self.get_game_status()

        if self.winner is not None or any("" in row for row in self.game_board) is False:
            self.end_game(label)

    def get_game_status(self):

        if (self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == "X"
                or self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == "X"
                or self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == "X"
                or self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == "X"
                or self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == "X"
                or self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == "X"
                or self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == "X"
                or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == "X"):
            self.winner = self.player1

        elif (self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == "O"
              or self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == "O"
              or self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == "O"
              or self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == "O"
              or self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == "O"
              or self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == "O"
              or self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == "O"
              or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == "O"):
            self.winner = self.player2

    def end_game(self, label):
        if self.winner is None:
            label.config(text="The Game is over! No winner for this round")
        else:
            label.config(text=f"The Game is over! Winner is {self.winner}")

        self._root.after(10000, self._root.destroy)