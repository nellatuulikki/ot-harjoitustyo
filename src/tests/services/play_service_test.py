import unittest
from entities.game import Game
from entities.player import Player
from services.play_service import PlayService


class FakeGameRepository:
    def __init__(self, games=None):
        self.games = games


class FakePlayerRepository:
    def __init__(self, players=None):
        self.players = []

    def check_player(self, name):
        for i in range(0, len(self.players)):
            if self.players[i].get_name() == name:
                return self.players[i]

        return None

    def create_player(self, name):
        self.players.append(Player(name, 0, 0))

    def update_wins(self, player_name):
        for i in range(0, len(self.players)):
            if self.players[i].get_name() == player_name:
                name = self.players[0].get_name()
                wins = self.players[0].get_wins() + 1
                defeats = self.players[0].get_defeats()

                self.players[0] = Player(name, wins, defeats)

    def update_defeats(self, player_name):
        for i in range(0, len(self.players)):
            if self.players[i].get_name() == player_name:
                name = self.players[0].get_name()
                wins = self.players[0].get_wins()
                defeats = self.players[0].get_defeats() + 1

                self.players[0] = Player(name, wins, defeats)


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.play_service = PlayService(FakeGameRepository(), FakePlayerRepository())
        self.player_1 = Player('Nella', 0, 1)
        self.player_2 = Player('Mikko', 1, 0)
        self.board_height = 5
        self.board_width = 5
        self.game = Game(self.player_1, self.player_2, self.board_width, self.board_height)

    def test_initialize_player(self):
        player_data = self.play_service.initialize_player('Nella')
        self.assertEqual(player_data.name, 'Nella')
        self.assertEqual(player_data.wins, 0)
        self.assertEqual(player_data.defeats, 0)

        self.play_service.update_wins('Nella')

        player_data_updated = self.play_service.initialize_player('Nella')
        self.assertEqual(player_data_updated.wins, 1)

    def test_create_players(self):
        self.play_service.create_players('Mikko', 'Kimmo', 5, 5)

        self.assertEqual(self.play_service.game.player_1.get_name(), 'Mikko')
        self.assertEqual(self.play_service.game.player_2.get_name(), 'Kimmo')

    def test_start_new_game(self):
        self.play_service.create_players('Mikko', 'Kimmo', 5, 5)
        self.play_service.start_new_game()

        self.assertEqual(self.play_service.game.winner, 'No winner yet')
        self.assertEqual(self.play_service.game.player_1_turn, True)
        self.assertEqual(self.play_service.game.moves, 0)
        self.assertEqual(self.play_service.game.game_board, [['', '', '', '', ''],
                                                             ['', '', '', '', ''],
                                                             ['', '', '', '', ''],
                                                             ['', '', '', '', ''],
                                                             ['', '', '', '', '']])

    def test_player_1_make_move(self):
        self.play_service.create_players('Mikko', 'Kimmo', 5, 5)
        self.play_service.start_new_game()

        self.play_service.game.game_board = [['X', 'X', 'X', 'X', ''],
                                             ['O', 'O', 'O', 'O', ''],
                                             ['', '', '', '', ''],
                                             ['', '', '', '', ''],
                                             ['', '', '', '', '']]

        self.play_service.player_1_move(0, 4)
        self.assertEqual(self.play_service.get_winner(), 'Mikko')
