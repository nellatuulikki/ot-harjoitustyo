from tkinter import ttk, constants
import tkinter.messagebox
from services.play_service import play_service


class NamePlayersView:

    def __init__(self, root, handle_show_play_view):
        self._root = root
        self._frame = None
        self._handle_show_play_view = handle_show_play_view
        self._player_1_entry = None
        self._player_2_entry = None
        self._board_size_entry = None
        self._error_variable = None
        self._error_label = None

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
        board_height_label = ttk.Label(self._frame, text='Board height')
        self.board_height_entry = ttk.Entry(self._frame)

        board_width_label = ttk.Label(self._frame, text='Board width')
        self.board_width_entry = ttk.Entry(self._frame)

        board_height_label.grid(row=5, column=0, padx=2, pady=2)
        self.board_height_entry.grid(row=5, column=1, padx=2, pady=2)

        board_width_label.grid(row=5, column=2, padx=2, pady=2)
        self.board_width_entry.grid(row=5, column=3, padx=2, pady=2)

    def _start_play_handler(self):
        try:
            player1, player2 = str(self.player_1_entry.get()), str(self.player_2_entry.get())

            board_height, board_width = int(self.board_height_entry.get()), int(self.board_width_entry.get())

            if len(player1) > 10 or len(player2) > 10:
                self._show_error('Check player names. Name with 10 letters or less are acceptable')
                return
            elif len(player1) == 0 or len(player2) == 0:
                self._show_error('Name must have at least one letter')
                return
            elif board_height < 5 or board_width < 5:
                self._show_error('Board size must be larger than 5x5')
                return

            play_service.create_players(player1,
                                        player2,
                                        board_height,
                                        board_width)

            self._handle_show_play_view()

        except ValueError:
            self._show_error('Board height and width must be integers')

    def _show_error(self, message):
        tkinter.messagebox.showinfo("Error", message)

    def _initialize(self):
        self._root.geometry("810x500")
        self._frame = ttk.Frame(master=self._root)
        self._initialize_grid()

        label = ttk.Label(self._frame,
                          text="Let's play Tic-Tac-Toe!")
        label.grid(row=0, column=1, columnspan=2)

        players_label = ttk.Label(self._frame,
                                  text="Who are playing today?")
        players_label.grid(row=1, column=0)

        board_size_label = ttk.Label(self._frame,
                                     text="Assign board size")
        board_size_label.grid(row=4, column=0)

        play_button = ttk.Button(self._frame,
                                 text='Start the game',
                                 command=self._start_play_handler)
        play_button.grid(row=6, column=1, columnspan=2)

        top_ten_players_label = ttk.Label(self._frame,
                                          text='Show top 5 players')
        top_ten_players_label.grid(row=7, column=1, columnspan=2)

        last_ten_games_label = ttk.Label(self._frame,
                                         text='Show Last 5 games')
        last_ten_games_label.grid(row=9, column=1, columnspan=2)

        self._show_data(play_service.get_top_players(), 8)
        self._show_data(play_service.get_last_ten(), 10)
        self._initialize_grid()

        self._initialize_player_1_field()
        self._initialize_player_2_field()

        self._initialize_board_size_field()

    def _initialize_grid(self):

        for col in range(0, 4):
            self._frame.grid_columnconfigure(col, weight=1, minsize=100)

    def _show_data(self, data, grid_row):
        s = ttk.Style()
        s.configure('Treeview', rowheight=20)

        columns = list(data.columns)

        tree = ttk.Treeview(self._frame, style='Treeview', height=6)
        tree["columns"] = columns
        for col in columns:
            tree.column(col, minwidth=0, width=75, stretch=False)
            tree.heading(col, text=col)

        for index, row in data.iterrows():
            tree.insert("", 0, text=index, values=list(row))

        tree.grid(row=grid_row, columnspan=5, column=0, padx=2, pady=2)
