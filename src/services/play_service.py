from entities.player import Player
from entities.game import Game


class PlayService:

    def __init__(self):
        self.player_1 = Player('')
        self.player_2 = Player('')
        self.game = Game(self.player_1, self.player_2)

    def create_players(self, player_1, player_2):

        self.player_1 = Player(player_1)
        self.player_2 = Player(player_2)
        self.game = Game(self.player_1, self.player_2)

    def get_player_1(self):

        return self.player_1.get_name()

    def get_player_2(self):

        return self.player_2.get_name()

    def get_winner(self):

        return self.game.get_winner()

    def player_1_turn(self):

        return self.game.player_1_turn

    def player_1_move(self, row, column):

        self.game.player_1_makes_move(row, column)

        if self.game.get_winner() == self.get_player_2():
            self.player_1.add_win()

    def player_2_move(self, row, column):

        self.game.player_2_makes_move(row, column)

        if self.game.get_winner() == self.get_player_1():
            self.player_2.add_win()


play_service = PlayService()
