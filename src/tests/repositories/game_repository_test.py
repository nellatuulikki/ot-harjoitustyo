import unittest
from repositories.game_repository import game_repository
from repositories.player_repository import player_repository
from entities.player import Player
from entities.game import Game


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_all()
        game_repository.delete_all()

        self.player_1 = Player('Nella', 0, 0)
        self.player_2 = Player('Mikko', 0, 0)
        self.game = Game(self.player_1, self.player_2, 5, 5)
        self.game_2 = Game(self.player_2, self.player_1, 5, 5)

    def test_create_game(self):
        self.game.initialize_game()

        game_repository.create_game(self.game, self.player_1, self.player_2)
        game = game_repository.check_game(self.game)

        self.assertEqual(game['game_id'], self.game.game_id)
        self.assertEqual(game['player_1'], self.player_1.name)
        self.assertEqual(game['player_2'], self.player_2.name)
        self.assertEqual(game['moves'], self.game.moves)

    def test_get_last_ten(self):
        self.game.initialize_game()
        self.game_2.initialize_game()

        game_repository.create_game(self.game, self.player_1, self.player_2)
        game_repository.create_game(self.game_2, self.player_2, self.player_1)

        last_five = game_repository.get_last_ten()
        self.assertEqual(len(last_five), 2)

    def test_delete_all(self):
        self.game.initialize_game()
        game_repository.create_game(self.game, self.player_1, self.player_2)
        game_repository.delete_all()
        last_five = game_repository.get_last_ten()
        self.assertEqual(len(last_five), 0)