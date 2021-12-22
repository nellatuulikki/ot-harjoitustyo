from tkinter import ttk, constants
import tkinter as tk
from services.play_service import play_service


class NamePlayersView:

    def __init__(self, root, handle_show_play_view):
        self._root = root
        self._frame = None
        self._handle_show_play_view = handle_show_play_view
        self._player_1_entry = None
        self._player_2_entry = None
        self._board_size_entry = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize_player_1_field(self):
        player_1_label = ttk.Label(self._frame, text='Player 1 name')
        self.player_1_entry = ttk.Entry(self._frame)

        player_1_label.grid(row=2, column=0, padx=2, pady=2)
        self.player_1_entry.grid(row=2, column=1, padx=2, pady=2)

    def _initialize_player_2_field(self):
        player_2_label = ttk.Label(self._frame, text='Player 2 name')
        self.player_2_entry = ttk.Entry(self._frame)

        player_2_label.grid(row=3, column=0, padx=2, pady=2)
        self.player_2_entry.grid(row=3, column=1, padx=2, pady=2)

    def _initialize_board_size_field(self):
        board_height_label = ttk.Label(self._frame, text='Board width')
        self.board_height_entry = ttk.Entry(self._frame)

        board_width_label = ttk.Label(self._frame, text='Board length')
        self.board_width_entry = ttk.Entry(self._frame)

        board_height_label.grid(row=5, column=0, padx=2, pady=2)
        self.board_height_entry.grid(row=5, column=1, padx=2, pady=2)

        board_width_label.grid(row=5, column=2, padx=2, pady=2)
        self.board_width_entry.grid(row=5, column=3, padx=2, pady=2)

    def _start_play_handler(self):
        player1, player2 = self.player_1_entry.get(), self.player_2_entry.get()
        board_height, board_length = self.board_height_entry.get(), self.board_width_entry.get()

        if len(player1) > 10:
            error_label = ttk.Label(self._frame, text=f'Too long name for Player 1')
            error_label.grid(row=9, column=1, padx=2, pady=2)

        elif len(player2) > 10:
            error_label = ttk.Label(self._frame, text=f'Too long name for Player 2')
            error_label.grid(row=9, column=1, padx=2, pady=2)

        else:
            play_service.create_players(player1,
                                        player2,
                                        int(board_height),
                                        int(board_length))

            self._handle_show_play_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(self._frame,
                          text="Let's play Tic-Tac-Toe!")
        players_label = ttk.Label(self._frame, text="Who are playing today?")
        board_size_label = ttk.Label(self._frame, text="Assign board size")

        play_button = ttk.Button(self._frame,
                                 text='Start the game',
                                 command=self._start_play_handler)

        top_ten_players_label = ttk.Label(self._frame, text='Show top 5 players')

        last_ten_games_label = ttk.Label(self._frame, text='Last 5 games')


        label.grid(row=0, column=1, columnspan=2)
        players_label.grid(row=1, column=0)
        board_size_label.grid(row=4, column=0)
        play_button.grid(row=6, column=1, columnspan=2)
        top_ten_players_label.grid(row=7, column=1, columnspan=2)
        last_ten_games_label.grid(row=9, column=1, columnspan=2)
        self.show_data(play_service.get_top_players(), 8)
        self.show_data(play_service.get_last_ten(), 10)

        self._initialize_player_1_field()
        self._initialize_player_2_field()
        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        self._frame.grid_columnconfigure(1, weight=1, minsize=100)
        self._frame.grid_columnconfigure(2, weight=1, minsize=100)
        self._frame.grid_columnconfigure(3, weight=1, minsize=100)
        self._initialize_board_size_field()

    def show_data(self, data, grid_row):
        s = ttk.Style()
        s.configure('Treeview', rowheight=20)

        cols = list(data.columns)

        tree = ttk.Treeview(self._frame, style='Treeview', height=6)
        tree["columns"] = cols
        for i in cols:
            tree.column(i, minwidth=0, width=75, stretch=False)
            tree.heading(i, text=i)

        for index, row in data.iterrows():
            tree.insert("", 0, text=index, values=list(row))

        tree.grid(row=grid_row, columnspan=5, column=0, padx=2, pady=2)
