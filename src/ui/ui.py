from ui.play_view import TicTacToeView
from ui.select_players_view import NamePlayersView
from ui.game_ended_view import EndView


class Ui:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self.player_1 = None
        self.player_2 = None

    def start(self):
        self._show_select_player_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_select_player_view(self):
        self._hide_current_view()

        self._current_view = NamePlayersView(self._root,
                                             self._show_play_view)

        self._current_view.pack()

    def _show_play_view(self):
        self._hide_current_view()

        self._current_view = TicTacToeView(self._root,
                                           self._end_play_view)

        self._current_view.pack()

    def _end_play_view(self):
        self._hide_current_view()

        self._current_view = EndView(self._root,
                                     self._show_play_view,
                                     self._show_select_player_view)

        self._current_view.pack()
