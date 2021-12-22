from services.play_service import play_service
import tkinter as tk
from tkinter import constants


class EndView:
    def __init__(self, root, handle_play, handle_return):
        self._root = root
        self._frame = None
        self.handle_play = handle_play
        self.handle_return = handle_return
        self._initialize()
        play_service.save_game()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize_headers(self):

        status_label = tk.Label(self._frame, text="")

        if play_service.get_winner() == 'No winner':
            status_label.config(text="The Game is over! No winner for this round")
        else:
            status_label.config(text=f"The Game is over! Winner is {play_service.get_winner()}")

        status_label.grid(row=1, columnspan=6)

    def _initialize_buttons(self):

        return_button = tk.Button(
            master=self._frame,
            text='Return to front page',
            command=self.handle_return
        )

        play_button = tk.Button(
            master=self._frame,
            text='Play again',
            command=self.handle_play
        )

        return_button.grid(row=2, columnspan=1)
        play_button.grid(row=3, columnspan=1)

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._initialize_headers()
        self._initialize_buttons()