from tkinter import ttk, constants
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

        player_1_label.grid(row=2, column=0)
        self.player_1_entry.grid(row=2, column=1)

    def _initialize_player_2_field(self):
        player_2_label = ttk.Label(self._frame, text='Player 2 name')
        self.player_2_entry = ttk.Entry(self._frame)

        player_2_label.grid(row=4, column=0)
        self.player_2_entry.grid(row=4, column=1)

    def _initialize_board_size_field(self):
        board_height_label = ttk.Label(self._frame, text='Board height')
        self.board_height_entry = ttk.Entry(self._frame)

        board_length_label = ttk.Label(self._frame, text='Board length')
        self.board_length_entry = ttk.Entry(self._frame)

        board_height_label.grid(row=6, column=0)
        self.board_height_entry.grid(row=6, column=1)

        board_length_label.grid(row=7, column=0)
        self.board_length_entry.grid(row=7, column=1)

    def _start_play_handler(self):
        player1, player2 = self.player_1_entry.get(), self.player_2_entry.get()
        board_height, board_length = self.board_height_entry.get(), self.board_length_entry.get()

        if len(player1) > 10:
            error_label = ttk.Label(self._frame, text=f'Too long name for Player 1')
            error_label.grid(row=9, column=1)

        elif len(player2) > 10:
            error_label = ttk.Label(self._frame, text=f'Too long name for Player 2')
            error_label.grid(row=9, column=1)

        else:
            play_service.create_players(player1,
                                        player2,
                                        int(board_height),
                                        int(board_length))

            self._handle_show_play_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(self._frame,
                          text="Let's play Tic-Tac-Toe! Who are playing today?")

        play_button = ttk.Button(self._frame,
                                 text='Start the game',
                                 command=self._start_play_handler)

        label.grid(row=0, column=0)
        play_button.grid(row=8, column=0)

        self._initialize_player_1_field()
        self._initialize_player_2_field()
        self._initialize_board_size_field()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)







